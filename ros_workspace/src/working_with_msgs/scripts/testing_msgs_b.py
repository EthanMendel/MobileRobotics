#!/usr/bin/env python
import rospy
from working_with_msgs.msg import MyMsg
from nav_msgs.msg import Odometry

def callbackmsg(data):
	print('ID: %s' % data.id)
	print('Message: %s' % data.message)

def callbackodo(data):
	print('X: %s' % data.pose.pose.position.x)
	print('Y: %s' % data.pose.pose.position.y)

def testing_msgs_b():
	rospy.init_node('testing_msgs_b',anonymous=True)
	rospy.Subscriber('mymsg_a',MyMsg,callbackmsg)
	rospy.Subscriber('odom',Odometry,callbackodo)
	rospy.spin()

if __name__=='__main__':
	try:
		testing_msgs_b()
	except rospy.ROSInterruptException:
		pass
