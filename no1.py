import rospy as rp
from std_msgs.msg import String


rp.init_node('node_1')

def getBack(msg2):
    global volta
    volta = msg2.data
    print(volta)

def timerCallBack(event):
    msg1 = String()
    msg1.data = '2016002046'
    pub.publish(msg1)


pub = rp.Publisher('/topic1', String, queue_size=1)
timer = rp.Timer(rp.Duration(0.1), timerCallBack)
sub = rp.Subscriber('/topic2', String, getBack)

rp.spin()