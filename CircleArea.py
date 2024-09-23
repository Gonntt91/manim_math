from manim import *


class OctagonAndTriangles(Scene):
    def construct(self):
        # Step 1: Draw a regular octagon with 8 edges
        octagon = RegularPolygon(n=8, radius=2, color=BLUE)  # n=8 for octagon
        self.play(Create(octagon))

        # Step 2: Draw the center point of the octagon
        center = Dot(ORIGIN, color=YELLOW)
        self.play(Create(center))

        # Step 3: Connect the center to each vertex to form 8 triangles
        vertices = octagon.get_vertices()  # Get all the vertices of the octagon
        lines = VGroup()
        triangles = VGroup()

        for i in range(len(vertices)):
            # Get the current vertex and the next vertex
            vertex = vertices[i]
            next_vertex = vertices[(i + 1) % len(vertices)]  # Wrap around to the first vertex

            # Draw lines from the center to each vertex
            line = Line(ORIGIN, vertex, color=GREEN)
            lines.add(line)

            # Form triangles by connecting the center, current vertex, and next vertex
            triangle = Polygon(ORIGIN, vertex, next_vertex, color=WHITE, fill_opacity=0.2)
            triangles.add(triangle)

        # Step 4: Display all triangles
        self.play(Create(lines), Create(triangles))
        # self.wait(2)

        vertex_1 = vertices[0]
        vertex_2 = vertices[1]

        # Step 5: Calculate and draw the height of the triangle (from the center to the edge)
        edge_midpoint = (vertex_1 + vertex_2) / 2  # Midpoint of the edge
        height = Line(ORIGIN, edge_midpoint, color=RED)  # Height from center to midpoint
        self.play(Create(height))

        # Label the height and the edge
        height_label = MathTex("h").next_to(height, UP)
        edge_label = MathTex("n").next_to((vertex_1 + vertex_2) / 2, RIGHT)
        self.play(Write(height_label), Write(edge_label))

        # Step 6: Display the area formula using height and edge length
        area_formula = MathTex(r"A = \frac{1}{2} \times h \times e").to_edge(DOWN)
        self.play(Write(area_formula))

        self.wait(2)

# manim -pql CircleArea.py OctagonAndTriangles