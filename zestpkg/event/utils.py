import os
import secrets
from PIL import Image
from flask import current_app
import glob
import csv
from xlsxwriter.workbook import Workbook
from flask import url_for

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


def generate_sheet_solo(fileName, niggas):
    count = 1
    col_name = ['Sr.No.', 'PID', 'Name', 'Course', 'Roll Number', 'College Name']
    with open(fileName , 'w+') as sheet:
        for name in col_name:
            sheet.write(str(name) + ",")

        sheet.write("\n")


    with open(fileName , "a") as sheet:
        for nigga in niggas:
            sheet.write(str(count).upper()+",")
            sheet.write(str(nigga.id+1000).upper()+",")
            sheet.write(str(nigga.profile.name).upper()+",")
            sheet.write(str(nigga.profile.course).upper()+",")
            sheet.write(str(nigga.profile.roll_number).upper()+",")
            sheet.write(str(nigga.profile.college).upper())
            count = count+1
            sheet.write("\n")

    for csvfile in glob.glob(os.path.join('.', fileName)):
        workbook = Workbook(csvfile[:-4] + '.xlsx')
        worksheet = workbook.add_worksheet()
        with open(csvfile, 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        workbook.close()

    print('Sheet Written!')
    os.remove(fileName)
    return csvfile
