#!/usr/bin/env python2.7
import math
import rospy
import tf.transformations
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

currentOdom = Odometry()

def findDistanceBetweenAngles(a, b):
    result = 0
    difference = b - a
    if difference > math.pi:
      difference = math.fmod(difference, PI)
      result = difference - PI
    elif(difference < -math.pi):
      result = difference + (2*math.pi)
    else:
      result = difference
    return result

# Callback function for odometry data
def odomCb(data):
    global currentOdom
    currentOdom = data


# Drive the robot based on distance
def driveDist(dist, pub):
    # Make a rate to publish messages
    rate = rospy.Rate(30)
    # Get the robot's current odometry info
    tempOdom = currentOdom
    # Initial distance from starting position is 0
    tempDist = 0
    # Create the Twist msg
    vel = Twist()
    vel.linear.x = 0.33 # Speed could be a parameter
    vel.angular.z = 0
    # While we haven't moved the specified distance
    while tempDist < dist and not rospy.is_shutdown():
        # Drive the robot
        pub.publish(vel)
        # Update distance
        tempDist = math.sqrt( math.pow(tempOdom.pose.pose.position.x - currentOdom.pose.pose.position.x,2) + math.pow(tempOdom.pose.pose.position.y - currentOdom.pose.pose.position.y,2) )
        # Sleep
        rate.sleep()
    # Stop robot by publishing 1 more Twist with 0 speed
    vel.linear.x = 0
    pub.publish(vel)


# Turn the robot to a specific orientation value
def turnTo(theta, pub):
    # The orientation before we start turning
    thetaStart = tf.transformations.euler_from_quaternion( [currentOdom.pose.pose.orientation.x, currentOdom.pose.pose.orientation.y, currentOdom.pose.pose.orientation.z, currentOdom.pose.pose.orientation.w] )[2]
    # Get the angle between the robot's current orientation and the target orientation
    thetaDist = findDistanceBetweenAngles(theta, thetaStart)
    # Make a rate
    rate = rospy.Rate(30)
    # Create the Twist msg
    vel = Twist()
    vel.linear.x = 0
    vel.angular.z = 0.785 # Speed could be a parameter
    # Make a threshold to check for stopping the robot
    threshold = 0.35
    # While the robot is not at the specified orientation (or within a small threshold)
    while abs(thetaDist) > threshold and not rospy.is_shutdown():
        # Drive the robot
        pub.publish(vel)
        # Get the robot's current orientation
        thetaNow = tf.transformations.euler_from_quaternion( [currentOdom.pose.pose.orientation.x, currentOdom.pose.pose.orientation.y, currentOdom.pose.pose.orientation.z, currentOdom.pose.pose.orientation.w] )[2]
        # Update the angle between
        thetaDist = findDistanceBetweenAngles(thetaNow, theta)
        print('thetaNow: %s thetaDist: %s' % (thetaNow, thetaDist))
        # Sleep
        rate.sleep()
    # Stop robot by publishing 1 more Twist with 0 speed
    vel.angular.z=0
    pub.publish(vel)



def main():
    rospy.init_node('drive_robot', anonymous=False)

    pubVel = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/odom', Odometry, odomCb)

    rospy.sleep(1)

    #driveDist(0.5, pubVel)
    turnTo(-0.785, pubVel)

    print('Exiting normally')



if __name__ == '__main__':
    main()
