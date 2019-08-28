from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from zestpkg.profile.forms import ProfileForm
from flask_login import current_user, login_required
from zestpkg import db
from zestpkg.models import Profile, User
from zestpkg.profile.utils import save_picture

profile = Blueprint('profile', __name__)

def getProfile(uname):
	user = User.query.filter_by(username=uname).first()
	if user is None:
		abort(403)

	profile = user.profile
	if not profile:
		return redirect(url_for('main.home'))

	return profile[0]

@profile.route('/<string:username>')
def show_profile(username):
	profile = getProfile(username)
	if profile:
		return render_template('profile.html', user=profile ,title=username)
	else:
		abort(404)


@profile.route('/<string:username>/create', methods=['GET', 'POST'])
@login_required
def create_profile(username):
	if current_user.username != username:
		abort(403)

	form = ProfileForm()
	if form.validate_on_submit():
		if form.image.data:
			picture = save_picture(form.image.data)
		else:
			picture = "default.png"

		name = form.first_name.data + " " + form.last_name.data
		profile = Profile(name=name, image=picture, course=form.course.data, branch=form.branch.data, roll_number=form.roll_num.data, phone=form.phone.data, college=form.college.data, gender=form.gender.data,  user_id=current_user.id)
		db.session.add(profile)
		db.session.commit()
		flash("You created your profile successfully!", 'success')

		return redirect(url_for('main.home'))


	return render_template('addprofile.html', form=form, legend='Create profile', title='Create Profile')


@profile.route('/<string:username>/update', methods=['GET', 'POST'])
@login_required
def update_profile(username):
	if current_user.username != username:
		abort(403)

	profile = getProfile(username)
	form = ProfileForm()
	if form.validate_on_submit():
		profile.name = form.first_name.data + ' ' + form.last_name.data
		print(str(form.image.data))
		if not form.image.data:
			profile.image = "default.png"	
		else:
			profile.image = save_picture(form.image.data)

		profile.course = form.course.data
		profile.branch = form.branch.data
		profile.roll_num = form.roll_num.data
		profile.phone = form.phone.data
		profile.college = form.college.data
		profile.gender = form.gender.data

		db.session.commit()
		flash('Your Profile is Successfully updated!', 'success')
		return redirect(f'/{username}')

	elif request.method == 'GET':
		name = profile.name.split()
		fname = name[0]
		lname = name[1]
		form.first_name.data = fname
		form.last_name.data = lname
		form.course.data = profile.course
		form.branch.data = profile.branch
		form.roll_num.data = profile.roll_number
		form.phone.data = profile.phone
		form.college.data = profile.college
		form.gender.data = profile.gender

		return render_template('addprofile.html', form=form, legend='Update Profile', title='Update Profile')






