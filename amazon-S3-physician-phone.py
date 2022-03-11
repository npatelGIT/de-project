import boto3
import pandas

# Creating the low level functional client
client = boto3.client(
    's3',
    aws_access_key_id = '',
    aws_secret_access_key = '',
    region_name = 'ap-south-1'
)
# Fetch the list of existing buckets
clientResponse = client.list_buckets()

""""  
# Print the bucket names one by one
print('Printing bucket names...')
for bucket in clientResponse['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')
"""

# Create the S3 object
obj = client.get_object(
    Bucket = 'mydeproject',
    Key = 'Names.csv'
)
    
# Read data from the S3 object
data = pandas.read_csv(obj['Body'])
    
# Print the data frame
print('Printing the data frame...')
print(data)


