# Inistal bug list

from flask import request, jsonify, Flask
from azure.storage.queue import (
        QueueClient,
        BinaryBase64EncodePolicy,
        BinaryBase64DecodePolicy
)

from storagesecrets import * # this will be replaced with keyvault stuff before deployment
import os, uuid

app = Flask(__name__)
app.config["DEBUG"] = True

# Test Bug
bugs = [
    {
        'id': 1,
        'name': 'The First Bug',
        'description': 'In the begining there was a bug',
        'department': 'general',
        'priority': 'High'
    },
    {
        'id': 2,
        'name': 'The Second Bug',
        'description': 'In the begining there was lots of bugs',
        'department': 'general',
        'priority': 'Medium'
    },
]

# Creating queue client conection and send function
def addtoqueue(q_name, data):
    connect_str = AZURE_STORAGE_CONNECTION_STRING
    message = str(data)
    queue_client = QueueClient.from_connection_string(connect_str, q_name)
    queue_client.send_message(message)

# Basic messeage framework

@app.route('/', methods=['GET'])
def home():
    return (
"<h1>Bug Triarge API</h1>"
    )

@app.route('/api', methods=['GET', 'POST'])
def api():
    # send bug to correct queue/bus/howerever I get this to work
    # Send bad bugs to log queue
    # Check if has a priority

    if request.method == 'GET':
        for bug in bugs:
            if bug['priority'] not in {"High", "Medium", "Low"}:
                return "<p>Bad priority detected send to logs </p>"
        return jsonify({'bugs': bugs})

    elif request.method == 'POST':
        if not 'priority' in request.json or request.json['priority'] not in {"High", "Medium", "Low"}:
            addtoqueue('invalidinputs', request.json)
            return 'Bad priority detected send to the logs', 400 #request.json # send to the logs

        if request.json['priority'] in {"High","Critical"}:
            addtoqueue('bugtoforward', request.json)
            return 'High priority send to Slack queue', 200 #request.json # send to Slack queue

        if request.json['priority'] in {"Medium","Low"}:
            addtoqueue('bugtoforward', request.json)
            return 'Not High priority send to Trello queue', 200 #request.json # send to Jira queue
    


if __name__ == '__main__':
    app.run()