# failure.py

import random
import time

def simulate_failure(node, failure_probability=0.1):
    if random.random() < failure_probability:
        print(f"Node {node.node_id} has failed!")
        node.is_running = False

def recover_node(node):
    print(f"Node {node.node_id} is recovering.")
    node.is_running = True
    node.state = 'follower'
    node.last_heartbeat = time.time()
