#include "mybot_ros_control/hardware_interface_node.h"
#include "geometry_msgs/Twist.h"
#include "std_msgs/Float64MultiArray.h" 


ROBOTHardwareInterface::ROBOTHardwareInterface(ros::NodeHandle& nh) : nh_(nh) {

// Declare all JointHandles, JointInterfaces and JointLimitInterfaces of the robot.
    init();
    
// Create the controller manager
    controller_manager_.reset(new controller_manager::ControllerManager(this, nh_));
    
//Set the frequency of the control loop.
    loop_hz_=50;
    ros::Duration update_freq = ros::Duration(1.0/loop_hz_);

//Declare ROS nodes
		pub = nh_.advertise<std_msgs::Float64MultiArray>("/joint_update_to_aurdino",10);
    
//Run the control loop
    my_control_loop_ = nh_.createTimer(update_freq, &ROBOTHardwareInterface::update, this);
}


ROBOTHardwareInterface::~ROBOTHardwareInterface() {
}


void ROBOTHardwareInterface::init() {
        
// Create joint_state_interface for JointA
    hardware_interface::JointStateHandle jointStateHandleA("left_wheel_hinge", &joint_position_[0], &joint_velocity_[0], &joint_effort_[0]);
    joint_state_interface_.registerHandle(jointStateHandleA);
// Create velocity joint interface as JointA accepts effort command.
    hardware_interface::JointHandle jointVelocitytHandleA(jointStateHandleA, &joint_velocity_command_[0]);
    velocity_joint_interface_.registerHandle(jointVelocitytHandleA);  

    
// Create joint_state_interface for JointB
    hardware_interface::JointStateHandle jointStateHandleB("right_wheel_hinge", &joint_position_[1], &joint_velocity_[1], &joint_effort_[1]);
    joint_state_interface_.registerHandle(jointStateHandleB);
// Create velocity joint interface as JointB accepts effort command..
    hardware_interface::JointHandle jointVelocityHandleB(jointStateHandleB, &joint_velocity_command_[1]);
    velocity_joint_interface_.registerHandle(jointVelocityHandleB);       


// Register all joints interfaces    
    registerInterface(&joint_state_interface_);
    registerInterface(&velocity_joint_interface_);
}


//This is the control loop
void ROBOTHardwareInterface::update(const ros::TimerEvent& e) {
    elapsed_time_ = ros::Duration(e.current_real - e.last_real);
    read();
    controller_manager_->update(ros::Time::now(), elapsed_time_);
    write(elapsed_time_);
}

void ROBOTHardwareInterface::read(){
		//geometry_msgs::TwistConstPtr right_msg;
		//geometry_msgs::TwistConstPtr left_msg;
		//right_msg = ros::topic::waitForMessage<geometry_msgs::Twist>("/right_vel");
		//left_msg = ros::topic::waitForMessage<geometry_msgs::Twist>("/left_vel");
		//joint_velocity_[0] = right_msg->angular.z;
		//joint_velocity_[1] = left_msg->angular.z;	

		//lazm el msg tkon pointer w nst5dm arrow operator
		std_msgs::Float64MultiArrayConstPtr msg;
		msg = ros::topic::waitForMessage<std_msgs::Float64MultiArray>("/joint_states_from_arduino");
		joint_position_[0] = msg->data[0];
		joint_position_[1] = msg->data[1];
		joint_velocity_[0] = msg->data[2];
		joint_velocity_[1] = msg->data[3];
		joint_effort_[0] = 0;
		joint_effort_[1] = 0;
}

void ROBOTHardwareInterface::write(ros::Duration elapsed_time) {
/*
		VelocityJointSaturationInterface_.enforceLimits(elapsed_time);
		std_msgs::Float64MultiArray vel;
		vel.data.clear();
		vel.data.push_back(joint_velocity_command_[0]);
		vel.data.push_back(joint_velocity_command_[1]);
		pub.publish(vel);
*/
}


int main(int argc, char** argv)
{

    //Initialze the ROS node.
    ros::init(argc, argv, "MyRobot_hardware_interface_node");
    ros::NodeHandle nh;
    
    //Separate Sinner thread for the Non-Real time callbacks such as service callbacks to load controllers
    ros::MultiThreadedSpinner spinner(2); 
    
    
    // Create the object of the robot hardware_interface class and spin the thread. 
    ROBOTHardwareInterface ROBOT(nh);
    spinner.spin();
    
    return 0;
}
