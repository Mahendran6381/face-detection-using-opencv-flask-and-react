from flask import Flask,request,Response,render_template,url_for, send_file
from werkzeug.utils import redirect, secure_filename, send_from_directory
from flask_cors import CORS,cross_origin
import cv2 as cv
import os
app = Flask(__name__,template_folder='templates')
cors  = CORS(app)
folder =  'static/uploads/'
app.config["UPLOAD_FOLDER"] = folder
ALLOWDED_FORMATS = set(['jpg','png','jpeg'])

class Detection:
    def __init__(self,path):
        self.path = path
        self.UPLOAD = "static\Mock"
    def face_detect(self):
        print(self.path)
        img = cv.imread(self.path)
        grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        detect = cv.CascadeClassifier("face.xml")
        print(detect)
        face_detect = detect.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=10)
        print(face_detect)
        for (x, y, w, h) in face_detect:
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 200, 0), thickness=2)       
        cv.imwrite(os.path.join(self.UPLOAD,"facedetect.jpg"),img)
        cv.waitKey(0)

def allowed_formats(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWDED_FORMATS
  
@app.route('/')
def hello():
    return render_template("index.html")

@app.route("/detcted_image/<filename>",methods = ["GET"])
def send_image(filename):
    file = "./static/Mock/"+filename
    return send_file(file,as_attachment=True)
    
@app.route('/upload',methods =["POST"])
def test():
    file = request.files['file']
    if (file) and allowed_formats(file.filename):
        print(file)
        filename = secure_filename(file.filename)
        file.seek(0)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        detect = Detection(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        detect.face_detect()
    return render_template("index.html")

if __name__ == '__main__':
    app.run()