from manim import *

class RightArcAngleExample(Scene):
    def construct(self):
        # Step 1: Define the two points
        point_A = np.array([1, 1.2, 0])  # Point (2, 3)
        point_B = np.array([-1, -1.2, 0])  # Point (-2, -3)

        # Step 2: Draw the line between these two points
        line1 = Line(start=point_A, end=point_B, color=BLUE)

        line2 = Line( LEFT, RIGHT)
        line3 = Line( DOWN, UP )


        rightarcangles = [
            Angle(line2, line3, quadrant=(1, 1), dot=True, elbow=True),
            Angle(line1, line2, radius=0.4, quadrant=(1,-1), dot=True, other_angle=True),
            Angle(line1, line2, radius=0.5, quadrant=(-1,1), stroke_width=8, dot=True, dot_color=YELLOW, dot_radius=0.04, other_angle=True),
            Angle(line1, line2, radius=0.7, quadrant=(-1,-1), color=RED, dot=True, dot_color=GREEN, dot_radius=0.08),
            ]
        plots = VGroup()
        for angle in rightarcangles:
            plot = VGroup( line1.copy(), line2.copy(), line3.copy(), angle)
            plots.add(plot)

        plots.arrange(buff=1.5)
        self.add(plots)

# manim -pql Angle.py RightArcAngleExample