from manim import *

class EquationTransformation(Scene):
    def construct(self):

        initial_eq = MathTex(r"\frac{1}{2} \times h \times Chu Vi")
        initial_eq.to_edge(UP)  # Position it at the top of the screen

        # Simplified equation: 2x = 7 - 3
        simplified_eq = MathTex("2x = 7 - 3")
        simplified_eq.next_to(initial_eq, DOWN, buff=1)

        # Final equation: x = 2
        final_eq = MathTex("x = 2")
        final_eq.next_to(simplified_eq, DOWN, buff=1)

        # Step 1: Display the initial equation
        self.play(Write(initial_eq))
        self.wait(1)

        # Step 2: Transform the initial equation to the simplified equation
        self.play(Transform(initial_eq, simplified_eq))
        self.wait(1)

        # Step 3: Transform the simplified equation to the final equation
        self.play(Transform(initial_eq, final_eq))
        self.wait(2)


# manim -pql formulus.py EquationTransformation
