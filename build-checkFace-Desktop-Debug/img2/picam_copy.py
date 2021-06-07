
        
        
def face_recognize():

    with open('data.txt','w') as f:
        f.write('Warming up...')
    import timeit
    start = timeit.default_timer()
    import time 
    import face_recognition
    import picamera
    from annoy import AnnoyIndex
    import numpy as np
    import math
    from utils.read_files import readFile

    open('data.txt', 'w').close()
    camera = picamera.PiCamera()
    camera.resolution = (128, 128)
#     # Set ISO to the desired value
#     camera.iso = 100
#     # Wait for the automatic gain control to settle
#     time.sleep(2)
#     # Now fix the values
#     camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'sports'
#     g = camera.awb_gains
#     camera.awb_mode = 'off'
#     camera.awb_gains = g
    rgb_small_frame = np.empty((128, 128, 3), dtype=np.uint8)







    stop = timeit.default_timer()
    print('Startup time : ' + str(stop-start))
    print("Capturing image...")

    def face_rec(rgb_small_frame):
        # Load Annoy tree
        f = 128
        u = AnnoyIndex(f, 'euclidean')
        u.load('all_hyper1.ann')
        
        # Person ID list
        known_face_names = readFile('hyper_id1.txt')
        # Initialize some variables
        face_locations = []
        face_encodings = []
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        # Choose the face with largest area if there are more than 1
        # More than 1 face
        if (len(face_locations) > 0):
            dists = []
            # largest_face_location = []
            print("Found {} Face(s). {}fps".format(len(face_locations),round(1.0/(time.time() -start_time), 1)))
            for i in range(len(face_locations)):
                p = face_locations[i]
                dist = math.hypot(p[2] - p[0], p[3] - p[1])
                dists.append(dist)
            largest_face_id = np.argmax(dists)

            face_encodings = face_recognition.face_encodings(rgb_small_frame, [face_locations[largest_face_id]])

            face_locations = [face_locations[largest_face_id]]

            face_encoding = face_encodings[0]
            # index vector  annoy
            matches_id, dis = u.get_nns_by_vector(face_encoding, 1, include_distances = True)
            matches_id = matches_id[0]
            dis = dis[0]

            name = "0"
            # # If a match was found in known_face_encodings, just use the first one.
            if (dis<0.375):
                # first_match_index = matches.index(True)
                name = known_face_names[matches_id]
                print("PERSON ID: {} {}".format(name,round(dis,3)))
                return int(name)
            else:
                print(name, round(dis,3))
                return int(name)
        else:
            
            return -1
               
    #start preview
    camera.start_preview(fullscreen=False,window=(110,185,300,300))
    process_this_frame = True

    while True:
        duc1 = open('switch.txt', 'r')
        if (duc1.read()=='0'):
            start_time = time.time()

            camera.capture(rgb_small_frame, format="rgb")

            # Only process every other frame of video to save time
            if process_this_frame:
                id = face_rec(rgb_small_frame)
                if (id > 0):
                    with open('attendance.txt', 'w') as f:
                        f.write('ID: '+str(id)+' - Checkin time: '+ str(time.ctime())+'\n')
                with open('data.txt', 'w') as f:
           
                    if (id == 0):
                        f.write("Unknown")
                    if (id > 0):
                        f.write('\n'+'ID: '+str(id)+'\n' +'\n' +'Checkin time:  '+ str(time.ctime()))

                            
            print('FPS:',round(1.0/(time.time() -start_time), 1))
        else:
            print("Chuyen sang enroll face")

            camera.stop_preview()
            camera.close()
            with open('switch.txt', 'w') as log:
                log.write('1')
            break

        process_this_frame = not process_this_frame

def enroll_face():
    def notification(string):
        with open('data.txt', 'w') as log:
                log.write('{}'.format(string))
    notification('Starting the Camera...')
    import shutil
    import time
    from time import sleep
    import picamera
    import os
    import face_recognition
    import argparse
    import numpy as np
    import tqdm
    from PIL import Image
    from annoy import AnnoyIndex
    from utils.read_files import listdirs, listfiles

    parser = argparse.ArgumentParser()
    # parser.add_argument('--path', type=str, default='foo1.jpg', help='add img path')
    parser.add_argument('--id', type=str, default='new-guy', help='id number')
    args = parser.parse_args()
    name = args.id


    def overlay_image(path):
        # Load the arbitrarily sized image
        img = Image.open(path)
        # Create an image padded to the required size with
        # mode 'RGB'
    #     pad = Image.new('RGB', (
    #         ((img.size[0] + 31) // 32) * 32,
    #         ((img.size[1] + 15) // 16) * 16,
    #         ))
    #     # Paste the original image into the padded one
    #     pad.paste(img, (0, 0))

        # Add the overlay with the padded image as the source,
        # but the original image's dimensions
        overlay = camera.add_overlay(img.tobytes(), size=img.size)
        # By default, the overlay is in layer 0, beneath the
        # preview (which defaults to layer 2). Here we make
        # the new overlay semi-transparent, then move it above
        # the preview
        overlay.fullscreen = False
        overlay.window = (110,185,300,300)
        overlay.alpha = 255
        overlay.layer = 3




    # New ID names base on how many exist dirs
    new_id = len(listdirs('encode')) + 1



    def image_encoding(imagePath):
        filename = os.path.basename(imagePath)
        if ('.jpg' in filename) or ('.jpeg' in filename):
            filename = filename.replace('.jpg', '')
            filename = filename.replace('.jpeg', '')
            img = face_recognition.load_image_file(imagePath)
            img_ = face_recognition.face_locations(img)
            if (len(img_) > 0):
                top, right, bottom, left = [v for v in img_[0]]
                face = img[top:bottom, left:right]
                img_emb = face_recognition.face_encodings(face)[0]
                if not os.path.exists('encode/' + name):
                    #new_id = len(listdirs('encode')) + 1
                    os.mkdir('encode/{}'.format(new_id))
                    with open('encode/{}/{}'.format(new_id, new_id) + '.txt', 'w') as f:
                        for item in img_emb:
                            f.write("%s\n" % item)
                    print('Create ID: {} done'.format(new_id))
                    
                    return True
                
                else:
                    _, _, files = next(os.walk('encode/' + name))
                    n = len(files)
                    with open('encode/{}/{}({})'.format(name, filename, n) + '.txt', 'w') as f:
                        for item in img_emb:
                            f.write("%s\n" % item)
                    print('Added 1 image to id: {}'.format(name))
                    notification('Added 1 image to id: {}'.format(name))

                    return True
            else:
                return False

        return False

    def register():
        #generate annoy tree
        NUMBER_OF_TREES = 10000
        f = 128
        t = AnnoyIndex(f, 'euclidean')

        dirpaths = listdirs('encode')

        file1 = open("hyper_id1.txt", "w")
        count = -1
        for imagePaths in dirpaths:
            dirnames = os.path.basename(imagePaths)
            imagePaths = listfiles(imagePaths)
            for i, imagePath in tqdm.tqdm(enumerate(imagePaths)):
                if (".txt" in imagePath):
                    filename11 = os.path.basename(imagePath)
                    filename11 = filename11.replace(".txt","")
                    # use directory name for person id
                    file1.write(dirnames)
                    file1.write("\n")
                    with open(imagePath, 'r') as file_in:

                        lines = []
                        for line in file_in:
                            line = line.replace("\n","")
                            line = float(line)
                            lines.append(line)
                        lines = np.array(lines)
                        count += 1
                    #add to tree
                    t.add_item(count, lines)
        t.build(NUMBER_OF_TREES,-1)

        t.save(r'all_hyper1.ann')
        
    
    try:

        with picamera.PiCamera() as camera:
            camera.resolution = (512, 512)
            camera.start_preview(fullscreen=False, window=(110,185,300,300))
            # camera.exposure_compensation = 2
    #             camera.brightness = 55
    #             camera.exposure_mode = 'sports'
    #             camera.meter_mode = 'matrix'
    #             camera.image_effect = 'saturation'
            # Set ISO to the desired value
            camera.iso = 100
            # Wait for the automatic gain control to settle
            sleep(2)
            # Now fix the values
            camera.shutter_speed = camera.exposure_speed
            camera.exposure_mode = 'sports'
            g = camera.awb_gains
            camera.awb_mode = 'off'
            camera.awb_gains = g
            # Give the camera some time to adjust to conditions
            notification('Keep Looking straight into the Camera')
            # log.write('Keep Looking straight into the Camera\n\n')
            time.sleep(2)
            img_path = 'images/image.jpg'
            #img_path = 'encode/{}/{}'.format(new_id, new_id) + '.jpg'
            # Action Pipeline
            camera.capture(img_path)
            overlay_image(img_path)
#             time.sleep(1)

            if (image_encoding(img_path) == True):
                register()
                shutil.copy('images/image.jpg', 'encode/{}/{}.jpg'.format(new_id, new_id))
                print('Create ID: {} done'.format(new_id))
                notification('Create ID: {} done'.format(new_id))
                time.sleep(5)
                camera.stop_preview()
                camera.close()

            else:
                print("There is no face")
                notification('There is no face!')
#                 overlay_image('images/foo1.jpg')
#                 time.sleep(1)
                time.sleep(5)
                camera.stop_preview()
                camera.close()
    except:
        print("Error! Please try again")
        notification("Error! Please try again")

    with open('switch.txt', 'w') as log:
        log.write('0')


while True:
    duc = open('switch.txt', 'r')
    if (duc.read()=='0'):
        face_recognize()
    else:
        enroll_face()