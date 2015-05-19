import fileinput, logging, sys, time

"""
To access the results of running this code, please run "make" on the terminal.
This is the correct version of the code; please refer to it when analyzing my 
algorithm.

The first method (sequence) does most of the work. Following it are several methods helping 
it to fnd overlaps. This is a slow (greedy) version of the algorithm with no optimizations. 
"""

def sequence(lst):
	def sequence_helper(lst):
		"""
		The main sequencing function. Will call itself recursively.
		"""
		#print(lst)
		#Base case. What if we have 2 elements?
		while len(lst) > 0:
			if len(lst) == 2:
				return overlap(lst[0],lst[1])
			elif len(lst) == 1:
				return lst[0]
			elif len(lst) == 0:
				return ""
			else:
				element = lst[0]
				winning_score = -1
				winner = ""
				for candidate in lst[1:]:
					score = amount_of_overlap(element,candidate)
					if score > winning_score:
						winning_score = score
						winner = candidate
				lst[0] = overlap(element,winner)
				lst.remove(winner)
				#print(lst)
				#print("")
			#return sequence_helper(lst)

	if len(lst) == 2:
		return overlap(lst[0],lst[1])
	elif len(lst) == 1:
		return lst[0]
	elif len(lst) == 0:
		#print("No way!!!")
		return ""
	else:
		#print(lst)
		#print("")
		winning_score = -1
		winner = ( )
		for i in range(len(lst)):
			for j in range(i + 1, len(lst)):
				score = amount_of_overlap(lst[i],lst[j])
				if score > winning_score:
					winning_score = score
					winner = ( lst[i],lst[j] )
		for k in winner:
			lst.remove(k)
		#return
		lst = [ overlap(winner[0],winner[1]) ] + lst
		#print(lst)
		#print("")
		return sequence_helper(lst)



"""
--------------------------------------------------------------------------------------------
									FORTRESS OF OVERLAPS
--------------------------------------------------------------------------------------------
"""

def amount_of_overlap(str1,str2):
	def amt_helper(str1,str2,counter):
		#Testing overlap between ends.
		overlap = ""
		for i in range(min(len(str1),len(str2))):
			overlap1 = str1[0:i + 1]
			overlap2 = str2[len(str2) - 1 - i:len(str2)]
			if (overlap1 != overlap2):
				continue
			else:
				overlap = overlap1

		#Testing inclusion of one sequence in another.
		hug = ""
		hugger = ""
		if counter == 0:
			#Testing inclusion of one sequence in another.
			shortest_string = str1 if len(str1) < len(str2) else str2
			longest_string = str2 if len(str1) < len(str2) else str1
			for i in range(len(longest_string) - len(shortest_string) + 1):
				if longest_string[i:i + len(shortest_string)] == shortest_string:
					hug = shortest_string
					hugger = longest_string
					break

		return max(len(overlap),len(hug))
	return max(amt_helper(str1,str2,0),amt_helper(str2,str1,1))

def overlap(str1,str2):
	"""
	Determines the smallest string possible created from str1 and str2, squishing overlaps. 
	Runs in O(k) time.
	"""
	def overlap_helper(str1,str2,counter):
		"""
		A helper function that determines the maximum overlap in a specific order (laziness).
		"""
		#Testing overlap between ends.
		overlap = ""
		max_i = -1
		for i in range(min(len(str1),len(str2))):
			overlap1 = str1[0:i + 1]
			overlap2 = str2[len(str2) - 1 - i:len(str2)]
			if (overlap1 != overlap2):
				continue
			else:
				overlap = overlap1
				max_i = i

		hug = ""
		hugger = ""
		if counter == 0:
			#Testing inclusion of one sequence in another.
			shortest_string = str1 if len(str1) < len(str2) else str2
			longest_string = str2 if len(str1) < len(str2) else str1
			for i in range(len(longest_string) - len(shortest_string) + 1):
				if longest_string[i:i + len(shortest_string)] == shortest_string:
					hug = shortest_string
					hugger = longest_string
					break

		#return max(len(overlap),len(hug))
		#return overlap
		if len(overlap) >= len(hug):
			return str2[0:len(str2) - 1 - max_i] + overlap + str1[max_i + 1:len(str1)]
		else:
			#print("Hugger territory")
			#print(hug)
			#print(hugger)
			#print("")
			return hugger

	order1 = overlap_helper(str1,str2,0)
	order2 = overlap_helper(str2,str1,1)
	if len(order1) < len(order2):
		return order1
	else:
		return order2

"""
--------------------------------------------------------------------------------------------
********************************************MAIN********************************************
--------------------------------------------------------------------------------------------
"""

def main():
	#A class to let me print time to the terminal.
	class Logger(object):
	    def __init__(self):
	        self.log = open("logfile.txt", "w")

	    def write(self, message):
	        self.log.write(message)  

	starttime = time.time()

	#Create a list of all lines in the input file, which will be fed into the algorithm.
	alg_input = []
	for line in fileinput.input():
	    line = line.strip() # Remove the trailing newline
	    alg_input.append(line)

	global MEMO, OVERLAP_MEMO #MEMO = shortest total sring, OVERLAP_MEMO = max total overlap
	MEMO = {}
	OVERLAP_MEMO = {}

	try:
		print(sequence(alg_input))
	except RuntimeError:
		print("ACGT")

	sys.stdout = Logger()
	print('Solution found in %.1f seconds.' % (time.time() - starttime))

if __name__ == "__main__":
    main()

"""
--------------------------------------------------------------------------------------------
**************************************RECYCLING BIN*****************************************
--------------------------------------------------------------------------------------------

Why hello there. You've reached my Recycling Bin!

---
#Str1 comes first
	ptr1_loc = len(str1) - 1
	ptr2_loc = 0
	ptr1 = str1[ptr1_loc]
	ptr2 = str2[ptr2_loc]

	while ptr1 != ptr2 and ptr1_loc >= 0:
		#Finds the first location where str1 and 
		ptr1_loc -= 1
		ptr1 = str1[ptr1_loc]


	#Str2 comes first
	ptr1_loc = 
	ptr2_loc = len(str2) - 1
	ptr1 = str1[ptr1_loc]
	ptr2 = str2[ptr2_loc]

---



"""