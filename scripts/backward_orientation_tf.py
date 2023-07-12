import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped
from tf.transformations import quaternion_from_euler, euler_from_quaternion

if __name__ == '__main__':
    rospy.init_node('backward_frame_publisher')
    tf_broadcaster = tf2_ros.TransformBroadcaster()
    
    # Loop principal
    rate = rospy.Rate(10)  # Frequência de publicação (10 Hz)
    while not rospy.is_shutdown():
        try:
            # Obter a transformação entre os frames "base_link" e "odom"
            tf_buffer = tf2_ros.Buffer()
            tf_listener = tf2_ros.TransformListener(tf_buffer)
            transform = tf_buffer.lookup_transform("odom", "base_link", rospy.Time(0), rospy.Duration(1.0))
            
            # Configurar a transformação do frame "backward_orientation_link" com base na transformação do frame "base_link"
            backward_transform = TransformStamped()
            backward_transform.header.stamp = rospy.Time.now()
            backward_transform.header.frame_id = "odom"
            backward_transform.child_frame_id = "backward_orientation_link"
            
            # Aplicar a rotação de 180° em torno do eixo Z à orientação da transformação
            quaternion = (
                transform.transform.rotation.x,
                transform.transform.rotation.y,
                transform.transform.rotation.z,
                transform.transform.rotation.w
            )
            euler = euler_from_quaternion(quaternion)
            euler = (euler[0], euler[1], euler[2] + 3.14159)  # Rotação de 180° em radianos
            quaternion = quaternion_from_euler(euler[0], euler[1], euler[2])
            
            backward_transform.transform.translation = transform.transform.translation
            backward_transform.transform.rotation.x = quaternion[0]
            backward_transform.transform.rotation.y = quaternion[1]
            backward_transform.transform.rotation.z = quaternion[2]
            backward_transform.transform.rotation.w = quaternion[3]
            
            # Publicar a transformação do frame "backward_orientation_link"
            tf_broadcaster.sendTransform(backward_transform)
        
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rospy.logwarn("Failed to lookup transform from 'base_link' to 'odom'")
        
        rate.sleep()
