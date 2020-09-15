# RentEazi

RentEazi is a rental marketplace where users can rent out their rarely used products and monetize them. Likewise for those consumers who want products for single use, can rent products from this marketplace for a specific period of time rather than buying it.

# Contents
- Tech Stack
- Features
- Future State
- Installation

# Technologies
  - Python
  - Flask
  - Jinja2
  - PostgreSQL
  - SQLAlchemy ORM
  - HTML
  - CSS
  - Bootstrap
  - jQuery
  - Amazon S3
  - Amazon SES
  - Boto3
 
# Features
### Home Page
User Registration or login

![Register_Page](https://github.com/Supreethamg/rent-easi-HB-project/blob/master/static/image/register_page.PNG?raw=true)

### Landing Page
After user login, default view is to display to the users product listing page where all the products available for rent are listed
![Landing_Page](https://github.com/Supreethamg/rent-easi-HB-project/blob/master/static/image/home_page.PNG?raw=true)

### My Ads
On this page, user can view all the products listed for rent 
![My_Ads_Page](https://github.com/Supreethamg/rent-easi-HB-project/blob/master/static/image/my_ads_page.PNG?raw=true)

### My Rentals 
On this page, user can view all their rented products 
![My_Rentals_Page](https://github.com/Supreethamg/rent-easi-HB-project/blob/master/static/image/my_rentals_page.PNG?raw=true)

### Product Search
This feature allows users to search for any specific product
![Search_Page](https://github.com/Supreethamg/rent-easi-HB-project/blob/master/static/image/search_page.png?raw=true)

### Post product for Rent
In this page, users can fill in a form, upload all the images/videos related to the product that they want to list for rent
![Create_Ad_Page](https://github.com/Supreethamg/rent-easi-HB-project/blob/master/static/image/create_ad_page.PNG?raw=true)

### Admin page
Upon posting a product to rent, every ad goes through an admin review process and only after approval, the product is availble for rent
![Admin_Page](https://github.com/Supreethamg/rent-easi-HB-project/blob/master/static/image/admin_approval.PNG?raw=true)

### Admin user email notification
Upon posting a product to rent, an email alert is triggered to the admin user for seamless approval process
![Email_Page](https://github.com/Supreethamg/rent-easi-HB-project/blob/master/static/image/email.PNG?raw=true)

# Future State
  - Payment app (Paypal) integration
  - Address verification (USPS) api integration
  - Geo-location (google api) integration
  - Deployment to AWS with load balancer

### Installation

Install PostgreSQL (Windows/MacOS)

Clone or fork this repo 
```sh
https://github.com/Supreethamg/rent-easi-project
```
Create and activate a virtual environment inside your rent-eazi directory

```sh
virtualenv env
source env/bin/activate
```
Install the dependencies

```sh
pip install -r requirements.txt
```
Sign up to use Amazon S3 API
Save your API keys in a file called secrets.sh using this format
```sh
export AWS_API_KEY="YOUR_KEY_HERE"
export AWS_CLIENT_ID="YOUR_ID_HERE"
```
Source your keys from your secrets.sh file into your virtual environment:
```sh
source secrets.sh
```
Setup the database
```sh
createdb renteazi
python3 seed_database.py
```
Run the app
```sh
python3 server.py
```
Open a browser url and navigate to
```sh
http://localhost:5000/
```
