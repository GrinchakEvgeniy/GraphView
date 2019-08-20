from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import Graph, MeshLinePlot
from data_cord import *
from math import *
import parser

class Graphics(BoxLayout):
	def __init__(self,):
		super(Graphics, self).__init__()
		self.plot = MeshLinePlot(color=[1,0,0,1])

		self.ids.graph.add_plot(self.plot)
		# Clock.schedule_interval(self.get_formul, 0.001)
		# self.plot.points = self.get_value()

	def parser_formul(self,string_formula,x):
		return eval(parser.expr(string_formula).compile())
		

	def get_value(self, formula=""):
		n = 0
		if formula:
			for x in second_data:
				first_data[n][1] = self.parser_formul(formula,x)
				n += 1
			return first_data
		return first_data
		

	def get_formul(self):
		formul = self.text_input.text
		self.plot.points = self.get_value(formul)

class MyApp(App):
	def build(self):
		return Graphics()
		

MyApp().run()
