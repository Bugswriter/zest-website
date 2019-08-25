from flask import Blueprint, render_template, redirect, url_for, flash
from zestpkg.profile.forms import ProfileForm
from flask_login import current_user, login_required
from zestpkg import db
from zestpkg.models import Profile, User

profile = Blueprint('profile', __name__)

@profile.route('/<string:username>')
def show_profile(username):
	user = User.query.filter_by(username=username).first()
	profile = user.profile[0]
	if profile:
		return render_template('profile.html', user=profile ,title=username)
	else:
		abort(404)


@profile.route('/<string:username>/add', methods=['GET', 'POST'])
@login_required
def add_profile(username):
	if current_user.username != username:
		abort(403)

	pform = ProfileForm()
	if pform.validate_on_submit():
		picture = "default.jpg" #soon will be replaced
		name = pform.first_name.data + " " + pform.last_name.data
		profile = Profile(name=name, image=picture, course=pform.course.data, branch=pform.branch.data, roll_number=pform.roll_num.data, phone=pform.phone.data, college=pform.college.data,  user_id=current_user.id)
		db.session.add(profile)
		db.session.commit()
		flash("You created your profile successfully!", 'success')

		return redirect(url_for('main.home'))


	return render_template('addprofile.html', form=pform, legend="Create profile")

