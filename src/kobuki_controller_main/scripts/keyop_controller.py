#!/usr/bin/env python

import rospy
import time
from kobuki_msgs.msg import KeyboardInput
from std_msgs.msg import String

movem = KeyboardInput()
pub = rospy.Publisher('/keyop/teleop', KeyboardInput, queue_size=100)

def talker(msg):
	if (msg.data == 'U'):
		rospy.loginfo("Going forward")
		goForward()
	elif (msg.data == 'L'):
		rospy.loginfo("Going left")
		goLeft()
	elif (msg.data == 'R'):
		rospy.loginfo("Going right")
		goRight()		

def goLeft():
	stopForward()
	pub.publish(68)
	time.sleep(0.1)
	stopLeft()

def stopLeft():
	pub.publish(67)

def goRight():
	stopForward()
	pub.publish(67)
	time.sleep(0.1)
	stopRight()

def stopRight():
	pub.publish(68)

def goForward():
	pub.publish(65)

def stopForward():
	pub.publish(66)

def listener():
	rospy.init_node('keyop_controller', anonymous=True)
	#rate = rospy.Rate(10) #frequency
	#while not rospy.is_shutdown()

#	data = Twist()
#	[data.linear.x, data.linear.y, data.linear.z] = [0.2, 0.0, 0.0]
#	[data.angular.x, data.angular.y, data.angular.z] = [0.0, 0.0, 0.0]
#	previousInput = 'R'
#	pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=100)

	rospy.Subscriber("/random_direction", String, talker)

	rospy.spin()

if __name__ == '__main__':
	try:	
		listener()
	except rospy.ROSInterruptException:
		pass



