import os
import random
from PIL import Image, ImageEnhance, ImageOps, ImageFilter

def augmentation(image):

    image = ImageEnhance.Brightness(image).enhance(random.uniform(0.9, 1.1))

    image = ImageEnhance.Contrast(image).enhance(random.uniform(0.9, 1.1))

    image = ImageEnhance.Color(image).enhance(random.uniform(0.9, 1.1))

    return image

def application(path):
    for class_folder in os.listdir(path):
        path_class = os.path.join(path, class_folder)

        if os.path.isdir(path_class):
            for file in os.listdir(path_class):
                path_file = os.path.join(path_class, file)

                if (file.endswith('.jpg') or file.endswith('.png')) and "_" not in file:
                    try:
                        image = Image.open(path_file)

                        # Resize and save original
                        original_resized = image.resize((224, 224))
                        original_resized.save(os.path.join(path_class, f"resized_{file}"))

                        # Augment 3 times only
                        for i in range(1, 4):
                            image_aug = augmentation(image)
                            nom_aug = os.path.join(path_class, f"aug_{i}_{file}")
                            image_aug.save(nom_aug)

                    except Exception as e:
                        print(f"Erreur {path_file} : {e}")

# مسار المجلد الرئيسي الذي يحتوي على مجلدات الفئات
dataset = r"C:\Users\LENOVO\Documents\new_dataset_projet\dataset\valid"
application(dataset)
