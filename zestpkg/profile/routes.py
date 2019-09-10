from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from zestpkg.profile.forms import ProfileForm
from flask_login import current_user, login_required
from zestpkg import db
from zestpkg.models import Profile, User
from zestpkg.profile.utils import save_picture, create_image

profile = Blueprint('profile', __name__)




@profile.route('/<string:username>')
def show_profile(username):
	user = User.query.filter_by(username=username).first()
	if user == None:
		flash('There is no account with this username', category='danger')
		abort(404)

	profile = user.getProfile()
	if profile == None and user.id != current_user.id:
		flash('User does not created any profile yet!', category='info')
		abort(404)

	return render_template('profile.html', profile=profile ,title=username)
	



@profile.route('/create_profile', methods=['GET', 'POST'])
@login_required
def create_profile():
	profile = Profile.query.filter_by(user_id=current_user.id).first()
	if profile:
		flash('You already created one profile. You can only update!', category='info')
		return redirect(url_for('profile.update_profile'))

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
		flash("You created your profile successfully!", category='success')

		return redirect(url_for('main.home'))

	return render_template('addprofile.html', form=form, legend='Create profile', title='Create Profile')


@profile.route('/upload_profile', methods=['GET', 'POST'])
def upload_profile_pic():
	image = request.args.get('image')
	profile = current_user.getProfile()
	if profile:
		profile.image = create_image(image)
		db.session.commit()

	return ""


@profile.route('/update_profile', methods=['GET', 'POST'])
@login_required
def update_profile():
	profile = Profile.query.filter_by(user_id=current_user.id).first()
	if not profile:
		flash("You have not created your profile. First create", category='danger')
		return redirect('profile.create_profile')

	profile = current_user.getProfile()
	form = ProfileForm()
	if form.validate_on_submit():
		profile.name = form.first_name.data + ' ' + form.last_name.data
		print(str(form.image.data))
		if form.image.data:
			profile.image = save_picture(form.image.data)
			

		profile.course = form.course.data
		profile.branch = form.branch.data
		profile.roll_number = form.roll_num.data
		profile.phone = form.phone.data
		profile.college = form.college.data
		profile.gender = form.gender.data

		db.session.commit()
		flash('Your Profile is Successfully updated!', 'success')
		return redirect('/events')

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






