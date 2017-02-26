#!/usr/bin/env python

import rospy
#import numpy as np
import random as rn
from std_msgs.msg import String

def globalDirection():
	pub = rospy.Publisher('/random_direction', String, queue_size=100)
	rospy.init_node('random_direction', anonymous=True)
	rate = rospy.Rate(1) #frequency
	previousIn = 'R'
	dummy = 1

	while not rospy.is_shutdown():
		rand = rn.randint(1,100)
		outData = 'U'
		if (rand >= 1 and rand <= 5 and previousIn != 'L'):
			outData = 'R'
		elif (rand >= 11 and rand <= 15 and previousIn != 'R'):
			outData = 'L'
		if (outData == previousIn):
			dummy = 2
			# do nothing
		else:
			pub.publish(outData)
		previousIn = outData
		rate.sleep()
		
if __name__ == '__main__':
	
	try:
		globalDirection()
	except rospy.ROSInterruptException:
		pass
