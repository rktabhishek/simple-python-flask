from flask import Flask, jsonify, request
import logging
import sys

#Creating and Configuring Logger
Log_Format = "%(message)s"

logging.basicConfig(stream = sys.stdout, 
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.ERROR)

logger = logging.getLogger()

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/', methods=['GET', 'POST'])
def helloworld():
    if(request.method == 'POST'):
        content_type = request.headers.get('Content-Type')
        logger.error(request.get_data().decode("utf-8") )
        data = {"response": "Message Posted"}
        return jsonify(data)
    if(request.method == 'GET'):
	    data = {"data": "Hello World"}
	    return jsonify(data)

if __name__ == '__main__':
	app.run(port='8080')
