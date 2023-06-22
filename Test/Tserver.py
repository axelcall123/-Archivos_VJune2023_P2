from flask import Flask,jsonify,request,Response
import boto3
from key import *
import json
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

@app.route('/uploadS', methods=['PUT'])#se necesita get, post al mismo tiempo
def upload_file():
   rs = request.get_json()
   s3.put_object(Body=open(rs["url"], 'rb'), Bucket=name, Key=rs["key"])
   return jsonify({'status': 'subido'})

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
    #metodo postaman url mas largo
    # url = request.args.get('url')
    #saludo = request.args.get('saludo')
    #postman:>http://192.168.0.29:1000/get_data?url=123456
    #postman:>http://192.168.0.29:1000/get_data?url=123456&saludo=abc
    #return f'No file provided. {url} , {saludo}'


    #https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
    #http://192.168.0.29:1000/get_data
    '''envio json
    {
        "txt":"text",
        "hola":"meme"
    }
    '''
    resp=Response('',500)
    rs=request.get_json()
    print(resp)
    print(f'server<\n {rs}')
    # #print(rs["txt"],rs["hola"])
    return jsonify({'tf': 'bien', 'envio':rs})


def recursivamente(ruta,aJson):
    for aA in aJson:  # NORMAL
        if '.' in   aA:#txt
            print(ruta,'>>',aA,'<>',aJson[aA])
        else:#folder
            recursivamente(f'{ruta}/{aA}',aJson[aA])

def recorrerJson():
    txt="""
{
"carp1": {
"carp2": {
    "a.tx": "hola mundo"
},
"b.txt": "que onda"
},
"holis.txt": "tiburconcin"
}
    """
    aJson = json.loads(txt)
    for aA in aJson:#NORMAL
        print(f'{aA}<>{aJson[aA]}')
    recursivamente('', aJson)

recorrerJson()
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=1000,debug=True)#debug modo solo sirve para que se acutalice automaticamente
    #FIXME:cambiar puerto a 5000 en el server