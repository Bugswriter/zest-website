from zestpkg import db
from zestpkg.models import *

db.create_all()

admin = User(id='1000', username='admin', email='admin@zest2019.in', password='$2b$12$Q4f8/ixabKLz2cEg.XRluu3BabbUUvvDb.N36WGn19SHXMCR34I/2')
db.session.add(admin)
adminProfile = Profile(name='Suraj Kushwah', course='B.Tech', branch='CS', roll_number='1701410104', phone='7417224655', college='SRMS CET Bareilly', gender='M', user_id='1000')
db.session.add(adminProfile)
try:
	db.session.commit()
except Exception as e:
	print(e)
	print("Skipping...")

dummy_detail = 'Zest / Aamod event.'


events = [

		##  -- ZEST EVENTS ##

		#Dance Club
		Event(title='Group Dance' ,category='zestopen', subcategory='dance', min_limit='10' ,team_limit='30', about=dummy_detail), #1
		Event(title='Solo Dance' ,category='zestclose', subcategory='dance', team_limit='1', about=dummy_detail), #2
		Event(title='Duet Dance' ,category='zestclose', subcategory='dance', team_limit='2', about=dummy_detail), #3
		Event(title='Best Dancer' ,category='zestopen', subcategory='dance', team_limit='1', about=dummy_detail), #4


		#Dramatics Club
		# Team limit special case in all
		Event(title='Multi Scene' ,category='zestclose', subcategory='drama', min_limit='8', team_limit='20', about=dummy_detail), #5
		Event(title='Street Play' ,category='zestclose', subcategory='drama', min_limit='10', team_limit='20', about=dummy_detail), #6
		Event(title='Mime' ,category='zestclose', subcategory='drama', min_limit='6', team_limit='15', about=dummy_detail), #7
		Event(title='Movie Spoof' ,category='zestclose', subcategory='drama', min_limit='6', team_limit='15', about=dummy_detail), #8
		Event(title='Mono Act' ,category='zestclose', subcategory='drama', team_limit='1', about=dummy_detail), #9 #don't know the team limit

		#Fine Arts
		Event(title='Gratis' ,category='zestclose', subcategory='fine arts', team_limit='2', about=dummy_detail), #10
		Event(title='Charcolate' ,category='zestclose', subcategory='fine arts', team_limit='1', about=dummy_detail), #11
		Event(title='Mehendika' ,category='zestopen', subcategory='fine arts', team_limit='1', about=dummy_detail), #12
		
		#Music Club
		Event(title='Indian Solo' ,category='zestclose', subcategory='music', team_limit='1', about=dummy_detail), #13
		Event(title='Western Solo' ,category='zestclose', subcategory='music', team_limit='1', about=dummy_detail), #14
		Event(title='Duet Song' ,category='zestopen', subcategory='music', team_limit='2', about=dummy_detail), #15
		Event(title='Rap Battle' ,category='zestclose', subcategory='music', team_limit='1', about=dummy_detail), #16 
		Event(title='Voice of Zest' ,category='zestclose', subcategory='music', team_limit='1', about=dummy_detail), #17 
		Event(title='Battle of bands' ,category='zestopen', subcategory='music', min_limit='4', team_limit='8', about=dummy_detail), #18  #team limit special case 

		#Informals
		Event(title='Dumb Charades' ,category='zestclose', subcategory='informals', team_limit='2', about=dummy_detail), #19
		Event(title='Situational Antakshari' ,category='zestclose', subcategory='informals', team_limit='4', about=dummy_detail), #20
		Event(title='Whistling' ,category='zestclose', subcategory='informals', team_limit='1', about=dummy_detail), #21
		Event(title='Mind Buzz' ,category='zestclose', subcategory='informals', team_limit='2', about=dummy_detail), #22
		Event(title='Twig the treasure' ,category='zestclose', subcategory='informals', team_limit='2', about=dummy_detail), #23
		Event(title='Zest got talent' ,category='zestclose', subcategory='informals', team_limit='1', about=dummy_detail), #24 #don't know the team
		
		#Literary Events
		Event(title='Translation' ,category='zestclose', subcategory='literary', team_limit='1', about=dummy_detail), #25
		Event(title='Story Recitation' ,category='zestclose', subcategory='literary', team_limit='10', about=dummy_detail), #26 #don't know the limit but team hai
		Event(title='Open Mic' ,category='zestclose', subcategory='literary', team_limit='1', about=dummy_detail), #27
		Event(title='Calligraphy' ,category='zestclose', subcategory='literary', team_limit='1', about=dummy_detail), #28
		Event(title='Movie Quiz' ,category='zestclose', subcategory='literary', team_limit='2', about=dummy_detail), #29

		#Deco Events
		Event(title='Best out of waste' ,category='zestclose', subcategory='deco', min_limit='2', team_limit='4', about=dummy_detail), #30
		Event(title='Rangoli' ,category='zestclose', subcategory='deco', team_limit='2', about=dummy_detail), #31

		#Renaissance
		Event(title='Fashion Show' ,category='zestclose', subcategory='renaissance', team_limit='1', about=dummy_detail), #32


		#Aamod events
		Event(title='Badminton (single)',category='aamod', subcategory='sports', team_limit='1', about=dummy_detail, gender='M'),
		Event(title='Badminton (single)',category='aamod', subcategory='sports', team_limit='1', about=dummy_detail, gender='F'),
		Event(title='Badminton (doubles)',category='aamod', subcategory='sports', team_limit='2', about=dummy_detail, gender='M'),
		Event(title='Badminton (doubles)',category='aamod', subcategory='sports', team_limit='2', about=dummy_detail, gender='F'),
		Event(title='Table Tennis (single)',category='aamod', subcategory='sports', team_limit='1', about=dummy_detail, gender='M'),
		Event(title='Table Tennis (single)',category='aamod', subcategory='sports', team_limit='1', about=dummy_detail, gender='F'),
		Event(title='Table Tennis (doubles)',category='aamod', subcategory='sports', team_limit='2', about=dummy_detail, gender='M'),
		Event(title='Table Tennis (doubles)',category='aamod', subcategory='sports', team_limit='2', about=dummy_detail, gender='G'),
		Event(title='Chess',category='aamod', subcategory='sports', team_limit='1', about=dummy_detail, gender='M'),
		Event(title='Chess',category='aamod', subcategory='sports', team_limit='1', about=dummy_detail, gender='F'),
		Event(title='Basketball',category='aamod', subcategory='sports', team_limit='10', about=dummy_detail, gender='M'),
		Event(title='Basketball',category='aamod', subcategory='sports', team_limit='10', about=dummy_detail, gender='F'),
		Event(title='Volley Ball',category='aamod', subcategory='sports', team_limit='6', about=dummy_detail, gender='M'),
		Event(title='Volley Ball',category='aamod', subcategory='sports', team_limit='6', about=dummy_detail, gender='F'),
		Event(title='Football only',category='aamod', subcategory='sports', team_limit='11', about=dummy_detail, gender='M'),
		Event(title='Cricket',category='aamod', subcategory='sports', team_limit='11', about=dummy_detail, gender='M'),
		Event(title='Kho Kho',category='aamod', subcategory='sports', team_limit='9', about=dummy_detail, gender='M'),
		Event(title='Kho Kho',category='aamod', subcategory='sports', team_limit='9', about=dummy_detail, gender='F'),
		Event(title='Race 100m',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='M'),
		Event(title='Race 100m',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='F'),
		Event(title='Race 200m',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail,  gender='M'),
		Event(title='Race 200m',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail,  gender='F'),
		Event(title='Relay race',category='aamod', subcategory='atheletics', team_limit='4', about=dummy_detail, gender='M'),
		Event(title='Relay race 400m',category='aamod', subcategory='atheletics', team_limit='4', about=dummy_detail, gender='F'),
		Event(title='Relay race',category='aamod', subcategory='atheletics', team_limit='4', about=dummy_detail, gender='M'),
		Event(title='Relay race 400m',category='aamod', subcategory='atheletics', team_limit='4', about=dummy_detail, gender='F'),
		Event(title='Race 400m',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail),
		Event(title='Javelin Boys',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='M'),
		Event(title='Javelin Girls',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='F'),
		Event(title='Shot put Boys',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='M'),
		Event(title='Shot put Girls',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='F'),
		Event(title='Discus Throw Boys',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='M'),
		Event(title='Discus Throw Girls',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='F'),
		Event(title='Long jump Boys',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='M'),
		Event(title='Long jump Girls',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='F'),
		Event(title='High Jump Boys',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='M'),
		Event(title='High Jump Girls',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='F'),
		Event(title='Shot put Boys',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='M'),
		Event(title='Shot put Girls',category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='F'),
		Event(title='Squash only' ,category='aamod', subcategory='atheletics', team_limit='1', about=dummy_detail, gender='M'),
]

for event in events:
	db.session.add(event)

db.session.commit()

print("Events registered..")

rules = [
		# Group dance
		Rule(rule="Number of participants in a group should be between 10 to 30", event_id='1'),
		Rule(rule="Song(s) should be from Indian movie, beats, album (only 2 song), Punjabi (only 1 song). Although songs for fillers/punch lines can be of any origin.", event_id='1'),
		Rule(rule="Mixing of songs are allowed.", event_id='1'),
		Rule(rule="Time duration: 8 to 11 minutes", event_id='1'),
		Rule(rule="Minimum FIVE members should be on stage throughout the performance.", event_id='1'),
		Rule(rule="All the groups must perform on the theme of 'VIHANG' - Unity in diversity (at least 1 dance continuous sequence).", event_id='1'),
		Rule(rule="At most 3 Blackouts are allowed.", event_id='1'),

		#Solo dance
		Rule(rule="Song should be from an Indian movie, album or hollywood songs, Punjabi, Beats are allowed.", event_id='2'),
		Rule(rule="Time limit: 1:30 to 2:30 minutes.", event_id='2'),
		Rule(rule="Any song as per the participant's choice.", event_id='2'),
		Rule(rule="Fusion of maximum 2 songs is allowed.", event_id='2'),
		Rule(rule="Use of props are mandatory.", event_id='2'),
		Rule(rule="Costumes are encouraged", event_id='2'),

		# Duet Dance
		Rule(rule="Time limit: 2 to 3 minutes.", event_id='3'),
		Rule(rule="Song selection as per participant choice.", event_id='3'),
		Rule(rule="Fusion is allowed.", event_id='3'),

		# Best Dancer
		Rule(rule="Top 3 rankers of solo and duet dance will be the contestants for Best Dancer.", event_id='4'),
		Rule(rule="Participants must perform on the theme. (at least once dance form).", event_id='4'),
		Rule(rule="Participant must perform for at least 3 minutes.", event_id='4'),
		Rule(rule="From duet team any one member can participate.", event_id='4'),
		Rule(rule="Songs will be disclosed after zest inaugural & participant can choose 3 songs from it.", event_id='4'),

		# Multiscene
		Rule(rule="Each Team should have a minimum of 8 and maximum of 20 members", event_id='5'),
		Rule(rule="Maximum time is 18 minutes (curtain to curtain) and minimum time is 8 minutes (excluding set-up time)..", event_id='5'),
		Rule(rule="There should be at least three scenes.", event_id='5'),
		Rule(rule="Background music is allowed. But not that sad one which every one plays every year. (Sorry for this admin joke)", event_id='5'),
		Rule(rule="Props are allowed and the participants must arrange themselves.", event_id='5'),

		#Street Play
		Rule(rule="Each team should have minimum 10 members & maximum 20 members.", event_id='6'),
		Rule(rule="Time limit is 8 minutes to 115 minutes.", event_id='6'),
		Rule(rule="No music supports.", event_id='6'),
		Rule(rule="For props only duppatta, hand-made posters, calling bells , drum, and steel plates are allowed.", event_id='6'),
		Rule(rule="Unformity in dress is required.", event_id='6'),

		#Mime
		Rule(rule="There should be a minimum of 6 and maximum of 15 members.", event_id='7'),
		Rule(rule="Time limit is 7 to 12 minutes.", event_id='7'),
		Rule(rule="The act should not contain any dialogue, lip sync, song or props. Only instrumental sound is allowed.", event_id='7'),
		Rule(rule="Uniformity in dresses is compulsory.", event_id='7'),
		Rule(rule="Face color variations are allowed.", event_id='7'),
		Rule(rule="Negative points will be awarded in case of Teeth of participant is visible.", event_id='7'),

		#Movie spoof
		Rule(rule="Team of minimum of 6 and maximum 15 members are allowed.", event_id='8'),
		Rule(rule="Time limit is 8 to 15 minutes (including setup time).", event_id='8'),
		Rule(rule="Script must be based upon one or more movies.", event_id='8'),
		Rule(rule="Background sounds are allowed.", event_id='8'),

		# Mono Act
		Rule(rule="Time limit is 4:30 minutes (thinking 1:30 minutes, performance-2 to 3 minutes (not less than 2 minutes and not more than 3 minutes)).", event_id='9'),
		Rule(rule="Props are not allow.", event_id='9'),
		Rule(rule="Background sound/music is not allowed.", event_id='9'),

		# Gratis (handfree painting)
		Rule(rule="Time limit: 30 minutes.", event_id='10'),
		Rule(rule="Team of two members.", event_id='10'),
		Rule(rule="Theme based.", event_id='10'),
		Rule(rule="Participants can use their environment.", event_id='10'),
		Rule(rule="A4 sized sheets and colored paper will be provided.", event_id='10'),

		# Charcolate 
		Rule(rule="Time limit 30 minutes.", event_id='11'),
		Rule(rule="Individual event.", event_id='11'),
		Rule(rule="Theme based. Theme will be provided.", event_id='11'),
		Rule(rule="Charcoals lead & A4 sheets will be provided.", event_id='11'),

		# Mehndhika
		Rule(rule="Time limit 30 minutes.", event_id='12'),
		Rule(rule="Individual event.", event_id='12'),
		Rule(rule="Mehndi cones will be provided. (only 1)", event_id='12'),
		Rule(rule="Participants either nut mehndi in his/her hand or may bring an extra pers.", event_id='12'),

		# Indian Solo
		Rule(rule="Song in any Indian language is allowed.", event_id='13'),
		Rule(rule="Time limit 2 to 5 minutes", event_id='13'),
		Rule(rule="Instrument/ Karaoke is must.", event_id='13'),

		# Western Solo
		Rule(rule="Any western song can be selected.", event_id='14'),
		Rule(rule="Time limit 2 to 5 minutes.", event_id='14'),
		Rule(rule="Instrument/ Karaoke is must.", event_id='14'),

		# Duet song
		Rule(rule="Songs in any language are allowed.", event_id='15'),
		Rule(rule="Male-Female constraints not compulsory.", event_id='15'),

		# Rap battle
		Rule(rule="Songs in any language are allowed.", event_id='16'),
		Rule(rule="Participant should perform on his/her own lyrics, no copy is allowed and leads to disqualification.", event_id='16'),

		# Voice of Zest 
		Rule(rule="1st round - The top 2 contestants of Indian solo, duet song and wetern solo will get direct entry to the voice of zest.", event_id='17'),
		Rule(rule="1st round - From duet song only one member of team will be allowed.", event_id='17'),
		Rule(rule="1st round - First round will be 'own choice round'. Any song can be selected as per contestant choice.", event_id='17'),
		Rule(rule="2nd round - Second round will be 'Judge's choice Round.'", event_id='17'),
		Rule(rule="2nd round - Judges will announce 2 songs from the VOZ songs list, anyone of them must be selected on spot.", event_id='17'),
		Rule(rule="The (VOZ) songs list will be displayed after Zest inaugural.", event_id='17'),

		# Battle of bands
		Rule(rule="Only 6 entries are allowed (On first Come, First serve basis).", event_id='18'),
		Rule(rule="20 minutes time will be allotted, including sound check.", event_id='18'),
		Rule(rule="Only a piece drum set, along with 2 crash and 1 ride cymbals will be provided by the organising team.", event_id='18'),
		Rule(rule="Marks shall be deducted if the band exceeds the time limit.", event_id='18'),
		Rule(rule="Songs only in Hindi/English/Punjabi languages are allowed.", event_id='18'),
		Rule(rule="Lyrics of the songs are required to be submitted prior to the performance.", event_id='18'),
		Rule(rule="The band must comprise of 4-8 members only.", event_id='18'),
		Rule(rule="Decision of the judges will be final.", event_id='18'),
		Rule(rule="Any in-disciplinary action will lead to disqualification.", event_id='18'),


		# Informals
		Rule(rule="Team of two members is alloed.", event_id='19'),
		Rule(rule="Number of rounds will be one.", event_id='19'),
		Rule(rule="Movie's name", event_id='19'),
		Rule(rule="Time limit to guess the movie will be one minute.", event_id='19'),

		# Situationsal antakshari
		Rule(rule="Team of 4 members is allowed.", event_id='20'),
		Rule(rule="Time limit one minute 30 seconds.", event_id='20'),
		Rule(rule="Team must sing maximum number of songs related to the situation.", event_id='20'),
		Rule(rule="Number of rounds will be one.", event_id='20'),
		Rule(rule="Situation will be selected by the Participants. (Pick a slip)", event_id='20'),

		# Whistling
		Rule(rule="There will be two rounds for whistling.", event_id='21'),
		Rule(rule="1st round-one song of Participants choice.", event_id='21'),
		Rule(rule="2nd Round - Pick a slip.", event_id='21'),

		# Mind buzz
		Rule(rule="Question will be given on G.K and aptitude.", event_id='22'),
		Rule(rule="Team of 2 members.", event_id='22'),
		Rule(rule="Time limit will be 30 minutes.", event_id='22'),

		# Twig the Treasure
		Rule(rule="Team of two members. Maximum time limit 30 minutes.", event_id='23'),
		Rule(rule="There will be one round. There will be three winners.", event_id='23'),
		Rule(rule="Rules can be detailed on spot.", event_id='23'),

		#Zest got talent
		Rule(rule="Event rules will be disclosed on the event time.", event_id='24'),

		# Translation
		Rule(rule="A total of 6 sentences and 4 words will be given.", event_id='25'),
		Rule(rule="3 Sectences and 2 words will be given in Hindi and are supposed to be translated to English.", event_id='25'),
		Rule(rule="3 sentences and 2 words will be given in English and are supposed to be translated to Hindi.", event_id='25'),
		Rule(rule="Marks will be given in accordance with the nearst meaning of the given word/sentence in translated language.", event_id='25'),
		Rule(rule="A total of 10 min. will be given for tranlation. <br> i.e 5 min. for Hindi to English tranlation of 3 sentences and 2 words <br> 5 min. for English to Hindi translation of 3 sentences and 2 word.", event_id='25'),


		# Story recitation
		Rule(rule="Only 4 participants are allowed from each college.", event_id='26'),
		Rule(rule="The event will consist of 2 rounds.", event_id='26'),
		Rule(rule="1st round: All teams will be shown some pictures.", event_id='26'),
		Rule(rule="Second round (the top 6 teams will qualify for this round.", event_id='26'),
		Rule(rule="2nd round: Teams must choose a chit in which a phrase will be written.", event_id='26'),
		Rule(rule="2nd round: First 10 min.s for planning and 3-5 min. for recitation will be given.", event_id='26'),
		Rule(rule="Internet or any other source will not be allowed during the event.", event_id='26'),
		Rule(rule="Evaluation will be based on presentation, imagination and creativity.", event_id='26'),
		Rule(rule="In any case decision of judges shall be final.", event_id='26'),

		# Open mic
		Rule(rule="It will be an individual event.", event_id='27'),
		Rule(rule="A time of 3 min. to 6 min. will be given to each participant.", event_id='27'),
		Rule(rule="However, the judges have the discretion to stop the performance in between  ", event_id='27'),
		Rule(rule="The content should not be taken from any other source, it should be your own material.", event_id='27'),
		Rule(rule="The decision of judges shall be final in case of any discrepany.", event_id='27'),

		# Calligraphy
		Rule(rule="Individual Event.", event_id='28'),
		Rule(rule="Open for all.", event_id='28'),
		Rule(rule="Time duration: 30 mins.", event_id='28'),
		Rule(rule="Suitable content will be provided for writing to each participant.", event_id='28'),
		Rule(rule="Sheets will be provided.", event_id='28'),
		Rule(rule="Any type of writing material will be allowed.", event_id='28'),

		# Movie quiz
		Rule(rule="Team event of 2 members", event_id='29'),
		Rule(rule="2 teams will be allowed from each invited college & 4 teams from each SRMS Trust Institution.", event_id='29'),
		Rule(rule="Question will be based on any movie scene or act, video song, picture of a scene etc.", event_id='29'),
		Rule(rule="Rapid-Fire event.", event_id='29'),
		Rule(rule="5 Questions for each group.", event_id='29'),
		Rule(rule="Points will be awarded on first come first corrent answer basis.", event_id='29'),

		# Best out of waste
		Rule(rule="Time limit: 30 min.", event_id='30'),
		Rule(rule="Team of 2-4 members.", event_id='30'),
		Rule(rule="Requirements must be bringing by participants.", event_id='30'),
	
		# Rangoli
		Rule(rule="A team event of two members.", event_id='31'),
		Rule(rule="Time limit: 45 minutes", event_id='31'),
		Rule(rule="Participants must make within prescribed area.", event_id='31'),
		Rule(rule="Requiremnet must be bringing by participants.", event_id='31'),

		# Renaissance 
		Rule(rule="This year's theme for renaissance is 'BHRAMAN': - The world tour.", event_id='32'),
		Rule(rule="Only SRMS Trust Institutions can participate with one team only & maximum of 15 members.", event_id='32'),
		Rule(rule="No external participation is allowed", event_id='32'),
		Rule(rule="The maximum time for each group to be on stage will be 8 minutes and if the time exceeds the whole team will be disqualified and the track will be muted.", event_id='32'),
		Rule(rule="For girls no short dresses (above knees), no backless and no off-shoulder clothes are allowed.", event_id='32'),
		Rule(rule="For boys no revealing chest and cut sleeves.", event_id='31'),
		Rule(rule="Touching is not allowed.", event_id='32'),
		Rule(rule="Props are allowed (excluding any sharp things, fire).", event_id='32'),
		Rule(rule="Each participant will enter the stage only twice and gets two chance to go to the T-point (one individual & one with pair or team)", event_id='32'),

]

for rule in rules:
	db.session.add(rule)

db.session.commit()
print("Rules done!")

team = Team(id='100', name='testteam', event_id='35')
db.session.add(team)
db.session.commit()
print('Team done!')

print("Script done!")
