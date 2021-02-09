from manim import *

class testing(Scene):
    def construct(self):
        self.group = groupTest()
        self.add(self.group)
        self.wait()
        print(self.mobjects)
        self.remove(self.group.circle)
        self.wait()
        print(self.group.getCircle())
        print(self.mobjects)
        self.play(ApplyMethod(self.group.shuffle))
        self.wait()
        print(self.mobjects)



class groupTest(VGroup):
    def __init__(self):
        super().__init__()
        self.circle = Circle()
        self.circle2 = Circle().shift(LEFT)
        self.triangle = Triangle().shift(RIGHT*2)
        self.add(self.circle, self.triangle, self.circle2)
    
    def getCircle(self):
        return self.circle

    def shuffle(self):
        self.remove(self.triangle)
        self.remove(self.circle)
        #self.add(Circle().shift(UP).set_color(BLUE))
        self.circle2.move_to(UL)
        