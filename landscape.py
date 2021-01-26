"""
boiler plate code for modules
"""
import numpy as np
from numba import jit_module
import random

def compute_average(*args):
    """
    compute the float average of input arguments
    """
    return float((sum(args))/len(args))


def random_generator(seed):
    """
    randon generator to use in diamond square algorithm
    """
    return random.randint(-seed, seed)

def init_grid(size, random_seed):
    """
    initialize the diamond square grid
    """
    i = int(size)
    grid = np.zeros([i, i])
    grid[0,0] = random_generator(random_seed)
    grid[(i-1), 0] = random_generator(random_seed)
    grid[(0,(i-1) )] = random_generator(random_seed)
    grid[((i-1), (i-1))] = random_generator(random_seed)

    return grid

def find_square_step_neighbors(nw_position, current_length):
    """
    find the upper_left (NW), upper_right (NE)
    lower_left (SW), lower_right (SE) neighbors
    for the square_step part of the algorithm
    """

    nw_neighbor = [nw_position[0], nw_position[1]]
    ne_neighbor = [nw_position[0], (nw_position[1] + current_length)]
    sw_neighbor = [(nw_position[0] + current_length), nw_position[1]]
    se_neighbor = [(nw_position[0] + current_length), (nw_position[1] + current_length)]

    return nw_neighbor, \
	    ne_neighbor, \
        sw_neighbor, \
        se_neighbor

def find_north_west_south_east_points(grid, midpoint, distance):
    """
    find the upper_left (NW), upper_right (NE)
    lower_left (SW), lower_right (SE) neighbors
    for the square_step part of the algorithm
    """
    def point_is_on_top_or_bottom_edge(grid, point):
        return ((point[0]-1) == 0) or ((point[0]- 1) == (len(grid) -1))


    def point_is_on_left_or_right_edge(grid, point):
        return ((point[1]-1) == 0) or ((point[1]-1) == (len(grid) -1))
        

    length = len(grid) - 1    
    """
    calculate north and south points including wrapping at the edges
    """
    if point_is_on_top_or_bottom_edge(grid, midpoint):
        north = [(length - distance), midpoint[1]]
        south = [(0 + distance), midpoint[1]] 
    else:
        north = [(midpoint[0] - distance), midpoint[1]]
        south = [(midpoint[0] + distance), midpoint[1]]

    
    """
    calculate west and east points, including wrapping at the edges
    """
    if point_is_on_left_or_right_edge(grid, midpoint):
        west = [midpoint[0], (length - distance)]
        east = [midpoint[0], (0 + distance)] 
    else:
        west = [midpoint[0], (midpoint[1] - distance)]
        east = [midpoint[0], midpoint[1] + distance]


    return north, west, south, east


def calculate_midpoint(nw_point, distance):
    """
    calculate midpoint of the square in the diamond square algorithm
    """

    y = nw_point[1] + distance
    x = nw_point[0] + distance

    return int(x), int(y)

def recalculate_positions(midpoint, current_length):
    """
    define the uppercorners of the four children; prepare for next iteration of quadtree
    """
    nw_position = [int((midpoint[0] - current_length)), int((midpoint[1] - current_length))]
    ne_position = [int((midpoint[0] - current_length)),  int(midpoint[1])]
    sw_position = [int(midpoint[0]), int((midpoint[1] - current_length))]
    se_position = [int(midpoint[0]), int(midpoint[1])]

    return nw_position, ne_position, sw_position, se_position


def calculate_squarestep_value(grid, midpoint, upper_left,  upper_right, lower_left, lower_right, current_random_seed):
    """
    calculate the new value for the midpoint in the square step
    """
    new_value = 0.0
    for point in [upper_left, upper_right, lower_left, lower_right]:
        new_value = new_value + grid[(point[0]-1), (point[1]-1)]

    grid[(midpoint[0]-1), (midpoint[1]-1)] = (new_value / 4) + random_generator(current_random_seed)

    return

def calculate_diamondstep_values(grid, north, west, south, east, distance, current_random_seed):
    """
    calculate the new value for the diamond points step
    """
    def calculate_value(grid, point1, point2, point3, point4):
        """
        """
        average_value = compute_average(grid[(point1[0]-1), (point1[1]-1)], grid[(point2[0]-1), (point2[1]-1)], \
                                grid[(point3[0]-1), (point3[1]-1)], grid[(point4[0]-1), (point4[1]-1)]) 
        average_value = average_value + random_generator(current_random_seed)
        return float(average_value)

    for point in [north, west, south, east]:
        point1, point2, point3, point4 = find_north_west_south_east_points(grid, point, distance)
        if grid[(point[0] - 1), (point[1] - 1)] == 0:
            grid[(point[0] - 1), (point[1] - 1)] = calculate_value(grid, point1, point2, point3, point4)

    return

def quadtree_diamond_square_algorithm(grid, nw_position, current_length, current_random_seed):
    """
    in this recursive procedure the heavy lifting of calculating the square step and
    diamond step is executed, using a quadtree approach
    """
    midpoint = [0,0]

    if  ((current_length % 2) == 0):
        nw_point, ne_point, sw_point, se_point = find_square_step_neighbors(nw_position, current_length)
        new_length = int(current_length / 2)
        midpoint[0], midpoint[1] = calculate_midpoint(nw_point, new_length)
        calculate_squarestep_value(grid, midpoint, nw_point, ne_point, sw_point, se_point, current_random_seed)
        north, west, south, east = find_north_west_south_east_points(grid, midpoint, new_length)
        calculate_diamondstep_values(grid, north, west, south, east, new_length, current_random_seed)


        nw_position, ne_position, sw_position, se_position = recalculate_positions(midpoint, new_length)
        current_random_seed = current_random_seed - 1
        quadtree_diamond_square_algorithm(grid, nw_position, new_length, current_random_seed)
        quadtree_diamond_square_algorithm(grid, ne_position, new_length, current_random_seed)
        quadtree_diamond_square_algorithm(grid, sw_position, new_length, current_random_seed)
        quadtree_diamond_square_algorithm(grid, se_position, new_length, current_random_seed)
    return

#jit_module(nopython=True)
