import cv2
from cv_bridge import CvBridge
import rospy
from sensor_msgs.msg import Image
from linuxpy.video.device import Device, BufferType
import glob

if __name__ == '__main__':

    rospy.init_node('gopro_server', anonymous=True)

    bridge = CvBridge()

    image_pub = rospy.Publisher("/gopro/image_raw",Image)

    num_devices = len(glob.glob('/dev/video*'))

    gopro_cam_ind = 0
    for i in range(num_devices):
        with Device.from_id(i) as cam:
            if 'Elgato' in cam.info.card:
                gopro_cam_ind = i
                break

    # Open the device at the ID 0
    # Use the camera ID based on
    # /dev/videoID needed
    cap = cv2.VideoCapture(gopro_cam_ind)

    #Check if camera was opened correctly
    if not (cap.isOpened()):
        print("Could not open video device")

    #Set the resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    # Capture frame-by-frame
    while not rospy.is_shutdown(): 
        ret, frame = cap.read()

        cv_image = bridge.cv2_to_imgmsg(frame, 'bgr8')
        cv_image.header.stamp = rospy.Time.now()
        image_pub.publish(cv_image)

    # When everything done, release the capture
    cap.release()
