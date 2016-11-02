import re

lower_value= 3.440924
upper_value= 14.573949

def main():
	match_list= []
	fill_list=[]
	control_dict= []

	lineNumbersThatICareAbout = []


	with open("C:\Python\UM2+_magnetTest.py") as f:
	    for line in f:
	    	fill_list.append(line)
	    	
	    	z_regex = re.compile(r'G0\sX\d+\.\d+\sY\d+\.\d+\sZ[0-9][0-9]?\.\d+')
	    	my_test = z_regex.search(line)
	    	
	    	if my_test is not None:
	    		match_list.append(my_test.group())


	print match_list


	for Line_number, f in enumerate(fill_list):
		# or make list_number= 0 at the topm then line_number= line_number + 1, then add line number to the line number dict-  But easier to do it as an index in a loop
		line_dict={}
		line_dict ["line_No"] = Line_number + 1
		line_dict["line"]=f
		control_dict.append(line_dict)




	digit_list= []

	for f in match_list:
		Z_component= f.split()[3]
		if Z_component.startswith("Z"):
			digit_list.append(float(Z_component[1:])) 
		else:
			raise Exception("Item does not start with a Z!")

	print digit_list
	


	prev_01 = digit_list[0]
	prev_02 = digit_list[0]


	for f in digit_list:
		# if the current number is greater than the lower_value, break out of the loop
		if f <= lower_value:
			prev_01 = f

		elif f <= upper_value:
			prev_02 = f

	print prev_02


	result_01= str("Z") + str(prev_01)
	result_02= str("Z") + str(prev_02)



	#Match to control dic

	print result_01

	for f in control_dict:
		if result_01 in f["line"] or result_02 in f["line"]:
			print f
			lineNumbersThatICareAbout.append(f["line_No"])
		#if result_01 in f["Line"]
		#print f["Line_No"]
		#print f["Line"]


	return lineNumbersThatICareAbout

if main() == [3427, 8645]:
	print "*******************\n* you are the man *\n*******************"
else:
	print "you still suck"

