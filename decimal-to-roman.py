def number_to_roman(number):

    number = int(number)
    number_roman = ""
    number_millions = number // 10**6 % 10
    number_hundred_thousands = number // 10**5 % 10
    number_ten_thousands = number // 10**4 % 10
    number_thousands = number // 10**3 % 10
    number_hundreds = number // 10**2 % 10
    number_tens = number // 10**1 % 10
    number_ones = number // 10**0 % 10

    # number input check
    if number > 3999999 or number < 0:
        print("Invalid entry. Please enter a number between 0-3999999:")
        return

    # format superscript spacing
    output_decimal_number = int(str(number_millions)+str(number_hundred_thousands)+
                              str(number_ten_thousands)+str(number_thousands)+
                              str(number_hundreds)+str(number_tens)+str(number_ones))
    print(" " * len(str(output_decimal_number)), "  ", end="")
    
    # add millions
    number_roman = number_roman + ("M"*number_millions) ; number_roman_superscript(number_millions)
    # add hundred_thousands
    if number_hundred_thousands == 9: number_roman = number_roman + "CM" ; number_roman_superscript(2)
    elif number_hundred_thousands == 4: number_roman = number_roman + "CD" ; number_roman_superscript(2)
    elif number_hundred_thousands < 4: number_roman = number_roman + ("C"*number_hundred_thousands) ; number_roman_superscript(number_hundred_thousands)
    else: number_roman = number_roman + "D" + ("C"*(number_hundred_thousands-5)) ; number_roman_superscript(1) ; number_roman_superscript(number_hundred_thousands-5)
    # add ten_thousands
    if number_ten_thousands == 9: number_roman = number_roman + "XC" ; number_roman_superscript(2)
    elif number_ten_thousands == 4: number_roman = number_roman + "XL" ; number_roman_superscript(2)
    elif number_ten_thousands < 4: number_roman = number_roman + ("X"*number_ten_thousands) ; number_roman_superscript(number_ten_thousands)
    else: number_roman = number_roman + "L" + ("X"*(number_ten_thousands-5)) ; number_roman_superscript(1) ; number_roman_superscript(number_ten_thousands-5)
    # add thousands
    if number_thousands == 9: number_roman = number_roman + "IX" ; number_roman_superscript(2)
    elif number_thousands == 4: number_roman = number_roman + "IV" ; number_roman_superscript(2)
    elif number_thousands < 4: number_roman = number_roman + ("M"*number_thousands)
    else: number_roman = number_roman + "V" + ("M"*(number_thousands-5)) ; number_roman_superscript(1)
    # add hundreds
    if number_hundreds == 9: number_roman = number_roman + "CM"
    elif number_hundreds == 4: number_roman = number_roman + "CD"
    elif number_hundreds < 4: number_roman = number_roman + ("D"*number_hundreds)
    else: number_roman = number_roman + "D" + ("C"*(number_hundreds-5))
    # add tens
    if number_tens == 9: number_roman = number_roman + "XC"
    elif number_tens == 4: number_roman = number_roman + "XL"
    elif number_tens < 4:  number_roman = number_roman + ("X"*number_tens)
    else: number_roman = number_roman + "L" + ("X"*(number_tens-5))
    # add ones
    if number_ones == 9: number_roman = number_roman + "IX"
    elif number_ones == 4: number_roman = number_roman + "IV"
    elif number_ones < 4: number_roman = number_roman + ("I"*number_ones)
    else: number_roman = number_roman + "V" + ("I"*(number_ones-5))


    print()
    print(output_decimal_number, "=", number_roman)

def number_roman_superscript(x):
    print("_"*x, end="")

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
number_to_roman("49999")
number_to_roman("499999")
number_to_roman("669999")
number_to_roman("3999999")

while True:
    number_to_roman(input("\nEnter a number (Max 3999999): "))
