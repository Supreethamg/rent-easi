from model import db,User,Product,connect_to_db
 
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


if __name__ == '__main__':
    from server import app
    connect_to_db(app)