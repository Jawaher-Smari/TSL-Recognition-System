import os
import numpy as np
import cv2

# ─── إعدادات عامة ───────────────────────────────────────────────────
IMG_SIZE = 224
T = 20  # طول كل تسلسل (fragment) بعد المعالجة

# ─── دوال مساعدة ────────────────────────────────────────────────────
def load_image(path):
    """اقرأ الصورة، غيّر حجمها لـ224×224 وطبّع قيمها إلى [0,1]."""
    img = cv2.imread(path)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    return img.astype(np.float32) / 255.0

def process_static(static_dir, class_to_idx):
    """
    معالجة الصور الثابتة:
    - كل صورة تُعامل كتسلسل طوله 1.
    - الإخراج: X_static.shape == (N,1,224,224,3), y_static.shape == (N,)
    """
    X, y = [], []
    for cls in sorted(os.listdir(static_dir)):
        label = class_to_idx[cls]
        cls_path = os.path.join(static_dir, cls)
        for fname in sorted(os.listdir(cls_path)):
            img = load_image(os.path.join(cls_path, fname))
            X.append(img[np.newaxis, ...])  # (1,224,224,3)
            y.append(label)
    return np.array(X), np.array(y)

def process_sequences(seq_dir, class_to_idx):
    """
    معالجة الصور المتسلسلة:
    - TRAIN: لو فيه مجلدات فرعيّة لكل fragment → كل مجلد أول 20 إطار
    - VALID/TEST: لو ما فيهش مجلدات فرعيّة → نعتبر مجلد الكلاس fragment واحد
      * نقرأ كل الصور (مثلاً 5) ثم نكملها بصفر frames حتى نصل T
    """
    X, y = [], []
    zero_frame = np.zeros((IMG_SIZE, IMG_SIZE, 3), dtype=np.float32)

    for cls in sorted(os.listdir(seq_dir)):
        label = class_to_idx[cls]
        cls_path = os.path.join(seq_dir, cls)
        items = sorted(os.listdir(cls_path))

        # شوف إذا موجود مجلدات فرعية
        subdirs = [d for d in items if os.path.isdir(os.path.join(cls_path, d))]

        if subdirs:
            # TRAIN case
            for fragment in subdirs:
                frag_path = os.path.join(cls_path, fragment)
                frames = sorted(os.listdir(frag_path))[:T]
                seq = [load_image(os.path.join(frag_path, f)) for f in frames]
                if len(seq) < T:
                    seq += [zero_frame] * (T - len(seq))
                X.append(np.stack(seq, axis=0))  # (T,224,224,3)
                y.append(label)
        else:
            # VALID/TEST case
            image_files = [f for f in items if f.lower().endswith((".jpg", ".png"))][:T]
            seq = [load_image(os.path.join(cls_path, f)) for f in image_files]
            if len(seq) < T:
                seq += [zero_frame] * (T - len(seq))
            X.append(np.stack(seq, axis=0))
            y.append(label)

    return np.array(X), np.array(y)

def save_npz_files(dataset_root, split):
    """
    لكل split (train/valid/test):
    1) نجمع أسماء الأصناف من static و sequences لبناء mapping كامل
    2) نولّد ملفات split_static.npz و split_sequences.npz
    """
    static_dir = os.path.join(dataset_root, split, "static")
    seq_dir    = os.path.join(dataset_root, split, "sequences")

    # نبني قائمة موحدة للأصناف
    classes_static = set(os.listdir(static_dir))
    classes_seq    = set(os.listdir(seq_dir))
    all_classes    = sorted(classes_static.union(classes_seq))
    class_to_idx   = {cls_name: idx for idx, cls_name in enumerate(all_classes)}

    print(f"\n⚙️  Split '{split}' → Classes: {all_classes}")

    # معالجة الصور الثابتة
    Xs, ys = process_static(static_dir, class_to_idx)
    np.savez_compressed(f"{split}_static.npz", X=Xs, y=ys)
    print(f"✅ Saved {split}_static.npz  X={Xs.shape}  y={ys.shape}")

    # معالجة الصور المتسلسلة
    Xq, yq = process_sequences(seq_dir, class_to_idx)
    np.savez_compressed(f"{split}_sequences.npz", X=Xq, y=yq)
    print(f"✅ Saved {split}_sequences.npz  X={Xq.shape}  y={yq.shape}")

if __name__ == "__main__":
    DATA_ROOT = r"C:\Users\LENOVO\Documents\new_dataset_projet\dataset\dataset_complet_ssd"
    for split in ["train", "valid", "test"]:
        save_npz_files(DATA_ROOT, split)
