from manim import *

class CircleAnimation(Scene):
    def construct(self):
        # Step 1: Create the first circle with a diameter
        small_circle = Circle(radius=1, color=BLUE)  # Small circle
        small_diameter = Line(small_circle.get_left(), small_circle.get_right(), color=YELLOW)  # Diameter of the small circle

        # Position the circle in the center
        small_circle_group = VGroup(small_circle, small_diameter)

        # Step 2: Create the bigger circle with a diameter (but don't show it yet)
        big_circle = Circle(radius=2, color=GREEN)  # Bigger circle
        big_diameter = Line(big_circle.get_left(), big_circle.get_right(), color=YELLOW)  # Diameter of the big circle

        # Step 3: Position the larger circle group (off-screen initially)
        big_circle_group = VGroup(big_circle, big_diameter)
        big_circle_group.shift(RIGHT )  # Start it on the right side (out of view)

        # Step 2: Create the bigger circle with a diameter (but don't show it yet)
        biggest_circle = Circle(radius=3, color=GREEN)  # Bigger circle
        biggest_diameter = Line(biggest_circle.get_left(), biggest_circle.get_right(), color=YELLOW)  # Diameter of the big circle

        # Step 3: Position the larger circle group (off-screen initially)
        biggest_circle_group = VGroup(biggest_circle, biggest_diameter)


        # Step 4: Animate showing the small circle first
        self.play(Create(small_circle))
        self.play(Create(small_diameter))

        self.wait(1)

        # Step 5: Animate the small circle moving left and simultaneously show the larger circle
        self.play(
            small_circle_group.animate.shift(LEFT * 3),  # Move the small circle to the left
        )
        self.play(Create(big_circle))
        self.play(Create(big_diameter))

        # Keep the scene on screen for 2 seconds
        self.wait(2)

        self.play(small_circle_group.animate.shift(LEFT*4), big_circle_group.animate.shift(LEFT*4))
        biggest_circle_group.next_to(big_circle_group, RIGHT, buff=2)
        self.play(Create(biggest_circle_group))



# manim -pql circle_pi.py CircleAnimation