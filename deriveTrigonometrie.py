from manim import *

class Magic(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min = -1,
            x_max = 7,
            x_axis_width= 8,
            num_graph_anchor_points=100,
            y_min=-2,
            y_max=2,
            y_axis_height=4,
            graph_origin=[-5,0,0],
            axes_color=WHITE,
            x_labeled_nums=range(-1, 7, 2),
            y_labeled_nums=range(-1,2,1),
            include_tip=True,
            **kwargs
        )
        self.function_color = RED

    def construct(self):
        self.setup_axes(animate = True)
        sin = self.get_graph(np.sin, self.function_color)
        sin_label = self.get_graph_label(sin, label = "\\sin(x)")
        cos = self.get_graph(np.cos, color = BLUE)
        cos_label = self.get_graph_label(cos, label = "\\cos(x)")
        #self.play(FadeInFrom(sin, LEFT))
        #self.wait()
        x2 = self.get_graph(lambda x: x)
        self.play(FadeInFrom(sin, LEFT))
        self.wait()
        der = self.get_derivative_graph(sin)
        self.play(ReplacementTransform(sin, der))
        self.wait()





        