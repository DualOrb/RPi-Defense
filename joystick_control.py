import pygame

class JoystickController:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        try:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
        except pygame.error:
            raise RuntimeError("No Xbox controller found")

    def get_joystick_axes(self):
        pygame.event.pump()
        left_joy_y = self.joystick.get_axis(1)
        right_joy_y = self.joystick.get_axis(4)
        return left_joy_y, right_joy_y

    def cleanup(self):
        pygame.quit()
