#include <ros/ros.h>
#include <std_msgs/Int8.h>
#include <std_msgs/Bool.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib/client/simple_action_client.h>
#include <unistd.h>


typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> MoveBaseClient;

#define goal_lab 1
#define goal_elev 2

int request = 0;
bool req_donatello_status = 0;

void goal_elev_Callback(const std_msgs::Bool::ConstPtr& msg)
{
	if(msg->data)
	{
	MoveBaseClient ac("/move_base", true);
	ROS_INFO("Sending Elevator Goal");
	while(!ac.waitForServer(ros::Duration(5.0))){
		ROS_INFO("Waiting for the move_base action server to come up");
	}
	move_base_msgs::MoveBaseGoal goal;
	goal.target_pose.header.frame_id = "map";
	goal.target_pose.header.stamp = ros::Time::now();
	goal.target_pose.pose.position.x = 10.22254467010498;
	goal.target_pose.pose.position.y = -1.047184944152832;
	goal.target_pose.pose.orientation.z = -0.764862650669;
	goal.target_pose.pose.orientation.w = 0.644193391469;
	ROS_INFO("Sending goalB");
	ac.sendGoal(goal);
	}
}

void goal_lab_Callback(const std_msgs::Bool::ConstPtr& msg)
{
	if(msg->data)
	{
	MoveBaseClient ac("/move_base", true);
	ROS_INFO("Sending Elevator Goal");
	while(!ac.waitForServer(ros::Duration(5.0))){
		ROS_INFO("Waiting for the move_base action server to come up");
	}
	move_base_msgs::MoveBaseGoal goal;
	goal.target_pose.header.frame_id = "map";
	goal.target_pose.header.stamp = ros::Time::now();
	goal.target_pose.pose.position.x =  1.4941892623901367; 
	goal.target_pose.pose.position.y = -18.515785217285156;
	goal.target_pose.pose.orientation.z = 0.752250863692;
	goal.target_pose.pose.orientation.w = 0.658876800376;
	ROS_INFO("Sending goalA");
	ac.sendGoal(goal);
	}

}



int main(int argc, char** argv){

	ros::init(argc, argv, "simple_navigation_goals");
        // MoveBaseClient ac("/move_base", true);
        // ROS_INFO("First we are in state ", ac.getState());

    //     while(!ac.waitForServer(ros::Duration(5.0))){
	// 	ROS_INFO("Waiting for the move_base action server to come up");
	// }

    ros::NodeHandle n ;
	ros::Subscriber sub1 = n.subscribe("goal_elev_request", 100, goal_elev_Callback);
	ros::Subscriber sub2 = n.subscribe("goal_lab_request", 10, goal_lab_Callback);

	// move_base_msgs::MoveBaseGoal goal;

	// goal.target_pose.header.frame_id = "map";
	// goal.target_pose.header.stamp = ros::Time::now();

	// ros::Duration(20.0).sleep();
	// goal.target_pose.pose.position.x =  1.4941892623901367; 
	// goal.target_pose.pose.position.y = -18.515785217285156;
	// goal.target_pose.pose.orientation.z = 0.752250863692;
	// goal.target_pose.pose.orientation.w = 0.658876800376;
	// ROS_INFO("Sending goalA");
  	// ac.sendGoal(goal);
	// if (request == goal_lab) {
	// 	goal.target_pose.pose.position.x =  1.4941892623901367; 
	// 	goal.target_pose.pose.position.y = -18.515785217285156;
	// 	goal.target_pose.pose.orientation.z = 0.752250863692;
	// 	goal.target_pose.pose.orientation.w = 0.658876800376;
	// 	ROS_INFO("Sending goalA");
	//   	ac.sendGoal(goal);
	// }

	// if (request == goal_elev) {
	// 	goal.target_pose.pose.position.x = 10.22254467010498;
	// 	goal.target_pose.pose.position.y = -1.047184944152832;
	// 	goal.target_pose.pose.orientation.z = -0.764862650669;
	// 	goal.target_pose.pose.orientation.w = 0.644193391469;
	// 	ROS_INFO("Sending goalB");
	//   	ac.sendGoal(goal);
	// }


  // ros::Publisher state = n.advertise<std_msgs::Int8>("goal", 1000);

  //std_msgs::Int8 state_msg;

  ros::spin();
  return 0;
}

