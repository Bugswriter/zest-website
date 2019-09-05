from zestpkg import db, bcrypt
65;5603;1cfrom zestpkg.models import *



def uid_from_username(username):
    try:
        user = User.query.filter_by(username=username).first()
    except:
        return False

    return user.id



if __name__=='__main__':
    db.create_all()
    while True:
        print(
            '''
            Choose table:
            1. User
            2. Profile
            3. Event
            4. Team
            5. Participant
            '''
        )
        choice = int(input())

        if choice == 1:
            #user
            print("Enter Username:", end=" ")
            username = str(input())
            print("Enter Email:", end=" ")
            email = str(input())
            print("Enter Password:", end=" ")
            password = str(input())
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(username=username, email=email, password=hashed_password)
            db.session.add(user)
            
        elif choice == 2:
            #Profile
            print("Enter Name:", end=" ")
            name = str(input())
            print('''
                Choose Course:
                1. B.Tech
                2. B.Pharm
                3. MBA
                4. Other
            ''')
            x = int(input())
            branch = "NA"
            while True:
                if x == 1:
                    course = "B.Tech"
                    b = random.randint(0,5)
                    if b == 0:
                        branch = "CS"
                    elif b == 1:
                        branch = "EC"
                    elif b == 2:
                        branch = "EN"
                    elif b == 3:
                        branch = "ME"
                    elif b == 4:
                        branch = "IT"
                
                    break

                elif x == 2:
                    course = "B.Pharm"
                    break

                elif x == 3:
                    course = "MBA"
                    break

                elif x == 4:
                    course = "Other"
                    break

                else:
                    print("Choose corrent option")
                    continue


            print("Roll Number last 3 digit:", end=" ")
            last = str(input())
            roll_num = "1701410"+last

            print("Enter your phone number:", end=" ")
            phone = input()
            college = "SRMS CET Bareilly"
            print("Gender in M or F format:", end=" ")
            gender = input()

            print("Enter username of user", end=" ")
            username = input()
            uid = uid_from_username(username)
            if not uid:
                print("User with this username doesn't exist!")
                break

            profile = Profile(name=name, course=course, branch=branch, roll_number=roll_num, college=college, phone=phone, gender=gender, user_id=uid)

            db.session.add(profile)

        elif choice == 3:
            #Event
            print("Enter Event Title:", end=" ")
            title = str(input())
            print("Enter User id of organizer:", end=" ")
            user_id = int(input())
            print("Enter team limit:", end=" ")
            team_limit = int(input())
            event = Event(title=title, user_id=user_id, team_limit=team_limit)
            db.session.add(event)

        elif choice == 4:
            #Team
            print("Enter Name of team:", end = " ")
            name = str(input())
            print("Enter Event ID:", end=" ")
            event = int(input())
            secret_code = generate_team_code()
            team = Team(name=name, event_id=event, team_code=secret_code)

            db.session.add(team)
            

        elif choice == 5:
            #Participation
            print("Enter Username of participant", end=" ")
            username = input()
            uid = uid_from_username(username)
            if not uid:
                print("User with this username doesn't exist!")
                break

            print("Enter Event ID", end=" ")
            eid = int(input())

            event = Event.query.get(eid)
            if not event:
                print("No Event with this ID Exist")
                break

            if event.eventType() == "Team":
                print("Enter Team Secret Code:", end=" ")
                secret_code = input()
                team = Team.query.filter_by(team_code=secret_code).first()
                if not team:
                    print("Invalid Secret Code!")
                    break

                tid = team.id
                

            participation = Participants(user_id=uid, event_id=eid, team_id=tid)
            db.session.add(participation)

        else:
            print("Please choose correct Option")
            continue


        try:
            db.session.commit()
            print("Data inserted successfully")
        except Exception as e:
            print("Error: {}".format(e))
    
