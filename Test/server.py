from flask import Flask,jsonify, request
import boto3
from key import *
app = Flask(__name__)

s3 = boto3.client(
    's3',
    aws_access_key_id=acces_key,
    aws_secret_access_key=secret_acces_key
)
@app.route('/')
def index():
    return 'Welcome to Flask with AWS S3 Example!'
  
#LISTADO DEL BUCKET

@app.route('/uploadS', methods=['GET','POST'])#se necesita get, post al mismo tiempo
def upload_file():
   return 'No file provided.'

@app.route('/listado', methods=['GET'])#listado
def listado():
    files = []
    folders = []
    response = s3.list_objects_v2(Bucket=name)
    for obj in response['Contents']:
    #for obj in response.get('Contents', []):
        if obj['Key'].endswith('/'):
            folders.append(obj['Key'])
        else:
            txt = obj['body'].read().decode('utf-8')
            files.append(obj['Key'])

    # Return the list of files and folders as JSON
    return jsonify({'files': files, 'folders': folders})


@app.route('/get_data', methods=['GET'])
def rP():
    url = request.args.get('url')
    #postman:>http://192.168.0.29:1000/get_data?url=123456
    return f'No file provided. {url}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000,debug=True)