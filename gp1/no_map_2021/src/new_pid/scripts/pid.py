#!/usr/bin/env python
from __future__ import division
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Byte
import math
import time
from simple_pid import PID

"""
    *** Velocity PID Control Node ***
    This node is responsible for applying PID control
    over the DC motors to reach certain set velocities
"""

# PID Gains for right motor
pid_r = PID(25.0, 200.0, 0.0, setpoint=0)
pid_r.output_limits = (-255, 255)

# Global Variables for PID of right motor
wr_actual = 0           # Actual Velocity
wr_target = 0           # Target Velocity
action_r = 0            # Control action on right motor

# PID Gains for right motor
#Kp_r = 0.42 #0.6 , 0.42 , 0.8
#Ki_r = 0.15 #0.07 , 0.15 , 0.17
#Kd_r = 0.001 #0.0009, 0.001 , 0.015

# PID Gains for left motor
pid_l = PID(25.0, 200.0, 0.0, setpoint=0)
pid_l.output_limits = (-255, 255)

# Global Variables for PID of left motor
wl_actual = 0
wl_target = 0
action_l = 0

# PID Gains for left motor
#Kp_l = 0.45#2 #0.45
#Ki_l = 0.14#1 #0.14
#Kd_l = 0.001#0.00 #0.001

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
	global goal_flag
	global wr_actual, wr_target, e_wr, e_wr_prev, e_wr_sum, action_r
	global wl_actual, wl_target, e_wl, e_wl_prev, e_wl_sum, action_l

	if((wr_target != 0) or (wl_target != 0)):
		pid_r.setpoint = wr_target
		pid_l.setpoint = wl_target		
		action_r = pid_r(wr_actual)		
		action_l = pid_l(wl_actual)

	if((wr_target == 0) and (wl_target == 0)):
		resetPID()

def wr_act_callback(data):
	global wr_actual
	wr_actual = data.data

def wl_act_callback(data):
	global wl_actual
	wl_actual = data.data

def wr_targ_callback(data):
	global wr_target
	wr_target = data.data

def wl_targ_callback(data):
	global wl_target
	wl_target = data.data

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
