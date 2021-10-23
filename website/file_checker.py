import os
from werkzeug.utils import secure_filename
from PIL import Image

image_files_location = "static/image/"

def check_upload_file(form):
    #get file data from form
    fp = form.image.data
    filename = fp.filename
    #get the current path of the module file… store image file relative to this path
    BASE_PATH = os.path.dirname(__file__)

    #upload file location – directory of this file/static/image
    upload_path = os.path.join(BASE_PATH, image_files_location,
                               secure_filename(filename))

    
    #store relative path in DB as image location in HTML is relative
    db_upload_path = "/" + image_files_location + secure_filename(filename)
    #save the file and return the db upload path
    fp.save(upload_path)
    return db_upload_path

def set_default_photo():
    default_photo = "account.png"
    BASE_PATH = os.path.dirname(__file__)
    #upload file location – directory of this file/static/image
    upload_path = os.path.join(BASE_PATH, image_files_location, default_photo)
    print("DEFAULT PHOTO: " + upload_path)
    return Image.open(upload_path)


    #CAN EITHER DO IT AT THE DATABASE LEVEL AND ATTEMPT TO SKIP VALIDATION IF EMPTY

    #OR FILL IT WITH THE NEW ONE