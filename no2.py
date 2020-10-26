import rospy as rp
from std_msgs.msg import String


rp.init_node('node_2')

def getMessage(msg2):
    global matricula
    matricula = msg2.data
    soma = 0
    for i in matricula:
        soma +=int(i)
    msg = String()
    msg.data = str(soma)
    pub.publish(msg)

pub = rp.Publisher('/topic2', String, queue_size=1)
sub = rp.Subscriber('/topic1', String, getMessage)
rp.spin()