def year_to_roman(year):

    year = int(year)
    year_roman = ""
    year_thousands = year // 10**3 % 10
    year_hundreds = year // 10**2 % 10
    year_tens = year // 10**1 % 10
    year_ones = year // 10**0 % 10

    # year input check
    if year > 9999 or year < 0:
        print("Invalid entry. Please enter a year between 0-9999:")
        return
    
    # add thousands
    if year_thousands == 9: year_roman = year_roman + "_I_X"
    elif year_thousands == 4: year_roman = year_roman + "_I_V"
    elif year_thousands < 4: year_roman = year_roman + ("M"*year_thousands)
    else: year_roman = year_roman + "_V" + ("M"*(year_thousands-5))
    # add hundreds
    if year_hundreds == 9: year_roman = year_roman + "CM"
    elif year_hundreds == 4: year_roman = year_roman + "CD"
    elif year_hundreds < 4: year_roman = year_roman + ("D"*year_hundreds)
    else: year_roman = year_roman + "D" + ("C"*(year_hundreds-5))
    # add tens
    if year_tens == 9: year_roman = year_roman + "XC"
    elif year_tens == 4: year_roman = year_roman + "XL"
    elif year_tens < 4:  year_roman = year_roman + ("X"*year_tens)
    else: year_roman = year_roman + "L" + ("X"*(year_tens-5))
    # add ones
    if year_ones == 9: year_roman = year_roman + "IX"
    elif year_ones == 4: year_roman = year_roman + "IV"
    elif year_ones < 4: year_roman = year_roman + ("I"*year_ones)
    else: year_roman = year_roman + "V" + ("I"*(year_ones-5))

    print(str(year_thousands)+str(year_hundreds)+str(year_tens)+str(year_ones), "=", year_roman)

# test cases
year_to_roman("0000")
year_to_roman("2999")
year_to_roman("1973")
year_to_roman("1956")
year_to_roman("2018")
year_to_roman("2000")
year_to_roman("0400")
year_to_roman("0040")
year_to_roman("0004")
# extended test cases
year_to_roman("1111")
year_to_roman("2222")
year_to_roman("3333")
year_to_roman("4444")
year_to_roman("5555")
year_to_roman("6666")
year_to_roman("7777")
year_to_roman("8888")
year_to_roman("9999")

while True:
    year_to_roman(input("Enter a 4 digit year (Max 9999): "))
