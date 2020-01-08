from inspect import signature	
import itertools

test = lambda p,q: p and q
test8a = lambda p,q: (p and q) or (not p and not q)
test8b = lambda p,q: not p or q
test8c = lambda p,q: (p or not q) and (q or not p)
test8d = lambda p,q: not (p or q)
test8e = lambda p,q: (q and p) or not p
t9a = lambda p,q: (p or q) and (not p or not q)
t9b = lambda p,q: (p or q) and (not p and not q)
t9c = lambda p,q: (p or q) or (not p or not q)
t9d = lambda p,q,r: (p and (q or not r)) or (not p or r)

m1 = lambda p,q: not (p or q) #DeMorgan's Law (2) left hand side
m2 = lambda p,q: not p and not q #DeMorgan's Law (2) right hand side



def truthTableMaker(expr):
	"""Creates a truth table based on some expression passed in as a lambda function, with variable arguments (unlimited # of letters)"""
	bools = [True, False]
	numEvents = len(signature(expr).parameters)
	eventPermutations = list(itertools.product(bools, repeat=numEvents))
	for tbl_row in eventPermutations:
		result = expr(*tbl_row)
		print(str(tbl_row) + ":" + "\t" + str(result))

def areEquivalent(expr1, expr2):
	"""Returns TRUE if the two statements are logically equivalent, and FALSE if they are not."""
	s1 = []
	s2 = []
	bools = [True, False]
	assert len(signature(expr1).parameters) == len(signature(expr2).parameters), "Compared expressions must have same number of unique events."
	numEvents = len(signature(expr1).parameters)
	eventPermutations = list(itertools.product(bools, repeat=numEvents))
	for tbl_row in eventPermutations:
		s1.append(expr1(*tbl_row))
		s2.append(expr2(*tbl_row))
	return s1 == s2

truthTableMaker(t9d) #generate truth Table for expression t9d (above)
print()
print(areEquivalent (m1,m2)) #test that DeMorgan's Law holds.