from manim import *

config.frame_width = 9  # Corresponds to the width of the screen
config.frame_height = 16  # Corresponds to the height of the screen
config.pixel_height = 1920  # Height in pixels (full HD)
config.pixel_width = 1080   # Width in pixels (full HD)

class EquationTransformation(Scene):
    edge_number = 8
    def construct(self):
        n_edge_text = MathTex(f"N = {self.edge_number}").to_edge(UP)
        n_edge_text.shift(DOWN * 1)
        self.play(Write(n_edge_text))

# manim -pql formulus.py EquationTransformation
