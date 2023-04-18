import rospy
import tf2_ros
import tf_conversions
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import TransformStamped, Vector3, Quaternion

def scan_callback(scan):
    # Define a posição e orientação do rplidar em relação ao frame base_link
    sensor_pos = [0.225, 0, 0.07] # Exemplo de posição relativa
    sensor_quat = tf_conversions.transformations.quaternion_from_euler(0, 0, 0) # Exemplo de orientação relativa

    # Cria a mensagem de transformação
    transform = TransformStamped()
    transform.header.stamp = rospy.Time.now()
    transform.header.frame_id = "base_link"
    transform.child_frame_id = "laser_link"
    transform.transform.translation = Vector3(*sensor_pos)
    transform.transform.rotation = Quaternion(*sensor_quat)

    # Publica a mensagem de transformação
    tf_broadcaster.sendTransform(transform)

if __name__ == '__main__':
    rospy.init_node('rplidar_tf_publisher')
    tf_broadcaster = tf2_ros.TransformBroadcaster()
    scan_subscriber = rospy.Subscriber('/scan', LaserScan, scan_callback)
    rospy.spin()
