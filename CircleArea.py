from manim import *


config.frame_width = 9  # Corresponds to the width of the screen
config.frame_height = 16  # Corresponds to the height of the screen
config.pixel_height = 1920  # Height in pixels (full HD)
config.pixel_width = 1080   # Width in pixels (full HD)


class CircleAnimation(Scene):
    def introduction_pi(self):
        where_pi_from1 = Text("Số Pi đến từ đâu?", font_size=36).move_to(ORIGIN).shift(UP)
        where_pi_from2 = Text("Tại sao lại có số Pi ?", font_size=36).next_to(where_pi_from1, DOWN)
        self.play(Write(where_pi_from1))
        self.play(Write(where_pi_from2))
        self.wait(1)
        self.play(FadeOut(where_pi_from1, where_pi_from2))

    def draw_3_circle(self):
        self.introduction_pi()

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
        big_circle_group.shift(DOWN)  # Start it on the below side (out of view)

        # Step 2: Create the bigger circle with a diameter (but don't show it yet)
        biggest_circle = Circle(radius=3, color=GREEN)  # Bigger circle
        biggest_diameter = Line(biggest_circle.get_left(), biggest_circle.get_right(),
                                color=YELLOW)  # Diameter of the big circle

        # Step 3: Position the larger circle group (off-screen initially)
        biggest_circle_group = VGroup(biggest_circle, biggest_diameter)

        # Step 4: Animate showing the small circle first
        self.play(Create(small_circle))
        self.play(Create(small_diameter))

        self.wait(1)

        # Step 5: Animate the small circle moving left and simultaneously show the larger circle
        self.play(
            small_circle_group.animate.shift(UP * 3),  # Move the small circle to the left
        )
        self.play(Create(big_circle))
        self.play(Create(big_diameter))

        # Keep the scene on screen for 2 seconds
        self.wait(2)
        self.play(small_circle_group.animate.shift(UP * 3), big_circle_group.animate.shift(UP*3))

        biggest_circle_group.next_to(big_circle_group, DOWN, buff= 1)
        self.play(Create(biggest_circle_group))

    def construct(self):
        self.draw_3_circle()

class Equation(Scene):


    def explain_pi(self):

        fontSize = 30

        text1 = VGroup(
            Text(u"Người xưa đã nhận thấy rằng ", font_size=fontSize),
            Text(u"khi đường kính càng lớn thì ", font_size=fontSize),
            Text("chu vi hình tròn càng lớn lên bấy nhiêu lần", font_size=fontSize),
            Text("thì chu vi hình tròn càng lớn lên bấy nhiêu lần", font_size=fontSize)
        ).arrange(DOWN).to_edge(UP)

        text1.shift(DOWN)

        text2 = Text(u"Tỷ lệ này luôn xấp xỉ 3.1416", font_size=fontSize).next_to(text1, DOWN)
        text3 = Text(u"Đây chính là số Pi", font_size=fontSize).next_to(text2, DOWN)
        text4 = Text(u"Chu Vi  = đường kính x Pi", font_size=30, color=RED).move_to(ORIGIN)

        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.play(Write(text4))

        self.play(FadeOut(text1))
        self.play(FadeOut(text2))
        self.play(FadeOut(text3))

        self.wait(0.5)
        area_formula = MathTex(r"S = \pi r^2", font_size=50, color=YELLOW).move_to(ORIGIN)
        self.play(Transform(text4, area_formula))

        self.wait(0.5)
        why = Text("But Why?").next_to(area_formula, DOWN, buff=2)
        self.play(FadeIn(why))

    def explain_area(self):
        left_side = Text(u"S  = ", font_size=40)
        right_side = MathTex(r"\frac{1}{2} \times h \times P", font_size=35)
        area_formulus = VGroup(left_side, right_side).arrange(RIGHT).to_edge(UP)  # Position it at the top of the screen
        area_formulus.shift(DOWN * 1)

        text2 = (Text(u"Khi đa giác đều có càng lớn, nó càng trở nên càng tròn", font_size=24)
                 .next_to(area_formulus, DOWN))
        text3 = (Text(u"lúc đó diện tích đa giác càng gần đúng với diện tích hình tròn", font_size=24)
                 .next_to(text2, DOWN))
        text4 = (Text(u"và đoạn h dần trở thành bán kính", font_size=30, color=RED)
                 .next_to(text3, DOWN))

        text5 = (MathTex(r"S = \frac{1}{2} \times r \times P", font_size=50, color=YELLOW)
                 .next_to(text4, DOWN))
        text6 = (MathTex(r"S = \frac{1}{2} \times r \times 2 \times r \times \pi", font_size=50, color=YELLOW)
                 .next_to(text5, DOWN))
        area_formula = MathTex(r"S = \pi r^2", font_size=50, color=YELLOW).move_to(ORIGIN)

        self.play(Write(area_formulus))
        self.play(Write(text2))
        self.play(Write(text3))
        self.play(Write(text4))

        self.play(Write(text5))
        self.play(Write(text6))

        self.play(FadeIn(area_formula))

    def construct(self):
        self.explain_pi()
        # self.explain_area()


class PolygonAndTriangles(CircleAnimation, Equation):
    edge_number = 8

    def area_1_polygon(self):

        n_edge_text = MathTex(f"N = {self.edge_number}").to_edge(UP)
        n_edge_text.shift(DOWN * 1)
        self.play(Write(n_edge_text))

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
        vietnamese_text = VGroup(Text("S"), Text("( tam giác )", font_size=20), Text(" =")).arrange(RIGHT)
        math_expression = MathTex(r"\frac{1}{2} \times h \times e")
        area_formula = VGroup(vietnamese_text, math_expression).arrange(RIGHT).to_edge(DOWN).to_edge(LEFT)
        area_formula.shift(UP * 2)
        self.play(Write(area_formula))
        self.wait(1)

        self.play(FadeOut(area_formula))

        area_polygon_text = VGroup(Text("S"), Text("( đa giác )", font_size=20), Text(" =")).arrange(RIGHT)
        math_expression = MathTex(r"\frac{1}{2} \times h \times e \times " + str(self.edge_number))

        # area_formula = VGroup(vietnamese_text, math_expression).arrange(RIGHT).to_edge(DOWN)
        # self.play(Write(area_formula))
        area_polygon_text.to_edge(DOWN).to_edge(LEFT)
        area_polygon_text.shift(UP * 2)
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

        self.wait(1)
        self.clear()


    def construct(self):
        # draw circle
        self.draw_3_circle()
        self.wait(1)
        self.clear()

        self.explain_pi()
        self.wait(1)
        self.clear()

        self.edge_number = 4
        self.area_1_polygon()

        self.edge_number = 8
        self.area_1_polygon()

        self.wait(1)

        self.edge_number = 12
        self.area_1_polygon()

        self.edge_number = 18
        self.area_1_polygon()

        self.explain_area()


# manim -pql CircleArea.py PolygonAndTriangles

# manim -pql CircleArea.py Equation

# manim -pql CircleArea.py CircleAnimation