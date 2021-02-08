from manim import *


class balanceAnimations(Scene):
    def construct(self):
        group = beamBalance()
        self.play(FadeIn(group))
        self.wait(2)
        self.play(ApplyMethod(group.rotateUpperBar, PI/16))
        self.wait(3)
        self.play(ApplyMethod(group.rotateUpperBar, - PI/16))
        self.wait(2)

class beamBalance(VGroup):
    def __init__(self):
        super().__init__()
        self.base = Triangle(color = WHITE).to_edge(DOWN).stretch(2,1).set_fill(WHITE, opacity=1.0)
        self.middle_bar = Rectangle(height = 4, width = 0.3, color = WHITE).set_fill(WHITE,opacity = 1.0)
        self.upper_bar = Rectangle(width = 10, height = 0.3, color = WHITE).set_fill(WHITE, opacity= 1.0).next_to(self.middle_bar, UP, buff =0)
        self.add(self.base, self.middle_bar, self.upper_bar)

    def rotateUpperBar(self, angle):
        self.upper_bar.rotate(angle)