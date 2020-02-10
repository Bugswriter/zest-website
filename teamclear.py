from zestpkg.models import db, Team
import sqlite3


conn = sqlite3.connect('./zestpkg/site.db')
c = conn.cursor()
teams = Team.query.all()
deadt = []
for team in teams:
    if len(team.members) == 0:
        deadt.append(team.id)


for t in deadt:
    c.execute('delete from team where id=%s'%t)

conn.commit()
conn.close()
