import time
from flyt_python import api
drone = api.navigation()

#10s for sensor initialisation and callibration
time.sleep(3)

#Arm the Drone
drone.arm()

print 'Taking Off'
drone.take_off(10.0)

print 'Mission Underway'
drone.position_set(8.66, 5, 90.082, relative=False)
drone.position_set(-5, 8.66, 90.081, relative=False)
drone.position_set(0, -10, 90.084, relative=False)

print 'Landing'
drone.land(async=False)

#Disarm the Drone
drone.disarm()

#Disconnect from instance
drone.disconnect()
