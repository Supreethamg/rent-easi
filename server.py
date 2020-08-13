"""Server for Rentasi app."""

from flask import(Flask,render_template,request,flash,session,redirect)
from model import connect_to_db

from jinja2 import StrictUndefined
from config import S3_BUCKET, S3_KEY, S3_SECRET,S3_REGION,get_bucket,get_s3_resource
from s3_crud import upload_file

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
 

# # Replace this with routes and view functions!
@app.route('/')
def registerpage():
    return render_template('file.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    upload_file(file)
    

    flash('File uploaded successfully')
    return redirect("/")

# @app.route('/login', methods=['GET'])
# def login():
#     return render_template('login.html')

# @app.route('/home')
# def homepage():
#     '''View homepage'''
#     return render_template('homepage.html')

# @app.route('/movies')
# def all_movies():
#     movies = crud.get_all_movies()
#     return render_template('all_movies.html',movies=movies)


# @app.route('/movies/<movie_id>')
# def show_movie(movie_id):
#     """Show details on a particular movie."""

#     movie = crud.get_movie_by_id(movie_id)

#     return render_template('movie_details.html', movie=movie)


# @app.route('/users')
# def all_users():
#     users = crud.get_all_users()
#     return render_template('all_users.html',users=users)

# @app.route('/register',methods=['POST'])
# def register_user(): 
#     '''Create new user if user does not exists already'''
#     email = request.form.get('email')
#     pwd = request.form.get('password') 
#     print(email)
#     print(pwd)
#     user = crud.get_user_by_email(email)
#     print(user)
#     if user:
#         flash('This email is already used.Try with different email')
#     else:
#         crud.create_user(email,pwd)
#         flash('Account created!Please log in')
#     return redirect('/')

# @app.route('/login',methods=['POST'])
# def user_login(): 
#     '''Logs in the user if email and password match'''
#     email = request.form.get('useremail')
#     pwd = request.form.get('userpassword')
#     user = crud.get_user_by_email(email)
#     if pwd == user.password:
#         session['loggedin_user']=  user.user_id
#         flash('Logged In!!')
#         return redirect('/home')
#     else:
#          flash('Passwords do not match try again!!')
#          return redirect('/login')
    
          


# @app.route('/users/<user_id>')
# def show_user(user_id):
#     """Show details on a particular User."""

#     user = crud.get_user_by_id(user_id)

#     return render_template('user_details.html', user=user)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
