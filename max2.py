numbers = [3,4,5,6,7]
largest = max(numbers)
for i in range(0,len(numbers)):
    if(largest==numbers[i]):
        numbers.pop(i)
largest2= max(numbers)
print("Second largest no.",largest2)
