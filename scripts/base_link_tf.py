import rospy
import tf2_ros
import tf2_geometry_msgs
from geometry_msgs.msg import TransformStamped, Vector3, Quaternion

if __name__ == '__main__':
    rospy.init_node('base_footprint_to_base_link_tf')
    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            # Obter a transformação do frame base_footprint para o frame base_link
            trans = tf_buffer.lookup_transform('base_link', 'base_footprint', rospy.Time())

            # Criar a mensagem de transformação
            transform = TransformStamped()
            transform.header.stamp = rospy.Time.now()
            transform.header.frame_id = trans.header.frame_id
            transform.child_frame_id = trans.child_frame_id
            transform.transform.translation = Vector3(trans.transform.translation.x,
                                                       trans.transform.translation.y,
                                                       trans.transform.translation.z)
            transform.transform.rotation = Quaternion(trans.transform.rotation.x,
                                                       trans.transform.rotation.y,
                                                       trans.transform.rotation.z,
                                                       trans.transform.rotation.w)

            # Publicar a mensagem de transformação
            tf2_broadcaster = tf2_ros.TransformBroadcaster()
            tf2_broadcaster.sendTransform(transform)

        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            pass

        rate.sleep()
