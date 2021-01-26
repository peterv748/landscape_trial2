
"""
main workflow to create a fractal landscape
bases on the diamond square algorithm
"""
import time
import landscape
import draw_landscape


def main():
    """
    main procedure
    """

    size = 10
    last_position = [(2**size + 1), (2**size + 1)]
    first_position = [1,1]
    length = last_position[0] - first_position[0]
    current_length = length
    current_random_seed = 10
    grid = landscape.init_grid(int(last_position[0]), current_random_seed)
    start = time.time()
    landscape.quadtree_diamond_square_algorithm(grid, first_position, current_length, current_random_seed)
    time_elapsed = time.time() - start

    print(grid)
    graph_type = "2D"
    draw_landscape.plot_landscape(grid, time_elapsed, graph_type)

if __name__ == "__main__":
    main()
