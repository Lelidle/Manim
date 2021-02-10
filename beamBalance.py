from manim import *
import copy

class balanceAnimations(Scene):
    def construct(self):
        #self.intro()
        self.setupBeam()
        to_Fade_in = VGroup(self.balance, self.left_basket, self.right_basket, self.weight_list[0], self.weight_list[1])
        self.play(FadeIn(to_Fade_in))
        self.wait()
        self.removeWeights(1,0,False, False)
        self.wait()
        self.tilt("DR")
        self.wait()
        self.weight_list[0].addWeight(beamWeight(False))
        self.wait()
        self.tilt("UR")
        self.wait()
        self.removeWeights(1,0,False, False)
        self.removeWeights(1,1, False, False)
        self.wait(2)
        self.removeWeights(1,0, True, False)
        self.removeWeights(1,1,True,False)
        self.wait(2)
        self.removeWeights(1,0,True,False)
        self.removeWeights(2,1,False,False)
        self.wait(2)


    def intro(self):
        intro_text = Text("Das Waagemodell für Gleichungen")
        self.play(FadeInFrom(intro_text, UP))
        self.wait(2)
        self.play(FadeOut(intro_text))
        self.wait(2)

    def setupBeam(self):
        self.balance = beamBalance()
        weight_list_left = [beamWeight(False),beamWeight(True),beamWeight(True),beamWeight(True)]
        weight_list_right = [beamWeight(True),beamWeight(False),beamWeight(False),beamWeight(False),beamWeight(False),beamWeight(False)] 
        self.weights_left = weightGroup(weight_list_left)
        self.weights_right= weightGroup(weight_list_right)
        self.left_basket = basket().next_to(self.balance.upper_bar,direction=DOWN, buff = 0).shift(4*LEFT)
        self.right_basket = basket().next_to(self.balance.upper_bar,direction=DOWN, buff = 0).shift(4*RIGHT)  
        self.basket_list = [self.left_basket, self.right_basket]
        self.weight_list = [self.weights_left, self.weights_right]
        self.weights_left.positionWeights(self.left_basket.dot)
        self.weights_right.positionWeights(self.right_basket.dot)


    def tilt(self, direction):
        if direction == "DL" or direction == "UR":
            self.play(ApplyMethod(self.balance.rotateUpperBar, PI/16), ApplyMethod(self.left_basket.shift, DOWN*0.8), ApplyMethod(self.right_basket.shift, UP*0.8),
            ApplyMethod(self.weights_left.shift, DOWN*0.8), ApplyMethod(self.weights_right.shift, UP*0.8))
        elif direction == "UL" or direction == "DR":
            self.play(ApplyMethod(self.balance.rotateUpperBar, - PI/16), ApplyMethod(self.left_basket.shift, UP*0.8), ApplyMethod(self.right_basket.shift, DOWN*0.8),
            ApplyMethod(self.weights_left.shift, UP*0.8), ApplyMethod(self.weights_right.shift, DOWN*0.8))

    def removeWeights(self,number, side, isX, pause):
        indices_to_pop = []
        i = 0
        for j in range(0,len(self.weight_list[side].weight_list)):
            if self.weight_list[side].weight_list[j].getIsX() == isX:
                indices_to_pop.append(j)
                i += 1
                if i == number:
                    break
        print(indices_to_pop)
        if pause:
            for i in range(0, len(indices_to_pop)):
                self.play(FadeOut(self.weight_list[side].weight_list[indices_to_pop[i]]))
                self.weight_list[side].removeWeight(isX)    
                self.play(ApplyMethod(self.weight_list[side].positionWeights,self.basket_list[side].dot , run_time =0.5))
        else:
            v = VGroup()
            for i in range(0, len(indices_to_pop)):
                v.add(self.weight_list[side].weight_list[indices_to_pop[i]])  
            self.play(FadeOut(v))
            for i in range(0, len(indices_to_pop)):
                self.weight_list[side].removeWeight(isX) 
            self.play(ApplyMethod(self.weight_list[side].positionWeights,self.basket_list[side].dot, run_time =0.5))


class beamBalance(VGroup):
    def __init__(self):
        super().__init__()
        self.base = Triangle(color = WHITE).to_edge(DOWN).stretch(2,1).set_fill(WHITE, opacity=1.0)
        self.middle_bar = Rectangle(height = 4, width = 0.3, color = WHITE).set_fill(WHITE,opacity = 1.0)
        self.upper_bar = Rectangle(width = 10, height = 0.3, color = WHITE).set_fill(WHITE, opacity= 1.0).next_to(self.middle_bar, UP, buff =0)
        self.add(self.base, self.middle_bar, self.upper_bar)

    def rotateUpperBar(self, angle):
        self.upper_bar.rotate(angle)

class basket(VGroup):
    def __init__(self):
        super().__init__()
        self.dot = Dot(fill_opacity=0)
        self.left_line = Line(start =(0,0,0), end = (0,3,0)).rotate(-PI/8).shift(0.57*LEFT)
        self.right_line = Line(start =(0,0,0), end = (0,3,0)).rotate(PI/8).shift(0.57*RIGHT)
        self.bowl = Sector(outer_radius=1.15, inner_radius = 1.12, angle = PI).rotate(PI).shift(1*DOWN)
        self.add(self.left_line, self.right_line, self.bowl, self.dot)


class weightGroup(VGroup):
    def __init__(self, weight_list):
        super().__init__()
        self.positions = [0.6*DOWN, 0.64*LEFT+0.24*DOWN,0.64*RIGHT+0.24*DOWN, 0.12*UP, 0.64*LEFT+0.47*UP, 0.64*RIGHT+0.47*UP, 0.85*UP]
        self.weight_list = weight_list
        self.dot = None

    def addWeight(self,weight):
        self.weight_list.append(weight)
        self.positionWeights(self.dot)

    def positionWeights(self, dot):
        self.dot = dot
        for i in range(0, len(self.weight_list)):
            self.weight_list[i].move_to(self.dot)
            self.add(self.weight_list[i].shift(self.positions[i]))

    def removeWeight(self, isX):
        for j in range(0, len(self.weight_list)):
            if self.weight_list[j].getIsX() == isX:
                self.remove(self.weight_list[j])
                self.weight_list.pop(j)
                break

class beamWeight(VGroup):
    def __init__(self, isX):
        super().__init__()
        self.isX = isX
        self.circle = Circle().scale(0.35)
        if isX:
            self.text = Text("X").align_to(self.circle).scale(0.5)
            self.circle.set_color(RED)
        else: 
            self.circle.set_color(BLUE)
            self.text = Text("1").align_to(self.circle).scale(0.5).set_color(BLUE)
        self.add(self.circle, self.text)

    def getIsX(self):
        return self.isX
