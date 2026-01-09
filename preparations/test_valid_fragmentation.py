import os
import cv2
import numpy as np

# المسار الرئيسي الذي يحتوي مجلدات الـClasses
base_dir = r"C:\Users\LENOVO\Documents\new_dataset_projet\dataset\valid"

# امتدادات الفيديوهات المستهدفة
VIDEO_EXTENSIONS = ('.mp4', '.avi', '.mov', '.mkv')

for class_name in os.listdir(base_dir):
    class_path = os.path.join(base_dir, class_name)
    if not os.path.isdir(class_path):
        continue

    # استخراج الفيديوهات فقط
    videos = [f for f in sorted(os.listdir(class_path))
              if f.lower().endswith(VIDEO_EXTENSIONS)]
    
    for vid in videos:
        vid_path = os.path.join(class_path, vid)
        cap = cv2.VideoCapture(vid_path)

        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_indices = np.linspace(0, total_frames - 1, 5, dtype=int)

        print(f"Processing {vid} into 5 frames...")

        for i, frame_no in enumerate(frame_indices, start=1):
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
            ret, frame = cap.read()
            if not ret:
                continue

            resized_frame = cv2.resize(frame, (320, 320))  # توحيد الحجم إذا تحب
            frame_name = f"{os.path.splitext(vid)[0]}_frame_{i}.jpg"
            cv2.imwrite(os.path.join(class_path, frame_name), resized_frame)

        cap.release()
        os.remove(vid_path)
        print(f"Finished and removed video: {vid}")

print("All validation/testing videos processed.")
