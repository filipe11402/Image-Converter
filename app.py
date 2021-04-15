from flask import Flask, request
from flask_restful import Api, Resource, abort
import base64
import cv2
import numpy as np
import os

app = Flask(__name__)
api = Api(app)
cwd = os.getcwd() # getting current working directory


# func to check if image exists
def check_if_exists(img_id):
    file_list = os.listdir(cwd)
    filename = str(img_id) + ".jpg"
    if filename not in file_list:
        abort(404, message="NO PHOTO WITH THAT NAME")


class Image(Resource):
    def get(self, img_id):
        check_if_exists(img_id)
        filename = str(img_id) + ".jpg"
        img = cv2.imread(filename, 0)
        cv2.imshow("Existe", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return 200 


    
    def post(self, img_id):

        # getting post data from dict sent
        b64_string = request.form['img_b64']
        new_img_size = int(request.form['new_size'])
        b64_decoded = base64.b64decode(b64_string)

        # creating array from the b64 string that is in memory buffer
        np_arr = np.frombuffer(b64_decoded, np.uint8)
        img_np = cv2.imdecode(np_arr, cv2.IMREAD_GRAYSCALE)


        filename = str(img_id) + ".jpg"

        
        # resizing by percentage to maintain aspect ratio 
        # size is based in percentage
        new_width = int(img_np.shape[1] * new_img_size / 100)
        new_heigth = int(img_np.shape[0] * new_img_size / 100)
        dim = (new_width, new_heigth)

        print("Dimensions: ", dim)

        # applying the new sizes, saving the file and showing it
        resized = cv2.resize(img_np, dim, interpolation=cv2.INTER_AREA)
        cv2.imwrite(filename, resized)
        cv2.imshow("Your resized and gray color foto", resized)


        # keep image open until closed
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        return "success", 200
        


api.add_resource(Image, '/teste/<int:img_id>/')

if __name__ == '__main__':
    app.run(debug=True)