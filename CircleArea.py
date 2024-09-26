from manim import *


class PolygonAndTriangles(Scene):
    edge_number = 8

    def area_1_polygon(self):
        # Step 1: Draw a regular octagon with 8 edges
        octagon = RegularPolygon(n=self.edge_number, radius=2, color=BLUE)  # n=8 for octagon
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

        edge_1 = Line(edge_midpoint, vertex_2)
        height_1 = Line(edge_midpoint, ORIGIN)

        self.play(Create(height))

        # Label the height and the edge
        height_label = MathTex("h").next_to(height, UP).shift(DOWN * 0.5)
        height_label.scale(0.8).set_color(BLUE)
        edge_label = MathTex("e").next_to((vertex_1 + vertex_2) / 2, RIGHT)
        edge_label.scale(0.8).set_color(BLUE)
        self.play(Write(height_label), Write(edge_label))

        # Step 6: Add a perpendicular mark at the intersection of the height and the edge
        # Create a small right-angle mark at the intersection
        perpendicular_marker = Angle(height_1, edge_1, radius=0.2, quadrant=(1, -1), elbow=True, color=RED )

        triangles[0].set_color(GREEN)

        self.play(Create(perpendicular_marker))

        # Step 7: Display the area formula using height and edge length
        vietnamese_text = Text("Diện tích tam giác =")
        math_expression = MathTex(r"\frac{1}{2} \times h \times e")
        area_formula = VGroup(vietnamese_text, math_expression).arrange(RIGHT).to_edge(DOWN).to_edge(LEFT)
        self.play(Write(area_formula))
        self.wait(1)

        self.play(FadeOut(area_formula))

        area_polygon_text = Text(f"Diện tích đa giác = ")
        math_expression = MathTex(r"\frac{1}{2} \times h \times e \times " + str(self.edge_number))

        # area_formula = VGroup(vietnamese_text, math_expression).arrange(RIGHT).to_edge(DOWN)
        # self.play(Write(area_formula))
        area_polygon_text.to_edge(DOWN).to_edge(LEFT)
        math_expression.next_to(area_polygon_text, RIGHT)
        self.play(Write(area_polygon_text))
        self.play(Write(math_expression))

        self.play(FadeOut(math_expression))

        math_expression = MathTex(r"\frac{1}{2} \times h \times (e \times " + str(self.edge_number) + ")")
        math_expression.next_to(area_polygon_text, RIGHT)
        self.play(Write(math_expression))
        self.play(FadeOut(math_expression))

        math_expression = MathTex(r"\frac{1}{2} \times h \times " + "Chu Vi")
        math_expression.next_to(area_polygon_text, RIGHT)
        self.play(Write(math_expression))



        self.clear()

    def construct(self):
        self.edge_number = 4
        self.area_1_polygon()

        self.edge_number = 8
        self.area_1_polygon()

        self.wait(1)

        self.edge_number = 12
        self.area_1_polygon()

        self.edge_number = 18
        self.area_1_polygon()


# manim -pql CircleArea.py PolygonAndTriangles