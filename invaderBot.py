
from controller import Robot


class invaderBot():
    def __init__(self): # this might be overly complicated :/
        self.robot = Robot()
        
        def setup_motors(robot, motor_names):
            return [robot.getMotor(motor_name) for motor_name in motor_names]
        
        (self.m_fl, self.m_fr, self.m_rl, self.m_rr) = setup_motors(self.robot, ["front_left", "front_right", "rear_left", "rear_right"])
        
        self.leftMotor = 0
        self.rightMotor = 0
        
        self.timestep = int(self.robot.getBasicTimeStep())
        
    def setup(self): # let's have this here for cross-language compatibility -it will be needed for C
        pass
    
    def doTimeStep(self):
        return (self.robot.step(self.timestep) != -1)
    
    def setMotors(self, left, right):
        def _setMotors(inp, motors):
            mult = 1 if inp > 0 else -1
            for motor in motors:
                motor.setPosition(mult*float('+inf'))
                motor.setVelocity(inp)
        
        def setAllMotors(speeds):
            motors = (self.m_fl, self.m_rl, self.m_fr, self.m_rr)
            for i, speed in enumerate(speeds):
                _setMotors(speed, [motors[i]])
            
        setAllMotors((left, left, right, right))
        
        self.left = left
        self.right = right
    
    def setLeftMotor(self, value):
        self.left = value
        setMotors(self.left, self.right)
        
    
    def setRightMotor(self, value):
        self.right = value
        setMotors(self.left, self.right)
