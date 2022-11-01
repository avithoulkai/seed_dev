#!/usr/bin/env python

from multiprocessing.connection import wait
import sys
import rospy
import moveit_commander
import moveit_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_seed_wave')

robot = moveit_commander.RobotCommander
rarm_group = moveit_commander.MoveGroupCommander('rarm')
larm_group = moveit_commander.MoveGroupCommander('larm')
rhand_group = moveit_commander.MoveGroupCommander('rhand')
trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)

rarm_values = rarm_group.get_current_joint_values()
larm_values = larm_group.get_current_joint_values()
rhand_values = rhand_group.get_current_joint_values()

# Make sure arms are set down
rarm_values[0] = 0
rarm_values[1] = 0
rarm_values[2] = 0
rarm_values[3] = 0
rarm_group.set_joint_value_target(rarm_values)
rarm_group.set_max_velocity_scaling_factor(0.9)

larm_values[0] = 0
larm_values[1] = 0
larm_values[2] = 0
larm_values[3] = 0
larm_group.set_joint_value_target(larm_values)
larm_group.set_max_velocity_scaling_factor(0.9)

plan = rarm_group.plan()
plan2 = larm_group.plan()
rarm_group.go(wait=True)
larm_group.go(wait=True)

# Pick arm up and put it in wave location
rarm_values[0] = -0.35
rarm_values[1] = -0.4
rarm_values[3] = -1.75
rarm_group.set_joint_value_target(rarm_values)

plan3 = rarm_group.plan()
rarm_group.go(wait=True)

# Open hand up
rhand_values[0] = 1
rhand_group.set_joint_value_target(rhand_values)

plan4 = rhand_group.plan()
rhand_group.go(wait=True)

# Wave
rarm_values[4] = 1.57
rarm_group.set_joint_value_target(rarm_values)

plan4 = rarm_group.plan()
rarm_group.go(wait=True)

rarm_values[4] = 0.6
rarm_group.set_joint_value_target(rarm_values)

plan5 = rarm_group.plan()
rarm_group.go(wait=True)

rarm_values[4] = 1.57
rarm_group.set_joint_value_target(rarm_values)

plan6 = rarm_group.plan()
rarm_group.go(wait=True)

rarm_values[4] = 0.6
rarm_group.set_joint_value_target(rarm_values)

plan7 = rarm_group.plan()
rarm_group.go(wait=True)

rarm_values[4] = 1.57
rarm_group.set_joint_value_target(rarm_values)

plan8 = rarm_group.plan()
rarm_group.go(wait=True)

rarm_values[4] = 0.6
rarm_group.set_joint_value_target(rarm_values)

plan9 = rarm_group.plan()
rarm_group.go(wait=True)

# Put arms back
rarm_values[0] = 0
rarm_values[1] = 0
rarm_values[2] = 0
rarm_values[3] = 0
rarm_values[4] = 0
rarm_group.set_joint_value_target(rarm_values)

plan10 = rarm_group.plan()
rarm_group.go(wait=True)

# Finish
moveit_commander.roscpp_shutdown
