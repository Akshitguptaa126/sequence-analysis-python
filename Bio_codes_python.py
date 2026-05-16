seq="    atcgtacgtcga"  # strings are immutable

print(seq.upper())   #make letters uppercase

print(seq.count("a"))   #count a certain letters in a string

print(seq.replace("a","x"))     #replace any letter with other letter in a string 

print(seq.strip())  #it is used for to remove unwanted spaces and\n new lines in the string 



seq1=["A","T","C","G"]  #list will be joined by a join function   # lists are mutable 
print("".join(seq1))

print("_".join(seq1))     # add a underscore and joined letters in the list  

print(",,".join(seq1))



for bases in seq:   #loops
    print(bases)


nucs = ["A", "T", "G", "C"]    
for n in nucs:      #again normal loop
    print(nucs)
    print(n)


nucs = ["A", "T", "G", "C"]  #this one is nested loop
for n in nucs:
    print(nucs)
    for n in nucs:
           print(n)


for n  in range(0,10):    #range function use
    print(n)



for n in range(10,-1,-1):  #reverse range numbers 
    print(n,end=" \n")

    

for i in range(9,3,-1):
     print(i,end=" ")


seq2="ATCGCTAGFYUJHGCGCT"

nuc=["A","C","T","G"]
for bases in seq2:                        #if else conditioning and validating sequence 
    if bases not in nuc:
        print("not valid  sequence")
        break
else:
    print("valid sequence")    


def validateseq(seq2):
    for bases in seq2:
        if bases not in nuc:    ###using function to get a validation or checking a function
            return False
        
    else:
        return True
result=validateseq(seq2)
print(result)


seq3="ATCGTCGTAGCTCGATCGATCGATGCTAGCTAGCTAGCTAGCTAGCTAGTCGATCGATCGATCGATGCTACGTAGCTAGCATGCTACGATCGATGCTAGCCCCC"
nuc={"A":"T","C":"G","T":"A","G":"C"}

def complimenting(seq3):
    X=seq3[::-1]
    compleseq=""
    for bases in seq3:
        compleseq+=nuc[bases]
    return compleseq,X
result,Y=complimenting(seq3)
print(result)
print(Y)  



nuc1={"A":0,"C":0,"T":0,"G":0}

def count(seq3):                   ####counting nucleotides
    for bases in seq3:            #uses dictionary
        if bases in nuc1:
            nuc1[bases]+=1
    return nuc1
print(count(seq3))        


def complimenting(seq3):
    
    compleseq=""
    for bases in seq3[::-1]:
        compleseq+=nuc[bases]
    return compleseq
result=complimenting(seq3)
print(result)
 

def countings(seq3):
    
    seq3.count("A")
    seq3.count("G")
    seq3.count("C")                          # uses dictionary
    seq3.count("T")
    return {"A": seq3.count("A"),
        "G": seq3.count("G"),
        "C": seq3.count("C"),
        "T": seq3.count("T")}

print( countings(seq3))
     
seq4= "ATCGTCGAGCTGCTCGCTAGCTCGACTGATCGATGGCTAGCTCGATCGCTAGCTCGATCGCTAGCTCGACGTCCGCGCGGGTGTGATGATGCTGATCGTGAGATCGATGCTCGATGCTGGTCGATGCTAGTCGATCGTAGCTGATCGATGCTAGCTAGCTAGTGT"

def gccontent(seq4):
    G= seq4.count("G")        #### CALCULTING GC CONTENT BY using function calling
    C= seq4.count("C")
    totalgc=(G+C)/len(seq4)*100
    return totalgc
result=(gccontent(seq4))
print(f"GC content: {result:.2f}%" )

count=0
l= ["G","C"]
for bases in seq4:
    if bases in l:
        count+=1                    ###another ways to count gc without using fucntion
print(count)        

g1=seq4.count("G")
c1=seq4.count("C")
per= (g1+c1)/len(seq4)*100

print(per)        



def gcsubsection(seq4):
    k=5
    result=[]
    for bases in range(0,len(seq4)-k+1):
        subsection =seq4[bases:bases+k]
        G= subsection.count("G")        #### CALCULTING GC CONtent
        C= subsection.count("C")
        totalgc=(G+C) / len(subsection) * 100
        result.append((subsection,totalgc))
    return result
print(gcsubsection(seq4))



sequence="ATCGTCGCTAGCTCGATCGT"



def calculate_gc_content(sequence, window_size=None):
# Make sure sequence is in upperc

    # Calculate total GC content
    total_c = sequence.count("C")
    total_g = sequence.count("G")
    total_gc = (total_c + total_g) / len(sequence) * 100

    # Calculate gc in subseccTIon
    windows = []
    window_size=3

    for i in range(len(sequence) - window_size + 1):
            window = sequence[i:i + window_size]
            c = window.count("C")
            g = window.count("G")
            gc_content = (c + g) / len(window )* 100
            windows.append((window, gc_content))

    # Return both total GC and the list of window GC%
    return total_gc, windows
#print(calculate_gc_content(sequence, window_size=None))


seqz="ATCGTCGCTCGTACGTC"
total_gc,windows=calculate_gc_content(seqz, window_size=2)                       ### GC CALCULATOR####
print(total_gc)            ###can directly get gc content of any winndow
print(windows)
print(f"Total GC Content: {total_gc:.2f}%")
for win,gc in windows:                 ##### to get the and print also the value of subsection and window
    print(f"{win} → GC = {gc:.2f}%")





seq5="""TTTACCACCACCAGGCTGTCATCAAGGGACGCTTTGGCCTGGATGCTACTGCTGTGGGTGATGAGGG
TGGCTTTGCCCCCATCCTGAACAACAAGGATGCTCTGCAGCTCATCCAGGAGGCCATCAGCAAGGCT
GGCTACACTGGAAAGATTGAAATTGGTATGGATGTGGCTGCCTCTGAGTTCTACAAGGGCAACAATGTTT
ATGACCTGGACTTCAAGACTGCCAACAATGATGGCTCCCAGAAGATCTCTGGTGACCAGCTCAGGGACAT
GTACATCGAGTTCTGCAAGGACTTCCCCATCACCTC"""

seq51=seq5.replace("\n","").upper()
codon_table = {
    "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
    "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
    "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
    "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
    "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
    "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
    "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
    "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
    "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
    "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
    "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
    "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
    "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
    "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
    "TAC":"Y", "TAT":"Y", "TAA":"_", "TAG":"_", "TGA":"_"
}


def translationcodon(seq5):
    
    protiencode=""
    for i in range(0,len(seq5)-2,1):                     ###TRANSLATIONcodon
        codons=seq5[i:i+3]
        aminoacid=codon_table.get(codons,"X")
        protiencode+=aminoacid
        if aminoacid =="_":
            break
        
    return protiencode
print(translationcodon(seq5))    

seq = """TTTACCACCACCAGGCTGTCATCAAGGGACGCTTTGGCCTGGATGCTACTGCTGTGGGTGATGAGGG
TGGCTTTGCCCCCATCCTGAACAACAAGGATGCTCTGCAGCTCATCCAGGAGGCCATCAGCAAGGCT
GGCTACACTGGAAAGATTGAAATTGGTATGGATGTGGCTGCCTCTGAGTTCTACAAGGGCAACAATGTTT
ATGACCTGGACTTCAAGACTGCCAACAATGATGGCTCCCAGAAGATCTCTGGTGACCAGCTCAGGGACAT
GTACATCGAGTTCTGCAAGGACTTCCCCATCACCTC"""
seq1=seq.replace("\n", "").upper()







def find_all_forward_orfs(seq1):
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    all_orfs = []

    for frame in range(3):               # Outer loop for frame 0, 1, 2
        i = frame                        
        while i < len(seq1) - 2:
            codon = seq1[i:i+3]
            if codon == start_codon:
                for j in range(i+3, len(seq1)-2, 3):
                    stopcodon = seq1[j:j+3]
                    if stopcodon in stop_codons:
                        orf = seq1[i:j+3]
            
                        all_orfs.append((orf, frame)) 
                        break
            i += 3
    return all_orfs
print(find_all_forward_orfs(seq1))


seq = """TTTACCACCACCAGGCTGTCATCAAGGGACGCTTTGGCCTGGATGCTACTGCTGTGGGTGATGAGGG
TGGCTTTGCCCCCATCCTGAACAACAAGGATGCTCTGCAGCTCATCCAGGAGGCCATCAGCAAGGCT
GGCTACACTGGAAAGATTGAAATTGGTATGGATGTGGCTGCCTCTGAGTTCTACAAGGGCAACAATGTTT
ATGACCTGGACTTCAAGACTGCCAACAATGATGGCTCCCAGAAGATCTCTGGTGACCAGCTCAGGGACAT
GTACATCGAGTTCTGCAAGGACTTCCCCATCACCTC"""
seq1=seq.replace("\n", "").upper()

def openreadingframes(seq1):
    start_codon="ATG"
    stop_codon=["TAA", "TGA", "TAG"]
    ORF=[]
    i=0
    while i <len(seq1)-2 :
        codon=seq1[i:i+3]
        if codon == start_codon:
            for j in range(i+3,len(seq1)-2,3):
                stopcodon=seq1[j:j+3]
                if stopcodon in stop_codon:
                    ORF.append(seq1[i:j+3])
                    break
        i+=3
    return ORF
print(openreadingframes(seq1))           


seq="""TTTACCACCACCAGGCTGTCATCAAGGGACGCTTTGGCCTGGATGCTACTGCTGTGGGTGATGAGGG
TGGCTTTGCCCCCATCCTGAACAACAAGGATGCTCTGCAGCTCATCCAGGAGGCCATCAGCAAGGCT
GGCTACACTGGAAAGATTGAAATTGGTATGGATGTGGCTGCCTCTGAGTTCTACAAGGGCAACAATGTTT
ATGACCTGGACTTCAAGACTGCCAACAATGATGGCTCCCAGAAGATCTCTGGTGACCAGCTCAGGGACAT
GTACATCGAGTTCTGCAAGGACTTCCCCATCACCTC"""

seq1 =  seq.replace("\n", "").upper()
codon_table = {
    "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
    "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
    "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
    "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
    "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
    "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
    "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
    "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
    "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
    "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
    "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
    "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
    "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
    "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
    "TAC":"Y", "TAT":"Y", "TAA":"_", "TAG":"_", "TGA":"_"
}
reversecompliment={'A':'T','C':'G','T':'A','G':'C'}

def translation(seq1):
     complement=""
     for nuc in seq1[::-1]:
         complement+=reversecompliment[nuc]   
 
     print(complement)
                                                                 ######only revered strand 6 frames but we have to make another 3 frames of forwarded strand 

     for frame in range(0,6):
         
         protien=""
         for bases in range(frame,len(complement)-2,3):

            codon =complement[bases:bases+3]
            aminoacid=codon_table.get(codon,"X")                    ####use of nested loops
            if aminoacid == "_":
                break
            protien+=aminoacid
         print(f"Frame {frame+1}: {protien}")



translation(seq1)


seq = """TTTACCACCACCAGGCTGTCATCAAGGGACGCTTTGGCCTGGATGCTACTGCTGTGGGTGATGAGGG
TGGCTTTGCCCCCATCCTGAACAACAAGGATGCTCTGCAGCTCATCCAGGAGGCCATCAGCAAGGCT
GGCTACACTGGAAAGATTGAAATTGGTATGGATGTGGCTGCCTCTGAGTTCTACAAGGGCAACAATGTTT
ATGACCTGGACTTCAAGACTGCCAACAATGATGGCTCCCAGAAGATCTCTGGTGACCAGCTCAGGGACAT
GTACATCGAGTTCTGCAAGGACTTCCCCATCACCTC"""
seq1=seq.replace("\n", "").upper()

def openreadingframes(seq1):
    start_codon = "ATG"

    for frame in range(3):
        print(f"\nFrame {frame}:")
        positions = []

        for i in range(frame, len(seq1)-2, 3):
            codon = seq1[i:i+3]
            if codon == start_codon:
                positions.append(i)

        print(f"ATG found at positions: {positions}")
print(openreadingframes(seq1))        




