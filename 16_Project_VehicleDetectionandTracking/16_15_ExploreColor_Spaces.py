import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot3d(pixels, colors_rgb, axis_title, axis_labels=list("RGB"), axis_limits=((0, 255), (0, 255), (0, 255))):
    """Plot pixels in 3D."""

    # Create figure and 3D axes
    fig = plt.figure(figsize=(8, 8))
    # ax = Axes3D(fig)  # UserWarning
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    # Set axis limits
    ax.set_xlim(*axis_limits[0])
    ax.set_ylim(*axis_limits[1])
    ax.set_zlim(*axis_limits[2])

    # Set axis labels and sizes
    ax.tick_params(axis='both', which='major', labelsize=14, pad=8)
    ax.set_xlabel(axis_labels[0], fontsize=16, labelpad=16)
    ax.set_ylabel(axis_labels[1], fontsize=16, labelpad=16)
    ax.set_zlabel(axis_labels[2], fontsize=16, labelpad=16)
    ax.set_title(axis_title)

    # Plot pixel values with colors given in colors_rgb
    ax.scatter(
        pixels[:, :, 0].ravel(),
        pixels[:, :, 1].ravel(),
        pixels[:, :, 2].ravel(),
        # c=colors_rgb.reshape((-1, 3)), edgecolors='none'
        c=colors_rgb.reshape((-1, 3)), edgecolors='face'
    )

    # Return Axes3D object for further manipulation
    return ax


# Read a color image
# img_name = "bbox-example-image"
img_name = "scene_3"
img = cv2.imread(img_name + '.png')

# Select a small fraction of pixels to plot by sub-sampling it
scale = max(img.shape[0], img.shape[1], 64) / 64  # at most 64 rows and columns
img_small = cv2.resize(img, (np.int(img.shape[1] / scale), np.int(img.shape[0] / scale)), interpolation=cv2.INTER_NEAREST)

# Convert sub-sampled image to desired color space(s)
img_small_RGB = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)  # OpenCV uses BGR, matplotlib likes RGB
img_small_HSV = cv2.cvtColor(img_small, cv2.COLOR_BGR2HSV)
img_small_LUV = cv2.cvtColor(img_small, cv2.COLOR_BGR2LUV)
img_small_rgb = img_small_RGB / 255.  # scaled to [0, 1], only for plotting

# Plot and Show
plot3d(img_small_RGB, img_small_rgb, img_name + '_RGB')
plt.savefig(img_name + '_RGB')
plt.show()


plot3d(img_small_HSV, img_small_rgb, img_name + '_HSV', axis_labels=list("HSV"))
plt.savefig(img_name + '_HSV')
plt.show()

plot3d(img_small_LUV, img_small_rgb, img_name + '_LUV', axis_labels=list("LUV"))
plt.savefig(img_name + '_LUV')
plt.show()
