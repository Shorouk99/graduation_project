# Testing Checklist
This document provides a detailed checklist to test the robot's software in a decoupled way, to be able to detect potential problems before testing the whole system's functionality.
The testing procedure is divided into three partions: Low-Level Control testing, Middleware testing, and High-Level Control testing.
In each partion exists several tests to be carried out in either ROS1 or ROS2 or both.


## Low-Level Control Testing
**ROS1**
- IMU data: echo `/imu/data` topic to ensure data is being sent, and perform sanity-check on the resulting data [*Independant*]
- Encoder ticks: echo `/lwheel` and `/rwheel` topics to ensure data is being sent, and perform sanity-check on the resulting data [*Independant*]
- Motors PWM signals: echo `/lmotor_pwr` and `/rmotor_pwr` topics to ensure data is being sent, and perform sanity-check on the resulting data [*Dependant*: depends on `/cmd_vel` topic, which will not contain data untill a goal is sent and being navigated towards] - check at the end of the testing process: after testing the High-Level Control

**ROS2**
- Lidar data: echo `/scan` topic to ensure data is being sent, and perform sanity-check on the resulting data [*Independant*]

## Middleware Testing
**ROS1**
- Odometry publisher: echo `/wheel/odometry` topic to ensure data is being sent, and perform sanity-check on the resulting data [*Dependant*: depends on `/lwheel` and `/rwheel` topics as well as `/initial_2d`, which depends on `/initialpose` topic published by a ROS2 node once after 15 seconds from launching the robot's ROS2 software partion]

**ROS2**
- Odometry: echo `/wheel/odometry` topic to ensure msgs are recieved on ROS2 through the bridge
- IMU: echo `/imu/data` topic to ensure msgs are recieved on ROS2 through the bridge

## High-Level Control Testing
**ROS2**
- Sensor Fusion: echo `/odometry/filtered` to ensure the ekf node is working, and perform sanity-check on the resulting data [*Dependant*: depends on `/wheel/odometry` , `/imu/data`, and the static transform of base_link >> base_footprint. If any of these topics are not *well* supllied the node will not output anything. Also, check the terminal for any error]
- Localization on map: Check rviz to ensure the robot is localized on the map, no 'map frame doesn't exist' message appear, and inflation of obstacle areas is done [*Dependant*: depends on `/odometry/filtered` and `/initialpose` topics]
- Navigation: 
	- send a very close goal using rviz and observe the performance and perform sanity-check
	- echo `/cmd_vel` topic to ensure nav2 is not stuck and perform sanity check on the results
	- once the above is successful, test with a further goal
	- echo `/cmd_vel` topic to ensure nav2 is not stuck and perform sanity check on the results
	- once the above is succesful, test with a dynamic obstacle -an obstacle that isn't visible on the static map
	- echo `/cmd_vel` topic to ensure nav2 is not stuck and perform sanity check on the results
	- [*Dependant*: depends on `/scan` and `/odometry/filtered` topics, static transforms, and map >> odom transform. Performance depends on nav2_parameters]

**Note:** Independant tests don't depend on any other nodes, thus if mulfunction exists, troubleshoot the node itself. On the other hand, tests that depend on multiple nodes have their dependancies listed. Thus, if mulfunction exists, troubleshoot the node itself as well as its dependencies in the order that seems most appropriate. 
