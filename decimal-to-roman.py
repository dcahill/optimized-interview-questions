def number_to_roman(number):

    if int(number) > 3999999 or int(number) < 0:
        print("Invalid entry. Please enter a number between 0-3999999:")
        return
    
    numbers = list(number)
    numbers.reverse()

    roman_numerals = {
     'S1000000':['','_','__','___'],
        1000000:['','M','MM','MMM'],
      'S100000':['','_','__','___','__','_','__','___','____','__'],
         100000:['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
       'S10000':['','_','__','___','__','_','__','___','____','__'],
          10000:['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
        'S1000':['','','','',      '__','_','_ ','_  ','_   ','__'],
           1000:['','M','MM','MMM','IV','V','VM','VMM','VMMM','IX'],
            100:['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
             10:['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
              1:['','I','II','III','IV','V','VI','VII','VIII','IX'],
                }

    count = 0
    roman_output = ""
    superscript_roman_output = ""
    for digit in numbers:
        key = 10 ** count
        roman_output = roman_numerals[key][int(digit)] + roman_output
        if count >= 3:
            superscript_roman_output = roman_numerals[('S'+str(key))][int(digit)] + superscript_roman_output
        count += 1

    print(" " * len(str(number)), "  ", end="")
    print(superscript_roman_output)
    
    print(int(number), '= ', end='')
    print(roman_output)

# test cases
number_to_roman("0000")
number_to_roman("2999")
number_to_roman("1973")
number_to_roman("1956")
number_to_roman("2018")
number_to_roman("2000")
number_to_roman("0400")
number_to_roman("0040")
number_to_roman("0004")
# extended test cases
number_to_roman("1111")
number_to_roman("2222")
number_to_roman("3333")
number_to_roman("4444")
number_to_roman("5555")
number_to_roman("6666")
number_to_roman("7777")
number_to_roman("8888")
number_to_roman("9999")
number_to_roman("499999")
number_to_roman("567894")
number_to_roman("3999999")

while True:
    number = input("\nEnter a number (Max 3999999 or [Q]uit): ").lower()
    if number == 'q':
        break
    number_to_roman(number)
