from lcgrand import *
import math
Q_LIMIT=100
BUSY=1
IDLE=0

def expon(mean):
    val = -mean*math.log(lcgrand(1))
    return val

