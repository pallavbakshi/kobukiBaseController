#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

movem = Twist()
#[data.linear.x, data.linear.y, data.linear.z] = [0.2, 0.0, 0.0]
#[data.angular.x, data.angular.y, data.angular.z] = [0.0, 0.0, 0.0]
#previousInput = 'R'
pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=100)

def talker(msg):
	if (msg.data == 'U' and changed == True):
		ros.loginfo("Going forward")
		goStraight()
	elif (msg.data == 'L' and changed == True):
		ros.loginfo("Going left")
		goLeft()
	elif (msg.data == 'R' and changed == True):
		ros.loginfo("Going right")
		goRight()		

def goLeft():
	movem.linear.x = 0
	movem.linear.y = 0
	movem.linear.z = 0
	movem.angular.z = 2.375
	pub.publish(movem)

def goRight():
	movem.linear.x = 0
	movem.linear.y = 0
	movem.linear.z = 0
	movem.angular.z = -2.375
	pub.publish(movem)

def goForward():
	movem.linear.x = 0.2
	movem.linear.y = 0
	movem.linear.z = 0
	movem.angular.z = 0
	pub.publish(movem)

def listener():
	rospy.init_node('m_controller', anonymous=True)
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



