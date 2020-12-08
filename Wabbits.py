'''
Marcin Radziszewski solution for:
Rabbits and Recurrence Relation
http://rosalind.info/problems/fib/

this program reading file rosalind_fib.txt in Downloads folder,
result is coppied to clipboard and printed as well
'''

import read_files as rf
import pyperclip

def main():
	n, k = rf.read_files("/Users/marcin/Downloads/rosalind_fib.txt") #read file to variables
	# create 2 arrays for young and old. Starting after two months, when we have one mature couple
	rabbits_old = [1,1]
	rabbits_young = [0,0]
	if n-2 > 0: # checking if we consider more than two months
		for i in range(n-2): #for every month after 2nd we create rabbits
			rabbits_old.append(rabbits_young[-1] + rabbits_old[-1]) #checking how many mature rabbits we have this month
			rabbits_young.append(rabbits_old[-2]*k) #new rabbits are born

		result = rabbits_old[-1] + rabbits_young[-1] #Result are mature and young rabbits
	else:
		result = rabbits_old[-1] + rabbits_young[-1]

	pyperclip.copy(result)
	print("Result:", result, "\nCopied to clipboard")
	rf.printbunnies()

if __name__ == '__main__':
	main()
