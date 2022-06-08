# Inistal bug list
from flask import request, jsonify, Flask

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

# Basic messeage framework

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
            # send to log queue
            return 'Bad priority detected send to the logs', 400 #request.json # send to the logs
        if request.json['priority'] in {"High","Critical"}:
            return 'High priority send to Slack queue', 200 #request.json # send to Slack queue
        if request.json['priority'] in {"Medium","Low"}:
            return 'Not High priority send to Jira queue', 200 #request.json # send to Jira queue
    


if __name__ == '__main__':
    app.run()