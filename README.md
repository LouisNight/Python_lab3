def get_peer_node(username): # function name is get_peer_node
username = Pyre node is initialized with this username
return = returns the initialized node 'n' which is used in the rest of the code

def join_group(node, group): # function name is join_group
node = The node I'm using to join the group chat
group = the group chat of all the connected nodes
return = no return, the function is used to join the node to the group.


def chat_task(ctx, pipe, n, group): # function name is chat_task
ctx = ZeroMQ context for managing sockets (according to Google)
pipe = communication pipe between threads
n = the node
group = the group of connected nodes -- or the group to which the node belongs
return = no return, this is the core chat logic of the program

def get_channel(node, group): # function name is get_channel
node = the Pyre node
group = the group to which the node belongs
the return function = "zhelper.zthread_fork() is used to run the chat_task
in a separate thread so it can listen for and send messages asynchronously." - ChatGPT 
(I also spent time trying to understand it without ChatGPT's help)