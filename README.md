# Fred - Transform System (TF)
**note: Package for ROS 1**

## Fred's current TF Tree

![Fred's TF Tree](/tf_tree/FRED_tf.png)

## Transform System
In ROS (Robot Operating System), "TF" refers to "Transformations" or "Transform Frame." It is a system used to track and manage transformations between different coordinate systems in a robotic environment. A coordinate system is associated with each part of the robot and objects in the environment.

![TF frames](/tf_tree/tf_frames.png)

For example, a distance sensor positioned in the middle of the robot, what is the distance measured in relation to the front of the robot? In other words, TF assists in managing orientation systems, especially between sensors and actuators.

Key concepts in TF:

* **Frames:** These are coordinate systems. Each movable part of the robot, such as the base, camera, robotic arm, etc., has its own associated coordinate system.

* **Transformations:** These are the pieces of information that specify how one frame is related to another. For example, the transformation between the robot's base and the camera, indicating how the camera is positioned and oriented relative to the base.

* **TF Tree:** This is a graphical representation of how different frames and their transformations are related to each other. This tree helps in understanding the hierarchy of frames in the environment.

* **TF Broadcaster and Listener:** In ROS, nodes that need to publish or listen to transformations use the TF Broadcaster and Listener. The Broadcaster is used to send transformations, while the Listener is used to receive and utilize these transformations.

## Debug tools 

**Rviz**
```{shell}
rosrun rviz rviz 
```

**TF Tree on RQT visualization**
```{sheel}
rqt
```

**Save TF tree as a PDF file**
```{sheel}
rosrun tf view_frames
evince frames.pdf
```

**See current data**
```{sheel}
rosrun tf tf_monitor <frame1> <frame2>
```

## Fred's previous TF Tree

1. Iron Cup edition
![iron-cup](/tf_tree/iron.png)

2. Hector SLAM tutorial
![hector-tutorial](/tf_tree/hector-tutorial.png)

3. Fred + Hector SLAM 
![fred-and-hector](/tf_tree/fred_hector_slam.png)

