# Robot Simulation Package 
In this package, the robot's main function is simulated, which is autonomous navigation. The robot is simulated using Rviz and Gazebo. ROS2 and Nav2 are used for the autonomous navigation 


## How To Run The Simulation
To run the simulation, you must first ensure the dependencies are installed:
- ROS2 Foxy Fitzroy
- rviz2
- gazebo (Classical Gazebo)
- xacro
- robot_localization
- nav2
- slam_toolbox
- joint_state_publisher_gui
- rqt_robot_steering

Navigate to the workspace root and source it:
```
. install/setup.bash
```
Then launch the launch file corresponding to your desired outcome. Note that there are several launch files engineered to exhibit specific phases of developing the robot's simulation. However, the navigation_sim launch file includes all the phases, and most features can be turned on and off using the launch parameters documented in the launch file

the basic syntax to launch a launch file is as follows:
```
ros2 launch <package_name> <launch_file_name>
```

For example:
```
ros2 launch robot_sim navigation_sim.launch.py
```


## Overview
Building the simulation consists of several phases. First is building the robot's model. The robot's model describes the robot's geometry, physical properties, its components and sensors, etc.
The robot's model(s) will be used to both visualize the robot, and simulate its interactions with the enviroment, as well as the enviroment itself.

The next phase would be programming the robot itself the same way it would have been programmed (mostly except for some obvious modules like hardware interfacing) if it were a real robot in the physical world.
to go through this phase, we will first need to understant briefly the robot's function and how it's performed

In the simulation, the robot's sole function is autonomous navigation. Which means the robot should be able to map its enviroment, and use the generated map to calculate the -almost- most optimal trajectory (global path planning), while avoiding obstacles and regulating the robot's velocity (local path planning).

To be able to perform any of these functions, the robot needs to track its movements. To do so, encoder data can be used to measure the distance traveled by each wheel, and an IMU sensor can be used to measure the robot's rotational velocity and linear acceleration. Each sensor's measurement contains noise and drifting. Thus data from both sensors is fused using Extended Kalman Filter (EKF) from the robot_localization package. The fused data is then published to a topic (/odometry/filtered) and includes the pose (position and orientation) and twist (linear and angular velocities).

To perform the rest of the autonomous navigation tasks, we will use the filtered odomerty data obtained above, alongside data from the lidar which will be published to a topic (/scan). The published message's type is LaserScan and it includes the distance returned from each laser beam sample.

The next step would be building a map for the robot to use in its autonomous navigation. Note that if the robot operates indoors in a an environemt that doesn't change statically, this step can be done only once to generate the map(s).
We will use SLAM to build the map. The slam_toolbox package uses fused odometry data to determine the robot's location relative to the world frame, alongside laser scan data to detect obstacles and log them in the costmap (note that the generated map will be a global costmap, which is a grid whose cell values indicate whether it's occupied by an obstacle or not, it's also called occupancy grid). After the map is built, we can save it as yaml and pgm files using the map_saver launch file.

Now that we have our map, we can use ROS2's navigation stack, which is called nav2, to perform autonomous navigation. Put in simple words, the navigation stack is a collection of packages responsible for the tasks of autnomous navigation like localization, global path planning, local path planning, and much more auxilary tasks. We can integrate those package and tune them according to our specific needs, however, nav2 provides a integration of the basic needed packages to make things easier on developers.
This package is called nav2_bringup, and its most useful feature is the launch files it provides that coordinate the package responsible for the various autonomous navigation tasks. In other words, instead of dealing with and launching numerous nav2 packages, we only need to launch nav2_bringup and tune its paramters in yaml file (nav2_params.yaml).

The basic packages that nav2_bringup include are nav2_amcl (used for robot localization), nav2_planner (used for global path planning), and nav2_controller (used for local path planning and velocity regulation). The other packages included are used for better performance.


## Integrating Everything Together
In the previous section, every module of the robot's simulation and operation was explained individually. To integrate all these packages we create a launch file that launches all these package, and provide the paths to needed files like robot models, maps, and parameters. The paramters files is where the names of the transforms and topics, message types, ..etc., are specified alongside other performance-related paramters. This is how all the packages (which in turn are collections of nodes) communicate and function together. 

