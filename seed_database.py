'''Script to seed database'''
import os
import json
from random import choice,randint
from datetime import datetime
import model
import user_crud
import product_crud
import product_category_crud
import server
import rented_product_crud


os.system('dropdb renteasi')
os.system('createdb renteasi')
model.connect_to_db(server.app)
model.db.create_all()

#load data and save it to a variable
with open('data/users.json') as f:
    user_data = json.loads(f.read())
users_in_db = []
for user in user_data:
    username,password,firstname,lastname,email,door_no,street_addr,zipcode,city,state,country,phone_no = (user['username'],
                                  user['password'],
                                  user['firstname'],
                                  user['lastname'],
                                  user['email'],
                                    user['door_no'],
                                    user['street_addr'],
                                    user['zipcode'],
                                    user['city'],
                                    user['state'],
                                    user['country'],
                                    user['phone_no'])

    created_date = datetime.strptime(user['created_date'],'%Y-%m-%d')
    db_user = user_crud.create_user(username,password,firstname,lastname,email,door_no,street_addr,zipcode,city,state,country,phone_no,created_date)
    users_in_db.append(db_user)


with open('data/category.json') as f:
    category_data = json.loads(f.read())
category_in_db = []
for cat in category_data:
    category_name = (cat['category_name'])
    created_date = datetime.strptime(cat['created_date'],'%Y-%m-%d')
    db_category = product_category_crud.create_product_category(category_name,created_date)
    users_in_db.append(db_category)


# // product_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
# //     owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    
# //     category_id = db.Column(db.String, db.ForeignKey('product_category.category_id'))

with open('data/products.json') as f:
    product_data = json.loads(f.read())
products_in_db = []
for product in product_data:
    title,description,s3_image_url,s3_video_url,condition,available_from,available_to,price,status,isverified = (product['title'],
                                  product['description'],
                                  product['s3_image_url'],
                                  product['s3_video_url'],
                                  product['condition'],
                                    product['available_from'],
                                    product['available_to'],
                                    product['price'],
                                    product['status'],
                                    product['isverified'])
                                 
    created_date = datetime.strptime(product['created_date'],'%Y-%m-%d')
    owner_id = choice(user_crud.get_user_ids())
    category_id = choice(product_category_crud.get_product_category_ids())
    db_product = product_crud.create_product(owner_id,title,description,category_id,s3_image_url,s3_video_url,condition,available_from,available_to,price,status,isverified,created_date)
    users_in_db.append(db_product)


with open('data/rented_products.json') as f:
    rproduct_data = json.loads(f.read())
rproducts_in_db = []
for rproduct in rproduct_data:
    rented_from,rented_to,price,payment_id = (rproduct['rented_from'],
                                    rproduct['rented_to'],
                                    rproduct['price'],
                                    rproduct['payment_id'])
                                   
                                 
    created_date = datetime.strptime(product['created_date'],'%Y-%m-%d')
    owner_id = choice(user_crud.get_user_ids())
    renter_id = choice(user_crud.get_user_ids())
    product_id = choice(product_crud.get_all_product_ids())
    db_rproduct = rented_product_crud.create_rented_product(product_id,owner_id,renter_id,rented_from,rented_to,price,payment_id,created_date)
    rproducts_in_db.append(db_rproduct)




# # Create 10 users; each user will make 10 ratings
# for n in range(10):
#     email=f'user{n}@test.com'
#     password='test'

#     user = crud.create_user(email,password)
#     for _ in range(10):
#         random_movie = choice(movies_in_db)
#         score = randint(1,5)
        # crud.create_rating(user,random_movie,score)
