import unittest
from shortest_paths_algorithm import bfs


class TestShortestPaths(unittest.TestCase):
    def test_shortest_paths(self):
        graph = {
            "A": [
                ["B", 3],
            ],
            "B": [
                ["C", 300],
                ["E", 30],
            ],
            "C": [
                ["D", 15],
            ],
            "D": [],
            "E": [
                ["F", 70],
            ],
            "F": [],
        }


        all_shortest_paths = {}

        for start in graph:
            all_shortest_paths[start] = bfs(graph, start)
            #print(all_shortest_paths)

        self.assertEqual( all_shortest_paths["A"]["F"], 3)
        self.assertEqual( all_shortest_paths["A"]["D"], 3)
        self.assertEqual( all_shortest_paths["A"]["B"], 1)

if __name__ == "__main__":
    unittest.main()
