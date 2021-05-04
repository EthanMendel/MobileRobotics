#!/usr/bin/env python
import rospy
from working_with_msgs.msg import MyMsg

def testing_msgs_a():
	m=MyMsg()
	m.id=6
	m.message="hello"
	pub=rospy.Publisher('mymsg_a',MyMsg,queue_size=10)
	rospy.init_node('testing_msgs_a', anonymous=True)
	rate=rospy.Rate(10)
	while not rospy.is_shutdown():
		#rospy.loginfo(m)
		pub.publish(m)
		rate.sleep()

if __name__=='__main__':
	try:
		testing_msgs_a()
	except rospy.ROSInterruptException:
		pass