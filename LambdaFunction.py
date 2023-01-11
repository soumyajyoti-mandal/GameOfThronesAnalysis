import json
import boto3
import csv
import mysql.connector
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement
    #print(event)
    bucket = event['Records'][0]['s3']['bucket']['name']
    csvfile = event['Records'][0]['s3']['object']['key']
    csvfile_obj = s3_client.get_object(Bucket = bucket,Key =csvfile)
    lines = csvfile_obj['Body'].read().decode('utf-8').split('\r\n')
    lines_list = []
    for i in csv.DictReader(lines):
        lines_list.append(i.values())
    #print(lines_list)
    try:
        mydb = mysql.connector.connect(
                host="gottaskdb.ctydl14ji75t.ap-south-1.rds.amazonaws.com",
                user="admin",password="Qwer1234", database ='mydatabase')
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    else:
        mycursor = mydb.cursor()
        try:
            myquery = '''insert into mydatabase.got (name_of_battle , year_of_battle , battle_number,attacker_king , 
            defender_king, attacker_1, attacker_2,attacker_3 ,attacker_4 ,defender_1, 
            defender_2 , defender_3,defender_4, attacker_outcome, battle_type ,major_death ,
            major_capture , attacker_size , defender_size ,attacker_commander , 
            defender_commander , summer ,location , region , note )
            values (%s, %s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            mycursor.executemany(myquery,lines_list)
            mydb.commit()
        except mysql.connector.Error as e:
            print("Error while executing ", e)
        else:
            print("Execution complete")
            mycursor.close()
            mydb.close
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
