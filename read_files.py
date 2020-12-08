'''
program for reading files for fibonacci rabbits from Rosalind db
'''

def read_files(file):
    '''
    Reading files as array of integers
    Input files should have number values seperated with spaces or new lines
    '''
    with open(file, "r") as f:
        raw_read = f.read() #Reading given file
    if "\n" in raw_read:
        raw_read = raw_read.replace("\n", " ") #replacing new lines with spaces
    raw_read = raw_read.strip() #removing spaces from ends
    raw_read = raw_read.split(" ") #creating array with strings from given file, single space id consider as separator
    result_read = [int(a) for a in raw_read] #changing strings in array into integers
    return result_read

def printbunnies():
    print(r'''
     (\ /)     (\ /)
     (=o.o)   (^.^=)
    o(")_(") (")_(")o''')

def main():
    file = input("Which file do you wish to read? Returning array of numbers")
    read_files(file)

if __name__ == '__main__':
    main()
