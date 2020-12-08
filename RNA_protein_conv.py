def uploadRNA(fileRNA):
	with open(fileRNA, "r") as s:
		RNA = s.read()
	RNA = ''.join(RNA.split('\n'))
	return RNA
	
def convert_RNA(RNA):
	codon_dict = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 'UUC': 'F', 'CUC': 'L', 
	'AUC': 'I', 'GUC': 'V', 'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V', 'UUG': 'L', 
	'CUG': 'L', 'AUG': 'M', 'GUG': 'V', 'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A', 
	'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 
	'GCA': 'A', 'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', 'UAU': 'Y', 'CAU': 'H', 
	'AAU': 'N', 'GAU': 'D', 'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 'UAA': 'Stop',
	'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', 'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
	'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G', 'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 
	'GGC': 'G', 'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 'UGG': 'W', 'CGG': 'R',
	'AGG': 'R', 'GGG': 'G'}

	polimerase = 0
	reading = False
	protein = []
	for i in RNA:
		if RNA[polimerase:polimerase+3]=='AUG':
			reading = True
		if reading:
			codon = codon_dict[RNA[polimerase:polimerase+3]]
			if codon == 'Stop':
				break
			else:
				protein.append(codon)
			polimerase+=3
		else:
			polimerase+=1
	protein = ''.join(protein)
	return protein

def main():
	RNA = uploadRNA('/Users/marcin/Downloads/rosalind_prot.txt')
	protein = convert_RNA(RNA)
	print(protein)

if __name__ == '__main__':
	main()