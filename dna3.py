

"""
Genes that code for proteins comprise open reading frames (ORFs) consisting of a series of codons that 
specify the amino acid sequence of the protein that the gene codes for. The ORF begins with an initiation 
codon - usually (but not always) ATG - and ends with a termination codon: TAA, TAG or TGA


What is the length of the longest ORF appearing in reading frame 2 of any of the sequences
"""
def find_orf_2(sequence):        # Find orf 2
    # Find all ATG indexs
    start_position = 1
    start_indexs = []
    stop_indexs = []
    for i in range(1, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    # Find all stop codon indexs
    for i in range(1, len(sequence), 3):
        stops =["TAA", "TAA", "TGA"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    for i in range(0,len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                mark = stop_indexs[j]+3
                break
    return orf


"""
Q1 = How many records are in the file?
A1 = 17

https://www.genomatix.de/online_help/help/sequence_formats.html
A sequence file in FASTA format can contain several sequences.
Each sequence in FASTA format begins with a single-line description, followed by lines of sequence data. The description line must begin with a greater-than (">") symbol in the first column.

An example sequence in FASTA format is:

>AB000263 |acc=AB000263|descr=Homo sapiens mRNA for prepro cortistatin like peptide, complete cds.|len=368
ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCC
CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC
CTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG
AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCC
CTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG
TTTAATTACAGACCTGAA

"""

f = open("dna3.fasta", "r")
file = f.read()
seqcount = file.count('>')
print("Number of sequence = " + str(seqcount))

"""
Q2 = What are the lengths of the sequences in the file? What is the longest sequence and what is the shortest sequence?
"""

f = open("dna3.fasta", "r")
file = f.readlines()

sequences = []
seq = ""
for f in file:
    if not f.startswith('>'):
        f = f.replace(" ", "")      # remove all spaces and newline from the text 
        f = f.replace("\n", "")
        seq = seq + f 				# ... then form a long sequence
    else:
        sequences.append(seq)
        seq = ""

# Add the last seq
sequences.append(seq)

sequences = sequences[1:]          # discard the first sequence, since it is null

lengths = [len(s) for s in sequences]
print("\nMax sequence length = " + str(max(lengths)))
print("Min sequence length = " + str(min(lengths)))

print("\nSequence Length Report:")
for j in range(seqcount):
	print ("Length of sequence " + str(j) + " is " + str(lengths[j]))

"""
what is the length of the longest ORF in the file?
"""

n = 1
lengths = []
for s in sequences:
    orfs = find_orf_2(s)
    print("ORF")
    for j in orfs:
        print(j)
        print("================")
        lengths.append(len(j))

print("\nLongest ORF is:" + str(max(lengths)))


