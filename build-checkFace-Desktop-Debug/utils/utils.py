import numpy as np
import tqdm
from annoy import AnnoyIndex
import os
import picamera
import time
from PIL import Image
import face_recognition
import shutil
import json
import math
from config import *
# from utils.finger_enroll import *
from finger_enroll import fingerprinter_enroll

### Do with dirs, files
def listdirs(rootdir):
    rootdirs = []
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            listdirs(d)
            rootdirs.append(d)
    return rootdirs


def listfiles(rootdir):
    files = []
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        files.append(d)
    return files


# Read .txt file by lines and put to an array
def readFile(fileName):
    fileObj = open(fileName, "r")  # opens the file in read mode
    words = fileObj.read().splitlines()  # puts the file into an array
    fileObj.close()
    return words


# Write log to txt file
def write_log(file_path, string):
    with open(file_path, 'w') as f:
        f.write(string)


def get_content(file_path):
    data = open(file_path, 'r')
    return data.read()


def delete_content(file_path):
    open(file_path, 'w').close()


# def log_json(id):
#
#     # Create JSON String
#     obj = {"id": id, "name": "", "time": time.ctime()}
#
#     # Write to json file
#     with open(json_file, 'a') as f:
#         json.dump(obj, f)
#         f.write('\n')

def log_json(id, filename=json_file):
    with open(filename) as json_file:
        data = json.load(json_file)

        temp = data['data']

        # python object to be appended
        y = {"id": id, "time": time.ctime()}
        # appending data to emp_details
        temp.append(y)

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

# def pingQT(color, file_path=color):
#     with open(file_path, 'w') as f:
#         f.write(color)


### Annoy Algorithm
class Annoy:
    def __init__(self, dim=128, distance='euclidean'):
        self.dim = dim
        self.distance = distance
        # Create Annoy Tree
        self.tree = AnnoyIndex(dim, distance)

    def load_annoy(self, ann_file_path=ann_file):
        self.tree.load(ann_file_path)

    def get_array(self, id_file_path=id_file):
        self.known_face_names = readFile(id_file_path)
    
        return self.known_face_names

    def build_annoy(self, id_file_name, ann_file_name, image_data_dir, num_of_tree=NUMBER_OF_TREES):
        self.num_of_tree = num_of_tree
        self.id_file_name = id_file_name
        self.ann_file_name = ann_file_name
        self.image_data_dir = image_data_dir

        dirpaths = listdirs(self.image_data_dir)
        file1 = open(id_file_name, "w")
        index = -1
        for imagePaths in dirpaths:
            dirnames = os.path.basename(imagePaths)
            imagePaths = listfiles(imagePaths)
            for i, imagePath in tqdm.tqdm(enumerate(imagePaths)):
                if (".txt" in imagePath):
                    filename11 = os.path.basename(imagePath)
                    filename11 = filename11.replace(".txt", "")
                    # use directory name for person id
                    file1.write(dirnames)
                    file1.write("\n")
                    with open(imagePath, 'r') as file_in:

                        lines = []
                        for line in file_in:
                            line = line.replace("\n", "")
                            line = float(line)
                            lines.append(line)
                        lines = np.array(lines)
                        index += 1
                    # add to tree
                    self.tree.add_item(index, lines)
        self.tree.build(self.num_of_tree, -1)

        self.tree.save(r'{}'.format(ann_file_name))

    def search(self, face_encoding, known_face_names):
        # index vector  annoy
        matches_id, dis = self.tree.get_nns_by_vector(face_encoding, 1, include_distances=True)
        if len(matches_id) > 0:
            matches_id = matches_id[0]
            dis = dis[0]
            with open('/home/pi/build-checkFace-Desktop-Debug/log_data/dist_tracking.txt', 'a') as f:
                f.write(str(known_face_names[matches_id]) +" "+ str(dis))
                f.write('\n')
            name = "0"
            # # If a match was found in known_face_encodings, just use the first one.
            if (dis < threshold):
                name = known_face_names[matches_id]
                print("PERSON ID: {} {}".format(name, round(dis, 3)))
                name = int(name)
                with open('/home/pi/build-checkFace-Desktop-Debug/log_data/dist_tracking.txt', 'a') as f:
                    f.write(str(name) + " " + str(dis) +" Passed!!")
                    f.write('\n')
            else:
                print(name, round(dis, 3))
                name = int(name)
        else:
            name = 0
        return name

### Face-encoding
class Register:
    def __init__(self, imagePath=img_path):
        self.imagePath = imagePath

    def save_face_encoding(self, data_dir=Data_dir):
        # Creat Annoy
        # Create Annoy Tree
        self.tree = AnnoyIndex(128, 'euclidean')
        self.tree.load(ann_file)
        self.known_face_names = readFile(id_file)
        self.data_dir = data_dir
        self.new_id = len(listdirs(self.data_dir)) + 1

        encode_dir = self.data_dir
        new_id = self.new_id
        imagePath = self.imagePath
        filename = os.path.basename(imagePath)

        if ('.jpg' in filename) or ('.jpeg' in filename):
            filename = filename.replace('.jpg', '')
            filename = filename.replace('.jpeg', '')
            img = face_recognition.load_image_file(imagePath)
            img_ = face_recognition.face_locations(img)

            if (len(img_) > 0):
                p = img_[0]
                dist = math.hypot(p[2] - p[0], p[3] - p[1])
                frame_area = h0 * w0

                if dist / frame_area > 0.0023:
                    top, right, bottom, left = [v for v in img_[0]]
                    face = img[top:bottom, left:right]
                    img_emb = face_recognition.face_encodings(face, num_jitters=1, model='large')[0]
                    # index vector  annoy
                    matches_id, dis = self.tree.get_nns_by_vector(img_emb, 1, include_distances=True)
                    if len(dis) < 1:

                        write_log(notification_file, fingerprint_mode)
                        if (fingerprinter_enroll(new_id) == True):
                            new_id = len(listdirs('encode')) + 1
                            write_log(notification_file, 'Vân tay đã xong!')
                            os.mkdir(encode_dir + '/{}'.format(new_id))
                            with open(encode_dir + '/{}/{}'.format(new_id, new_id) + '.txt', 'w') as f:
                                for item in img_emb:
                                    f.write("%s\n" % item)
                            shutil.copy(img_path, Data_dir + '/{}/{}.jpg'.format(new_id, new_id))
                            print('Create ID: {} done'.format(new_id))

                            status = "creatFace"
                        else:
                            write_log(notification_file, deny)
                            status = "noFace"
                    else:
                        name = self.known_face_names[matches_id[0]]
                        if (dis[0]>0.383):
                            write_log(notification_file, fingerprint_mode)
                            if (fingerprinter_enroll(new_id) == True):
                                write_log(notification_file, 'Vân tay đã xong!')
                                new_id = len(listdirs('encode')) + 1
                                os.mkdir(encode_dir + '/{}'.format(new_id))
                                with open(encode_dir + '/{}/{}'.format(new_id, new_id) + '.txt', 'w') as f:
                                    for item in img_emb:
                                        f.write("%s\n" % item)
                                shutil.copy(img_path, Data_dir + '/{}/{}.jpg'.format(new_id, new_id))
                                print('Create ID: {} done'.format(new_id))

                                status = "creatFace"
                            else:
                                write_log(notification_file, deny)
                                status = "noFace"

                        else:
                            write_log(notification_file, 'Bạn đã đăng ký rồi! ID: {}'.format(name))
                            time.sleep(1)
                            name = str(name)
                            # _, _, files = next(os.walk(encode_dir + '/' + name))
                            n = len(listfiles(encode_dir + '/' + name))/2
                            with open(encode_dir + '/{}/{}({})'.format(name, filename, n) + '.txt', 'w') as f:
                                for item in img_emb:
                                    f.write("%s\n" % item)
                            shutil.copy(img_path, Data_dir + '/{}/{}({}).jpg'.format(name, filename, n))
                            print('Added 1 image to id: {}'.format(name))

                            status = "addFace"
                else:
                    print('tooFar')
                    status = 'tooFar'
            else:
                print('There is no face')
                status = "noFace"

        return status


### Picamera Setup
class Pi_Cam:
    def __init__(self, mode):
        self.mode = mode
        self.camera = picamera.PiCamera()

        if (self.mode == 'recognize'):
            print('Start Recognize Mode')
            self.camera.hflip = True #Optional
            self.camera.resolution = (h0, w0)
            self.camera.brightness = brightness
            # self.camera.saturation = saturation
            self.rgb_small_frame = np.empty((h0, w0, 3), dtype=np.uint8)
            self.camera.exposure_mode = 'sports'
            self.camera.framerate = 15
            self.rgb_small_frame = np.empty((w0, h0, 3), dtype=np.uint8)

        if (self.mode == 'register'):
            print('Start Register Mode')
            self.camera.hflip = True  # Optional
            self.camera.resolution = (h1, w1)
            self.camera.brightness = brightness
            # self.camera.saturation = saturation
            self.rgb_small_frame = np.empty((w1, h1, 3), dtype=np.uint8)
            # Set ISO to the desired value
            self.camera.iso = iso
            # Wait for the automatic gain control to settle
            time.sleep(2)
            # Now fix the values
            self.camera.shutter_speed = self.camera.exposure_speed
            self.camera.exposure_mode = 'sports'
            g = self.camera.awb_gains
            self.camera.awb_mode = 'off'
            self.camera.awb_gains = g
        if (self.mode == 'fingerprint'):
            print('Start Finger Print Mode')
            self.camera.hflip = True  # Optional
            self.camera.resolution = (h1, w1)
        if (self.mode == 'sleep'):
            print('Camera off')
            self.camera.stop_preview()
            self.camera.close()

    def start_preview(self):
        return self.camera.start_preview(fullscreen=False, window=window)

    def stop_preview(self):
        return self.camera.stop_preview()

    def close(self):
        return self.camera.close()

    def capture(self, img_path=img_path):
        return self.camera.capture(img_path)

    def capture_frame(self, rgb_small_frame, format="rgb"):
        self.camera.capture(rgb_small_frame, format)

    def frame(self):
        return self.rgb_small_frame

    def overlay_image(self, path=img_path):
        # Load the arbitrarily sized image
        img = Image.open(path)
        # Add the overlay with the padded image as the source,
        # but the original image's dimensions
        overlay = self.camera.add_overlay(img.tobytes(), size=img.size)
        # By default, the overlay is in layer 0, beneath the
        # preview (which defaults to layer 2). Here we make
        # the new overlay semi-transparent, then move it above
        # the preview
        overlay.fullscreen = False
        overlay.window = window
        overlay.alpha = 255
        overlay.layer = 3
        
    def overlay_alpha_box(self):
        box = np.zeros((320, 320, 3), dtype=np.uint8)
        box[30:285, 30:285, :] = 0x80
        overlay = self.camera.add_overlay(box.tobytes(), size=(320, 320), layer=3, alpha=64)
        overlay.fullscreen = False
        overlay.window = (window)

    def draw_box(self):
        return 0
