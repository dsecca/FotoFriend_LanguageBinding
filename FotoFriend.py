import requests
import json
import httplib2
import os

#Python FotoFriend API

class FotoFriend():
    def __init__(self):
        #Credentials
        self.http_server = "fotofriendserver.us-west-2.elasticbeanstalk.com"
        self.ALLOWED_EXTENSIONS = set(['jpeg', 'jpg', 'png'])

    def login(self, username):
        #Connect to FotoFriend server
        headers = {'Content-Type': 'application/json'}
        data = json.dumps({'username': username})
        response = requests.post("http://%s/login" % self.http_server, data = data, headers = headers)

        return response.json()

    def uploadImage(self, fileObject, uploadFolderPath, sessionUsername):
        
        response = requests.post("http://%s/storeImage" % self.http_server, files={'file': open(os.path.join(uploadFolderPath, fileObject.filename), 'rb'), 'username': sessionUsername})

        return response

    #Check whether the filename extension is allowed 
    def checkFileExtension(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




if __name__ == '__main__':
    app.run(debug=false)