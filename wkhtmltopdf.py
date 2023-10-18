import pdfkit
pdfkit.from_string("""
    <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                }
                h1 {
                    color: #ff0000;
                }
            </style>
        </head>
        <body>
            <h1>Hello, world!</h1>
            <p>This is an example PDF generated from inline HTML code with CSS.</p>
        </body>
    </html>
    """
,'out.pdf')



import subprocess
import boto3

def lambda_handler(event, context):
    # Retrieve the HTML content from the event payload
    html_content = event['html_content']
    # Set the desired output PDF file name
    output_pdf_file = '/tmp/output.pdf'
    # Set the S3 bucket name and key for storing the PDF
    bucket_name = 'www.carodrive.com'
    pdf_key = 'output.pdf'

    # Convert HTML to PDF
    convert_html_to_pdf(html_content, output_pdf_file)

    # Upload PDF to S3
    upload_to_s3(output_pdf_file, bucket_name, pdf_key)

    # Return the S3 URL of the uploaded PDF
    pdf_url = f"https://{bucket_name}.s3.amazonaws.com/{pdf_key}"
    return {
        'statusCode': 200,
        'body': {
            'pdf_url': pdf_url
        }
    }

def convert_html_to_pdf(html_content, output_pdf_file):
    cmd = ['wkhtmltopdf', '-', output_pdf_file]
    subprocess.run(cmd, input=html_content.encode(), check=True)

def upload_to_s3(file_path, bucket_name, object_key):
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, object_key)





# import pdfkit
# import json
# def lambda_handler(event, context):
#     # HTML content
#     html_content = '''
#     <html>
#     <head>
#         <title>My HTML to PDF Conversion</title>
#     </head>
#     <body>
#         <h1>Hello, World!</h1>
#         <p>This is an example of converting HTML to PDF using wkhtmltopdf and pdfkit.</p>
#     </body>
#     </html>
#     '''

#     # Generate PDF from HTML content using wkhtmltopdf and pdfkit
#     pdfkit.from_string(html_content, '/tmp/output.pdf')

#     # Optionally, save the PDF to an S3 bucket
#     s3_bucket = 'www.carodrive'
#     s3_key = 'output.pdf'
#     s3_path = f's3://{s3_bucket}/{s3_key}'
#     pdfkit.from_string(html_content, s3_path)

#     return {
#         'statusCode': 200,
#         'body': 'PDF generated successfully!'
#     }

# import pdfkit

# def lambda_handler(event, context):
#     try:
#         url = 'http://www.google.com/'
#         output_pdf_file = '/tmp/output.pdf'  # Specify the output file path

#         # Execute the wkhtmltopdf command
#         cmd = ['wkhtmltopdf', url, output_pdf_file]
#         subprocess.run(cmd, check=True)
#         print("executed")
#     except:
#         print("Not Working")


#working one
# import subprocess
# import json
# import base64
# def lambda_handler(event, context):
#     # Retrieve the HTML content from the event payload
#     html_content = event['html_content']
#     # Set the desired output PDF file name
#     output_pdf_file = 'output1.pdf'

#     # Convert HTML to PDF
#     convert_html_to_pdf(html_content, output_pdf_file)

#     # Return the output PDF file path
#     return {
#         'statusCode': 200,
#         'body': {
#             'pdf_file_path': output_pdf_file
#         }
#     }

# def convert_html_to_pdf(html_content, output_pdf_file):
#     cmd = ['wkhtmltopdf', '-', output_pdf_file]
#     subprocess.run(cmd, check=True)





final working



import subprocess
import boto3
import json
def lambda_handler(event, context):
    # Retrieve the HTML content from the event payload
    #html_content = event['html_content']
    request_body = json.loads(event['body'])
    html_content = request_body['html_content']
    # Set the desired output PDF file name
    output_pdf_file = '/tmp/output.pdf'
    # Set the S3 bucket name and key for storing the PDF
    bucket_name = 'www.carodrive.com'
    pdf_key = 'output_fin.pdf'

    # Convert HTML to PDF
    convert_html_to_pdf(html_content, output_pdf_file)

    # Upload PDF to S3
    upload_to_s3(output_pdf_file, bucket_name, pdf_key)

    # Return the S3 URL of the uploaded PDF
    pdf_url = f"https://{bucket_name}.s3.amazonaws.com/{pdf_key}"
    # return {
    #     'statusCode': 200,
    #     'body': 'PDF generation successful!'
    #     }
    
    return {
        'statusCode': 200,
        'body': pdf_url
        }

def convert_html_to_pdf(html_content, output_pdf_file):
    cmd = ['wkhtmltopdf', '-', output_pdf_file]
    subprocess.run(cmd, input=html_content.encode(), check=True)

def upload_to_s3(file_path, bucket_name, object_key):
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, object_key)





import subprocess
import boto3
import json
import uuid
def lambda_handler(event, context):
    request_body = json.loads(event['body'])
    html_content = request_body['html_content']
    #written here
    unique_id = str(uuid.uuid4())
    
    output_pdf_file = '/tmp/output.pdf'
    bucket_name = 'www.carodrive.com'
    #pdf_key = 'output_fin.pdf'
    pdf_key = f"output_{unique_id}.pdf"
    convert_html_to_pdf(html_content, output_pdf_file)
    
    # Upload PDF to S3
    upload_to_s3(output_pdf_file, bucket_name, pdf_key)
    # Return the S3 URL of the uploaded PDF
    pdf_url = f"https://{bucket_name}.s3.amazonaws.com/{pdf_key}"

    return {
        'statusCode': 200,
        'body': pdf_url+'<- '+'url generation successfull'
        }

def convert_html_to_pdf(html_content, output_pdf_file):
    cmd = ['wkhtmltopdf', '-', output_pdf_file]
    subprocess.run(cmd, input=html_content.encode(), check=True)

def upload_to_s3(file_path, bucket_name, object_key):
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, object_key)



latest with dynamoDB
import subprocess
import boto3
import json
import uuid
import boto3

def lambda_handler(event, context):
    request_body = json.loads(event['body'])
    html_content = request_body['html_content']
    id=request_body['id']
    css_content = request_body.get('css_content', '')  
    unique_id = str(uuid.uuid4())
    output_pdf_file = '/tmp/output.pdf'
    bucket_name = 'www.carodrive.com'
    pdf_key = f"Ttrip-"+str(id)+"-"+unique_id+".pdf"

    full_html_content = f"""
    <html>
    <head>
        <style>
            {css_content}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    convert_html_to_pdf(full_html_content, output_pdf_file)
    upload_to_s3(output_pdf_file, bucket_name, pdf_key)
    # Return the S3 URL of the uploaded PDF
    pdf_url = f"https://{bucket_name}.s3.amazonaws.com/{pdf_key}"
    store_pdf_url_in_dynamodb(id, pdf_url)
   
    return {
        'statusCode': 200,
        'body': pdf_url + ' <- URL generation successful'
    }
def convert_html_to_pdf(html_content, output_pdf_file):
    cmd = ['wkhtmltopdf', '-', output_pdf_file]
    subprocess.run(cmd, input=html_content.encode(), check=True)

def upload_to_s3(file_path, bucket_name, object_key):
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, object_key)
def store_pdf_url_in_dynamodb(id, pdf_url):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('pdfurl')
    response = table.put_item(Item={'TripID': id, 'Pdfurl': pdf_url})
