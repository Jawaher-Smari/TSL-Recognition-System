import os
import cv2
import numpy as np
import mediapipe as mp
import tempfile

mediapipe_hands = mp.solutions.hands
def detect_hands(detection_confidence = 0.7, tracking_confidence = 0.7, number_of_hands = 2):

    return mediapipe_hands.Hands(static_image_mode = False, number_of_hands = number_of_hands, detection_confidence = detection_confidence, tracking_confidence = tracking_confidence)

#pour fichier .npz
def process_npz(input_npz, output_npz, hands, sequential=False, T=20, target_size=(224,224)):

    data = np.load(input_npz, mmap_mode='r')
    X, y = data["X"], data["y"]
    
    out_frames, out_labels = [], []
    for xi, label in zip(X, y):
        # si c'est static, on a (1,H,W,3)
        frames = [xi] if not sequential else list(xi)
        processed = []
        for frame in frames:
            if frame.ndim == 4 and frame.shape[0] == 1:
                frame = frame[0]

            # convertir de float à uint8
            frame_uint8 = (frame * 255).astype(np.uint8)

            # convertir de RGB à BGR
            frame_bgr = cv2.cvtColor(frame_uint8, cv2.COLOR_RGB2BGR)

            # maintenant on peut détecter
            _ = hands.process(cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB))

            roi = cv2.resize(frame_bgr, target_size)
            
            # convertir de uint8 à float
            processed.append(roi.astype(np.float32) / 255.0) # + normlaisation
        out_frames.append(np.stack(processed, axis=0))
        out_labels.append(label)
    
    out_X = np.array(out_frames)
    out_y = np.array(out_labels)
    np.savez_compressed(output_npz, X=out_X, y=out_y)
    print(f"Saved {output_npz}: X={out_X.shape}, y={out_y.shape}")

# pour dossier
def process_npy_folder(folder_path, output_npz, hands, sequential=False, T=20, target_size=(224,224)):

    x_path = os.path.join(folder_path, "X.npy")
    y_path = os.path.join(folder_path, "y.npy")
    if not os.path.isfile(x_path) or not os.path.isfile(y_path):
        raise FileNotFoundError(f"X.npy ou y.npy introuvable dans {folder_path}")
    
    X = np.load(x_path, mmap_mode='r')
    y = np.load(y_path, mmap_mode='r')
    
    with tempfile.NamedTemporaryFile(suffix=".npz", delete=False) as tmpf:
        np.savez_compressed(tmpf.name, X=X, y=y)
        tmp_npz = tmpf.name
    
    process_npz(tmp_npz, output_npz, hands, sequential, T, target_size)
    os.remove(tmp_npz)