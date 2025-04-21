####Hacking the Vigenere Cipher
##Alexander Carter
##4/12/25
##ISAC 240 - Hildebrand


import time, pyperclip, re, sys, cs11, itertools, cs12
import  initializedictandletters1, initializedictandletters

### color class to call using stack overflow https://stackoverflow.com/questions/8924173/how-can-i-print-bold-text-in-python
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


##Initialize constants

class constant:
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    MAX_KEY_LENGTH = 16 # max key length
    MAX_SUBKEY_CHARS = 4 # num letters per subkey
    NONLETTERS_PATTERN = re.compile("[^a-zA-Z]") ##Compile removed chars list that arent A-Z 
    ##Verbose Output
    SILENT_MODE = False

##Syntax for making a set of text BOLD AND RED
##print(color.BOLD + color.RED + 'Wow' + color.END)


def main():
    time.sleep(0.5)
    print(color.BOLD + color.RED + f'Welcome To Vigenere Cracker Script! \n' + color.END)
    
    
    ciphertext = str(input(color.BOLD +color.BLUE + f'Enter the Cipher Text that you recieved here: ' + color.END ))
    time.sleep(0.5)
    
    
    
    dictorcomplicated = input(" Dictionary Attack? Or Frequency Attack?  (Options: d/f): ")
    
    
    if dictorcomplicated.upper().startswith('D'):
        
        
        
        print(f"Decrypting {ciphertext} Now...  \n")
        time.sleep(3)
        plainy = DictionaryAttack(ciphertext)
        print("%s" % (plainy))
    
    elif dictorcomplicated.upper().startswith('F'):
        
        ciphertextt = ciphertext.upper()
       
       
       
        plaintext = RepeatedSequenceSpacing(ciphertextt)
        
        if plaintext != None:
            time.sleep(0.5)
            print(plaintext)
            #print(f"Your Plaintext {color.BOLD + color.RED + plaintext + color.END}")
        
        else:
            sys.exit(f"I am sorry, but we have found no decrypted plaintext for inputted {ciphertext}")




def DictionaryAttack(ciphertext):
    
    
    dictFile = open("/home/whftf/Downloads/Scripts/whftf_class_scripts-main/dict.txt")
    words = dictFile.readlines()
    dictFile.close()
    
    
    for word in words:
        word = word.strip()
        plaintext = cs11.Vinegar(ciphertext, word, 'd')
        
        print(f"plain text var: {plaintext} ")
        print(f"Current key of test : {word}")
        
        
        if initializedictandletters.englishPercentage(plaintext, perWords=50, perLetters=50):
            print( color.BOLD + color.PURPLE + str("FOUND POSSIBLE DECRYPTED STRING WITH BRUTEFORCE DICTIONARY ATTACK... " + color.END ))
            time.sleep(0.5)
            print( color.BOLD + color.RED + f" Key: {word} + {plaintext} " + color.END)
            
            choiceforuser = input("Enter 'im done' if you are done with decrypting. Or just press enter to continue: ")
            
            if choiceforuser.lower() == 'im done':
                print(plaintext)
                sys.exit("Goodbye:)")
            
            
            else:
                continue
        
        else:
            continue
    
    return plaintext
            



def RepeatedSequenceSpacing(ciphertext):
    
    ##Overall Goal: Find any 3-5 Letter Squence
    #Returns Dictionary with the key values of the SEQUENCE recorded
    #Lists spacings within the dictionary as well
    
    
    #First, a regex to remove any specific characters outside of the a-z premis
    ciphertext = constant.NONLETTERS_PATTERN.sub('', ciphertext.upper())
    
    
    #Initialize a sequence dictionary object carrying int spacings
    dictSeqSpace = {}
    
    #For var dictSeqLen from values 3-6, looking  thru patterns from 3-6 chars
    for dictSeqLen in range (3, 6):
        #Nested for loop, determining the start within the messages sequence determined via..
        #Determined via Length of Message - dictionary Sequence Legnth val from before
        for dictSeqStart in range(len(ciphertext) - dictSeqLen):
            
            print(f"Dict sequence length: {dictSeqLen}  + Dict seqyence Start: {dictSeqStart}")
        
            ##Creating a value to store the 'sequence' or pattern via DictionarySequenceLength + Sequence Start slice
            seq = ciphertext[dictSeqStart:dictSeqStart + dictSeqLen]
            print(f"CURRENT SEGMENT OF SLICED VAR SEQ: {seq}")

            
            ##Sequence == Sequence start in string ciphertext (23 (str length) - 5 = 16)
            #Sequence Len = val 3 for first loop - 5
            ##23 = len of cipher text for ex
            #this gets subtracted via dictionary sequence length, as seq val had dictionary sequence length added above
            ##We avoid out of bounds via kength of sequence subtacted via legnth to keep consitent diciponary sequence starts and len vars
            for sequence in range(dictSeqStart + dictSeqLen, len(ciphertext) - dictSeqLen):
                print(f"Found Current Sequence with {seq} : {sequence}, with length of key being: {dictSeqLen} ")
                print(f"SPLICED VAR {ciphertext[sequence:sequence + dictSeqLen] == seq}")
      
                
                #If ciphertext at slice - 1 sequence with Sequence legnth is the same value as seq var
                #Seq == SJW/SYUHT -- 3/5 letter text for test of frequency
                #T/F or bool of 
                if ciphertext[sequence:sequence + dictSeqLen] == seq:
                    print(f"IF STATEMENT DEPENDING ON IF SLICE OF SEQ {ciphertext[sequence:sequence + dictSeqLen]}")
                    if seq not in dictSeqSpace:
                        print("True")
                        ##If the sequence derrived from loop is not within the sequence space var
                        ##This then continues to figure out different set of space for the pattern within the ciphertext
                        dictSeqSpace[seq] = []
                        
                
                
                ##If the ciphertexts sequence compares with the sequence derrived via seq var, then..
                ##We also chekc if this var/sequence matches with added sequence length for the check/condition
                    dictSeqSpace[seq].append(sequence - dictSeqStart)
                    time.sleep(3)
                    print(dictSeqSpace)
        ##Finally return value dictionary Sequence space to determine the values compared via appendend compared sequences from the entire string
        ##val DictSequenceSpace at indicie seq, appends int val of each tested sequence pattern - where the sequence que appeared                
        return(dictSeqSpace)
                        
##Function Goal: REturn any useful factors less then MAX KEY LENGTH of 16 (Vigenere cipher req)
##Factors above 1/2
##Factor of 64, wouldreturn 4, 8, 16
def Importfactors(num):
    
    #If num is un-important
    if num < 2:
        #Return a blank list  to continnue building factors
        return []
    
    
    ##List for factors to append
    important = []
    
    #Checks for ints up to max key len
    #Starts at 2 for skipping any values with 1 as factor
    for factor in range(2, constant.MAX_KEY_LENGTH + 1):
        ##Checks if value num is a genuine factor of specific val factor from each int
        #Modulous for checking
        if num % factor == 0:
            #Append to list important
            important.append(factor)
            
            #var for factors that are between 16 - 1 from dividing any factor from num/factor
            ##This will return a sorted set that removes duplicates and checks for all possible factor values
            doubleFactor = int(num / factor)
            
            #If doubleFactor val < 16 and doesnt = 1    
            if doubleFactor < constant.MAX_KEY_LENGTH and doubleFactor != 1:
                important.append(doubleFactor)
    
    
        print(f"{list(set("IMPORTANT" + important))}")
    ##Return the important set via removing any duplicates
    ## [ 2, 5, 7, etc] -- seperates via comma
    return list(set(important))

##Pulls first index out of item from list / object

def getFirstIndex(things):
    #Return things indicie 0 everytime frunction is called with arg things
    return things[0]


#Goal of function: REturn Tuple like list with indicie factor with factor count of how rare/common a sequence of factors are within the string
#Arg factorSeq gets established later via the code
def CommonFactors(factorSeq):
    #Empty list for list conversion holding values
    factorCount = {}
    
    #For val sequence in factorSequence arg
    for sequence in factorSeq:
        ##listFactors val == the indicie sequence looped thru the argument
        #creates list via  sequence indicie from factorSeq arg
        listFactors = factorSeq[sequence]
        ##For each induvidual indicie within such sequence
        for induvidualSeq in listFactors:
            ##If this sequence is not within the FactorCount object(Dictionary)
            if induvidualSeq not in factorCount:
                ##If the factor does not appear in the list, then we simply show null val
                factorCount[induvidualSeq] = 0
            #If sequence of factors do show, then we add via 1
            factorCount[induvidualSeq] += 1
    
    ##Now initialize the tuple, to then coordinate a list to sort
    ##EG: ([3, 129], [4, 582], [5, 489] etc)
    FactorsFromCountVar = []
    for factor in factorCount:
        ##Error handle factor var via if its less then or equal to key length
        #The key thing here is that these factors prove for valuable key sets for different repeated segments
        ##The key must not be above such a length to prove ineffective however
        if factor <= constant.MAX_KEY_LENGTH:
            ##Append the values factor from factor count that are within bounds of string
            ##This is appended via factor:FactorCount list via indicie factor (Each value from loop)
            FactorsFromCountVar.append((factor, factorCount[factor]))    
    
    ##Finally outside of the loop sort the list before returning
    #Key = getitemindexatone via sorting the list via greatest factor count (First indicie within tuples)
    FactorsFromCountVar.sort(key=getFirstIndex, reverse=True)
    return FactorsFromCountVar
    
##Goal of Function: Finds Sequences from 3-5 letters numerous times at different indicies          
def kasiski(ciphertext):
    #Value holds function algorithm to figure sequence spacing list betwenn each cipher text chunk key between 3-5 characters long
    #The returned space from each repeated sequence is then used in this value
    repeatedSequence = RepeatedSequenceSpacing(ciphertext)
    print(f"{repeatedSequence}")
    sequenceFactors = {}
    #Indicie seq checks for each value within the repeatedSequence spacing funtion above
    for seq in repeatedSequence:
        #Initialize an empty list for sequence factors via indicie seq
        sequenceFactors[seq] = []
        ##Nested for loop containing the values of seq (List of spacings from sequences of ciphertext)
        #This then checks for repeated seuqences, as mentioned above via indicie sequence from the list
        for space in repeatedSequence[seq]:
            ##Append this new looped list with .extend to add each space value to the END of sequenceFactors list
            #This comes from importantFactors function, providing argument space to loop for the factors to append onto sequency factors list
            #The reasoning for this comes apparent next line
            sequenceFactors[seq].extend(Importfactors(space))
            print(f"{sequenceFactors}")
    
    #FactorCountTuple contains the returned key via factor, and factor consistency from the derived sequences of 'spaces'
    #this drags out common sequence patterns from the sequence space derived before
    FactorCountTuple = CommonFactors(sequenceFactors)
    
    #Extract the factor counts from the common factors derived from FactorCountTuple val
    #Initialize empty list
    LikelyKeyLen = []
    #For value twoVal in this list from Common Factors
    for twoVal in FactorCountTuple:
        #Append values factor twoVal via indicie 0 on each pattern []
        LikelyKeyLen.append(twoVal[0])
    
    #Return the list created above
    return LikelyKeyLen
    
#Function Goal: Return same indicie of whatever letter arg n -1 is at the time
##Ex: ABCDEABCDE Returns AA : indicies 1, 6 
def NthAlgorithLetters(n, keyLen, ciphertext):
    
    ##Remove any non A-Z chars using regex
    ciphertext = constant.NONLETTERS_PATTERN.sub('', ciphertext)
    #X is a val that keys the 'nth' character - 1  to keep inbounds from list
    x = n - 1
    #Letters list for return initilized 
    letters = []
    #While val x (nth letter - 1) less then length of cipher textinput
    while x < len(ciphertext):
        #Letters list gets value x within ciphertext appended (value 1 for A) creating the indicies of each repeating letter of nth
        letters.append(ciphertext[x])
        #We add x by "Key len" or the argument length for factor key to check for each letter within list
        x += keyLen
    #Return list of letters joining no spaces
    return ''.join(letters)


#Function Goals: Attempt to crack most likely letters for each letter within key for ciphertext
#
def attemptHackWithLength(ciphertext, keyLenLikely):
    
    ciphertextup = ciphertext.upper()
    
    ## [ A, 6]
    freakScores = []
    #For loop consisting from indicie 1 to the specific amount of char len in keyLenLikely derived from earlier functions
    for n in range(1, keyLenLikely + 1):
        nLetters = NthAlgorithLetters(n, keyLenLikely, ciphertextup)
        newFreakScores = []
        for possibleKeyLen in constant.LETTERS:
            decrypt = cs11.Vinegar(possibleKeyLen, nLetters, 'd')
            ##Tuple of keyLen w/ english decrypt function 
            KeyandFreq = (possibleKeyLen, cs12.matchEnglish(decrypt))
            ##Append to freakScores list
            freakScores.append(KeyandFreq)
        ##Sort via high -> low    
        newFreakScores.sort(key=getFirstIndex, reverse=True)
        freakScores.append(newFreakScores[:constant.MAX_SUBKEY_CHARS])
        
        
        for a in range (len(freakScores)):
            #call first letter
            print(f"Possible letters via key decryption: {a + 1}")
        
            for freaquencyScore in freakScores:
                print(f"\n Current Score for letters Frequency from ciphertext: {freaquencyScore}")
    #from python docs:
    ## product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) → 000 001 010 011 100 101 110 111
    ##From max length to loop thru value [16]
    for ind in itertools.product(range(constant.MAX_KEY_LENGTH), repeat=keyLenLikely):
        newpotkeys = ''
        ##Calculate potential key from "Frequency Score var"        
        for b in range(keyLenLikely):
            ##New potential keys gets added based off the KeyLenLikely param we grabbed from before(loop)
            #We grab key len candidates based off of frequency scores
            #Replaece potkey str with [b(var for looped), [first var of ind variable[b].] ]
            newpotkeys += freakScores[b][ind[b]][0] 

            print(f"\n Attempting with key {newpotkeys}")       
            time.sleep(1)
    

        decrypted = cs11.Vinegar(ciphertext, newpotkeys, 'd')

        actualText = []
        ##for loop to check if the origional text was uppercase or lower
        ##Changes the new text to append now with better casing for output
        for i in range(len(ciphertext) and not ' '):
            if ciphertext[i].isupper():
                actualText.append(decrypted[i].upper())
            else:
                actualText.append(decrypted[i].lower())

        
        print(f"YOUR NEW OUTPUTTED TEXT SNIPPET: {actualText[:50]}")


        print('Possible key used for encryption Above: %s' %  (newpotkeys))
    

        continuing = str(input("Would you like to continue to Decrypt With a more Complicated Technique? (c/d): "))

        if continuing.lower().startswith('d'):
            time.sleep(1)
            print(f"\n Your Final Text Message: {actualText}")
        
        elif continuing.lower().startswith('c'):
            cipher = VinegarFinalBoss(ciphertext)
            print({cipher})

    ##Failed via output of no results
    return None    

def VinegarFinalBoss(ciphertext):

    #First, kaski function to find length of the encrypted key
    LenLikely = kasiski(ciphertext)
    time.sleep(2)
    print(f"LEN LIKEY VAR VIA VINEGAR FINAL BOSS: {LenLikely}")
    
    keyStr = ''

    for keyLen in LenLikely:

        keyStr += '%s' % (keyLen)
        print(f"POSSIBLE KEY LENGTHS VIA KASKI EXAMINATION: {keyStr}\n")

    plaintext = None

    for keyLen in LenLikely:
        print(f"Attempting to crack with key {keyLen} : With Overall Possibilities: {LenLikely}")
        plaintext = attemptHackWithLength(ciphertext, keyLen)

        ##If we find solution, break

        if plaintext != None:
            time.sleep(3)
            sys.exit(f"YOUR TEXT: {color.BOLD + color.BLUE + plaintext + color.END}")
        
        if plaintext == None:

            time.sleep(1)
            print("Unable to crack.... Bruteforcing key now..")

            for keyLeng in range(1, constant.MAX_KEY_LENGTH + 1):
                if keyLeng not in keyLen:
                    plaintext = attemptHackWithLength(ciphertext, keyLeng)

                    if plaintext != None:
                        sys.exit(f"YOUR RETURNED PLAINTEXT: {color.BOLD + color.CYAN + plaintext + color.END}")
        

        return "".join(plaintext)



            
    
if __name__ == "__main__":
    main()