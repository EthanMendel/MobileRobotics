#!/usr/bin/env python
import rospy
from turtlebot3_msgs.msg import SensorState
from nav_msgs.msg import Odometry
import math
import tf.transformations

prevLeft=0.0
prevRight=0.0

def buildOdomMsg(x, y, theta, vx, vy, vtheta, odomMsg):
	odomMsg.pose.pose.position.x=x
	odomMsg.pose.pose.position.y=y
	odomMsg.pose.pose.position.z=0.0
	odomMsg.pose.pose.orientation=theta
	odomMsg.twist.twist.linear.x=vx
	odomMsg.twist.twist.linear.y=vy
	odomMsg.twist.twist.angular.z=vtheta
	return odomMsg


def callbacksns(data):
	global prevLeft
	global prevRight
	ld=((data.left_encoder - prevLeft)/4096.0)*.02073
	print("Left Distence:\t%s" % ld)
	rd=((data.right_encoder - prevRight)/4096.0)*.02073
	print("Right Distence:\t%s" % rd)
	d=(ld+rd)/2
	print("Displacement:\t%s" % d)
	#theta = tf.transformations.euler_from_quaternion([x, y, z, w])[2]
	dth=((rd-ld)/(2.0*0.1435))
	print("Delta Theta:\t%s" % dth)
	v=((ld+rd)/(1.0/28.0))/2
	xv=v*math.cos(dth)
	print("x velocity:\t%s" % xv)
	yv=v*math.sin(dth)
	print("y velocity:\t%s" % yv)
	tv=(.02073/(2*.1435))*((rd-ld)/(1.0/28.0))
	print("angular velocity:\t%s" % tv)

	pub=rospy.Publisher('my_odom',Odometry,queue_size=10)
	odomMsg=Odometry()
	pub.publish(buildOdomMsg(d*math.cos(dth), d*math.sin(dth), dth, xv, yv, tv,odomMsg))
	prevLeft=data.left_encoder
	prevRight=data.right_encoder
	print("End Tick")

def run():
	rospy.init_node('odom_compute',anonymous=True)
	rospy.Subscriber('/sensor_state',SensorState,callbacksns)
	
	
	rospy.spin()

if __name__=='__main__':
	try:
		run()
	except rospy.ROSInterruptException:
		pass



def findDistanceBetweenAngles(a, b):
    result = 0
    difference = b - a
    
    if difference > math.pi:
      difference = math.fmod(difference, math.pi)
      result = difference - math.pi

    elif(difference < -math.pi):
      result = difference + (2*math.pi)

    else:
      result = difference

    return result



def displaceAngle(a1, a2):
    a2 = a2 % (2.0*math.pi)

    if a2 > math.pi:
        a2 = (a2 % math.pi) - math.pi

    return findDistanceBetweenAngles(-a1,a2)