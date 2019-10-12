from zestpkg import db
from zestpkg.models import *

db.create_all()

users = [User(username='admin', email='bugswriter@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),
         User(username='bran', email='bran@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),
         User(username='tyrion', email='tyrion@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),
         User(username='khaleesi', email='khaleesi@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),
         User(username='jonsnow', email='jonsnow@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),
         User(username='arya', email='arya@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),
         User(username='cersei', email='saitama@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),
         User(username='ramsay', email='ramsay@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),
         User(username='sansa', email='sansa@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),
         User(username='joffrey', email='joffrey@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),
         User(username='kingslayer', email='kingslayer@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),
         User(username='hodor', email='hodor@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2')]

for user in users:
	db.session.add(user)

db.session.commit()

profiles=[Profile(name='Suraj Kushwah', course='B.Tech', branch='CS', roll_number='1701410014', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=1),
	  Profile(name='Bran Stark', course='B.Tech', branch='CS', roll_number='1701410015', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=2),
	  Profile(name='Tyrion Lannister', course='B.Tech', branch='CS', roll_number='1701410017', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=3),
	  Profile(name='Daenerys Targaryen', course='B.Tech', branch='CS', roll_number='1701410014', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=4),
	  Profile(name='Aegon Targaryen', course='B.Tech', branch='CS', roll_number='1701410016', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=5),
	  Profile(name='Arya Stark', course='B.Tech', branch='CS', roll_number='1701410018', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=6),
	  Profile(name='Cersei Lannister', course='B.Tech', branch='CS', roll_number='1701410019', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=7),
	  Profile(name='Ramsay Bolton', course='B.Tech', branch='CS', roll_number='1701410024', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=8),
	  Profile(name='Sansa Bolton', course='B.Tech', branch='CS', roll_number='1701410025', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=9),
	  Profile(name='Joffrey Lannister', course='B.Tech', branch='CS', roll_number='1701410026', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=10),
	  Profile(name='Jamie Lannister', course='B.Tech', branch='CS', roll_number='1701410017', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=11),
	  Profile(name='Wylis', course='B.Tech', branch='CS', roll_number='1701410018', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=12),]

for profile in profiles:
	db.session.add(profile)


dummy_detail = 'Felis potenti suspendisse. Commodo venenatis dictum aliquet torquent a, tempor luctus luctus viverra. Convallis elit integer torquent dictum lorem Sociosqu litora. Imperdiet.'


events = [Event(title='Badminton (single)',category='aamod', subcategory='sports', team_limit='1', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Badminton (single)',category='aamod', subcategory='sports', team_limit='1', about=dummy_detail, gender='F', user_id='1'),

		Event(title='Badminton (doubles)',category='aamod', subcategory='sports', team_limit='2', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Badminton (doubles)',category='aamod', subcategory='sports', team_limit='2', about=dummy_detail, gender='F', user_id='1'),

		Event(title='Table Tennis (single)',category='aamod', subcategory='sports', team_limit='1', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Table Tennis (single)',category='aamod', subcategory='sports', team_limit='1', about=dummy_detail, gender='F', user_id='1'),

		Event(title='Table Tennis (doubles)',category='aamod', subcategory='sports', team_limit='2', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Table Tennis (doubles)',category='aamod', subcategory='sports', team_limit='2', about=dummy_detail, gender='G', user_id='1'),

		Event(title='Chess',category='aamod', subcategory='sports', team_limit='1', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Chess',category='aamod', subcategory='sports', team_limit='1', about=dummy_detail, gender='F', user_id='1'),

		Event(title='Basketball',category='aamod', subcategory='sports', team_limit='5', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Basketball',category='aamod', subcategory='sports', team_limit='5', about=dummy_detail, gender='F', user_id='1'),

		Event(title='Volley Ball',category='aamod', subcategory='sports', team_limit='6', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Volley Ball',category='aamod', subcategory='sports', team_limit='6', about=dummy_detail, gender='F', user_id='1'),

		Event(title='Football only',category='aamod', subcategory='sports', team_limit='11', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Cricket',category='aamod', subcategory='sports', team_limit='11', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Kho Kho',category='aamod', subcategory='sports', team_limit='9', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Kho Kho',category='aamod', subcategory='sports', team_limit='9', about=dummy_detail, gender='F', user_id='1'),

		Event(title='Race 100m',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Race 100m',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='F', user_id='1'),

		Event(title='Race 200m',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail,  gender='M', user_id='1'),

		Event(title='Race 200m',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail,  gender='F', user_id='1'),

		Event(title='Relay race',category='aamod', subcategory='atheletics', team_limit='4', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Relay race 400m',category='aamod', subcategory='atheletics', team_limit='4', about=dummy_detail, gender='F', user_id='1'),

		Event(title='Relay race',category='aamod', subcategory='atheletics', team_limit='4', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Relay race 400m',category='aamod', subcategory='atheletics', team_limit='4', about=dummy_detail, gender='F', user_id='1'),

		Event(title='Race 400m',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Javelin Boys',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Javelin Girls',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='F', user_id='1'),

		Event(title='Shot put Boys',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Shot put Girls',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='F', user_id='1'),

		Event(title='Discus Throw Boys',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Discus Throw Girls',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='F', user_id='1'),

		Event(title='Long jump Boys',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Long jump Girls',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='F', user_id='1'),

		Event(title='High Jump Boys',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='M', user_id='1'),

		Event(title='High Jump Girls',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='F', user_id='1'),

		Event(title='Shot put Boys',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Shot put Girls',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='F', user_id='1'),

		Event(title='Squash only' ,category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='M', user_id='1'),

		#zest events 

		Event(title='Solo Dance' ,category='zestclose', subcategory='dance', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Duet Dance' ,category='zestclose', subcategory='dance', team_limit='2', about=dummy_detail, user_id='1'),

		Event(title='Best Dancer' ,category='zestopen', subcategory='dance', team_limit='1', about=dummy_detail, gender='M', user_id='1'),

		Event(title='Group Dance' ,category='zestopen', subcategory='dance', team_limit='30', about=dummy_detail, user_id='1'),

		Event(title='Multi Scene' ,category='zestclose', subcategory='drama', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Movie Spoof' ,category='zestclose', subcategory='drama', team_limit='1', about=dummy_detail,    user_id='1'),

		Event(title='Mime' ,category='zestclose', subcategory='drama', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Street Play' ,category='zestclose', subcategory='drama', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Mono Act / Stand Up' ,category='zestclose', subcategory='drama', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Indian Solo' ,category='zestclose', subcategory='music', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Western Solo' ,category='zestclose', subcategory='music', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Duet Song' ,category='zestopen', subcategory='music', team_limit='1', about=dummy_detail,    user_id='1'),

		Event(title='Voice of Zest' ,category='zestclose', subcategory='music', team_limit='1', about=dummy_detail,    user_id='1'),

		Event(title='Battle of bands' ,category='zestopen', subcategory='music', team_limit='1', about=dummy_detail,    user_id='1'),

		Event(title='Rap Battle' ,category='zestclose', subcategory='music', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Dumb Charades' ,category='zestclose', subcategory='informals', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Situational Singing' ,category='zestclose', subcategory='informals', team_limit='1', about=dummy_detail,    user_id='1'),

		Event(title='Whistling' ,category='zestclose', subcategory='informals', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Mind Buzz' ,category='zestclose', subcategory='informals', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Zest got talent' ,category='zestclose', subcategory='informals', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Twig the treasure' ,category='zestclose', subcategory='informals', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Handicraft' ,category='zestclose', subcategory='deco', team_limit='1', about=dummy_detail, user_id='1'),
		
		Event(title='Rangoli' ,category='zestclose', subcategory='deco', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Chitrakar' ,category='zestclose', subcategory='deco', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Gratis' ,category='zestclose', subcategory='fine arts', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Mehendika' ,category='zestopen', subcategory='fine arts', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Charcolate' ,category='zestclose', subcategory='fine arts', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Movie Quiz' ,category='zestclose', subcategory='literary', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Story Recitation' ,category='zestclose', subcategory='literary', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Translation' ,category='zestclose', subcategory='literary', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Open Mic' ,category='zestclose', subcategory='literary', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Calligraphy' ,category='zestclose', subcategory='literary', team_limit='1', about=dummy_detail, user_id='1'),

		Event(title='Fashion Show' ,category='zestclose', subcategory='renaissance', team_limit='1', about=dummy_detail, user_id='1'),	
]

for event in events:
	db.session.add(event)


db.session.commit()
