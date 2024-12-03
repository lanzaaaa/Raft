import random

def send_message(from_node, to_node, message):
    print(f"Node {from_node} sending message to Node {to_node}: {message}")

    if random.random() < 0.1:
        print(f"Communication failure between Node {from_node} and Node {to_node}")
        return False
    else:
        print(f"Node {to_node} received message: {message}")
        return True
