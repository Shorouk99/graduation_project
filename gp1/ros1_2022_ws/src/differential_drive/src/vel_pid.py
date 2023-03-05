#!/usr/bin/env python
from __future__ import division
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Byte
import math
import time

"""
    *** Velocity PID Control Node ***
    This node is responsible for applying PID control
    over the DC motors to reach certain set velocities
"""

# Global Variables for PID of right motor
wr_actual = 0           # Actual Velocity
wr_target = 0           # Target Velocity
e_wr = 0                # Error in Velocity
e_wr_prev = 0           # Derivative term
e_wr_sum = 0            # Intergal Term
action_r = 0            # Control action on right motor
# PID Gains for right motor
Kp_r = 105.0	#155.0
Ki_r = 7.0		#9.0
Kd_r = 0.1		#0.01

#####################################################################
#####################################################################

# Global Variables for PID of left motor
wl_actual = 0
wl_target = 0
e_wl = 0
e_wl_prev = 0
e_wl_sum = 0
action_l = 0
# PID Gains for left motor
Kp_l = 100.0	#150.0
Ki_l = 7.0		#9.0	
Kd_l = 0.1 	#0.01

# The function resets all PID variables for a clean start
def resetPID():
	global wr_actual, wr_target, e_wr, e_wr_prev, e_wr_sum, action_r
	global wl_actual, wl_target, e_wl, e_wl_prev, e_wl_sum, action_l
	# Reset terms to start cleanly next time
	e_wr = 0
	e_wr_prev = 0
	e_wr_sum = 0
	action_r = 0

	e_wl = 0
	e_wl_prev = 0
	e_wl_sum = 0
	action_l = 0

def PID():
	global wr_actual, wr_target, e_wr, e_wr_prev, e_wr_sum, action_r
	global wl_actual, wl_target, e_wl, e_wl_prev, e_wl_sum, action_l

	if((wr_target != 0) or (wl_target != 0)):
		# Calculate error
		e_wr = wr_target - wr_actual
		e_wl = wl_target - wl_actual

		# Calculate Output
		action_r = (e_wr * Kp_r) + (e_wr_sum * Ki_r) + (e_wr_prev * Kd_r)
		action_l = (e_wl * Kp_l) + (e_wl_sum * Ki_l) + (e_wl_prev * Kd_l)

		# Saturating Output to -100 , 100
		action_r = max(min(255, action_r), -255)
		action_l = max(min(255, action_l), -255)

		# Update Derivative Term
		e_wr_prev = e_wr
		e_wl_prev = e_wl

		# Update Integral Term
		e_wr_sum += e_wr
		e_wl_sum += e_wl

		# Saturating Integral Term to Prevent Integral Windup
		e_wr_sum = max(min(150, e_wr_sum), -150)
		e_wl_sum = max(min(150, e_wl_sum), -150)

	if((wr_target == 0) and (wl_target == 0)):
		resetPID()


def wr_act_callback(right_vel):
	global wr_actual
	wr_actual = right_vel.data
	
def wl_act_callback(left_vel):
	global wl_actual
	wl_actual = left_vel.data

def wr_targ_callback(right_target):
	global wr_target
	wr_target = right_target.data

def wl_targ_callback(left_target):
	global wl_target
	wl_target = left_target.data


if __name__ == '__main__':

	# Defining the ros node
	rospy.init_node('motion_control')

	#Initializing Publisher
	r_pwr = rospy.Publisher('rmotor_pwr', Float64, queue_size = 10)
	l_pwr = rospy.Publisher('lmotor_pwr', Float64, queue_size = 10)

	#Initializing Subscriber
	rospy.Subscriber('rwheel_vel', Float64, wr_act_callback)
	rospy.Subscriber('lwheel_vel', Float64, wl_act_callback)
	rospy.Subscriber('rwheel_vtarget', Float64, wr_targ_callback)
	rospy.Subscriber('lwheel_vtarget', Float64, wl_targ_callback)

	rate = rospy.Rate(50)

	while not rospy.is_shutdown():
		PID()
		r_pwr.publish(action_r)
		l_pwr.publish(action_l)
		rate.sleep()

