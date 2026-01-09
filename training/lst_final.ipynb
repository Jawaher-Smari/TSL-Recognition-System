{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f5cf4048-64fc-41bd-8a16-05c2dd5b0d1d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import importlib\n",
    "import detection_utils_modifié\n",
    "importlib.reload(detection_utils_modifié)\n",
    "\n",
    "from detection_utils_modifié import detect_hands, process_npz, process_npy_folder\n",
    "\n",
    "hands = detect_hands(detection_confidence=0.7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f01a5f4-b82a-48e4-8f6b-d7503ffb7754",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import numpy as np\n",
    "import tensorflow as tf\n",
    "\n",
    "from tensorflow.keras import Input, Model\n",
    "from tensorflow.keras.layers import (\n",
    "    TimeDistributed,\n",
    "    GlobalAveragePooling2D,\n",
    "    LSTM,\n",
    "    Dense,\n",
    "    BatchNormalization,\n",
    "    Dropout\n",
    ")\n",
    "from tensorflow.keras.applications import MobileNetV2\n",
    "from tensorflow.keras.optimizers import Adam\n",
    "from tensorflow.keras.callbacks import (\n",
    "    EarlyStopping,\n",
    "    ReduceLROnPlateau,\n",
    "    ModelCheckpoint,\n",
    "    TensorBoard\n",
    ")\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "babd1e63-7433-426b-aaf7-85aafd5374cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "T = 20                  \n",
    "size = 224         \n",
    "classes_number = 69        \n",
    "batch_size = 16\n",
    "epochs = 15\n",
    "learning_rate = 1e-4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d2807f4-9091-4001-b08a-c5147e948f3e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def npz_generator(npz_path, sequential):\n",
    "    data = np.load(npz_path, mmap_mode=\"r\")\n",
    "    X, y = data[\"X\"], data[\"y\"]\n",
    "    N = X.shape[0]\n",
    "    for i in range(N):\n",
    "        xi = X[i]  # shape = (t, H, W, C) ou (1, H, W, C)\n",
    "        label = int(y[i])\n",
    "        if not sequential:\n",
    "            xi = np.repeat(xi, repeats=T, axis=0)\n",
    "        yield xi.astype(np.float32), label"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c15e82e-6fe1-43df-9375-98d4069721eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def npy_generator(folder_path, sequential):\n",
    "    X = np.load(os.path.join(folder_path, \"X.npy\"), mmap_mode=\"r\")\n",
    "    y = np.load(os.path.join(folder_path, \"y.npy\"), mmap_mode=\"r\")\n",
    "    N = X.shape[0]\n",
    "    for i in range(N):\n",
    "        xi = X[i]  # shape = (t, H, W, C) ou (1, H, W, C)\n",
    "        label = int(y[i])\n",
    "        if not sequential:\n",
    "            xi = np.repeat(xi, repeats=T, axis=0)\n",
    "        yield xi.astype(np.float32), label"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f7a9e941-754d-43ed-a988-5fb9f673d60c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_npz_via_generator(npz_path, sequential):\n",
    "    output_types = (tf.float32, tf.int32)\n",
    "    output_shapes = ((T, size, size, 3), ())\n",
    "    ds = tf.data.Dataset.from_generator(\n",
    "        lambda: npz_generator(npz_path, sequential),\n",
    "        output_types=output_types,\n",
    "        output_shapes=output_shapes\n",
    "    )\n",
    "    return (\n",
    "        ds\n",
    "        .shuffle(buffer_size=1000)      \n",
    "        .batch(batch_size)             \n",
    "        .prefetch(tf.data.AUTOTUNE)\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7699fb8-951f-4cff-91a3-1e90d907fe38",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_npy_via_generator(folder_path, sequential):\n",
    "    output_types = (tf.float32, tf.int32)\n",
    "    output_shapes = ((T, size, size, 3), ())\n",
    "    ds = tf.data.Dataset.from_generator(\n",
    "        lambda: npy_generator(folder_path, sequential),\n",
    "        output_types=output_types,\n",
    "        output_shapes=output_shapes\n",
    "    )\n",
    "    return (\n",
    "        ds\n",
    "        .shuffle(buffer_size=1000)\n",
    "        .batch(batch_size)\n",
    "        .prefetch(tf.data.AUTOTUNE)\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "12ca9e9f-5db3-40d4-9f43-aa6223c68b72",
   "metadata": {},
   "outputs": [],
   "source": [
    "train_seq_ds = load_npz_via_generator(r\"C:\\Users\\21654\\Downloads\\dataset_again\\train_sequences.npz\", sequential=True)\n",
    "val_seq_ds   = load_npz_via_generator(r\"C:\\Users\\21654\\Downloads\\dataset_again\\valid_sequences.npz\",   sequential=True)\n",
    "\n",
    "train_static_ds = load_npy_via_generator(r\"C:\\Users\\21654\\Downloads\\dataset_again\\train_static_unzipped\", sequential=False)\n",
    "val_static_ds   = load_npz_via_generator(r\"C:\\Users\\21654\\Downloads\\dataset_again\\valid_static.npz\",   sequential=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ebda605-3f67-4746-bc18-9d9fcada4863",
   "metadata": {},
   "outputs": [],
   "source": [
    "train_ds = train_seq_ds.concatenate(train_static_ds)\n",
    "val_ds   = val_seq_ds.concatenate(val_static_ds)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70a09ec8-f8fd-49dd-88ae-23e5101004bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_batch, y_batch = next(iter(train_ds))\n",
    "plt.imshow(X_batch[0,0]); plt.title(int(y_batch[0])); plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aee86cef-747b-43d7-9755-a34187e62d23",
   "metadata": {},
   "outputs": [],
   "source": [
    "inputs = Input(shape=(T, size, size, 3))\n",
    "base = MobileNetV2(input_shape=(size, size, 3),\n",
    "                   include_top=False, weights=\"imagenet\")\n",
    "base.trainable = False\n",
    "\n",
    "\n",
    "x = TimeDistributed(base)(inputs)\n",
    "x = TimeDistributed(GlobalAveragePooling2D())(x)\n",
    "x = LSTM(128)(x)\n",
    "x = Dense(1024, activation=\"relu\")(x)\n",
    "x = BatchNormalization()(x)\n",
    "x = Dropout(0.3)(x)\n",
    "x = Dense(512, activation=\"relu\")(x)\n",
    "x = BatchNormalization()(x)\n",
    "x = Dropout(0.3)(x)\n",
    "outputs = Dense(classes_number, activation=\"softmax\")(x)\n",
    "\n",
    "model = Model(inputs, outputs)\n",
    "model.compile(optimizer=Adam(learning_rate),\n",
    "              loss=\"sparse_categorical_crossentropy\",\n",
    "              metrics=[\"accuracy\",\n",
    "                       tf.keras.metrics.TopKCategoricalAccuracy(3)])\n",
    "model.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "13205fc5-70b6-4dc9-9df6-bf748f6ccbc5",
   "metadata": {},
   "outputs": [],
   "source": [
    "callbacks = [\n",
    "    EarlyStopping(monitor=\"val_loss\", patience=5, restore_best_weights=True),\n",
    "    ReduceLROnPlateau(monitor=\"val_loss\", factor=0.5, patience=3),\n",
    "    ModelCheckpoint(\"best_model.h5\", save_best_only=True),\n",
    "    TensorBoard(log_dir=\"logs\", histogram_freq=1)\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec34ccc3-2305-4b01-ac62-7f1353bc9072",
   "metadata": {},
   "outputs": [],
   "source": [
    "history = model.fit(train_ds,\n",
    "                    validation_data=val_ds,\n",
    "                    epochs=epochs,\n",
    "                    callbacks=callbacks)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eaba3d01-237a-48ad-b117-f928bc4bc77b",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_seq_ds = load_npz_via_generator(r\"C:\\Users\\21654\\Downloads\\dataset_again\\test_sequences.npz\", sequential=True)\n",
    "\n",
    "test_static_ds = load_npz_via_generator(r\"C:\\Users\\21654\\Downloads\\dataset_again\\test_static.npz\", sequential=False)\n",
    "\n",
    "test_ds = test_seq_ds.concatenate(test_static_ds)\n",
    "\n",
    "results = model.evaluate(test_ds)\n",
    "print(f\"Test loss: {results[0]:.4f}\")\n",
    "print(f\"Test accuracy: {results[1]:.4%}\")\n",
    "print(f\"Test top-3 accuracy: {results[2]:.4%}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78ba48da-18ff-4939-a332-7cb57985864e",
   "metadata": {},
   "outputs": [],
   "source": [
    "model.save(\"tsl_model.h5\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04d24fa2-6eb3-4cee-9892-4f6f9fbcf726",
   "metadata": {},
   "outputs": [],
   "source": [
    "converter = tf.lite.TFLiteConverter.from_keras_model(model)\n",
    "\n",
    "converter.target_spec.supported_ops = \n",
    "    tf.lite.OpsSet.TFLITE_BUILTINS,    \n",
    "    tf.lite.OpsSet.SELECT_TF_OPS       \n",
    "    \n",
    "converter._experimental_lower_tensor_list_ops = False\n",
    "\n",
    "tflite_model = converter.convert()\n",
    "with open(\"tsl_model.tflite\", \"wb\") as f:\n",
    "    f.write(tflite_model)\n",
    "\n",
    "print(\"Success\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "771d4c80-16cc-4260-b1bc-9b0079cd87c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import mediapipe as mp\n",
    "from collections import deque\n",
    "from tensorflow.keras.models import load_model\n",
    "\n",
    "model     = \"tsl_model.h5\"\n",
    "T              = 20\n",
    "size       = 224\n",
    "min_confidence = 0.7\n",
    "\n",
    "class_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'behi', 'belhak', 'berda', 'beshwaya', 'esmi', 'express', 'fayek', 'hayej', 'ksir', 'masdoum', 'metghashesh', 'njewbek', 'omi', 'raked', 'tjewbni', 'twil', 'yaayshek', 'yakra', 'yekhdem', 'yemshi', 'Z', 'ahad', 'asam', 'baba', 'chorba', 'cv', 'erbaa', 'essalem', 'fhemt', 'jomaa', 'kafteji', 'khayeb', 'khmis', 'khouya', 'kosksi', 'lablebi', 'merci', 'okhti', 'sebt', 'skhouna', 'slata_meshwiya', 'thleth', 'thnin', 'tounsi']\n",
    "classes_number = len(class_names)\n",
    "\n",
    "model = load_model(model)\n",
    "assert model.output_shape[-1] == classes_number, (\n",
    "    f\"Le modèle prévoit {model.output_shape[-1]} classes, \"\n",
    "    f\"tu en as défini {classes_number} dans class_names.\"\n",
    ")\n",
    "\n",
    "mediapipe_hands = mp.solutions.hands\n",
    "hands = mediapipe_hands.Hands(static_image_mode = False, number_of_hands = number_of_hands, detection_confidence = detection_confidence, tracking_confidence = tracking_confidence)\n",
    "\n",
    "def box(landmarks, img_shape, margin=0.5):\n",
    "    h, w, _ = img_shape\n",
    "    xs = [lm.x for lm in landmarks.landmark]\n",
    "    ys = [lm.y for lm in landmarks.landmark]\n",
    "    min_x, max_x = max(min(xs), 0), min(max(xs), 1)\n",
    "    min_y, max_y = max(min(ys), 0), min(max(ys), 1)\n",
    "    x1, y1 = int(min_x * w), int(min_y * h)\n",
    "    x2, y2 = int(max_x * w), int(max_y * h)\n",
    "    dx, dy = int((x2 - x1) * margin), int((y2 - y1) * margin)\n",
    "    return max(0, x1 - dx), max(0, y1 - dy), min(w, x2 + dx), min(h, y2 + dy)\n",
    "\n",
    "cap = cv2.VideoCapture(0)\n",
    "\n",
    "# Un seul deque partagé pour toutes les mains\n",
    "frames_deque = deque(maxlen=T)\n",
    "\n",
    "while True:\n",
    "    ret, frame = cap.read()\n",
    "    if not ret:\n",
    "        break\n",
    "\n",
    "    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)\n",
    "    results = hands.process(rgb)\n",
    "\n",
    "    if results.multi_hand_landmarks:\n",
    "        for lm in results.multi_hand_landmarks:\n",
    "            x1, y1, x2, y2 = box(lm, frame.shape)\n",
    "\n",
    "            roi = frame[y1:y2, x1:x2]\n",
    "            if roi.size == 0:\n",
    "                roi = frame\n",
    "            roi = cv2.resize(roi, (size, size))\n",
    "            roi_norm = roi.astype(np.float32) / 255.0\n",
    "\n",
    "            # Ajoute l'image au buffer\n",
    "            frames_deque.append(roi_norm)\n",
    "            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)\n",
    "\n",
    "            # Prédiction quand T frames sont collectées\n",
    "            if len(frames_deque) == T:\n",
    "                seq = np.stack(frames_deque, axis=0)\n",
    "                seq = np.expand_dims(seq, axis=0)\n",
    "\n",
    "                preds = model.predict(seq, verbose=0)[0]\n",
    "                idx = np.argmax(preds)\n",
    "                label = class_names[idx]\n",
    "                prob = preds[idx]\n",
    "\n",
    "                # Affichage\n",
    "                text = f\"{label} ({prob*100:.1f}%)\"\n",
    "                cv2.putText(frame, text, (x1, y1 - 10),\n",
    "                            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255), 2)\n",
    "\n",
    "    cv2.imshow(\"Detection\", frame)\n",
    "    if cv2.waitKey(1) & 0xFF == 27:  # ESC pour quitter\n",
    "        break\n",
    "\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
