
from jetbot import Robot
class RobotController():

    MAX_MOTORLIMIT = 1.0
    MIN_MOTORLIMIT = 0.0

    def __init__(self):
        self.robot = Robot()


    def action(self, steering, throttle):
        self.robot.left_motor.value = max(min(throttle + steering, self.MAX_MOTORLIMIT), self.MIN_MOTORLIMIT)
        self.robot.right_motor.value = max(min(throttle - steering, self.MAX_MOTORLIMIG), self.MIN_MOTORLIMIT)


    