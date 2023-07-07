import rospy
import tf2_ros
from tf.transformations import *
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped, Vector3, Quaternion
import math

def odom_callback(odom_msg):
    # Define a posição e orientação
    robot_position = Vector3(0, 0, 0.08)  # Exemplo de posição relativa
    robot_orientation = odom_msg.pose.pose.orientation

    # q_rot = Quaternion()
    # q_rot.x = 0
    # q_rot.y = 0
    # q_rot.z = math.pi
    # q_rot.w = 0

    # # Aplica a rotação ao quaternion atual do IMU
    # robot_orientation = quaternion_multiply([robot_orientation.x, robot_orientation.y, robot_orientation.z, robot_orientation.w], [q_rot.x, q_rot.y, q_rot.z, q_rot.w])

    # Rotação de 180 graus em torno do eixo Z
    q_rot = quaternion_from_euler(0, 0, math.pi)

    # Aplica a rotação ao quaternion atual do IMU
    robot_orientation = quaternion_multiply([robot_orientation.x, robot_orientation.y, robot_orientation.z, robot_orientation.w], q_rot)



    # Cria a mensagem de transformação
    transform = TransformStamped()
    transform.header.stamp = rospy.Time.now()
    transform.header.frame_id = "odom"
    transform.child_frame_id = "backward_orientation_link"
    transform.transform.translation = robot_position
    transform.transform.rotation = Quaternion(*robot_orientation)

    # Publica a mensagem de transformação
    tf2_broadcaster.sendTransform(transform)

if __name__ == '__main__':
    rospy.init_node('backward_orientation_tf_broadcaster')
    tf2_broadcaster = tf2_ros.TransformBroadcaster()
    rospy.Subscriber('/odom', Odometry, odom_callback)
    rospy.spin()