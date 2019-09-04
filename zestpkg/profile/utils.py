import os
import secrets
import base64
from PIL import Image
from flask import current_app

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (300, 300)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def create_image(form_picture):
	data = 	form_picture.split(',')[1].encode()
	random_hex = secrets.token_hex(8)
	picture_fn = random_hex + '.png'
	picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
	with open(picture_path,'wb') as pic:
		pic.write(base64.decodebytes(data))

	return picture_fn

