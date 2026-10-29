
<div align="center">

# 🧙 Invisible Cloak
### Making Objects Disappear with Computer Vision

**Detect • Mask • Transform**

A fun Python project that uses a webcam, color detection, and background replacement to create an invisibility effect inspired by magical cloaks.

<br/>

![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Computer%20Vision-purple?style=for-the-badge)
![Project](https://img.shields.io/badge/Project-Visual%20Effects-green?style=for-the-badge)

</div>

---

## 🌍 About the Project

**Invisible Cloak** is a computer vision project that creates the illusion of invisibility by detecting objects or regions with a specific color in a webcam feed.

By default, the program detects green using the HSV color space and replaces matching regions with a previously captured background image. This creates an effect similar to an invisible cloak.

The HSV color range can be adjusted to experiment with detecting other colors.

---

## 🚀 Features

- 📷 **Real-Time Webcam Processing:** Analyze the camera feed as the program runs.
- 🎨 **Color Detection:** Identify green regions using HSV color thresholds.
- 👻 **Invisibility Effect:** Replace detected regions with the captured background.
- ⚙️ **Customizable HSV Values:** Adjust the color range to experiment with different colors.
- 🧪 **Interactive Learning:** Explore image masking, segmentation, and background replacement.

---

## 🛠️ Technologies

- **Python:** Core programming language.
- **OpenCV:** Webcam access, image processing, and color detection.
- **NumPy:** Image arrays and mask operations.

---

## ▶️ Getting Started

### Prerequisites

- Python installed on your computer.
- A working webcam.
- Required Python libraries installed.

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd <repository-folder>
   ```

3. Install the dependencies:

   ```bash
   pip install opencv-python numpy
   ```

### Run the Program

Run the main Python script:

```bash
python main.py
```

Replace `main.py` with the actual filename if necessary.

---

## 🎨 Customization

The program uses the **HSV (Hue, Saturation, Value)** color space to identify the target color.

You can adjust the lower and upper HSV thresholds in the source code to experiment with other colors.

For the best results:

- Use a background that remains still.
- Capture the background before introducing the target-colored object.
- Ensure the target color contrasts with the surroundings.
- Use consistent lighting to improve color detection.

---

## 🎓 Learning Objectives

This project introduces several core computer vision concepts:

- Real-time video capture.
- HSV color-space conversion.
- Color thresholding and image segmentation.
- Binary masks and image compositing.
- Background subtraction and replacement.

---

<div align="center">

**Learn • Experiment • Create**

*Turning computer vision concepts into visual magic.*

</div>
