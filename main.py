from threading import Thread
import time
from servo_control import ServoController
from joystick_control import JoystickController
from web_app import WebApp

def control_servos(servo_controller, joystick_controller):
    try:
        while True:
            left_joy_y, right_joy_y = joystick_controller.get_joystick_axes()
            servo_controller.update_angles(left_joy_y, right_joy_y)
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        servo_controller.cleanup()
        joystick_controller.cleanup()

if __name__ == '__main__':
    servo_controller = ServoController(servo_pin1=17, servo_pin2=18)
    joystick_controller = JoystickController()
    web_app = WebApp()

    servo_thread = Thread(target=control_servos, args=(servo_controller, joystick_controller))
    servo_thread.start()
    web_app.run()
