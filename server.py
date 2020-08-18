"""Server for Rentasi app."""

from flask import(Flask,render_template,request,flash,session,redirect,jsonify,Response)
from model import connect_to_db,User
from jinja2 import StrictUndefined
from config import S3_BUCKET, S3_KEY, S3_SECRET,S3_REGION,get_bucket,get_s3_resource
from s3_crud import upload_file,get_s3_url
import user_crud 
from datetime import datetime
import product_category_crud
import product_crud


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
 

# # Replace this with routes and view functions!

@app.route('/')
def base():
    session['current_user']= None
    return redirect('/api/login')

@app.route('/api/register')
def register_page():
           return render_template('register.html')

@app.route('/api/register',methods=['POST'])
def register_account():
    
        username= request.form.get('username') 
        password= request.form.get('password') 
        fname= request.form.get('fname') 
        lname= request.form.get('lname') 
        email= request.form.get('email') 
        door_no= request.form.get('doorno') 
        street_addr= request.form.get('streetaddr') 
        zipcode= request.form.get('zipcode') 
        phone_no= request.form.get('phone') 
        state= request.form.get('state') 
        city= request.form.get('city') 
        country= request.form.get('country') 
        current_date =datetime.date(datetime.now())
        print(f'curent date:{current_date}')
        user = user_crud.create_user(username,password,fname,lname,email,door_no,street_addr,zipcode,city,state,country,phone_no,current_date)
        flash('Account created!')
        return redirect("/api/login")


@app.route('/api/login')
def login_page(): 
    if session['current_user']:
        return redirect("/api/home")
    else:
        return render_template('login.html')


@app.route('/api/login',methods=['POST'])
def user_login(): 
    '''Logs in the user if email and password match'''
    username = request.form.get('username')
    password = request.form.get('password')
    user = user_crud.get_user_by_name(username)
    if not user:
        flash('Please create Account!!')
        return redirect('/api/register')
    else:
        if password == user.password:
            session['current_user'] =  user.user_id
            session['current_user_name'] =  user.username
            flash('Logged In!!')
            return redirect('/api/home')
        else:
            flash('Passwords do not match try again!!')
            return redirect('/api/login')


@app.route('/api/product-category')
def get_product_categories():
    '''Get all product categries'''

    categories = product_category_crud.get_all_product_category()
    return categories



@app.route('/api/home')
def homepage():
    '''View homepage'''
    #user=get_user_by_id(session['current_user'])
    return render_template('homepage.html')




@app.route('/api/post-ad')
def post_ad_page():
    '''Returns Post ad page for product to rent'''
    return render_template('post_product.html')



@app.route('/api/post-ad',methods=['POST'])
def post_ad():
    '''Save ad posts for product to rent'''
    print("inside post ad")
    title= request.form.get('title')
    category=request.form.get("category")
    print(f'category_user:{category}')
    description=request.form.get("description")
    image_file= request.files["image"]
    
    if request.files["video"]:
        video_file=request.files["video"].filename
    else:
        video_file=""
    print(f'image:{image_file.filename}')
    print(f'image:{video_file}')
    condition= request.form.get("condition")
    available_from=request.form.get("available_from")
    available_from = datetime.strptime(available_from,'%Y-%m-%d')
    available_to= request.form.get("available_to")
    available_to = datetime.strptime(available_to,'%Y-%m-%d')
    price=request.form.get("price")
    created_date = datetime.date(datetime.now())
    owner_id = session['current_user']
    upload_file(image_file)
    s3_image_url = get_s3_url(image_file.filename)
    s3_video_url = get_s3_url(video_file)

    product_crud.create_product(owner_id,title,description,category,s3_image_url,s3_video_url,condition,available_from,available_to,price,'pending',False,created_date)
    flash('Ad created successfully')
    return jsonify(dict(redirect='/api/home'))

@app.route('/api/get-all-categories')
def get_all_categories():
    categories= product_category_crud.get_all_product_category() 
    return jsonify(categories)


@app.route('/api/get-available-products')
def get_available_products():
    products= product_crud.get_available_products()
    return jsonify(products)



@app.route('/api/get-product/<product_id>')
def get_product(product_id):
    """Show details on a particular product."""
    print("inside get_product  :{product_id}")
    product = product_crud.get_product_by_id(product_id)

    return render_template('view_product.html', product=product)
    
# @app.route('/file')
# def upload_file_page():
#     return render_template('file.html')

# @app.route('/upload', methods=['POST'])
# def upload():
#     file = request.files['file']
#     upload_file(file)
#     flash('File uploaded successfully')
#     return redirect("/")

# @app.route('/download', methods=['POST'])
# def download():
#     key = 'test.txt'
#     my_bucket = get_bucket()
#     my_bucket = get_bucket()
#     file_obj = my_bucket.Object(key).get()

#     return file_obj
#     # Response(
    #     file_obj['Body'].read(),
    #     mimetype='text/plain',
    #     headers={"Content-Disposition": "attachment;filename={}".format(key)}
    # )


# @app.route('/login', methods=['GET'])
# def login():
#     return render_template('login.html')



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
@app.route('/api/logout')
def logoutpage():
    '''logout page'''
    session['current_user']=None
    return redirect('/')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
