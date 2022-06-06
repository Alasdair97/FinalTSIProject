# Inistal bug list
from flask import request, jsonify, Flask
from azure.servicebus import ServiceBusClient, ServiceBusMessage

app = Flask(__name__)
app.config["DEBUG"] = True

CONNECTION_STR = "Bug-Handler-001"
QUEUE_NAME = "add-bug-data"

def send_single_message(sender):
    # create a Service Bus message
    message = ServiceBusMessage("Single Message")
    # send the message to the queue
    sender.send_messages(message)
    print("Sent a single message")

def send_a_list_of_messages(sender):
    # create a list of messages
    messages = [ServiceBusMessage("Message in list") for _ in range(5)]
    # send the list of messages to the queue
    sender.send_messages(messages)
    print("Sent a list of 5 messages")

def send_batch_message(sender):
    # create a batch of messages
    batch_message = sender.create_message_batch()
    for _ in range(10):
        try:
            # add a message to the batch
            batch_message.add_message(ServiceBusMessage("Message inside a ServiceBusMessageBatch"))
        except ValueError:
            # ServiceBusMessageBatch object reaches max_size.
            # New ServiceBusMessageBatch object can be created here to send more data.
            break
    # send the batch of messages to the queue
    sender.send_messages(batch_message)
    print("Sent a batch of 10 messages")

# create a Service Bus client using the connection string
servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)
with servicebus_client:
    # get a Queue Sender object to send messages to the queue
    sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
    with sender:
        # send one message        
        send_single_message(sender)
        # send a list of messages
        send_a_list_of_messages(sender)
        # send a batch of messages
        send_batch_message(sender)

print("Done sending messages")
print("-----------------------")



@app.route('/', methods=[
    'GET'])  # which HTTP method we are using (GET) what route (extra bit of the URL) this method will be activated on.
def home():
    return (
        "<h1>Automated bug reporting</h1><p>Internal System</p>"  # what the api returns
    )


if __name__ == '__main__':
    app.run()