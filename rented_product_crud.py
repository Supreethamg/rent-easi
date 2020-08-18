from model import db,User,Product,connect_to_db,RentedProduct
 

 
def create_rented_product(product_id,owner_id,renter_id,rented_from,rented_to,price,payment_id,created_date):
    '''Create and return new rented product'''
    rproduct = RentedProduct(product_id=product_id,
                owner_id=owner_id,
                renter_id=renter_id,
                rented_from=rented_from,
                rented_to=rented_to,
                price=price,
                payment_id=payment_id,
                created_date=created_date)
    db.session.add(rproduct)
    db.session.commit()
    return rproduct

def get_all_rproduct_ids():
    rproducts = Product.query.all()
    ids=[]
    for product in rproducts:
        ids.append(product.rented_product_id)
    return ids


def get_all_rentedproducts():
    '''Returns dictionary of products availble for rent fetched from the db tabel'''
    rproducts = RentedProduct.query.all()
    rproducts_list={}
    for idx,val in enumerate(rproducts):
        rproducts_list[val.rented_product_id]=RentedProduct.serialize(val)
    print(rproducts_list)
    return rproducts_list




if __name__ == '__main__':
    from server import app
    connect_to_db(app)