# Inistal bug list
from flask import request, jsonify, Flask

app = Flask(__name__)
app.config["DEBUG"] = True

# https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/servicebus/azure-servicebus/samples/sync_samples/send_queue.py
# Basic messeage framework


@app.route('/', methods=[
    'GET'])  # which HTTP method we are using (GET) what route (extra bit of the URL) this method will be activated on.
def home():
    return (
        "<h1>Automated bug reporting</h1><p>Internal System</p>"  # what the api returns
    )


if __name__ == '__main__':
    app.run()