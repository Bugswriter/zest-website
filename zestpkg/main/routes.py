from flask import Blueprint, render_template, jsonify

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
	return render_template('home.html', title='home')


@main.route('/stats', methods=['GET', 'POST'])
def stats():
	return render_template('stats.html', title='Statistics')

@main.route('/faq')
def faq():
	return render_template('faq.html', title='FAQ')



@main.route('/stat_data', methods=['GET', 'POST'])
def stat_data():
	data = {
		'chart1': [34,56,76,23,12],
		'chart2': [36,67,23,51,65,44],
		'chart3': [5,78,457,31,46,7]
	}
	return jsonify(data)


@main.route('/emailtest')
def emailtest():
	data = {'username': 'Bugswriter', 'token': '#'}
	return render_template('account_email.html', **data)


'''
homepage
about
rule book
authorities

'''
