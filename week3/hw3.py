#################################################
# HW3
# Your andrewID:
#################################################

#################################################
# NOTES
# Strings are immutable, reassigning needs to be done by redefining
# chr and ord
# eval - evaluates arthematic expressions
# isalnum(), isalpha(), isdigit(), islower(), isspace(), isupper()
# Strip removes leading and trailing whitespace only
# count(), startswith(), endswith(), find(), index()

# Good style reduces time spent debugging, and...
# Around 75% of a developer's time is spent debugging (source)
# Fixing a bug takes 30 times longer than writing a line of code (source)
# Software errors cost the global economy over $300 billion annually in 2013! (source)
# Software errors have resulted in many spectacular failures (source)
#################################################

import cs112_s19_week3_linter
import string

#################################################
# The following problems are COLLABORATIVE
#################################################

# function returns longestCommonSubstring 
def longestCommonSubstring(s1, s2):
    # NOTE : Implemented solution is O(n * m^2) and use DP for O(m*n) 
    ss = ''
    final_count = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            x=i
            y=j
            sub_count = 0
            s  = ''
            while(s1[x]==s2[y]):
                sub_count+=1
                s+=s1[x]
                x+=1
                y+=1
                if(x==len(s1) or y==len(s2)):
                    break
            
            if (final_count<sub_count):
                ss = s
                final_count = sub_count
                
            elif (final_count == sub_count):
                if(s<ss):
                    ss=s
            
    return ss

def bestStudentAndAvg(gradebook):
    gradebook = gradebook.splitlines(True)
    name = ''
    total = 0
    for grade in gradebook:
        if ("#" in grade or grade=="\n"):
            continue
        else:
            grade = grade.split(',')
            val = grade[0]
            sum_v = 0 
            for i in grade[1:]:
                sum_v+=int(i)
            avg = sum_v/(len(grade[1:]))
            if(total==0):
                name = val
                max_grade = avg
                total+=1
            elif(avg>max_grade):
                name = val
                max_grade = avg

    return str(name)+":"+str(int(max_grade))

def encodeColumnShuffleCipher(message, key): 
    # Add "-" at the end in required numbers
    if len(message)%len(key)==0:
        pass
    else:
        message += ("-" * (len(key) - len(message)%len(key)))
    
    new_str = ''
    for i in range(len(message)//len(key)):
        # Create a substring
        string = message[i*len(key):(i+1)*len(key)]
        
        # Replace the substring with the given values
        for j in range(len(key)):
            new_str+=string[key.find(str(j))]
    
    # Read in column form
    mess = ''
    for i in range(len(key)):
        for j in range(len(message)//len(key)):
            mess+=new_str[j*len(key)+i]
    
    return key+mess

# #################################################
# # Everything below here is SOLO
# #################################################
  
def mostFrequentLetters(s):
    print(s)
    new_s = ''
    for i in s:
        if i in string.ascii_letters:
            new_s+=i
    new_s = new_s.lower()
    
    final_s = ''
    for j in range(len(new_s)):
        count = 0
        temp_s = ''
        for k in range(len(new_s)):
            if new_s[k] in final_s:
                continue

            elif count<new_s.count(new_s[k]):
                temp_s = new_s[k]
                count = new_s.count(new_s[k])

            elif (count == new_s.count(new_s[k])) and (new_s[k]<temp_s):
                temp_s = new_s[k]
                count = new_s.count(new_s[k])
 
        final_s+=temp_s
        
    return final_s

def patternedMessage(msg, pattern):
    # Remove whitespaces in message
    n_msg = ''
    for i in msg:
        if i not in string.whitespace:
            n_msg += i

    # Generate new pattern
    k = 0
    new_pattern = ''
    for i in range(len(pattern)):
        # Remove beginning and trailing whitespaces 
        if (i==0 or i==(len(pattern)-1)):
            if pattern[i] in string.whitespace:
                continue
        # Replace pattern
        if pattern[i] not in string.whitespace:
            new_pattern+=n_msg[k]
            k+=1
            if(k==len(n_msg)):
                k=0
        # Replace whitespaces in pattern
        else:
            new_pattern+=pattern[i]

    return new_pattern
    
def decodeColumnShuffleCipher(message):
    key = ''
    code = ''
    for i in message:
        if i in string.digits:
            key+=i
        else:
            code+=i
    key=int(key) # Should have kept it as string only
    
    final_s = ''
    for i in range(len(code)//len(str(key))):
        temp_s = ''
        for j in range(len(str(key))):
            temp_s += code[j*(len(code)//len(str(key)))+i]
        new_s  = ''
        for i in range(len(str(key))):
            new_s  += temp_s[int(str(key)[i])]
        final_s += new_s

    return final_s.replace("-","")

def decodeColumnShuffleCipherNoDashes(message):
    # NOTE :  Check other's solutions
    key = ''
    code = ''
    for i in message:
        if i in string.digits:
            key+=i
        else:
            code+=i
    key=int(key) # Should have kept it as string only
    
    # Insert "-" in the modified code
    modified_code = code
    
    if(len(code)%len(str(key)))!=0:
        for i in range((len(str(key)) - len(code)%len(str(key)))):
            k = (str(key)[-(i+1)])
            val = (int(k)+1)*((len(code)//len(str(key)))+1)-1
            modified_code = modified_code[0:val]+"-"+ modified_code[val:] # Here the numbers are ordered hence it works, else another loop might have to be implemented
    
    code = modified_code
    final_s = ''
    for i in range(len(code)//len(str(key))):
        temp_s = ''
        for j in range(len(str(key))):
            temp_s += code[j*(len(code)//len(str(key)))+i]
        new_s  = ''
        for i in range(len(str(key))):
            new_s  += temp_s[int(str(key)[i])]
            # print("new_s",new_s,"temp_s",temp_s)
        final_s += new_s
    
    return final_s.replace("-","")

# #################################################
# # Test Functions
# # ignore_rest
# #################################################

def testLongestCommonSubstring():
    print("Testing longestCommonSubstring()...", end="")
    assert(longestCommonSubstring("abcdef", "abqrcdest") == "cde")
    assert(longestCommonSubstring("abcdef", "ghi") == "")
    assert(longestCommonSubstring("", "abqrcdest") == "")
    assert(longestCommonSubstring("abcdef", "") == "")
    assert(longestCommonSubstring("abcABC", "zzabZZAB") == "AB")
    print("Passed!")

def testBestStudentAndAvg():
    print("Testing bestStudentAndAvg()...", end="")
    gradebook = """
# ignore  blank lines and lines starting  with  #'s
wilma,91,93
fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) ==  "wilma:92")
    gradebook   =   """
#   ignore  blank   lines   and lines   starting    with    #'s
wilma,93,95

fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) ==  "wilma:94")
    gradebook = "fred,0"
    assert(bestStudentAndAvg(gradebook) ==  "fred:0")
    gradebook = "fred,-1\nwilma,-2"
    assert(bestStudentAndAvg(gradebook) ==  "fred:-1")
    gradebook = "fred,100"
    assert(bestStudentAndAvg(gradebook) ==  "fred:100")
    gradebook = "fred,100,110"
    assert(bestStudentAndAvg(gradebook) ==  "fred:105")
    gradebook = "fred,49\nwilma" + ",50"*50
    assert(bestStudentAndAvg(gradebook) ==  "wilma:50")
    print("Passed!")

def testEncodeColumnShuffleCipher():
    print("Testing encodeColumnShuffleCipher()...", end="")
    
    msg = "WEATTACKATDAWN"
    result = "1320TKA-WTAWACD-EATN"
    assert(encodeColumnShuffleCipher(msg, "1320") == result)
    
    msg = "SUDDENLYAWHITERABBITWITHPINKEYESRANCLOSEBYHER"
    result = "210DNAIRBWHNYRCSYRUEYHEBTTIESNOBESDLWTAIIPKEALEH"
    assert(encodeColumnShuffleCipher(msg,"210") == result)

    print("Passed!")  

def testMostFrequentLetters():
    print("Testing mostFrequentLetters()...", end="")
    
    s = "We attack at Dawn"
    result = "atwcdekn"
    assert(mostFrequentLetters(s) == result)
    
    s = "Note that digits, punctuation, and whitespace are not letters!"
    result = "teanioscdhpruglw"
    assert(mostFrequentLetters(s) == result)
    
    s = ""
    result = ""
    assert(mostFrequentLetters(s) == result)
    
    print("Passed!")

def testPatternedMessage():
    print("Testing patternedMessage()...", end="")
    parms = [
    ("Go Pirates!!!", """
***************
******   ******
***************
"""),
    ("Three Diamonds!","""
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""),
    ("Go Steelers!","""
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
""")]
    solns = [
"""
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
,
"""
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
"""
,
"""
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
"""
    ]
    parms = [("A-C D?", """
*** *** ***
** ** ** **
"""),
    ("A", "x y z"),
    ("The pattern is empty!", "")
    ]
    solns = [
"""
A-C D?A -CD
?A -C D? A-
""",
"A A A",
""
    ]
    for i in range(len(parms)):
        msg,pattern = parms[i]
        soln = solns[i]
        soln = soln.strip("\n")
        observed = patternedMessage(msg, pattern)
        assert(observed == soln)
    print("Passed!")

def testDecodeColumnShuffleCipher():
    print("Testing decodeColumnShuffleCipher()...", end="")
    msg = "1320TKA-WTAWACD-EATN"
    result = "WEATTACKATDAWN"
    assert(decodeColumnShuffleCipher(msg) == result)

    msg = "210DNAIRBWHNYRCSYR-UEYHEBTTIESNOBE-SDLWTAIIPKEALEH-"
    result = "SUDDENLYAWHITERABBITWITHPINKEYESRANCLOSEBYHER"
    assert(decodeColumnShuffleCipher(msg) == result)

    print("Passed!")     

def testDecodeColumnShuffleCipherNoDashes():
    print("Testing decodeColumnShuffleCipherNoDashes()...", end="")

    # This is a place holder to force testing to fail.  Replace this with
    # real testcases.
    assert(decodeColumnShuffleCipherNoDashes("1320TKAWTAWACDEATN") == "WEATTACKATDAWN")

    # assert("Replace Me With Real Tests" == False)

    print("Passed!")

def testAll():
    # Call your tests from here.  If you aren't sure how, look at HW2
    testLongestCommonSubstring()
    testBestStudentAndAvg()
    testEncodeColumnShuffleCipher()
    testMostFrequentLetters()
    testPatternedMessage()
    testDecodeColumnShuffleCipher()
    testDecodeColumnShuffleCipherNoDashes()
    return

def main():
    cs112_s19_week3_linter.lint() # check rules
    testAll()

if __name__ == '__main__':
    main()    