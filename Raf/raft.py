import random
import time
from threading import Thread
from node import RaftNode
from communication import send_message
from failure import simulate_failure, recover_node

class RaftCluster:
    def __init__(self, num_nodes):
        self.nodes = [RaftNode(i, [j for j in range(num_nodes) if j != i], 5000 + i) for i in range(num_nodes)]

    def start(self):
        for node in self.nodes:
            thread = Thread(target=node.run)
            thread.start()

    def stop(self):
        for node in self.nodes:
            node.is_running = False

    def display_status(self):
        for node in self.nodes:
            print(f"Node {node.node_id} - State: {node.state}, Term: {node.term}")