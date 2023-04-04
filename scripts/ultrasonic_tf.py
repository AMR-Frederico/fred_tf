import rospy
import tf2_ros
import tf2_geometry_msgs
from geometry_msgs.msg import TransformStamped, Vector3, Quaternion

if __name__ == '__main__':
    rospy.init_node('ultrasonic_tf_broadcaster')
    tf2_broadcaster = tf2_ros.TransformBroadcaster()

    # Define a posição e orientação do base_footprint em relação ao frame base_link
    base_pos = Vector3(0.0, 0.0, 0.944) # exemplo de posição relativa
    base_quat = Quaternion(0.0, 0.0, 0.0, 1.0) # exemplo de orientação relativa

    # Cria a mensagem de transformação
    transform = TransformStamped()
    transform.header.stamp = rospy.Time.now()
    transform.header.frame_id = "ultrasonic_link"
    transform.child_frame_id = "base_link"
    transform.transform.translation = base_pos
    transform.transform.rotation = base_quat

    # Publica a mensagem de transformação
    tf2_broadcaster.sendTransform(transform)

    rospy.spin()
