import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('pdfurl')
response=table.put_item(Item={'TripID':id,'Pdfurl':pdf_url})

 dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('pdfurl')
    response = table.put_item(Item={'TripID': id, 'Pdfurl': pdf_url})
