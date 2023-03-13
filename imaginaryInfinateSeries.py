from manim import *


class CreateCircle(Scene):
    def construct(self):
        CS = Tex(r"""\begin{align*}
C &= -\frac{1}{2}\cos\theta + \frac{1}{4}\cos2\theta -\frac{1}{8}\cos3\theta +\cdots \\ 
S &= -\frac{1}{2}\sin\theta + \frac{1}{4}\sin2\theta -\frac{1}{8}\sin3\theta +\cdots
\end{align*}""", font_size=75)
        self.play(Create(CS), run_time=1.5)  # show the circle on screen
        self.wait(4)
        self.remove(CS)

