from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Santhosh Hello"

@app.route("/test")
def hello1():
    return "Hello Santhosh with Test Done"

import os
from azure.storage.blob import BlobServiceClient

storage_conn_string = 'DefaultEndpointsProtocol=https;AccountName=storagecr777;AccountKey=EzyoNEztVbscXT/x15/xKkF22ttbNw8sUbZb0YPktHFTdF1w3FABU+/VOlA5xNA2HaIl5jMZ03VP+AStMc/qcg==;EndpointSuffix=core.windows.net'
blob_service_client = BlobServiceClient.from_connection_string(storage_conn_string)
container_name = 'yolofiles'

#get container
container_client = blob_service_client.get_container_client(container_name)
@app.route("/storage-test")
def get_storage_test():
    blob_list = []
    for blob in container_client.list_blobs():
        #print("\t Blob name: "+ container_name+'/'+  blob.name)
        blob_list.append(blob.name)
        
    #total_blobs = 'total blob files :' + str(len(blob_list))
    return blob_list[0]

@app.route("/torch")
def torch_test():
    import torch
    print(torch.__version__)
    print(torch.cuda.is_available())
    print(torch.cuda.device_count())
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print('Using device:', device)
