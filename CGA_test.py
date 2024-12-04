from main import greedy_colouring_algorithm
import unittest

class TestGreedyColouringAlgorithm(unittest.TestCase):
    def test_empty_graph(self):
        edges = []
        vertices = []
        expected_colours = []
        result = greedy_colouring_algorithm(edges, vertices)
        self.assertEqual(result, expected_colours, "Failed on empty graph")

    def test_single_vertex(self):
        edges = []
        vertices = [0]
        expected_colours = [0]
        result = greedy_colouring_algorithm(edges, vertices)
        self.assertEqual(result, expected_colours, "Failed on single vertex graph")

    def test_no_edges(self):
        edges = []
        vertices = [0, 1, 2, 3]
        expected_colours = [0, 0, 0, 0]
        result = greedy_colouring_algorithm(edges, vertices)
        self.assertEqual(result, expected_colours, "Failed on graph with no edges")

    def test_two_connected_vertices(self):
        edges = [(0, 1)]
        vertices = [0, 1]
        expected_colours = [0, 1]
        result = greedy_colouring_algorithm(edges, vertices)
        self.assertEqual(result, expected_colours, "Failed on two connected vertices")

    def test_triangle_graph(self):
        edges = [(0, 1), (1, 2), (2, 0)]
        vertices = [0, 1, 2]
        expected_colours = [0, 1, 2]
        result = greedy_colouring_algorithm(edges, vertices)
        self.assertEqual(result, expected_colours, "Failed on triangle graph")

    def test_square_graph(self):
        edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
        vertices = [0, 1, 2, 3]
        expected_colours = [0, 1, 0, 1]
        result = greedy_colouring_algorithm(edges, vertices)
        self.assertEqual(result, expected_colours, "Failed on square graph")

    def test_bipartite_graph(self):
        edges = [(0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4)]
        vertices = [0, 1, 2, 3, 4]
        expected_colours = [0, 0, 0, 1, 1]
        result = greedy_colouring_algorithm(edges, vertices)
        self.assertEqual(result, expected_colours, "Failed on bipartite graph")

    def test_complete_graph(self):
        n = 5
        vertices = list(range(n))
        edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
        expected_colours = list(range(n))
        result = greedy_colouring_algorithm(edges, vertices)
        self.assertEqual(result, expected_colours, "Failed on complete graph")

    def test_line_graph(self):
        edges = [(0, 1), (1, 2), (2, 3), (3, 4)]
        vertices = [0, 1, 2, 3, 4]
        expected_colours = [0, 1, 0, 1, 0]
        result = greedy_colouring_algorithm(edges, vertices)
        self.assertEqual(result, expected_colours, "Failed on line graph")

    def test_disconnected_graph(self):
        edges = [(0, 1), (2, 3)]
        vertices = [0, 1, 2, 3]
        expected_colours = [0, 1, 0, 1]
        result = greedy_colouring_algorithm(edges, vertices)
        self.assertEqual(result, expected_colours, "Failed on disconnected graph")

    def test_star_graph(self):
        edges = [(0, 1), (0, 2), (0, 3), (0, 4)]
        vertices = [0, 1, 2, 3, 4]
        expected_colours = [0, 1, 1, 1, 1]
        result = greedy_colouring_algorithm(edges, vertices)
        self.assertEqual(result, expected_colours, "Failed on star graph")

    def test_wheel_graph(self):
        edges = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (2, 3), (3, 4), (4, 1)]
        vertices = [0, 1, 2, 3, 4]
        expected_colours = [0, 1, 2, 1, 2]
        result = greedy_colouring_algorithm(edges, vertices)
        self.assertEqual(result, expected_colours, "Failed on wheel graph")

if __name__ == '__main__':
    unittest.main()
