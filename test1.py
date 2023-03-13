from manim import *


class CreateCircle(Scene):
    def construct(self):
        tex = Tex(r"$x^2$", font_size=144)


        self.play(Create(tex), run_time=2)  # show the circle on screen