def reverse(x):
        
        new_x = int(str(x)[::-1]) if x>=0 else -int(str(-x)[::-1])
	        
	if abs(new_x)>>31: return 0
        return new_x

def reverse1(x):
	if abs(x)<10: return x
	new_x = 0
	sign =1 if x>0 else -1	
	x = abs(x)
	while x:	
		x, rmn =x//10, x%10
		new_x = new_x*10 + rmn
	if abs(new_x)>>31: return 0
        return new_x*sign

def main():
	x=-1000000000
	print(x, reverse1(x))

if __name__=='__main__':
	main()

