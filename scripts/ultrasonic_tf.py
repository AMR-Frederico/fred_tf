import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped, Vector3, Quaternion
from sensor_msgs.msg import Range

def left_callback(msg): 
    # Define a posição e orientação do sensor ultrassom em relação ao frame base_link
    sensor_pos = [0.05, 0, 0.1] # Exemplo de posição relativa
    sensor_quat = [0, 0, 0, 1] # Exemplo de orientação relativa

    # Cria a mensagem de transformação
    transform = TransformStamped()
    transform.header.stamp = rospy.Time.now()
    transform.header.frame_id = "base_link"
    transform.child_frame_id = "left_ultrasonic_link"
    transform.transform.translation = Vector3(*sensor_pos)
    transform.transform.rotation = Quaternion(*sensor_quat)
    
    ultrasonicLeft_broadcaster.sendTransform(transform)


def back_callback(msg): 
    # Define a posição e orientação do sensor ultrassom em relação ao frame base_link
    sensor_pos = [0.05, 0, 0.1] # Exemplo de posição relativa
    sensor_quat = [0, 0, 0, 1] # Exemplo de orientação relativa

    # Cria a mensagem de transformação
    transform = TransformStamped()
    transform.header.stamp = rospy.Time.now()
    transform.header.frame_id = "base_link"
    transform.child_frame_id = "back_ultrasonic_link"
    transform.transform.translation = Vector3(*sensor_pos)
    transform.transform.rotation = Quaternion(*sensor_quat)
    
    ultrasonicBack_broadcaster.sendTransform(transform)

def right_callback(msg): 
    # Define a posição e orientação do sensor ultrassom em relação ao frame base_link
    sensor_pos = [0.05, 0, 0.1] # Exemplo de posição relativa
    sensor_quat = [0, 0, 0, 1] # Exemplo de orientação relativa

    # Cria a mensagem de transformação
    transform = TransformStamped()
    transform.header.stamp = rospy.Time.now()
    transform.header.frame_id = "base_link"
    transform.child_frame_id = "right_ultrasonic_link"
    transform.transform.translation = Vector3(*sensor_pos)
    transform.transform.rotation = Quaternion(*sensor_quat)
    
    ultrasonicRight_broadcaster.sendTransform(transform)

if __name__ == '__main__':
    rospy.init_node('ultrasonic_sensor_tf_broadcaster')

    ultrasonicLeft_broadcaster = tf2_ros.TransformBroadcaster()
    ultrasonicRight_broadcaster = tf2_ros.TransformBroadcaster()
    ultrasonicBack_broadcaster = tf2_ros.TransformBroadcaster()

    rospy.Subscriber('sensor/range/ultrasonic/left', Range, left_callback)
    rospy.Subscriber('sensor/range/ultrasonic/right', Range, right_callback)
    rospy.Subscriber('sensor/range/ultrasonic/back', Range, back_callback)
    
    rospy.spin()
