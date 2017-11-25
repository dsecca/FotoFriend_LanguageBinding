import requests
import json
import httplib2

#Python FotoFriend API

class FotoFriend():
    def __init__(self):
        #Credentials
        self.http_server = "fotofriendserver.us-west-2.elasticbeanstalk.com"

    def login(self, username):
        #Connect to FotoFriend server
        headers = {'Content-Type': 'application/json'}
        data = json.dumps({'username': username})
        response = requests.post("http://%s/login" % self.http_server, data = data, headers = headers)

        return response.json()

    def uploadImage(self, fileObject):

        #Add the picture to the path where pictures will be stored
        if checkFileExtension(fileObject.name):
            #Send file to Backend Server
            file.save(os.path.join(application.config['UPLOAD_FOLDER'], fileObject.name))

            response = requests.post("http://%s/storeImage" % self.http_server, files={'file': open(os.path.join(application.config['UPLOAD_FOLDER'], file.filename), 'rb'), 'username': flask.session['username']})

            os.remove(os.path.join(application.config['UPLOAD_FOLDER'], file.filename))

            if response.status_code == 200:
                flask.flash("Your upload was successful!")

            return flask.redirect(flask.url_for('home'))
        else:
            flask.flash("Only jpeg, jpg and png files are supported. Please try again.")
            return flask.redirect(flask.url_for('home'))

    #Check whether the filename extension is allowed 
    def checkFileExtension(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




if __name__ == '__main__':
    app.run(debug=false)