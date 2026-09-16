name = "Sofia"
surname = "Stotska"
group = "IT-31"
d = 14
c = len (surname)
print (f"{name} {surname}, {group}")

numbers = []
count_for = 0
sum_for = 0
product_for = 1
even_for = 0
odd_for = 0

for num in range(d, 32):
    numbers.append(str(num))
    count_for += 1
    sum_for += num
    product_for *= num

    if num %2 == 0:
        even_for += 1
    else:
        odd_for +=1
    avg_for = sum_for / count_for
print(f"Numbers from {d} to 31: {' '.join(numbers)}")
print (f"Count: {count_for}")
print (f"Sum: {sum_for}")
print (f"Product: {product_for}")
print (f"Average: {avg_for:.2f}")
print (f"Even: {even_for}, odd: {odd_for}")

num = d
count_w = 0
sum_w = 0
product_w = 1
even_w = 0
odd_w = 0

while num <= 31:
    count_w += 1
    sum_w += num
    product_w *= num
    if num % 2 == 0:
        even_w += 1
    else:
        odd_w += 1
    num += 1

avg_w = sum_w / count_w

countdown_nums = []
for i in range(c, 0, -1):
    countdown_nums.append(str(i))

print(f"Countdown: {' '.join(countdown_nums)}")    


