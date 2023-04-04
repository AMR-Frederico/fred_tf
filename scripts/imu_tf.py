import rospy
import tf2_ros
from tf.transformations import *
from sensor_msgs.msg import Imu
from geometry_msgs.msg import TransformStamped, Vector3, Quaternion
import test 

def imu_callback(imu_msg):
    # Define a posição e orientação do IMU em relação ao frame base_link
    imu_pos = Vector3(3.0, 0.0, 0.0)  # exemplo de posição relativa
    imu_quat = imu_msg.orientation

    # Calcula a rotação de 90 graus em torno do eixo Z
    q_rot = Quaternion()
    q_rot.z = 0.707
    q_rot.w = 0.707

    # Aplica a rotação ao quaternion atual do IMU
    imu_quat = quaternion_multiply([imu_quat.x, imu_quat.y, imu_quat.z, imu_quat.w], [q_rot.x, q_rot.y, q_rot.z, q_rot.w])

    # Cria a mensagem de transformação
    transform = TransformStamped()
    transform.header.stamp = rospy.Time.now()
    transform.header.frame_id = "base_link"
    transform.child_frame_id = "imu_link"
    transform.transform.translation = imu_pos
    transform.transform.rotation = Quaternion(*imu_quat)

    # Publica a mensagem de transformação
    tf2_broadcaster.sendTransform(transform)

if __name__ == '__main__':
    rospy.init_node('imu_tf_broadcaster')
    tf2_broadcaster = tf2_ros.TransformBroadcaster()
    rospy.Subscriber('sensor/orientation/imu', Imu, imu_callback)
    rospy.spin()
