import lab_chat as lc


def get_username():
    username = input("Enter your username: ")
    new_user = username.strip()
    return new_user.upper()


def get_group():
    group = input("Enter the group name you would like to join: ")
    new_group = group.strip()
    return new_group.upper()


def get_message():
    message = input("Enter the message you would like to send: ")
    new_message = message.strip()
    return new_message


def initialize_chat():
    username = get_username()
    group = get_group()
    node = lc.get_peer_node(username)
    lc.join_group(node, group)
    return lc.get_channel(node, group)



def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")

print(start_chat())
