numbers = [int(input()) for i in range(3)]
if numbers[1] - numbers[0] > numbers[2] - numbers[1]:
      position = 2
elif numbers[1] - numbers[0] < numbers[2] - numbers[1]:
      position = 3
else:
      position = 4

if position == 2:
      print(numbers[0] + (numbers[2] - numbers[1]))
      print(position)
elif position == 3:
      print(numbers[2] - (numbers[1] - numbers[0]))
      print(position)
else:
      print(numbers[2] + (numbers[2] - numbers[1]))
      print(position)