# 🖼️ AI Watermark Remover

An AI-powered watermark remover built using **YOLOv8**, **PyTorch**, and **OpenCV**. The project automatically detects watermarks and removes them from images without requiring manual coordinates.

---

## 🚀 Features

* ✅ Automatic watermark detection
* ✅ YOLOv8-based object detector
* ✅ OpenCV inpainting for watermark removal
* ✅ Custom dataset generator
* ✅ GPU training support (CUDA)
* ✅ Fully automatic image processing pipeline
* 🔜 Better dataset generation
* 🔜 Segmentation masks
* 🔜 Video watermark removal
* 🔜 Web interface

---

## 📂 Project Structure

```text
watermark-remover-ai
│
├── app.py
├── train.py
├── predict.py
├── remove_watermark.py
├── dataset_generator.py
├── split_dataset.py
├── data.yaml
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Vaibhav007-star/watermark-remover-ai.git
cd watermark-remover-ai
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🏋️ Train the Model

```bash
python train.py
```

The trained weights will be saved in:

```text
runs/detect/watermark_detector/weights/best.pt
```

---

## 🔍 Predict Watermarks

```bash
python predict.py
```

This detects watermarks in input images and saves the results.

---

## 🧹 Remove Watermarks

```bash
python remove_watermark.py
```

Output images are saved automatically.

---

## 🛠 Technologies Used

* Python
* YOLOv8
* PyTorch
* CUDA
* OpenCV
* NumPy

---

## 🗺 Roadmap

### Current

* [x] Watermark detection
* [x] Automatic mask generation
* [x] OpenCV inpainting

### Future

* [ ] Better synthetic dataset generator
* [ ] Segmentation-based detection
* [ ] LaMa inpainting
* [ ] Batch image processing
* [ ] Video watermark remover
* [ ] Flask/FastAPI web interface
* [ ] Desktop application

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Vaibhav Lohchab**

GitHub: https://github.com/Vaibhav007-star
