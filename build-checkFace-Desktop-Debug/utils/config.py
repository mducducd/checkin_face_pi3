import time
import json

### Annoy Config
NUMBER_OF_TREES = 5000
dim = 128
distance = 'euclidean'
id_file = '/home/pi/build-checkFace-Desktop-Debug/hyper_id1.txt'
ann_file = '/home/pi/build-checkFace-Desktop-Debug/all_hyper1.ann'
threshold = 0.42

### Data files
Data_dir = 'encode'
switch_file = '/home/pi/build-checkFace-Desktop-Debug/log_data/switch.txt'
notification_file = '/home/pi/build-checkFace-Desktop-Debug/log_data/notification.txt'
option_file = '/home/pi/build-checkFace-Desktop-Debug/log_data/option.txt'
json_file = '/home/pi/build-checkFace-Desktop-Debug/log_data/checkin.json'
color = '/home/pi/build-checkFace-Desktop-Debug/log_data/color.txt'
is_capture = '/home/pi/build-checkFace-Desktop-Debug/log_data/capture.txt'

### Register
name = 'new-guy'
img_path = '/home/pi/build-checkFace-Desktop-Debug/images/image.jpg'
# timeout = time.time() + 60 * 5  # 5 minutes from now
wait_time = 20

### Face Recognize
dup = 0 # for duplicate id

### Pi Camera
window = (10,55, 300, 300)
brightness = 50
saturation = 60
iso = 400
# recognize mode (128p for pi0)
h0 = 128
w0 = 128
# register mode
h1 = 256
w1 = 256
face_area_limit = 0.0045 #128p 0.0023-256p

### Notifications English
# startup = 'Warming up...'
# checkin_time = 'Checkin time: ' 
# not_found = 'Not found'
# switch_to_register = 'Switching to Register mode'
# look_straight = 'Keep Looking directly to the Camera for '  # + time (secs)
# enroll_option = 'Do you want to use this Image (y/n)?'
# no_face = 'Cannot detect any face'
# error = 'Error, Back to Recognize mode'
# processing = 'Creating... Please wait'
# created = 'Enroll successfully, ID: '  # + new id
# deny = 'Denied, Back to Recognize mode'
# success = ' Sucessfully'
# back = 'Back to Recognize mode'
# Bạn có vân tay nhìn thẳng
### Notifications Vietnamese
fingerprint_mode = 'Mời xác nhận vân tay'
startup = 'Vui lòng chờ'
checkin_time = 'Thời gian Checkin : ' + str(time.ctime())
not_found = ' Không tìm thấy'
switch_to_register = 'Đặt tay vào cảm biến'
look_straight = 'Nhìn hướng vào camera trong  '  # + time (secs)
enroll_option = 'Sử dụng ảnh này để đăng ký (y/n)?'
no_face = 'Ảnh không đủ tiêu chuẩn'
error = 'Lỗi, quay lại chế độ nhận dạng'
processing = 'Đang tạo... vui lòng đợi'
created = 'Đăng ký thành công ID: '  # + new id
deny = 'Từ chối, về chế độ nhận dạng'
success = ' Thành công'
back = 'Về chế độ nhận dạng'
nomatch = 'Xin vui lòng thử lại'
existed = 'Vân tay đã tồn tại, thử lại.'
start_enroll = "Đang chuyển chế độ"
fingerprint_ready = 'Vân tay sẵn sàng'
#Trùng vân tay có thể bị hoặc
# Không thành công
