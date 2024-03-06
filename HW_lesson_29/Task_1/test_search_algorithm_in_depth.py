import unittest
from search_algorithm_in_depth import dfs


class TestDepthPaths(unittest.TestCase):
    def test_depth_paths(self):
        graph = {
            "A": [["B", 3]],
            "B": [["C", 300], ["E", 30]],
            "C": [["D", 15]],
            "D": [],
            "E": [["F", 70]],
            "F": [],
        }

        all_depth_paths = {
            "A": {"A", "B", "C", "D", "E", "F"},
            "B": {"B", "C", "D", "E", "F"},
            "C": {"C", "D"},
            "D": {"D"},
            "E": {"E", "F"},
            "F": {"F"},
        }

        for start in graph:
            result = dfs(graph, start)
            print("Next >>>>")

        self.assertEqual(result, all_depth_paths[start], f"Failed for start node {start}")
            

if __name__ == "__main__":
    unittest.main()
