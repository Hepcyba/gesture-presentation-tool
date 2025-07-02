# 🎯 SlideMaster – Gesture-Controlled Presentation Tool

A touchless presentation tool built using **Python**, **OpenCV**, **MediaPipe**, and **Reveal.js**, allowing users to control slides **with hand gestures** — no keyboard or mouse required!

---

## ✨ Features

- 👋 **Open Palm** → Start Presentation  
- 👉 **Swipe Right** → Next Slide  
- 👈 **Swipe Left** → Previous Slide  
- 👍 **Thumbs Up** → *(Zoom In - Coming Soon)*  

---

## 🛠️ Tech Stack

| Layer         | Technology       | Purpose                           |
|---------------|------------------|------------------------------------|
| CV Backend    | Python, OpenCV   | Frame capture, processing          |
| Hand Tracking | MediaPipe Hands  | Detects and tracks hand gestures   |
| Frontend      | HTML, CSS, JS    | Web-based slide rendering          |
| Presentation  | Reveal.js        | Lightweight HTML slide framework   |
| Automation    | PyAutoGUI        | Emulates keystrokes from gestures  |

---

## 🎬 Demo Video

🎥 Watch the Gesture-Controlled Presentation in action:  
📹 [Demo 1](https://drive.google.com/file/d/1zk329NhBwfnz9MHGpokI24psfGmvtEha/view?usp=drive_link)  
📹 [Demo 2](https://drive.google.com/file/d/15G-43sry-1W-SiO9YR9YUzP6DgC68j1D/view?usp=drive_link)

---

## 🧠 What I Learned

- Real-time computer vision and gesture recognition  
- Integrating MediaPipe landmarks with actionable logic  
- Interfacing Python with frontend HTML (via Reveal.js + pyautogui)  
- Cross-terminal development and local hosting  
- Debugging real-time gesture inputs  

---

## 📁 Directory Structure
gesture-presentation-tool/
├── gesture_controller.py # Main gesture recognition script
├── requirements.txt # Python dependencies
├── README.md # Project info and usage
└── reveal.js/ # Reveal.js slides (submodule or folder)

---

## 📌 Future Improvements

- ✅ Zoom In/Out gestures  
- 🧭 Pointer on screen using index finger  
- 🎯 Gesture for drawing/annotation  
- 🧪 Add unit tests for gesture functions  
- 🌐 Deploy presentation online for global access  

---

## 🔗 GitHub

👉 [github.com/Hepcyba/gesture-presentation-tool](https://github.com/Hepcyba/gesture-presentation-tool)

