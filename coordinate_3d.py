from manim import *


class Draw3DCoordinateSystem(ThreeDScene):
    def construct(self):
        # Set the camera to start in a 3D mode
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # Create the axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],  # Range of x-axis
            y_range=[-3, 3, 1],  # Range of y-axis
            z_range=[-3, 3, 1],  # Range of z-axis
            x_length=6,
            y_length=6,
            z_length=6
        )

        # Add labels for the axes
        x_label = MathTex("x").next_to(axes.x_axis.get_end(), RIGHT)
        y_label = MathTex("y").next_to(axes.y_axis.get_end(), UP)
        z_label = MathTex("z").next_to(axes.z_axis.get_end(), OUT)

        # Add axes and labels to the scene
        self.add(axes, x_label, y_label, z_label)

        # Animate a rotation of the scene for a better view of the 3D space
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)  # Hold for 5 seconds

# To run this script, use the following command:
# manim -pql coordinate_3d.py Draw3DCoordinateSystem
