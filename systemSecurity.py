import cv2
import dropbox
import time
import random

startTime = time.time()
def take_snapshot():
    number = random.randint(0,100)
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        #read the frames while the camera is on
        ret, frame = videoCaptureObject.read
        #cv2.inwrite() method is useed to save an image in any device
        img_name = "img"+str(number)+".png"
        cv2.imwrite("NewPicture1.jpg",frame) 
        startTime = time.time
        result = False
    return img_name
    print("snapshot taken")
    #close the camera 
    videoCaptureObject.release()
    #close windows that might be open while this process
    cv2.destroyAllWindows()

def upload_file(img_name): 
    access_token = "sl.A3pvoH6so4_CDRs14M3CCNHEtpo5xezHD467pIq9p0ZKlydqw9_0W5fLh_cMc4lBPULjSS2tlfofXibrnhQCb_XgWA3nYX2_5-3MqstDrM9H9LjAk9EBETjzpOlZbM8hsNrvDS8" 
    file =img_name 
    file_from = file 
    file_to="/testFolder/"+(img_name) 
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f: 
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite) 
        print("file uploaded")

def main(): 
    while(True):
    if((time.time() - startTime) >= 5): 
    name = take_snapshot() 
    upload_file(name) 

main()   