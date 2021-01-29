sum = 0
average = 0
i = 0
with open('data\chicken.txt', 'r', encoding='UTF8') as f:
    for line in f:
        numbers = line.strip().split(": ")
        sum += int(numbers[1])
        i += 1
print(sum / i)