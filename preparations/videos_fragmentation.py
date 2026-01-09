import os
import cv2
import numpy as np
import random


dataset = r"C:/Users/LENOVO/Documents/new_dataset_projet/dataset/train - Copie"

# امتدادات الفيديوهات التي نريد معالجتها
type = ('.mp4', '.avi', '.mov', '.mkv')

def augmentation(frame, aug_type):
    
    if aug_type == 'brightness':
        factor = random.uniform(0.9, 1.1)
        frame = np.clip(frame * factor, 0, 255).astype(np.uint8)
    elif aug_type == 'contrast':
        factor = random.uniform(0.9, 1.1)
        mean = np.mean(frame)
        frame = np.clip((frame - mean) * factor + mean, 0, 255).astype(np.uint8)
    return frame

for class_name in os.listdir(dataset):
    class_path = os.path.join(dataset, class_name)
    if not os.path.isdir(class_path):
        continue

    videos = [f for f in sorted(os.listdir(class_path)) 
              if f.lower().endswith(type)]
    if not videos:
        continue  

    for idx, vid in enumerate(videos, start=1):
        vid_path = os.path.join(class_path, vid)
        cap = cv2.VideoCapture(vid_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        index = np.linspace(0, total_frames - 1, 20, dtype=int)
        
        # Choix aléatoire de type d'augmentation pour chaque vidéo fragmentée
        aug_type = random.choice(['brightness', 'contrast'])
        print(f"Appliquer type d'aug {aug_type} sur {vid}")
        
        for i, frame_no in enumerate(index, start=1):
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
            ret, frame = cap.read()
            if not ret:
                continue

            aug_frame = augmentation(frame, aug_type)
            resized_frame = cv2.resize(aug_frame, (224, 224))

            frame_name = f"{os.path.splitext(vid)[0]}_frame_{i}.jpg"
            cv2.imwrite(os.path.join(class_path, frame_name), resized_frame)

        cap.release()
        os.remove(vid_path)
        print(f"Vidéo supprimée: {vid}")

    print(f"Effectuée: {class_name}")

print("Terminé tous")
