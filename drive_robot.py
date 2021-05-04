#!/usr/bin/env python 
import rospy
import math 
import tf.transformations
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry 
from geometry_msgs.msg import Point


odom = Odometry()

def callback(data):
	global odom
	odom = data
	print(odom)

def driveDistance(endDistance, pub):
	cmd = Twist()
	b = Point()
	distance = 0
	global odom 
	b.x= odom.pose.pose.position.x
	b.y = odom.pose.pose.position.y
	cmd.linear.x = .2
	while distance < endDistance and not rospy.is_shutdown():
		pub.publish(cmd)
		distance = math.sqrt((odom.pose.pose.position.x - b.x)**2 + (odom.pose.pose.position.y - b.y)**2)
		#rate.sleep()	

		#print("begin x: " + str(b.x))
		#print("begin y: " + str(b.y))
		#print("cur x: " + str(odom.pose.pose.position.x))
		#print("cur y: " + str(odom.pose.pose.position.y))
		#print ("dist: " + str(distance))
		#print ("EndDist: " + str(endDistance))
		#print("-----------------------------------------")
		#print("-----------------------------------------")

	cmd.linear.x = 0
	pub.publish(cmd)	
		

def turnTo (theta, pub):
	
	cmd = Twist()
	global odom
	cmd.linear.x = 0
	cmd.angular.z = 0.2
	q = [odom.pose.pose.orientation.x,odom.pose.pose.orientation.y,odom.pose.pose.orientation.z,odom.pose.pose.orientation.w]
	
	(roll, pitch, yaw) = tf.transformations.euler_from_quaternion(q)
	angle = yaw
	while abs(angle) <= theta and not rospy.is_shutdown():	
		pub.publish(cmd)
		#rate.sleep
		angle = findDistanceBetweenAngles(odom.pose.pose.orientation.z, theta)
		#print("angle" + str(angle))
		#print("theta" + str(theta))

	cmd.angular.z = 0
	pub.publish(cmd)


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
 
 

def drive_robot():
	msg = Twist()
	msg.linear.x = 0
	msg.angular.x = 0
	rospy.Subscriber("/odom", Odometry, callback)
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)


	rospy.init_node('drive_robot', anonymous=True)
	rate = rospy.Rate(30) 
	
	driveDistance(1.5, pub)
	turnTo(.2, pub)
	while not rospy.is_shutdown():
		pub.publish(msg)
		rate.sleep()
	rospy.spin()
drive_robot()
