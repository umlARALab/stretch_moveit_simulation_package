# stretch_moveit_simulation_package
Package for ROS 2 for getting Hello Robot's Stretch 3 to work in MoveIt 2 simulation.
The original intention was to get it to be able to control the real robot, but right now it is only working in simulation.

To get started, put this package in the src folder of a ROS 2 workspace, then build and source.
The package name is stretch_moveit, so it might be a good idea to rename this folder to stretch_moveit instead of stretch_moveit_simulation_package.
Don't forget to source in every new terminal (`source install/setup.bash`)
Then, run the following:
- `ros2 launch stretch_core stretch_driver.launch.py broadcast_odom_tf:=True`
- `ros2 launch stretch_moveit move_group.launch.py`
- `ros2 launch stretch_moveit moveit_rviz.launch.py`
The order of these 3 commands matters. The above order should work, but if it doesn't, try re-entering them one at a time in a different order. This can resolve some errors.

When rviz2 launches, you should see the Stretch's current position and a Stretch that can be moved for planning.
The gripper plan will most likely start in an invalid position, so just move it into a valid position.
If you need to home the robot (which is likely if you have not already done so), you can close everything that is running, home the robot, and then reopen everything.
Press 'Plan' under the 'Planning' tab to see the plan. If it does not work, it is possible that your Stretch is set up differently. There was something about needing to downgrade rviz2 to a previous version in order to get this to work, so maybe try that.
'Execute' will probably not work, so if anyone can get it working, that would be awesome.
