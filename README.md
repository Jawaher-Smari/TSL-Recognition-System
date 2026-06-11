## Introduction

Ce projet représente la réalisation d'un système intelligent pour la reconnaissance en temps réel de la langue des signes tunisienne.

---

## Contexte

La communauté sourde tunisienne compte environ **200 000 personnes**, dont 95 % sont analphabètes. Malgré cette réalité, la Langue des Signes Tunisienne (LST) reste largement non documentée sur le plan informatique.

Ce projet vise à combler ce vide en développant un système de reconnaissance automatique de la LST, avec une application mobile accessible aux sourds et aux entendants pour favoriser l'inclusion sociale.

---

## Fonctionnalités

| Interface Mobile | Description |
|---|---|
| **Détection vidéo en temps réel** | Reconnaissance des signes LST en temps réel via la caméra |
| **Dictionnaire** | Consultation des 69 signes avec images/vidéos et traductions en arabe dialectal |
| **Jeu éducatif** | Quiz interactif pour apprendre la LST de manière ludique |

---

## Dataset

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

## Pipeline technique

### Prétraitement des données
```
Vidéos brutes

- Fragmentation (20 frames/vidéo)
- Augmentation (rotation, miroir, luminosité, contraste, saturation)
- Équilibrage (40 images/signe pour l'entraînement)
- Redimensionnement 224×224 px + normalisation [0,1]
- Extraction des landmarks MediaPipe Hands (21 points clés/main)
- Compression au format .npz
```

### Architecture du modèle

```
Input (séquences T×224×224×3)

- TimeDistributed(MobileNetV2) : pour l'extraction des caractériqtiques spatiale
- LSTM : pour prendre en compte les dépendances temporelles
- Dense(1024, ReLU) + BatchNorm + Dropout
- Dense(512, ReLU)  + BatchNorm + Dropout
- Dense(69, Softmax) : pour la classification finale
```

- **Backbone** : MobileNetV2 pré-entraîné (ImageNet) avec des couches figées
- **Optimiseur** : Adam avec EarlyStopping
- **Régularisation** : Dropout + BatchNormalization
- **Export** : `.h5` → conversion TensorFlow Lite (`.tflite`) pour mobile


---

## Stack technique

| Composant | Technologies |
|---|---|
| Modèle IA | Python, TensorFlow, Keras, MediaPipe, OpenCV, NumPy |
| Application mobile | Flutter, Dart, TFLite |
| Environnement | Anaconda, Android Studio |

---

## Limitations

- Les paramètres phonologiques **non-manuels** (expression faciale, direction du regard) ne sont pas modélisés. C'est une simplification linguistique intentionnelle pour réduire la complexité du système
- La multicolinéarité entre certains signes représente un défi inhérent à la LST dû à son iconicité forte
