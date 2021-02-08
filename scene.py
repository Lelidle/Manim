from manim import *


class MovingBraces(Scene):
    def construct(self):
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=",       #0
            "f(x)\\frac{d}{dx}g(x)",        #1
            "+",                            #2
            "g(x)\\frac{d}{dx}f(x)",         #3
            "Hello!"
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff=SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff=SMALL_BUFF)
        t1 = brace1.get_text("$g'f$")
        t2 = brace2.get_text("$f'g$")
        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
            )
        self.wait()
        self.play(
            ReplacementTransform(brace1,brace2),
            ReplacementTransform(t1,t2)
            )
        self.wait()

class LaTeXAttributes(Scene):
    def construct(self):
        tex = Tex(r'Hello \LaTeX', color=BLUE).scale(3)
        self.add(tex)

class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r'\LaTeX').scale(3)
        self.add(tex)

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity = 0.5)

        square = Square()
        square.flip(RIGHT)
        square.rotate(-3* TAU/8)

        self.play(ShowCreation(square))
        self.wait(3)
        self.play(Transform(square, circle))
        self.wait(3)
        self.play(FadeOut(square))

class PlayingWithMobjects(Scene):
    def construct(self):
        pixel_height = config["pixel_height"]
        color = config["background_color"]
        self.add(Text(str(color)).to_corner(UL))
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT).set_stroke(color=GREEN, width = 20).set_fill(YELLOW, opacity=0.75)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle,square, triangle)
        self.wait()
        self.play(ApplyMethod(circle.move_to, LEFT*2), run_time = 3)
        self.play(ApplyMethod(square.next_to,circle, LEFT))
        self.play(ApplyMethod(triangle.align_to, circle, RIGHT))
        self.wait(3)
        self.remove(circle)
        self.play(Rotate(square, PI/4))
        self.play(FadeOut(triangle))
        self.wait()
        self.play(FadeIn(triangle))
        self.wait()
