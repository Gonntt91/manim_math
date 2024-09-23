from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen



class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(0.5)  # wait for 0.5 seconds
        self.replacement_transform()



class BooleanOperations(Scene):
    def construct(self):
        ellipse1 = Ellipse(
            width=4.0, height=5.0, fill_opacity=0.5, color=BLUE, stroke_width=10
        ).move_to(LEFT)
        ellipse2 = ellipse1.copy().set_color(color=RED).move_to(RIGHT)

        bool_ops_text = MarkupText("<b>Boolean Operation</b>").next_to(ellipse1, UP * 3)
        ellipse_group = Group(bool_ops_text, ellipse1, ellipse2).move_to(LEFT * 3)
        self.play(FadeIn(ellipse_group))

        # i = Intersection(ellipse1, ellipse2, color=GREEN, fill_opacity=0.5)
        # self.play(i.animate.scale(0.25).move_to(RIGHT * 5 + UP * 2.5))
        # intersection_text = Text("Intersection", font_size=23).next_to(i, UP)
        # self.play(FadeIn(intersection_text))
        #
        # u = Union(ellipse1, ellipse2, color=ORANGE, fill_opacity=0.5)
        # union_text = Text("Union", font_size=23)
        # self.play(u.animate.scale(0.3).next_to(i, DOWN, buff=union_text.height * 3))
        # union_text.next_to(u, UP)
        # self.play(FadeIn(union_text))
        #
        # e = Exclusion(ellipse1, ellipse2, color=YELLOW, fill_opacity=0.5)
        # exclusion_text = Text("Exclusion", font_size=23)
        # self.play(e.animate.scale(0.3).next_to(u, DOWN, buff=exclusion_text.height * 3.5))
        # exclusion_text.next_to(e, UP)
        # self.play(FadeIn(exclusion_text))
        #
        # d = Difference(ellipse1, ellipse2, color=PINK, fill_opacity=0.5)
        # difference_text = Text("Difference", font_size=23)
        # self.play(d.animate.scale(0.3).next_to(u, LEFT, buff=difference_text.height * 3.5))
        # difference_text.next_to(d, UP)
        # self.play(FadeIn(difference_text))


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