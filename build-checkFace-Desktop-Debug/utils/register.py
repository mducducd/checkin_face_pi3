import shutil
import time
# from utils.face_encoding import Register
# from utils.picamera_setup import Pi_Cam
from utils import *
from config import *
# from finger_enroll import fingerprinter_enroll
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--id', type=str, default='new-guy', help='id number')
args = parser.parse_args()
name = args.id


def register():
    delete_content(option_file)
    # Generate Annoy tree
    t = Annoy(dim=128, distance='euclidean')
    # Set up camera
    camera = Pi_Cam('register')
    print('tao xong cam')

    camera.start_preview()
    camera.overlay_alpha_box()
    for sec in range(5, -1, -1):
        time.sleep(1)
        print(sec)
        write_log(notification_file, look_straight + str(sec))
    time.sleep(0.5)
    # Shotting image
    camera.capture()
    camera.overlay_image()
    print('da chup, previewing')
    # Enroll
    register = Register()
    print('tao enroll')
    write_log(notification_file, enroll_option)
    timeout = time.time() + wait_time  # 5 minutes from now
    with open(option_file ,'r') as f:
        while (time.time() < timeout):
            print('Waiting')
            option = f.read()
            if (option == '1'):
                start_time = time.time()
                print('Creating...')
                write_log(notification_file, processing)
                try:
                    status = register.save_face_encoding()
                    if (status == 'creatFace'):

                        #Enroll Fingerprint
                        #time.sleep(2)

                        new_id = len(listdirs(Data_dir))
                        # fingerprinter_enroll(new_id)
                        # Face register
                        t.build_annoy(id_file, ann_file, Data_dir, num_of_tree=NUMBER_OF_TREES)
                        write_log(notification_file, created + str(new_id))
                        # write_log(notification_file, success)

                        print('Thoi gian tao: ' + str(time.time() - start_time))
                        time.sleep(3)
    #                         camera.stop_preview()
    #                         camera.close()
                    elif (status == 'addFace'):
                        t.build_annoy(id_file, ann_file, Data_dir, num_of_tree=NUMBER_OF_TREES)
                        write_log(notification_file, 'Đã xong!')
                    elif (status == 'tooFar'):
                        print('Face be qua/.....')
                        write_log(notification_file, 'Khuôn mặt chưa đủ lớn!')
                        time.sleep(2)
                    else:
                        print('Cannot detect any face')
                        write_log(notification_file, noface)
                        # write_log(color, 'red')
                        time.sleep(2)
    #                         camera.stop_preview()
    #                         camera.close()
                except:
                    print('Error, Back to Recognize mode')
                    write_log(notification_file, error)
                    time.sleep(3)
#                     camera.stop_preview()
#                     camera.close()
                break
            if (option == '0'):
                print('Denied')
                write_log(notification_file, deny)
                time.sleep(1)
#                 camera.stop_preview()
#                 camera.close()
                break

            time.sleep(0.2)

        
    print('Done')
    write_log(notification_file, back)
    write_log(switch_file, '0')
    camera.stop_preview()
    camera.close()

if __name__ == '__main__':
    register()
