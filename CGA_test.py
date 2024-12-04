from main import greedy_colouring_algorithm
import unittest

class TestGreedyColouringAlgorithm(unittest.TestCase):
    def test_triangle_graph(self):
        """Test a simple triangle graph."""
        edges = [(0, 1), (1, 2), (2, 0)]
        vertices = [0, 1, 2]
        expected = [0, 1, 2]  # Each vertex gets a unique color
        self.assertEqual(greedy_colouring_algorithm(edges, vertices), expected)

    def test_line_graph(self):
        """Test a line graph."""
        edges = [(0, 1), (1, 2), (2, 3)]
        vertices = [0, 1, 2, 3]
        expected = [0, 1, 0, 1]  # Alternating colors for line graph
        self.assertEqual(greedy_colouring_algorithm(edges, vertices), expected)

    def test_disconnected_graph(self):
        """Test a disconnected graph."""
        edges = [(0, 1), (2, 3)]
        vertices = [0, 1, 2, 3]
        expected = [0, 1, 0, 1]  # Components are colored independently
        self.assertEqual(greedy_colouring_algorithm(edges, vertices), expected)

    def test_single_vertex(self):
        """Test a graph with a single vertex."""
        edges = []
        vertices = [0]
        expected = [0]  # Only one color is needed
        self.assertEqual(greedy_colouring_algorithm(edges, vertices), expected)

    def test_empty_graph(self):
        """Test an empty graph."""
        edges = []
        vertices = []
        expected = []  # No vertices mean no colors
        self.assertEqual(greedy_colouring_algorithm(edges, vertices), expected)

    def test_complete_graph(self):
        """Test a complete graph (K4)."""
        edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        vertices = [0, 1, 2, 3]
        expected = [0, 1, 2, 3]  # Each vertex requires a unique color
        self.assertEqual(greedy_colouring_algorithm(edges, vertices), expected)

if __name__ == '__main__':
    unittest.main()
