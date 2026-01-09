import os
import random
from PIL import Image, ImageEnhance, ImageOps, ImageFilter

def augmentation(image):
    if random.random() > 0.5:
        image = ImageOps.mirror(image)
        
    brightness = ImageEnhance.Brightness(image)
    image = brightness.enhance(random.uniform(0.8, 1.2))

    contrast = ImageEnhance.Contrast(image)
    image = contrast.enhance(random.uniform(0.8, 1.2))

    color = ImageEnhance.Color(image)
    image = color.enhance(random.uniform(0.8, 1.2))

    if random.random() > 0.7:
        sharpness = ImageEnhance.Sharpness(image)
        image = sharpness.enhance(random.uniform(0.5, 2.0))

    angle = random.uniform(-10, 10)
    image = image.rotate(angle)

    if random.random() > 0.8:
        image = image.filter(ImageFilter.GaussianBlur(radius=1))

    return image

def application(path):
    for class_name in os.listdir(path):
        class_path = os.path.join(path, class_name)

        if os.path.isdir(class_path):
            for file in os.listdir(class_path):
                file_path = os.path.join(class_path, file)

                if (file.endswith('.jpg') or file.endswith('.png')) and "_" not in file: # pour éviter d'augmenter les fragments des vidéos
                    try:
                        image = Image.open(file_path)

                        original_resized = image.resize((224, 224))
                        original_resized.save(os.path.join(class_path, f"resized_{file}"))

                        for i in range(1, 19):
                            image_aug = augmentation(image)
                            nom_aug = os.path.join(class_path, f"aug_{i}_{file}")
                            image_aug.save(nom_aug)

                    except Exception as e:
                        print(f"Erreur {file_path} : {e}")

dataset = r"C:\Users\LENOVO\Documents\new_dataset_projet\dataset\train"
application(dataset)
