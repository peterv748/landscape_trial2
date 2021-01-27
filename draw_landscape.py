import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import axes3d
from matplotlib.colors import LightSource


def plot_landscape(image_temp, elapsed_time, graph_type):
    """
    plotting the calculated fractal landscape and writing it to fill
    """

    def plot_3D(image):
        """
        create 3D plot
        """

        x_index = [i for i in range(0, len(image_temp))]
        y_index = [i for i in range(0, len(image_temp))]
        x_value, y_value = np.meshgrid(x_index, y_index)
        fig = plt.figure(figsize=(10,10))
        fig2 = fig.add_subplot(111, projection="3d")
        fig2.set_title("Diamond Square 3D Surface Plot")
        fig2.set_aspect("auto")
        plt.xlabel("fractal landscape generation time: {0}".format(elapsed_time))
        
        ls = LightSource(270, 45)

        rgb = ls.shade(image, cmap=plt.get_cmap('gist_earth'), vert_exag=0.1, blend_mode='soft')
        surf = fig2.plot_surface(x_value, y_value, image_temp, rstride=1, cstride=1, facecolors=rgb, \
                       linewidth=0, antialiased=False, shade=False)
    
        plt.savefig("fractal_landscape_3D.png")
        plt.show()

    def plot_2D(image):
        """ 
        create 2D plot
        """

        fig = plt.figure()
        p3 = fig.add_subplot(111)
        p3.set_title("Diamond Square 2D Terrain Heatmap")
        p3.set_aspect("equal")
        plt.xlabel("fractal landscape generation time: {0}".format(elapsed_time))
        plt.savefig("fractal_landscape_2D.png")
        plt.imshow(image, interpolation='nearest', cmap=plt.get_cmap('gist_earth'))
        plt.show()

    matplotlib.use("Qt5Agg")
    
    if graph_type == "3D":
        plot_3D(image_temp)       
    else:
        plot_2D(image_temp)

    

if __name__ == "__main__":
    import numpy as np

    MAXIMUM_ITERATIONS = 300
    
    image = np.zeros([4096,4096])
   
    TIME_ELAPSED = 10
    plot_landscape(image,TIME_ELAPSED)
