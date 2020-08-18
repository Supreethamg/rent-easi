from model import db,User,ProductCategory,connect_to_db

def create_product_category(category_name,created_date):
    '''Create and return new User'''
    product_category = ProductCategory(category_name=category_name,created_date=created_date)
    db.session.add(product_category)
    db.session.commit()
    return product_category

def get_product_category_ids():
    categories = ProductCategory.query.all()
    ids=[]
    for cat in categories:
        ids.append(cat.category_id)
    return ids


def get_all_product_category():
    '''Return dictionary of ProductCategory objects fetched from DB table '''
    categoris = ProductCategory.query.all()
    category_list={}
    for idx,val in enumerate(categoris):
        category_list[val.category_name]=ProductCategory.serialize(val)
    return category_list


if __name__ == '__main__':
    from server import app
    connect_to_db(app)