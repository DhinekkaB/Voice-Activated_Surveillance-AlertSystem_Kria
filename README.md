#  Voice-Activated Surveillance & Alert System (Kria)

An **AI-powered real-time surveillance and voice-activated alert system** built on the **AMD Kria SoM** platform.  
This project integrates **computer vision**, **audio sensing**, and **cloud connectivity** to deliver a fully automated, intelligent monitoring solution for security and smart-environment applications.

---

##  Overview

The **Voice-Activated Surveillance & Alert System** merges **video analytics** and **audio processing** on an embedded edge device to provide intelligent, low-latency responses.  
It captures **live camera feeds**, performs **real-time object detection**, and supports **voice-command control** and **sound-triggered alerts**. The system can also send **instant notifications** and **live streams** to a **Telegram bot** for remote monitoring.

---

## ⚙️ Core Functionalities

### 🕵️‍♂️ Real-Time Video Surveillance
- Captures live video from the connected camera on Kria.
- Performs **YOLOv8-based object detection** for accurate recognition.
- Supports custom object categories and human activity detection.

### 🎙️ Voice Activation & Audio Processing
- Uses a **USB microphone** to detect and respond to voice commands.
- Records and processes environmental sounds for alert triggers.
- Compatible with ALSA tools (`arecord`, `aplay`).

### 🔔 Smart Alert & Notification System
- Sends **Telegram alerts** with live stream links and detection messages.
- Supports **voice-triggered emergency SOS alerts**.
- Configurable conditions for when alerts are sent.

### ☁️ Cloud & Remote Monitoring
- Telegram bot integration for **remote monitoring**.
- Real-time access to camera stream and system status.
- Optimized for edge deployment with minimal latency.

---

## 🧩 Hardware Requirements

- 🧠 **AMD Kria KV260 **  
- 📷 **USB Camera (e.g., Logitech C270)**  
- 🎤 **USB Microphone / Audio Device**  
- 💡 **DisplayPort Monitor (optional)**  
- ⚡ **Stable Power Supply / SMPS**

---

## 💻 Software Stack

| Layer | Technology Used |
|-------|------------------|
| **OS** | Ubuntu 22.04 (Kria) |
| **AI Framework** | YOLOv8 (Ultralytics) |
| **Programming** | Python, OpenCV, PyTorch |
| **Audio** | ALSA (`arecord`, `aplay`) |
| **Communication** | Telegram Bot API |
| **Cloud** | Firebase / Telegram Integration |

---

## 🚀 System Flow

1. Initialize Kria peripherals (camera, mic).  
2. Capture video stream and begin YOLOv8 detection.  
3. Monitor audio for keywords or trigger sounds.  
4. Send alerts or video stream links to Telegram bot.  
5. Allow user to control system via voice commands.

---

## 🔒 Use Cases

- 🏠 Home & Industrial Security Monitoring  
- 🚜 Smart Agriculture / Farm Surveillance  
- 🧠 AI-based Emergency Detection  
- 🤖 Autonomous Pet / Patrol Robots *(Future Scope)*  

---

## 🌱 Future Scope

- Integration into **autonomous mobile robots** for movement-based surveillance.  
- On-device **edge AI optimization** using Vitis-AI.  
- Multi-camera & multi-mic support for enhanced coverage.  
- **Cloud analytics dashboard** for insights and alert management.

---

## 🧑‍💻 Developed By

**Dhinekka B**  
*Specialization: VLSI Design & Technology*  

📦 Repository: `Voice-Activated_Surveillance-AlertSystem_Kria`  
💬 Telegram Integration | 🧠 YOLOv8 | 🎙️ Voice Detection | 🚨 Smart Alerts

---

## 🪪 License

This project is licensed under the **MIT License** — feel free to use and modify with proper attribution.

---

## ⭐ Show Your Support

If you found this project useful or inspiring —  
please ⭐ **star this repository** and share it with your peers!
