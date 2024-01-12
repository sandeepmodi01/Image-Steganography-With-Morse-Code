MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
                    'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 
                    'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

cntlist = []
swapped_cntlist = []

def encrypt(message):
    global cntlist
    cipher1 = ''
    cnt = ''
    for letter in message:
        if letter != ' ':
            cipher = ''
            cipher1 += MORSE_CODE_DICT[letter] + ' '
            cipher += MORSE_CODE_DICT[letter]
            
            count = 0
            for i in cipher:
                count +=1
                cnt = str(count)
            cntlist += cnt
            
        else:
            cipher += ''
    
    global swapped_cntlist
    for i in range(0, len(cntlist), 2):
        if i+1 < len(cntlist):
            swapped_cntlist.append(cntlist[i+1])
            swapped_cntlist.append(cntlist[i])
        else:
            swapped_cntlist.append(cntlist[i])
            
    print(swapped_cntlist)
    return cipher1

message = input()
res = encrypt(message.upper())
print(res)
print(cntlist)
print(swapped_cntlist)