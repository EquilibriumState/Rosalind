'''
Marcin Radziszewski solution for:
Mortal Fibonacci Rabbits
http://rosalind.info/problems/fibd/

this program reading file rosalind_fibd.txt in Downloads folder,
result is coppied to clipboard and printed as well
'''

import read_files as rf
import pyperclip

def main():
	n, m = rf.read_files("/Users/marcin/Downloads/rosalind_fibd.txt") #read file to variables
	#create 3 arrays for young, old and dead rabbits. Starting with one young rabbit couple
	rabbits_old = [0]
	rabbits_young = [1]
	rabbits_dead = [0]
	for i in range(n-1):
		if len(rabbits_old) >= m: #checking if rabbits starts dying
			rabbits_dead.append(rabbits_young[-m])  #append dead rabbits arrays with rabbits back from m months
		else:
			rabbits_dead.append(0) #if rabbits didn't starts dying append with 0
		rabbits_old.append(rabbits_young[-1] + rabbits_old[-1] - rabbits_dead[-1]) #appending with mature rabbits for this month
		rabbits_young.append(rabbits_old[-2]) #appending for new created rabbits pair

	pyperclip.copy(rabbits_old[-1] + rabbits_young[-1]) #Result are living mature and young rabbits
	print("Result:", rabbits_old[-1] + rabbits_young[-1], "copied to clipboard")
	rf.printbunnies()


if __name__ == '__main__':
	main()
