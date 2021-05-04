#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point

def testing_msgs_c():
	p=Point()
	p.x=2.5
	p.y=3.0
	pub=rospy.Publisher('my_points',Point,queue_size=10)
	rospy.init_node('testing_msgs_c',anonymous=True)
	rate=rospy.Rate(30)
	while not rospy.is_shutdown():
		rospy.loginfo(p)
		pub.publish(p)
		rate.sleep()

if __name__=='__main__':
	try:
		testing_msgs_c()
	except rospy.ROSInterruptException:
		pass