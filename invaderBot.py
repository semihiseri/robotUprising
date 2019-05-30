
#from controller import Robot
from controller import Supervisor
import math

class invaderBot():
    def __init__(self): # this might be overly complicated :/
        #self.robot = Robot()
        self.robot = Supervisor()
        
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
    
    def getPosition(self):
        """
        Returns x, z, angle.
        When looked from above, the coordinate system looks as follows:
           -------------------->x
          |\  (angle)
          | \ 
          |  \
          |   \
          |    \
          |     \
          |
          V
          z
        """
        subject = self.robot.getFromDef("kedi"); # note that kedi is the DEF value, not name!
        position = subject.getPosition()
        orientation = subject.getOrientation()
        orientation = math.atan2(orientation[0], orientation[2])
        orientation = math.degrees(orientation)
        return [position[0],position[2],orientation]
    
    def getGoals(self):
        goals = []
        coinRoot = self.robot.getFromDef("COINS").getField("children")
        
        for idx in reversed(range(coinRoot.getCount())):
            try:
                coin = coinRoot.getMFNode(idx)
                pos = coin.getPosition()
                goals.append([pos[0], pos[2]])
            except:
                pass
        return goals
