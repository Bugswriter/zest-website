import os
import secrets
from PIL import Image
from flask import current_app

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/event_pics', picture_fn)

    output_size = (850, 315)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def getProfile(uname):
	user = User.query.filter_by(username=uname).first()
	if user is None:
		abort(403)

	profile = user.profile
	if not profile:
		return redirect(url_for('main.home'))

	return profile[0]