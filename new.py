from zestpkg import db
from zestpkg.models import *
'''
users = [User(username='ziang', email='ziang@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='shiva', email='shiva@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='tyrion', email='tyrion@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='arya', email='arya@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='shiv', email='shiv@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='bucky', email='bucky@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='saitama', email='saitama@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='rick', email='rick@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='morty', email='morty@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='king', email='king@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='law', email='law@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='jyoti', email='jyoti@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2')]

for user in users:
	db.session.add(user)

db.session.commit()
'''

profiles=[Profile(name='ziang yang', course='B.Tech', branch='CS', roll_number='1701410014', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=7),
			Profile(name='shiva yogi', course='B.Tech', branch='CS', roll_number='1701410015', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=8),
			Profile(name='tyrion lan', course='B.Tech', branch='CS', roll_number='1701410017', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=9),
			Profile(name='arya stark', course='B.Tech', branch='CS', roll_number='1701410014', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=10),
			Profile(name='shiv raj', course='B.Tech', branch='CS', roll_number='1701410016', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=11),
			Profile(name='bucky rob', course='B.Tech', branch='CS', roll_number='1701410018', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=12),
			Profile(name='saitama one', course='B.Tech', branch='CS', roll_number='1701410019', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=13),
			Profile(name='rick yang', course='B.Tech', branch='CS', roll_number='1701410024', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=14),
			Profile(name='morty rick', course='B.Tech', branch='CS', roll_number='1701410025', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=15),
			Profile(name='king kazama', course='B.Tech', branch='CS', roll_number='1701410026', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=16),
			Profile(name='law blind', course='B.Tech', branch='CS', roll_number='1701410017', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=17),
			Profile(name='jyoti bitc', course='B.Tech', branch='CS', roll_number='1701410018', phone='8218004175', college='SRMS CET Bareilly', gender='M',  user_id=18),]

for profile in profiles:
	db.session.add(profile)

db.session.commit()