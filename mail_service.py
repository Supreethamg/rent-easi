
import boto3
from botocore.exceptions import ClientError
import config
import json


def send_request_approval_email(name,email,product):

    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    SENDER = "supreethamg@gmail.com"

    # Replace recipient@example.com with a "To" address. If your account 
    # is still in the sandbox, this address must be verified.
    RECIPIENT = 'services.renteasi@gmail.com'

    # Specify a configuration set. If you do not want to use a configuration
    # set, comment the following variable, and the 
    # ConfigurationSetName=CONFIGURATION_SET argument below.
    #CONFIGURATION_SET = "ConfigSet"

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = config.get_region()

    # The subject line for the email.
    SUBJECT = "RentEasi: Ad Approval request"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Hello Admin!\n" 
                "There is a pending prpduct Ad for approval.\n\n Details :\n\t" 
                "User      :   \n "+ name +
                "Email_id  :   \n" + email )
               
                
    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
    <h4>RentEasi Pending Approval</h4>
    <p>Hello Admin! <br/>
      There is a pending product Ad for approval.<br/>
      <br/>
      Detials: <br/>
    Customer Name: 
    </p>

    </body>
    </html>
                """            

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION,aws_access_key_id=config.S3_KEY,
    aws_secret_access_key=config.S3_SECRET)

    response = client.update_template(
  Template = {
    'TemplateName' : 'Rent-Easy-Template',
    'SubjectPart'  : 'Rent-Easi : Approval request',
    'TextPart'     : 'There is pending Product Ad for approval.\r \n Details :\n Name:{{name}}\n Email:{{email}}',
    'HtmlPart'     : '<h4>Hello Admin!,</h4><p>There is pending Product Ad for approval<br/> Details:<br/>Name:{{name}}<br/>Email : {{email}}<br/>Product Id :{{pid}}<br/>Title :{{title}}</p>'
     
  })
    json_data = {'name':name,'email':email,'pid':product.product_id,'title':product.title}
    
    # Try to send the email.
    try:
    #Provide the contents of the email.
        response = client.send_templated_email(

            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Template="Rent-Easy-Template",
            TemplateData= json.dumps(json_data),
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            #ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])