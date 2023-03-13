from manim import *


class CreateCircle(Scene):
    def construct(self):
        binomial = Tex(r"$X \sim  B(n, p)$", font_size=144)
        self.play(Create(binomial), run_time=1.5)  # show the circle on screen
        self.wait(2)
        self.remove(binomial)

        prob = Tex(r"$P(X=x)=$", font_size=144)
        self.play(Create(prob), run_time=1.7)
        self.wait(1)
        self.remove(prob)

        formula = Tex(r"$\binom{n}{x}(1-p)^{n-x}p^xt^x$", font_size=144)
        self.play(Create(formula), run_time=1)
        self.wait(5)
        self.remove(formula)

        merged = Tex(r"$\binom{n}{x}(1-p)^{n-x}pt^x$", font_size=144)
        self.play(Create(merged), run_time=1)
        self.wait(4)
        self.remove(merged)

        final = Tex(r"$((1-p) + pt)^n$", font_size=144)
        self.play(Create(final), run_time=1)
        self.wait(5)
        self.remove(final)