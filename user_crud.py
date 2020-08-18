from model import db,User,connect_to_db

def create_user(username,password,firstname,lastname,email,door_no,street_addr,zipcode,city,state,country,phone_no,created_date):
    '''Create and return new User'''
    user = User(username=username,
                password=password,
                firstname=firstname,
                lastname=lastname,
                email=email,
                door_no=door_no,
                street_addr=street_addr,
                zipcode=zipcode,
                city=city,
                state=state,
                country=country,
                phone_no=phone_no,
                created_date=created_date)
    db.session.add(user)
    db.session.commit()
    return user


def get_user_ids():
    users = User.query.all()
    ids=[]
    for user in users:
        ids.append(user.user_id)
    return ids

def get_user_by_name(name):
    user = User.query.filter(User.username == name).first()
    return user
def get_user_by_id(id):
    user = User.query.filter(User.user_id == id).first()
    return user
    
if __name__ == '__main__':
    from server import app
    connect_to_db(app)