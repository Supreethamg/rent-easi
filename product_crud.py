from model import db,User,Product,connect_to_db,RentedProduct
 
def create_product(owner_id,title,description,category_id,s3_image_url,s3_video_url,condition,available_from,available_to,price,status,isverified,created_date):
    '''Create and return new User'''
    product = Product(owner_id=owner_id,
                title=title,
                description=description,
                category_id=category_id,
                s3_image_url=s3_image_url,
                s3_video_url=s3_video_url,
                condition=condition,
                available_from=available_from,
                available_to=available_to,
                price=price,
                status=status,
                isverified=isverified,
                created_date=created_date)
    db.session.add(product)
    db.session.commit()
    return product

def get_all_product_ids():
    products = Product.query.all()
    ids=[]
    for product in products:
        ids.append(product.product_id)
    return ids


def get_all_products():
    '''Returns dictionary of products fetched from the db tabel'''
    products = Product.query.all()
    products_list={}
    for idx,val in enumerate(products):
        products_list[val.product_id]=Product.serialize(val)
    print(products_list)
    return products_list


def get_product_by_id(id):
    product = Product.query.get(id)
    #return Product.serialize(product)
    return product

def get_available_products():
    subquery =db.session.query(RentedProduct.rented_product_id)
    products = Product.query.filter(Product.product_id.notin_(subquery)).all()
    print(f"products*******:{products}")
    products_list={}
    for idx,val in enumerate(products):
        products_list[val.product_id]=Product.serialize(val)
    print(products_list)
    return products_list
    



if __name__ == '__main__':
    from server import app
    connect_to_db(app)