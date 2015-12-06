#! /usr/bin/env python3
# --*-- coding:utf-8 --*--
class student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
	def print_score(self):
		print('%s: %s' % (self.name,self.score))
	def get_grade(self):
		if self.score >=90:
			return 'A'
		elif self.score >=60:
			return 'B'
		else:
			return 'C'

bart=student('shiyu',98)

lisa=student('Lisa',89)

print('bart.name=',bart.name)
print('lisa.name=',lisa.name)
bart.print_score()

print('grade of bart:',bart.get_grade())
print('grade of lisa:',lisa.get_grade())
