# 🤟 Détecteur Intelligent de la Langue des Signes Tunisienne

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?logo=tensorflow)
![Flutter](https://img.shields.io/badge/Flutter-Mobile%20App-blue?logo=flutter)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> Système d'intelligence artificielle pour la détection en temps réel de la Langue des Signes Tunisienne (LST), intégré dans une application mobile Flutter.

---

## 📌 Contexte

La communauté sourde tunisienne compte environ **200 000 personnes**, dont 95 % sont analphabètes. Malgré cette réalité, la Langue des Signes Tunisienne (LST) reste largement non documentée sur le plan informatique.

Ce projet vise à combler ce vide en développant un système de reconnaissance automatique de la LST, avec une application mobile accessible à tous — sourds et entendants — pour favoriser l'inclusion sociale.

---

## 🎯 Fonctionnalités

| Interface | Description |
|---|---|
| 📹 **Détection vidéo** | Reconnaissance des signes LST en temps réel via la caméra |
| 📖 **Dictionnaire** | Consultation des 69 signes avec images/vidéos et traductions en arabe dialectal |
| 🎮 **Jeu éducatif** | Quiz interactif pour apprendre la LST de manière ludique |

---

## 🗂️ Dataset

Le jeu de données a été **entièrement constitué par l'équipe** afin de garantir l'authenticité linguistique des signes, en évitant le risque de "langue de laboratoire" observé dans les projets similaires existants.

- **69 signes** couverts, répartis en 6 catégories :
  - Alphabet latin (26 signes)
  - Jours de la semaine (7 signes)
  - Expressions de salutation (4 signes)
  - Membres de la famille (4 signes)
  - Plats tunisiens (4 signes)
  - Adjectifs (24 signes)
- **Conditions variées** : arrière-plan, luminosité, couleur de vêtements, teints de peau
- **Split** : 80% entraînement / 10% validation / 10% test

---

## ⚙️ Pipeline technique

### Prétraitement des données
```
Vidéos brutes
    → Fragmentation (20 frames/vidéo)
    → Augmentation (rotation, miroir, luminosité, contraste, saturation)
    → Équilibrage (40 images/signe pour l'entraînement)
    → Redimensionnement 224×224 px + normalisation [0,1]
    → Extraction des landmarks MediaPipe Hands (21 points clés/main)
    → Compression au format .npz
```

### Architecture du modèle

```
Input (séquences T×224×224×3)
    → TimeDistributed(MobileNetV2)   ← feature extraction spatiale
    → LSTM                           ← dépendances temporelles
    → Dense(1024, ReLU) + BatchNorm + Dropout
    → Dense(512, ReLU)  + BatchNorm + Dropout
    → Dense(69, Softmax)             ← classification finale
```

- **Backbone** : MobileNetV2 pré-entraîné (ImageNet), couches figées
- **Optimiseur** : Adam avec EarlyStopping
- **Régularisation** : Dropout + BatchNormalization
- **Export** : `.h5` → conversion TensorFlow Lite (`.tflite`) pour mobile

---

## 📱 Application Mobile

Développée avec **Flutter / Dart**, compatible Android et iOS.

```
lib/
├── main.dart
├── screens/
│   ├── home_screen.dart
│   ├── detection_screen.dart
│   ├── dictionnary_screen.dart
│   └── game_screen.dart
├── widgets/
│   ├── custom_button.dart
│   └── video_player.dart
assets/
├── images/      ← médias des signes
└── model/       ← tsl_model.tflite
```

---

## 🛠️ Stack technique

| Composant | Technologies |
|---|---|
| Modèle IA | Python, TensorFlow, Keras, MediaPipe, OpenCV, NumPy |
| Application mobile | Flutter, Dart, TFLite |
| Environnement | Anaconda, Android Studio |
| Gestion de projet | Méthode Agile / Kanban |

---

## 🚧 Limitations & Perspectives

- Les paramètres phonologiques **non-manuels** (expression faciale, direction du regard) ne sont pas modélisés — simplification linguistique intentionnelle pour réduire la complexité du système
- La multicolinéarité entre certains signes représente un défi inhérent à la LST dû à son iconicité forte
- **Perspectives** : enrichissement du dataset, intégration des signes dynamiques complexes, amélioration du pipeline de détection temps réel

---

## 👩‍💻 Auteurs

| Nom | Formation |
|---|---|
| **Smari Jawaher** | Licence en Ingénierie des Systèmes Informatiques — Spécialité IoT & Systèmes Embarqués |
| **Ben Salem Taheni** | Licence en Ingénierie des Systèmes Informatiques — Spécialité IoT & Systèmes Embarqués |

Institut Supérieur d'Informatique et des Technologies de Communication — **ISITCOM Sousse**
Année universitaire : 2024/2025

---

## 📄 Licence

Ce projet est distribué sous licence [MIT](LICENSE).
