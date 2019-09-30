from zestpkg import db
from zestpkg.models import *

users = [User(username='ziang', email='ziang@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='shiva', email='shiva@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='tyrion', email='tyrion@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='arya', email='arya@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='shiv', email='shiv@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='bucky', email='bucky@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='saitama', email='saitama@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='rick', email='rick@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='morty', email='morty@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='king', email='king@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='law', email='law@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2'),User(username='jyoti', email='jyoti@webhomes.net', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2')]

for user in users:
	db.session.add(user)

db.session.commit()
