from decimal import Decimal

#ZADANIE 1
def code_generator(code_1, code_2):
	print ("\n--ZADANIE 1 --")
	list = []
	code1, code2 = int(code_1.replace('-','')), int(code_2.replace('-',''))
	if code1 < code2:
		start, end = code1, code2
	else:
		start, end = code2, code1

	for i in range(start, end):
		list.append(str(i)[:2]+'-'+str(i)[2:])
		
	return list
	
	
#ZADANIE 2
def check_values(list, n):
	print ("\n--ZADANIE 2 --")
	n_list = [i for i in range (0,n)]
	output = [a for a in n_list if a not in list]
	return output
	

#ZADANIE 3
def generate_decimals(start, stop, step):
	print ("\n--ZADANIE 3 --")
	multiply = 10
	output = [Decimal(i/multiply) for i in range (int(start*multiply), int(stop*multiply), int(step*multiply))]
	return output
	
print (code_generator("79-900", "80-155"))
print (check_values([0,1,4,5], 12))
print (generate_decimals(2, 6, 0.5))
