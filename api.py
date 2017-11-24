import flask

application = flask.Flask(__name__)
api = Api(application)


if __name__ == '__main__':
    application.debug = False
    application.run()