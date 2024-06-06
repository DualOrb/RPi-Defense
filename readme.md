# Raspberry Pi Defense System
This project allows you to control / automate a sentry turret (airsoft) using a Raspberry Pi. The video feed is displayed in fullscreen with crosshairs overlaid in the center of the screen.

## Features
- Control servos using an Xbox controller -> lock targets / fire
- Stream live video feed from a USB webcam.
- Display video in fullscreen with crosshairs overlay.

## Requirements
- Raspberry Pi (tested on Raspberry Pi 4)
- USB Webcam (capable of 720p resolution)
- Servos (e.g., SG90, Miuzei Digital Servo MS24)
- Xbox One Controller
- Python 3

## Installation

1. **Update System Packages**

    ```bash
    sudo apt-get update
    sudo apt-get upgrade
    ```

2. **Install Required System Packages**

    ```bash
    sudo apt-get install python3-full libjpeg-turbo8-dev pigpio
    ```

3. **Create and Activate a Virtual Environment**

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

4. **Install Python Packages**

    ```bash
    pip install -r requirements.txt
    ```


## Configuration

- **`web_app.py`**: Set the desired resolution by changing the width and height in the `__init__` method.

    ```python
    self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    ```

## Usage

1. **Connect the USB Webcam** to the Raspberry Pi.

2. **Connect the Servos** to the GPIO pins as described in the code.

3. **Run the Main Script**

    ```bash
    python3 main.py
    ```

4. **Access the Video Feed**

    Open a web browser and go to `http://<your_raspberry_pi_ip>:5000` to view the live webcam feed with crosshairs.

## File Descriptions

- **`main.py`**: Entry point to run the Flask app and control the servos.
- **`servo_control.py`**: Handles servo motor control.
- **`joystick_control.py`**: Handles Xbox controller input.
- **`web_app.py`**: Handles the Flask web server and video streaming.
- **`static/css/styles.css`**: Contains the CSS for styling the video feed and crosshairs.
- **`templates/index.html`**: HTML template for displaying the video feed and crosshairs.
- **`requirements.txt`**: Lists the required Python packages.

## Troubleshooting

- **Black Screen**: Ensure the webcam is properly connected and `/video_feed` route returns a video stream.
- **Controller Not Detected**: Ensure the Xbox controller is connected and recognized by the Raspberry Pi.
- **Video Not Loading**: Check the browser console for errors and ensure the Flask server is running.

## Acknowledgements

This project uses the following open-source libraries:
- Flask
- OpenCV
- Pigpio
- Pygame
- TurboJPEG

## License

This project is licensed under the MIT License.


