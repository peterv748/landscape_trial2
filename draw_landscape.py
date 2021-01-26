import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm

matplotlib.use("Qt5Agg")

def plot_landscape(image_temp, elapsed_time, graph_type):
    """
    plotting the calculated fractal landscape and writing it to file
    """
    if graph_type == "3D":
        x_index = np.zeros([len(image_temp)])
        y_index = np.zeros([len(image_temp)])
        x_value, y_value = np.meshgrid(x_index, y_index)
        fig = plt.figure()
        p2 = fig.add_subplot(111, projection="3d")
        p2.set_title("Diamond Square 3D Surface Plot")
        p2.set_aspect("auto")
        plt.xlabel("fractal landscape generation time: {0}".format(elapsed_time))
        p2.plot_surface(x_value, y_value, image_temp, cmap=cm.gist_rainbow)
        plt.savefig("fractal_landscape.png")
        plt.show()
    else:
        fig = plt.figure()
        p3 = fig.add_subplot(111)
        p3.set_title("Diamond Square 2D Terrain Heatmap")
        p3.set_aspect("equal")
        plt.xlabel("fractal landscape generation time: {0}".format(elapsed_time))
        plt.savefig("fractal_landscape.png")
        plt.imshow(image_temp, interpolation='nearest', cmap=cm.gist_rainbow)
        plt.show()
    
    
    
    
    

if __name__ == "__main__":
    import numpy as np

    MAXIMUM_ITERATIONS = 300
    
    image = np.zeros([4096,4096])
   
    TIME_ELAPSED = 10
    plot_landscape(image,TIME_ELAPSED)
