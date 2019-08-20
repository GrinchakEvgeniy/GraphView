import parser
from math import *
def parser_formul(self,string_formula):
	formula = string_formula
	code = parser.expr(formula).compile()
	y = eval(code)
	return y