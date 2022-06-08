import requests
import sys
import getopt

# send messages to slack using slack api

def send_slack_message(message):
    payload = '{"text:"%s"}' % message
    response = requests.post('{"text:"%s"}' % channel, 
    data=payload)

    print(response.text)

def main(argv):

    message = ' '

    try: opts, args = getopt.getopt(argv, "hmc:", ["message="])

    except getopt.GetoptError:
        print('SlackMessage.py -m <message>')
        sys.exit(2)
    if len(opts) == 0:
        message = "No Message detected"
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('slackMessage.py -m <message>')
            sys.exit()
        elif opt in ("-m", "--message"):
            message = arg
        elif opt in ("-c", "--channel"):
            channel = arg
    send_slack_message(message)


if __name__ == "__main__":
    main(sys.argv[1:])