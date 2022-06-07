# Inistal bug list
from flask import request, jsonify, Flask
import os
from azure.servicebus import ServiceBusClient, ServiceBusMessage

app = Flask(__name__)
app.config["DEBUG"] = True

# https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/servicebus/azure-servicebus/samples/sync_samples/send_queue.py
# Basic messeage framework

CONNECTION_STR = os.environ["Bug-Handler-001"]
QUEUE_NAME = os.environ["add-bug-data"]

def send_single_message(sender):
    message = ServiceBusMessage("Single Message")
    sender.send_messages(message)


def send_a_list_of_messages(sender):
    messages = [ServiceBusMessage("Message in list") for _ in range(10)]
    sender.send_messages(messages)


def send_batch_message(sender):
    batch_message = sender.create_message_batch()
    for _ in range(10):
        try:
            batch_message.add_message(ServiceBusMessage("Message inside a ServiceBusMessageBatch"))
        except ValueError:
            # ServiceBusMessageBatch object reaches max_size.
            # New ServiceBusMessageBatch object can be created here to send more data.
            break
    sender.send_messages(batch_message)


servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)
with servicebus_client:
    sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
    with sender:
        send_single_message(sender)
        send_a_list_of_messages(sender)
        send_batch_message(sender)

print("Send message is done.")

@app.route('/', methods=[
    'GET'])  # which HTTP method we are using (GET) what route (extra bit of the URL) this method will be activated on.
def home():
    return (
        "<h1>Automated bug reporting</h1><p>Internal System</p>"  # what the api returns
    )


if __name__ == '__main__':
    app.run()