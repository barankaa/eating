a = int(raw_input("write a "))
b = int(raw_input("write b "))
c = int(raw_input("write c "))

D = b**2 - 4*a*c

result=""

if D<0: 
	result="no roots"
elif D==0:
	x=-b/2*a
	result="root: " + str(x)
else:
	x1=(-b+D**(0.5))/2*a
	x2=(-b-D**(0.5))/2*a
	result="roots: " + str(x1) + ", " + str(x2)
print result
