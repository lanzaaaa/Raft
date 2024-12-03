import time
import random
from threading import Thread


class RaftNode:
    def __init__(self, node_id, peers, port):
        self.node_id = node_id
        self.peers = peers  # Lista de nós vizinhos
        self.port = port
        self.state = "follower"
        self.voted_for = None
        self.term = 0
        self.election_started = False
        self.timeout = random.randint(150, 300)  # Timeout de eleição
        self.last_heartbeat = time.time()

    def run(self):
        while True:
            if self.state == "follower":
                self.check_heartbeat()
            elif self.state == "candidate":
                self.start_election()
            elif self.state == "leader":
                self.send_heartbeats()
            time.sleep(1)

    def check_heartbeat(self):
        if time.time() - self.last_heartbeat > self.timeout:
            print(f"Node {self.node_id} timeout. Transitioning to CANDIDATE.")
            self.state = "candidate"
            self.start_election()

    def start_election(self):
        if self.election_started:
            return
        self.election_started = True
        self.state = "candidate"
        self.term += 1
        print(f"Node {self.node_id} started election (Term {self.term})")

        for peer in self.peers:
            print(f"Node {self.node_id} is requesting a vote from Node {peer}")

        time.sleep(self.timeout / 1000)
        self.check_votes()

    def check_votes(self):
        votes = random.randint(0, len(self.peers))
        if votes > len(self.peers) / 2:
            self.state = "leader"
            print(f"Node {self.node_id} won election and is now the LEADER!")
        else:
            self.state = "follower"
            print(f"Node {self.node_id} lost the election, returning to follower state.")

        self.election_started = False

    def send_heartbeats(self):
        print(f"Node {self.node_id} sending heartbeats...")
        time.sleep(1)