import requests
import boto3
from fastapi import FastAPI, Depends, Form

s3 = boto3.client('s3')
allbuckets = s3.list_buckets()

ec2 = boto3.resource('ec2', region_name='us-east-1')
allinstances = ec2.instances.all()

app = FastAPI()

@app.post('/inventory')
async def vai(user_name: str = Form(...), text: str = Form(...)):
    if text == 'buckets':
        return allbuckets
    elif text == 'ec2':
        return allinstances
    else:
        return 'Opcao invalida'
