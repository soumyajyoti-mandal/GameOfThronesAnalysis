import boto3
import pandas as pd
import os
from io import StringIO

if os.path.exists(r"Dataset\battles.csv"):
    df = pd.read_csv(r"Dataset\battles.csv")
    #cleaning dataset
    df.dropna(subset=["attacker_king","attacker_outcome"],inplace=True)
    REGION = 'ap-south-1'
    ACCESS_KEY_ID = 'access key'
    SECRET_ACCESS_KEY = 'secret access key'
    BUCKET_NAME = 'bucket name'
    FileName='data.csv'
    csv_buffer=StringIO()
    df.to_csv(csv_buffer, index=False)
    #connect to aws and upload csv to S3
    try:
        s3csv = boto3.client('s3',
        region_name = REGION,
        aws_access_key_id = ACCESS_KEY_ID,
        aws_secret_access_key = SECRET_ACCESS_KEY)
    except:
        print("Unable to connect to AWS")
    else:
        #load to S3
        response=s3csv.put_object(Body=csv_buffer.getvalue(),
                               Bucket=BUCKET_NAME,
                               Key=FileName)
else:
    print("File not found")
