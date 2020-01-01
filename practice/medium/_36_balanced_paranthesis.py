#-*- coding:UTF - 8 -*-
"""
Check for balanced parentheses in Python

Given an expression string, write a python program to find whether a given string has balanced parentheses or not.

Examples:

Input : {[]{()}}
Output : Balanced

Input : [{}{}(]
Output : Unbalanced
"""


def check_balanced(str1):
	open_p = ["[","{", "("]
	close_p = ["]","}",")"]
	stack = []
	for i in str1:
		if i in open_p:
			stack.append(i)
		elif i in close_p:
			if len(stack) > 0 and stack.pop() != open_p[close_p.index(i)]:
				return -1
	return 0


if __name__ == "__main__":
	print check_balanced("{[]{()}}")
	print check_balanced("[{}{}(]")
