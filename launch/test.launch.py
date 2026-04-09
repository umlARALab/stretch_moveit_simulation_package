from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_moveit_rviz_launch

# copy of demo.launch

def generate_launch_description():
    moveit_config = (MoveItConfigsBuilder("stretch", package_name="stretch_moveit")
                     .planning_pipelines(pipelines=["ompl"])
                     .robot_description(file_path="config/stretch.urdf.xacro")
                     .robot_description_semantic(file_path="config/stretch.srdf")
                     .trajectory_execution(file_path="config/moveit_controllers.yaml")
                     .robot_description_kinematics(file_path="config/kinematics.yaml")
                     .planning_scene_monitor(
        publish_robot_description_semantic=True
    )
        .to_moveit_configs()
    )
    return generate_demo_launch(moveit_config)
    
