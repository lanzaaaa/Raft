import unittest
import time
from raft import RaftCluster
from node import RaftNode


class TestRaft(unittest.TestCase):

    def test_node_initialization(self):
        node = RaftNode(1, [0, 2], 5001)
        self.assertEqual(node.node_id, 1)
        self.assertEqual(node.state, "follower")
        self.assertIsNone(node.voted_for)

    def test_cluster_start(self):
        cluster = RaftCluster(3)
        cluster.start()
        time.sleep(1)
        self.assertEqual(len(cluster.nodes), 3)

    def test_leader_election(self):
        cluster = RaftCluster(3)
        cluster.nodes[0].state = "candidate"
        cluster.nodes[1].state = "candidate"
        cluster.nodes[2].state = "follower"
        cluster.start()

        time.sleep(2)

        leader_count = sum(1 for node in cluster.nodes if node.state == "leader")
        self.assertEqual(leader_count, 1, "Deve haver exatamente um líder")


if __name__ == '__main__':
    unittest.main()
