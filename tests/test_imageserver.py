from os import path
import pytest
from imageserver import imageserver
from imageserver.generate_thumbnails import generate_thumbnails

script_path = path.dirname(path.abspath(__file__))
test_images_path = path.join(script_path, 'test_images')

@pytest.fixture
def client(request):
    imageserver.app.config['TESTING'] = True
    imageserver.app.config['IMAGES_FOLDER'] = test_images_path
    generate_thumbnails(test_images_path)
    imageserver.init_db()
    client = imageserver.app.test_client()
    return client

def test_index_redirect(client):
    rv = client.get('/')
    assert rv.status == '302 FOUND'

def test_api_thumbnails(client):
    rv = client.get('/api/database/redothumbs')
    assert rv.status == '200 OK'
    assert int(rv.data) >= 0

def test_api_refresh(client):
    rv = client.get('/api/database/refresh')
    assert rv.status == '200 OK'
    assert int(rv.data) >= 0

def test_image_proxy(client):
    rv = client.get('/i/black.jpg')
    assert rv.status == '200 OK'
    assert len(rv.data) == 88943
    rv = client.get('/i/black.gif')
    assert rv.status == '200 OK'
    assert len(rv.data) == 135339
    rv = client.get('/i/black.gif.thumb')
    assert rv.status == '200 OK'
    assert len(rv.data) == 3612

def test_image_proxy_mime(client):
    rv = client.get('/i/black.gif')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'image/gif'
    rv = client.get('/i/black.gif.thumb')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'image/gif'
    rv = client.get('/i/black.png.thumb')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'image/png'

def test_404s(client):
    rv = client.get('/v/non_existant.png')
    assert rv.status == '404 NOT FOUND'
    rv = client.get('/i/non_existant.png')
    assert rv.status == '404 NOT FOUND'

def test_image_view(client):
    rv = client.get('/v/black.gif')
    assert rv.status == '200 OK'
    assert b'src="/i/black.gif"' in rv.data

def test_images(client):
    rv = client.get('/images')
    assert rv.status == '200 OK'
    assert b'6 images' in rv.data
