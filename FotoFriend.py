import requests
import json
import httplib2
import os
import base64

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

    def uploadImage(self, fileObject, fileName, sessionUsername):
        response = requests.post("http://%s/storeImage" % self.http_server, data=dict(file=base64.b64encode(fileObject), filename=fileName, username=sessionUsername))
        return response

    def deleteImage(self, imageUrl, sessionUsername):

        headers = {'Content-Type': 'application/json'}
        data = json.dumps({'url': imageUrl, 'username': sessionUsername})
        response = requests.post("http://%s/deleteImage" % self.http_server, data = data, headers = headers)
        return response

    def filter(self, keywordsList, sessionUsername):
        tag_list = []
        for keyword in keywordsList:
            tag_list.append(keyword)

        headers = {'Content-Type': 'application/json'}
        data = json.dumps({'keywords': tag_list, 'username': sessionUsername})
        response = requests.post("http://%s/filter" % self.http_server, data = data, headers = headers)
        return response.json()

    #Check whether the filename extension is allowed 
    def checkFileExtension(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




if __name__ == '__main__':
    app.run(debug=false)