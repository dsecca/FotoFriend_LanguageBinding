import pytest
import fotofriend
import urllib.request
import os

class TestLibrary:
    def test_login(self):
        links = fotofriend.login("fotofriendtest")
        assert links == { 'Links': ['https://s3-us-west-2.amazonaws.com/foto-friend/5a1848632bc46432713be66d/dog.jpg'] }

    @pytest.mark.dependency()
    def test_upload(self):
        urllib.request.urlretrieve('http://www.catster.com/wp-content/uploads/2017/08/A-fluffy-cat-looking-funny-surprised-or-concerned.jpg', 'tmp.jpg')
        file = open('tmp.jpg', 'rb').read()
        code = fotofriend.uploadImage(file, "tmp.jpg", "fotofriendtest")
        os.remove("tmp.jpg")
        assert code == 1

    @pytest.mark.dependency(depends=['test_upload'])
    def test_delete(self):
        code = fotofriend.deleteImage("https://s3-us-west-2.amazonaws.com/foto-friend/5a1848632bc46432713be66d/tmp.jpg", "fotofriendtest")
        assert code == 200

    def test_filter(self):
        links = fotofriend.filter(["dog"], "fotofriendtest")
        assert links == { 'Links': ['https://s3-us-west-2.amazonaws.com/foto-friend/5a1848632bc46432713be66d/dog.jpg'] }