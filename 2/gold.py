valid = 0
for line in open('input.txt'):
    line = line.strip()
    numbers = line.split('-')
    letter = line.split()[1][:1]
    string = line.split(':')[1].strip()
    cnt = string.count(letter)

    if (string[int(numbers[0]) - 1] == letter) != (string[int(numbers[1].split()[0]) - 1] == letter):
        valid += 1

print(valid)
