from gpiozero import Robot, LineSensor
from time import sleep
robot = Robot(left=(7, 8), right=(9, 10))
left_sensor = LineSensor(29)
left_sensor2 = LineSensor(31)
right_sensor= LineSensor(33)
right_sensor2= LineSensor(35)

speed = 0.65
x=1
def motor_speed():
    while True:
        left_detect  = int(left_sensor.value)
		left_detect2  = int(left_sensor2.value)
        right_detect = int(right_sensor.value)
        right_detect2 = int(right_sensor2.value)
      
        ## basic code 
	    ## if all white --avance
        if left_detect == 0 and right_detect == 0 and left_detect2 == 0 and right_detect2 == 0 :
            left_mot = 1
            right_mot = 1
                                                   
        ## if sensor1 turn right
        if left_detect == 0 and left_detect2 == 0 and (right_detect == 1 or right_detect2 == 1)  :
             left_mot = 1
             right_mot = 0
	   		
		## if sensor 1 and 2 turn right 
		if left_detect == 0 and left_detect2 == 0 and right_detect == 1 and right_detect2 == 1  :
            left_mot = 1
            right_mot = 0
		
		
		## if sensor1 turn left
        if right_detect == 0 and right_detect2 == 0 and (left_detect == 1 or left_detect2 == 1)  :
            left_mot = 0
            right_mot = 1
	   		
		## if sensor 1 and 2 turn left lx 
		if right_detect == 0 and right_detect2 == 0 and left_detect == 1 and left_detect2 == 1  :
            left_mot = 0
            right_mot = 1
			
        ## stop at the line and detect the image  
		if right_detect == 0 and right_detect2 == 0 and left_detect == 0 and left_detect2 == 0:
		     
             ## !!!!!!!!!!!!!!!!!!!!! here need to add face recog test dir/file.py  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 
			
		
		#print(r, l)
        yield (right_mot * speed, left_mot * speed)



robot.source = motor_speed()
sleep(60)
robot.stop()
robot.source = None
robot.close()
left_sensor.close()
right_sensor.close()
left_sensor2.close()
right_sensor2.close()

