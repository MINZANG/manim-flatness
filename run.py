from manim import *

class FlatnessScene(Scene):
    def construct(self):
        # 標題文字
        title = Text("Flatness ", font_size=48)

        # PNG 圖片
        symbol = ImageMobject("symbols/T_Flatness.png")
        symbol.scale(0.2)

        # 使用 Group 代替 VGroup
        group = Group(title, symbol).arrange(RIGHT, buff=0.2).to_edge(UP)

        # 顯示動畫
        self.play(FadeIn(group))
        self.wait(1)

        # 理想平面
        ideal_plane = Line(LEFT*5, RIGHT*5, color=BLUE)
        self.play(Create(ideal_plane))
        ideal_text = Text("理想平面", font_size=24, color=BLUE)
        ideal_text.next_to(ideal_plane, LEFT)
        self.play(Write(ideal_text))
        self.wait(1)

        # 不平整表面
        uneven_surface = VMobject()
        uneven_surface.set_points_as_corners([
            LEFT*5 + DOWN*1,
            LEFT*3 + UP*0.3,
            LEFT*1 + DOWN*0.3,
            RIGHT*1 + UP*0.5,
            RIGHT*3 + DOWN*0.5,
            RIGHT*5 + UP*0.1
        ])
        uneven_surface.set_color(RED)
        self.play(Create(uneven_surface))
        uneven_text = Text("不平整表面", font_size=24, color=RED).next_to(uneven_surface, DOWN)
        uneven_text.next_to(uneven_surface, LEFT).shift(DOWN*0.5)
        self.play(Write(uneven_text))
        
        # 標示最大偏差
        top_point = Dot(RIGHT*1 + UP*0.5, color=YELLOW)
        top_point_text = Text("最高點", font_size=18, color=YELLOW).next_to(top_point, UP)
        bottom_point = Dot(RIGHT*1 + DOWN*1, color=YELLOW)  # 最低點
        midpoint = (top_point.get_center() + bottom_point.get_center()) / 2   # 文字表示點
        bottom_point2 = Dot(LEFT*5 + DOWN*1, color=YELLOW)  # 最低點
        bottom_point2_text = Text("最低點", font_size=18, color=YELLOW).next_to(bottom_point2, DOWN)
        max_dev_yline = Line(top_point.get_center(), bottom_point.get_center(), color=YELLOW, stroke_width=4)
        max_dev_xline = DashedLine(bottom_point2.get_center(), bottom_point.get_center(), color=YELLOW, stroke_width=4)
        dev_text = Text("平面度", font_size=24, color=YELLOW).next_to(midpoint, RIGHT).shift(DOWN*0.3 + OUT*0.2)
        self.play(Create(max_dev_xline))        
        # 水平小段 (底部)
        bottom_tick = always_redraw(lambda: Line(
            bottom_point.get_center() + LEFT*0.2,
            bottom_point.get_center() + RIGHT*0.2,
            color=YELLOW
        ))
        # 水平小段 (頂部)
        top_tick = always_redraw(lambda: Line(
            top_point.get_center() + LEFT*0.2,
            top_point.get_center() + RIGHT*0.2,
            color=YELLOW
        ))
        self.wait(1)
        self.play(FadeIn(top_point_text),FadeIn(bottom_point2_text),FadeIn(top_point), FadeIn(bottom_point2),Create(max_dev_yline),Create(bottom_tick),Create(top_tick))
        self.play(Write(dev_text))
        self.wait(1)
        
        explanation = Text("平面度 = 最高點和最低點的垂直距離", font_size=32).shift(UP*4)
        explanation.next_to(dev_text, DOWN, buff=1)  # 放在最大偏差數值下方
        self.play(FadeIn(explanation))
        self.wait(3)