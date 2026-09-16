name = "Sofia"
surname = "Stotska"
group = "IT-31"

print(f"{name} {surname}, {group}")

num_input = int(input("Enter an integer: "))
n = abs(num_input)

if n == 0:
    count = 1
    sum_digits = 0
    max_digit = 0
    min_digit = 0
    reversed_num = 0
else:
    count = 0
    sum_digits = 0
    max_digit = -1
    min_digit = 10
    reversed_num = 0
    
    temp = n
    while temp > 0:
        digit = temp % 10
        count += 1
        sum_digits += digit
        
        if digit > max_digit:
            max_digit = digit
        if digit < min_digit:
            min_digit = digit
            
        reversed_num = reversed_num * 10 + digit
        temp //= 10

print(f"Digits: {count}")
print(f"Sum of digits: {sum_digits}")
print(f"Max digit: {max_digit}, min digit: {min_digit}")
print(f"Reversed: {reversed_num:0{count}d}")