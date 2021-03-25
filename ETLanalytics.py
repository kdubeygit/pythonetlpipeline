import psycopg2
import csv
import logging
import boto3
from botocore.exceptions import ClientError


#establishing the connection
conn = psycopg2.connect(database="postgres", user='kms', host='localhost', port= '5432')
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

# My code for Fetching Data from Python
cursor.execute('''SELECT * from roles''')

result = cursor.fetchall();

print(result)
# My code for writing results into CSV file
with open('/Users/kms/omusers/samplefiles/innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(result)
# My Next Step , write this file to S3



def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket"""

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

s3 = boto3.client('s3')
with open("/Users/kms/omusers/samplefiles/innovators.csv", "rb") as f:
    s3.upload_fileobj(f, "krantitestpythonbucket", "innovators.csv")

# My Next step , perform some changes Using  Lambda and move it to cleansed bucket in S3


# Next Step , Make the changes using s3 file and add data in DynamoDB




#Closing the connection
conn.close()
print('PostgreSQL 11.5, compiled by Visual C+pip install psycopg2-binary+ build 1914, 64-bit')
