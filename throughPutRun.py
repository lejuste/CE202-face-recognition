from PIL import Image, ImageDraw
import face_recognition
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", "--threads", dest="threads",
                  help="select number of threads to run the program on: 1,2,4,8", default=1)
parser.add_option("-s", "--size", dest="size", default=1,
                  help="number of training epochs")

(options, args) = parser.parse_args()

threads = int(options.threads)
sizeFraction = int(options.size)

print ('size in throughputRun: ' +str(sizeFraction))
# Load the jpg file into a numpy array
image = face_recognition.load_image_file("obama_small.jpg")


#10.9 billion
# ideal: 3.9 billion
if(sizeFraction == 256):
	# Find all facial features in all the faces in the image
	face_landmarks_list = face_recognition.face_landmarks(image)


#ideal: 15,625,000,000
if(sizeFraction == 64):
	# Find all facial features in all the faces in the image
	image = face_recognition.load_image_file("obama-480p.jpg")
	face_landmarks_list = face_recognition.face_landmarks(image)

#61,677,661,017
#ideal: 62,500,000,000
if(sizeFraction == 16):
	# Find all facial features in all the faces in the image
	face_landmarks_list = face_recognition.face_landmarks(image)
	image = face_recognition.load_image_file("biden.jpg")
	face_landmarks_list = face_recognition.face_landmarks(image)
	image = face_recognition.load_image_file("biden.jpg")
	face_landmarks_list = face_recognition.face_landmarks(image)
	image = face_recognition.load_image_file("biden.jpg")
	face_landmarks_list = face_recognition.face_landmarks(image)
	image = face_recognition.load_image_file("biden.jpg")
	face_landmarks_list = face_recognition.face_landmarks(image)

#249,091,938,249
#ideal: 250 billion
if(sizeFraction == 4):
	# Find all facial features in all the faces in the image
	face_landmarks_list = face_recognition.face_landmarks(image)
	image = face_recognition.load_image_file("biden.jpg")
	face_landmarks_list = face_recognition.face_landmarks(image)
	image = face_recognition.load_image_file("biden.jpg")
	face_landmarks_list = face_recognition.face_landmarks(image)
	image = face_recognition.load_image_file("biden.jpg")
	face_landmarks_list = face_recognition.face_landmarks(image)
	face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")


#1.01 trillion
if(sizeFraction == 1):
	image = face_recognition.load_image_file("biden.jpg")
	face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
	face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
	face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
	face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
	face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")



