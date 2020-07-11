# GROUP-1 LAB-4

def format(num):
    
    output_number = ""
    digit_tracker = 0
    number_length = len(str(num))
    
    for i in range(number_length): 
        digit = num // 10**i % 10
        output_number = str(digit) + output_number
        digit_tracker = digit_tracker + 1

        if digit_tracker == 3 and number_length > 3:
            if i+1 != number_length: 
                output_number = ',' + output_number
                digit_tracker = 0
                
    print(output_number)


format(1)
format(12)
format(123)
format(1234)
format(12345)
format(123456)
format(1234567)
format(12345678)
format(123456789)
format(1234567890)
format(12345678901)
format(123456789012)
format(1234567890123)
format(12345678901234)
format(123456789012345)
format(1234567890123456)
