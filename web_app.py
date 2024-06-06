import cv2
from flask import Flask, render_template, Response
import threading
from turbojpeg import TurboJPEG, TJPF_BGR, TJSAMP_422, TJFLAG_FASTUPSAMPLE
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class WebApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            logging.error("Could not open video device")
            raise RuntimeError("Could not open video device")
        # Increase resolution to 1920x1080 (1080p)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        self.lock = threading.Lock()
        self.jpeg = TurboJPEG()
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')

        @self.app.route('/video_feed')
        def video_feed():
            return Response(self.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

    def gen_frames(self):
        while True:
            with self.lock:
                ret, frame = self.cap.read()
                if not ret:
                    logging.error("Failed to read frame from camera")
                    continue
                encoded_image = self.jpeg.encode(frame, quality=90, flags=TJFLAG_FASTUPSAMPLE)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + encoded_image + b'\r\n\r\n')

    def run(self, host='0.0.0.0', port=5000):
        logging.info(f"Starting Flask server at http://{host}:{port}")
        self.app.run(host=host, port=port, threaded=True)

    def cleanup(self):
        logging.info("Releasing video capture and cleaning up")
        self.cap.release()
        cv2.destroyAllWindows()
