import cv2
from flask import Flask, Response
import threading
import time
import requests

# ==== CONFIGURATION ====
BOT_TOKEN = "8395100522:AAHc-Yy2acAInfbI0eDqwQ2y1CwLZE9LDW8"
CHAT_ID = "1453708579"
KRIA_IP = "172.16.4.7"   # Your Kria IP
PORT = 5000

VIDEO_URL = f"http://{KRIA_IP}:{PORT}/video"

# =======================

app = Flask(__name__)

# Open camera (try /dev/video0 first, fallback /dev/video1)
camera = None
for i in [0, 1]:
    cam = cv2.VideoCapture(i)
    if cam.isOpened():
        camera = cam
        print(f"[*] Using camera /dev/video{i}")
        break

if camera is None:
    raise RuntimeError("❌ No camera found on /dev/video0 or /dev/video1")

# Video frame generator
def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Encode as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Function to run Flask server
def run_flask():
    app.run(host="0.0.0.0", port=PORT, debug=False, use_reloader=False)

# Function to send Telegram alert
def send_telegram_alert():
    time.sleep(10)  # Wait before sending
    message = f"🚨 Video stream started!\n\nClick to watch: {VIDEO_URL}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        r = requests.post(url, data=payload)
        if r.status_code == 200:
            print("[*] Telegram alert sent successfully!")
        else:
            print(f"[!] Failed to send Telegram message: {r.text}")
    except Exception as e:
        print(f"[!] Error sending Telegram message: {e}")

if __name__ == "__main__":
    # Start Flask server in background thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    print(f"[*] Video stream server running at {VIDEO_URL}")

    # Send Telegram alert after 10s
    send_telegram_alert()

    # Keep script alive
    while True:
        time.sleep(1)
