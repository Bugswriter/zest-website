from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
	return render_template('home.html', title='home')


@main.route('/stats', methods=['GET', 'POST'])
def stats():
	return render_template('stats.html', title='Statistics')


'''
homepage
about
rule book
authorities

'''
