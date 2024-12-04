from typing import List


def make_neighbours(edges: List[tuple[int, int]], vertices: List[int]) -> dict[int, set[int]]:
    """
    Returns the neighbours of a vertex in a dictionary. dict[vertex] will return a list vertices connected to that vertex

    :param edges:
    :return: List representing the neighbours of each vertex.
    """
    neighbours = {}
    for edge in edges:
        from_vertex, to_vertex = edge
        if from_vertex not in neighbours:
            neighbours[from_vertex] = set()
        if to_vertex not in neighbours:
            neighbours[to_vertex] = set()
        neighbours[from_vertex].add(to_vertex)
        neighbours[to_vertex].add(from_vertex)


    for vertex in vertices:
        if vertex not in neighbours:
            # Disconnected Graph (Edge Case): A disconnected vertex has no neighbours, so set it to an empty set
            neighbours[vertex] = set()

    return neighbours


def greedy_colouring_algorithm(edges, vertices) -> List[int]:
    """
    :param edges:
    :param vertices:
    :return: A list of colours describing what colours to assign each vertex.
    """

    neighbour_lookup = make_neighbours(edges, vertices)
    max_colours = 0  # the number of colours needed to colour the graph
    vertex_colour = [-1] * len(vertices)  # colour[n] = colour of V_n

    if len(vertices) == 0:
        return vertex_colour

    vertex_colour[0] = max_colours

    for i in range(1, len(vertices)):
        # Assign V_i the lowest index colour which does not appear in neighbourhood
        # used_colours = [ [vertex_colour[neighbour] for neighbour in neighbour_lookup[vertices[i]]] ]

        used_colours = []
        for adjacent_vertex in neighbour_lookup[vertices[i]]:
            if vertex_colour[adjacent_vertex] == -1:
                # i.e., vertex is not coloured yet
                continue
            else:
                # adjacent vertex has some colour
                 used_colours.append(vertex_colour[adjacent_vertex])


        # check if there's a colour which we can still use
        for colour in range(len(vertices)):
            if colour not in used_colours:
                vertex_colour[i] = colour
                break


    return vertex_colour