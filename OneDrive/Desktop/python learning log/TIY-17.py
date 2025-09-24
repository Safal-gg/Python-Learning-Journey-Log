#messages:
messages=['Hello','How are you?','Whats up?']
send_messages=[]
def display_msg(msgs):
    for msg in msgs:
        print(msg)

display_msg(messages)

#sending messages:
def send_msg(msg_1,msg_2):
    while msg_1:
        message=msg_1.pop()
        print(f"Sending: {message}")
        msg_2.append(message)

send_msg(messages[:],send_messages)
print(messages)
