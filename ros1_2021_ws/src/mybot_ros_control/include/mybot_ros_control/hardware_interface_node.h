#include <hardware_interface/joint_state_interface.h>
#include <hardware_interface/joint_command_interface.h>
#include <hardware_interface/robot_hw.h>
#include <joint_limits_interface/joint_limits.h>
#include <joint_limits_interface/joint_limits_interface.h>
#include <joint_limits_interface/joint_limits_rosparam.h>
#include <joint_limits_interface/joint_limits_urdf.h>
#include <controller_manager/controller_manager.h>
#include <rospy_tutorials/Floats.h>
#include <boost/scoped_ptr.hpp>
#include <ros/ros.h>
#include "geometry_msgs/Twist.h" 
#include "gazebo_msgs/LinkState.h" 

class ROBOTHardwareInterface : public hardware_interface::RobotHW 
{
    public:
        ROBOTHardwareInterface(ros::NodeHandle& nh);
        ~ROBOTHardwareInterface();
        void init();
        void update(const ros::TimerEvent& e);
        void read();
        void write(ros::Duration elapsed_time);
				ros::Publisher pub;
        
    protected:
        hardware_interface::JointStateInterface joint_state_interface_;
        hardware_interface::VelocityJointInterface velocity_joint_interface_;
				
				joint_limits_interface::VelocityJointSaturationInterface VelocityJointSaturationInterface_;
        
				int num_joints_;
				double joint_position_[2];
        double joint_velocity_[2];
				double joint_effort_[2];
        double joint_velocity_command_[2];
        
        ros::NodeHandle nh_;
        ros::Timer my_control_loop_;
        ros::Duration elapsed_time_;
        double loop_hz_;
        boost::shared_ptr<controller_manager::ControllerManager> controller_manager_;
};
