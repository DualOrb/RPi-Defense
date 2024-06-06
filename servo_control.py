import pigpio

class ServoController:
    def __init__(self, servo_pin1, servo_pin2):
        self.pi = pigpio.pi()
        if not self.pi.connected:
            raise RuntimeError("Could not connect to pigpio daemon")
        self.servo_pin1 = servo_pin1
        self.servo_pin2 = servo_pin2
        self.servo1_angle = 90
        self.servo2_angle = 90
        self.deadzone_threshold = 0.1

    def set_servo_angle(self, gpio, angle):
        pulse_width = 500 + (angle * 2000 / 180)
        self.pi.set_servo_pulsewidth(gpio, pulse_width)

    def apply_deadzone(self, value):
        if abs(value) < self.deadzone_threshold:
            return 0
        return value

    def smooth_transition(self, current_angle, target_angle, step):
        if current_angle < target_angle:
            return min(current_angle + step, target_angle)
        elif current_angle > target_angle:
            return max(current_angle - step, target_angle)
        return current_angle

    def update_angles(self, left_joy_y, right_joy_y):
        left_joy_y = self.apply_deadzone(left_joy_y)
        right_joy_y = self.apply_deadzone(right_joy_y)

        target_angle1 = (left_joy_y + 1) * 90
        target_angle2 = (right_joy_y + 1) * 90

        self.servo1_angle = self.smooth_transition(self.servo1_angle, target_angle1, 0.5)
        self.servo2_angle = self.smooth_transition(self.servo2_angle, target_angle2, 0.5)

        self.set_servo_angle(self.servo_pin1, self.servo1_angle)
        self.set_servo_angle(self.servo_pin2, self.servo2_angle)

    def cleanup(self):
        self.pi.set_servo_pulsewidth(self.servo_pin1, 0)
        self.pi.set_servo_pulsewidth(self.servo_pin2, 0)
        self.pi.stop()
