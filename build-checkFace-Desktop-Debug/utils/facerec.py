from config import *
import time
import face_recognition
import math
import numpy as np
from utils import *
# from utils.files import readFile, write_log, get_content, delete_content


def facerec():
    dup = -1
    # Set up the Camera
    camera = Pi_Cam('recognize')
    delete_content(notification_file)
    rgb_small_frame = camera.frame()
    camera.start_preview()
    camera.overlay_alpha_box()

    process_this_frame = True

    # Creat Annoy
    u = Annoy(dim=128, distance='euclidean')
    u.load_annoy(ann_file)
    known_face_names = u.get_array()

    def face_rec(rgb_small_frame):
        # Find all the faces and faces encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        # Choose the face with largest area if there are more than 1
        if (len(face_locations) > 0):
            write_log(notification_file, "Phát hiện có người...")
            print('....')
            # time_rec = time.time()
            dists = []
            # largest_face_location = []
            print("Found {} Face(s). {}fps".format(len(face_locations), round(1.0 / (time.time() - start_time), 1)))
            for i in range(len(face_locations)):
                p = face_locations[i]
                dist = math.hypot(p[2] - p[0], p[3] - p[1])
                dists.append(dist)
            largest_face_id = np.argmax(dists)
            frame_area = h0 * w0
#            print('AREA:  ', max(dists) / frame_area)
            if max(dists) / frame_area > 0.0023:
                face_encodings = face_recognition.face_encodings(rgb_small_frame, [face_locations[largest_face_id]], num_jitters=1, model='large')
                # face_locations = [face_locations[largest_face_id]]
                face_encoding = face_encodings[0]
                # index vector  annoy
                id = u.search(face_encoding, known_face_names)
                # print('Time rec: '+ str(time.time()-time_rec))
                return id
            else:
                print('Too far..')

                return -2
        else:
            return -1
    
    while True:
        switch = get_content(switch_file)
        if (switch == '0'):
            start_time = time.time()
            camera.capture_frame(rgb_small_frame, format="rgb")
            # if process_this_frame:
            id = face_rec(rgb_small_frame)
            if (id > 0):
                print('ID: ' + str(id))
#                     write_log(color, 'green')
                write_log(notification_file, 'ID: {}'.format(id) + success)
                # print('IDDDDDDDDDDD:  ', id)
                if (id>0) and (id == dup):
                    print('duplicate')
                else:
                    dup = id
                    log_json(id)
                time.sleep(2)
                # write_log(json, checkin_time)
            if (id == 0):
#                     write_log(color, 'red')
                write_log(notification_file, not_found)
                print('Unknown dsjfgsdjkgsdjk')
                time.sleep(0)
            if (id == -2):
                write_log(notification_file, "Đứng quá xa..")
            else:
                delete_content(notification_file)
                print(id)
            print('FPS:', round(1.0 / (time.time() - start_time), 1))
        else:
            print("Switching to Register mode")
            write_log(notification_file, start_enroll)
            camera.stop_preview()
            camera.close()
            # write_log(switch_file, '1')
            break
        # process_this_frame = not process_this_frame


if __name__ == '__main__':
    facerec()
