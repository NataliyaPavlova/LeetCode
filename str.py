'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

'''

from toolz import reduce

def bs(s):
	func = lambda x,y: x+y if y!='#' else x[:-1]
	return reduce(func, s, '#')
    
def bs1(s):
	l = s.split('#')
	print(l)
	m = [el[:-1] for el in l if el]
	print(m)	
	return ''.join(m) 

def main():
	s='ab##'
	t='c#d#'
	print(bs1(s))	
	#print('s={} \nt={}\nbs={}'.format(s,t,bs1(s)))

if __name__=='__main__':
	main()
