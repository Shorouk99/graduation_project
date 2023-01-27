#include <ros/ros.h>
#include <std_msgs/Int8.h>
#include <std_msgs/UInt8.h>
#include <std_msgs/Bool.h>
#include <std_msgs/String.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib/client/simple_action_client.h>
#include <unistd.h>


typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> MoveBaseClient;

//define states of each robot according to move base
int state_donatello;
int state_angelo;

//define state of each robot according to reader
bool flag_donatello;
bool flag_angelo;

//define request of each button
bool reqA_status;
bool reqB_donatello_status;
bool reqB_angelo_status;
//bool reqC_donatello_status;
//bool reqC_angelo_status;
bool reqE_status;
bool reqC_status;

//define overall status of each robot
bool free_angelo;
bool free_donatello;

char goalA[] = "goalA";
char goalB[] = "goalB";
char goalC[] = "goalC";
char goalE[] = "goalE";

void move_donatello_to_goal(char* str)
{

 	MoveBaseClient ac("/move_base", true);

        ROS_INFO("First we are in state ", ac.getState());

	//wait for the action server to come up
	while(!ac.waitForServer(ros::Duration(5.0))){
		ROS_INFO("Waiting for the move_base action server to come up");
	}

	move_base_msgs::MoveBaseGoal goal;

	if(str == goalA)
	{
		//we'll send a goal to the robot to move xx meter forward
		goal.target_pose.header.frame_id = "map";
		goal.target_pose.header.stamp = ros::Time::now();

     
		goal.target_pose.pose.position.x = 0.267513275146;
		goal.target_pose.pose.position.y = -37.3273620605;

		goal.target_pose.pose.orientation.z = 0.752250863692;
		goal.target_pose.pose.orientation.w = 0.658876800376;

	  ROS_INFO("Sending goalA");
  	ac.sendGoal(goal);
           
          ROS_INFO("Now in state ", ac.getState());


	}

	if(str == goalB)
	{
		//we'll send a goal to the robot to move xx meter forward
		goal.target_pose.header.frame_id = "map";
		goal.target_pose.header.stamp = ros::Time::now();

		goal.target_pose.pose.position.x = 12.3553714752;
		goal.target_pose.pose.position.y = -0.775833845139;

		goal.target_pose.pose.orientation.z = -0.764862650669;
		goal.target_pose.pose.orientation.w = 0.644193391469;
	  ROS_INFO("Sending goalB");
  	ac.sendGoal(goal);
	}

	if(str == goalC)
	{	//we'll send a goal to the robot to move xx meter forward
		goal.target_pose.header.frame_id = "map";
		goal.target_pose.header.stamp = ros::Time::now();

		goal.target_pose.pose.position.x = -3.1701540947;
		goal.target_pose.pose.position.y =11.1667633057;

		goal.target_pose.pose.orientation.z = -0.0642696651424;
		goal.target_pose.pose.orientation.w = 0.997932567934;
	  ROS_INFO("Sending goalC after 3 seconds from now");
           usleep(3000000);
  	ac.sendGoal(goal);
	}

	
         if(str == goalE)
	{
		//we'll send a goal to the robot to move xx meter forward
		goal.target_pose.header.frame_id = "map";
		goal.target_pose.header.stamp = ros::Time::now();
 
		goal.target_pose.pose.position.x = 12.3293876648;
		goal.target_pose.pose.position.y = -3.72620582581;

		goal.target_pose.pose.orientation.z = 0.715777235156;
		goal.target_pose.pose.orientation.w = 0.698328683094;
        
	  ROS_INFO("Sending goalE after 3 seconds from now");
        usleep(3000000);
  	ac.sendGoal(goal);
	}

/* ************************************************************************************TESTING ONLY************************************************************************************

	ROS_INFO("Sending goal");
	ac.sendGoal(goal);
*/

}

void move_angelo_to_goal(char* str)
{
 	MoveBaseClient ac("/m_angelo/move_base", true);

	//wait for the action server to come up
	while(!ac.waitForServer(ros::Duration(5.0))){
		ROS_INFO("Waiting for the move_base action server to come up");
	}

	move_base_msgs::MoveBaseGoal goal;

	if(str == goalA)
	{
		//we'll send a goal to the robot to move xx meter forward
		goal.target_pose.header.frame_id = "map";
		goal.target_pose.header.stamp = ros::Time::now();

                goal.target_pose.pose.position.x = 0.899156570435;
		goal.target_pose.pose.position.y = -18.2349052429;
		goal.target_pose.pose.orientation.z = 0.756973096996;
		goal.target_pose.pose.orientation.w = 0.653446042474;
	  ROS_INFO("Sending goalA");
  	ac.sendGoal(goal);

	}

	 if(str == goalB)
	{
		//we'll send a goal to the robot to move xx meter forward
		goal.target_pose.header.frame_id = "map";
		goal.target_pose.header.stamp = ros::Time::now();

		goal.target_pose.pose.position.x = 12.3553714752;
		goal.target_pose.pose.position.y = -0.775833845139;
		goal.target_pose.pose.orientation.z = -0.764862650669;
		goal.target_pose.pose.orientation.w = 0.644193391469;
	  ROS_INFO("Sending goalB");
  	ac.sendGoal(goal);
	}

	 if(str == goalC)
	{
		//we'll send a goal to the robot to move xx meter forward
		goal.target_pose.header.frame_id = "map";
		goal.target_pose.header.stamp = ros::Time::now();

		goal.target_pose.pose.position.x = 1.39353990555;
		goal.target_pose.pose.position.y = 0.211335301399;
		goal.target_pose.pose.orientation.z = 0.075640425086;
		goal.target_pose.pose.orientation.w = 0.0;
	  ROS_INFO("Sending goalC");
  	ac.sendGoal(goal);
	}

         if(str == goalE)
	{
		//we'll send a goal to the robot to move xx meter forward
		goal.target_pose.header.frame_id = "map";
		goal.target_pose.header.stamp = ros::Time::now();

		goal.target_pose.pose.position.x = 12.3293876648;
		goal.target_pose.pose.position.y = -3.72620582581;
		goal.target_pose.pose.orientation.z = 0.715777235156;
		goal.target_pose.pose.orientation.w = 0.698328683094;
	  ROS_INFO("Sending goalE");
  	ac.sendGoal(goal);
	}

/* ************************************************************************************TESTING ONLY************************************************************************************

	ROS_INFO("Sending goal");
	ac.sendGoal(goal);
*/
}

void send_goal(char* str)
{
	ROS_INFO("Function Send Goal");
	std::cout<<str<<std::endl;
	if(str == goalA)
	{

//debugging only make donatello =1 and state = 3 so donatello can be free

               
		/*Check if Dontaello is free or not*/
                state_donatello =3;
                flag_donatello =1;


		if((state_donatello == 3) && (flag_donatello == 1))
			free_donatello = true;
		else
			free_donatello = false;

		/*Check if Michael Angelo is free or not*/
		if((state_angelo == 3) && (flag_angelo == 1))
			free_angelo = true;
		else
			free_angelo = false;

		/*Check if Button is pressed or not*/
		if(reqA_status == 0){
		ROS_INFO("No Request From Goal A");
		}

		else if((reqA_status == 1) && (free_donatello == 1) && (free_angelo == 1))
		{
			ROS_INFO("Donatello and Angelo are free");
			move_donatello_to_goal(str);
		}

		else if((reqA_status == 1) && (free_donatello == 1) && (free_angelo == 0))
		{
			ROS_INFO("Donatello is Free");
			move_donatello_to_goal(str);
		}
		else if((reqA_status == 1) && (free_donatello == 0) && (free_angelo == 1))
		{
			ROS_INFO("Angelo is Free");
			move_angelo_to_goal(str);
		}
		else if((reqA_status == 1) && (free_donatello == 0) && (free_angelo == 0)){ROS_INFO("No one is free");}
	}

	 if(str == goalB)
	{
		ROS_INFO("Going to goal B");
		if(reqB_donatello_status == 1)
			move_donatello_to_goal(str);

		else if(reqB_angelo_status == 1)
			move_angelo_to_goal(str);
	}

	 if(str == goalC)
	{
		ROS_INFO("Going to goal C");
		if(reqC_status== 1)
			move_donatello_to_goal(str);
/*
		else if(reqC_status== 1)
			move_angelo_to_goal(str);
*/
	}

         
         if(str == goalE)
	{
		ROS_INFO("Going to goal E");
		if(reqE_status== 1)
			move_donatello_to_goal(str);
/*
		else if(reqE_status== 1)
			move_angelo_to_goal(str);
*/

	}




}

void goalA_Callback(const std_msgs::Bool::ConstPtr& msg)
{

	reqA_status = msg->data;
	if(reqA_status == 1){
		ROS_INFO("Goal A is requested");
		send_goal(goalA);}

}

void goalB_donatello_Callback(const std_msgs::Bool::ConstPtr& msg)
{
	reqB_donatello_status = msg->data;
	if(reqB_donatello_status == 1)
		send_goal(goalB);
}

void goalB_angelo_Callback(const std_msgs::Bool::ConstPtr& msg)
{
	reqB_angelo_status = msg->data;
	if(reqB_angelo_status == 1)
		send_goal(goalB);
}


//******************************************************************************TRIAL FOR ELEVATOR, UNCOMMENT LATER************************************************************************************//
/*
void goalC_donatello_Callback(const std_msgs::Bool::ConstPtr& msg)
{
	reqC_donatello_status = msg->data;
	if(reqC_donatello_status == 1)
		send_goal(goalC);
}

void goalC_angelo_Callback(const std_msgs::Bool::ConstPtr& msg)
{
	reqC_angelo_status = msg->data;
	if(reqC_angelo_status == 1)
		send_goal(goalC);
}
*/

//******************************************************************************TRIAL FOR ELEVATOR, UNCOMMENT LATER************************************************************************************//
void donatello_flagCallback(const std_msgs::Bool::ConstPtr& msg)
{
	flag_donatello = msg->data;
}

void angelo_flagCallback(const std_msgs::Bool::ConstPtr& msg)
{
	flag_angelo = msg->data;
}

void angelo_stateCallback(const std_msgs::UInt8::ConstPtr& msg)
 {
	//ROS_INFO("I heard from angelo status: %d", msg->data);

	if(msg->data == 1)
		state_angelo = 1;
	else if(msg->data == 2)
		state_angelo = 2;
	else if(msg->data == 3)
		state_angelo = 3;
 }

void donatello_stateCallback(const std_msgs::UInt8::ConstPtr& msg)
 {
	//ROS_INFO("I heard from donatello status: %d", msg->data);

	if(msg->data == 1)
		state_donatello = 1;
	else if(msg->data == 2)
		state_donatello = 2;
	else if(msg->data == 3)
		state_donatello = 3;
 }


void goalE_Callback(const std_msgs::Bool::ConstPtr& msg)
{

	reqE_status = msg->data;
	if(reqE_status == 1)
      {
		ROS_INFO("Goal E is requested");
		send_goal(goalE);
      }

}

void goalC_Callback(const std_msgs::Bool::ConstPtr& msg)
{

	reqC_status = msg->data;
	if(reqC_status== 1)
      {
		ROS_INFO("Goal C is requested");
		send_goal(goalC);
      }

}


int main(int argc, char** argv){

        ros::init(argc, argv, "simple_navigation_goals");
        ros::NodeHandle n ;

        ros::Subscriber sub = n.subscribe("chatter", 1000, goalA_Callback); //goalA_request

        ros::Subscriber subE = n.subscribe("goalE_ZBAR_Request", 1000, goalE_Callback); //goalE_request
        ros::Subscriber subC = n.subscribe("goalC_ZBAR_Request", 1000, goalC_Callback); //goalC_request


	ros::Subscriber sub1 = n.subscribe("goalB_donatello_request", 1000, goalB_donatello_Callback);
	ros::Subscriber sub2 = n.subscribe("goalB_angelo_request", 1000, goalB_angelo_Callback);

	//ros::Subscriber sub3 = n.subscribe("goalC_donatello_request", 1000,goalC_donatello_Callback );
	//ros::Subscriber sub4 = n.subscribe("goalC_angelo_request", 1000, goalC_angelo_Callback);

        ros::Subscriber sub5 = n.subscribe("robot_state_angelo", 1000, angelo_stateCallback);
	ros::Subscriber sub6 = n.subscribe("robot_state_donatello", 1000, donatello_stateCallback);

	ros::Subscriber sub7 = n.subscribe("donatello_flag_status", 1000, donatello_flagCallback);
	ros::Subscriber sub8 = n.subscribe("angelo_flag_status", 1000, angelo_flagCallback);

  //ros::Publisher state = n.advertise<std_msgs::Int8>("goal", 1000);
  //std_msgs::Int8 state_msg;

  ros::spin();
  return 0;
}

