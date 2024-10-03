import random
NUM_DIGITS = 3
numbers = list('0123456789')  # Create a list of digits 0 to 9.
random.shuffle(numbers)  # Shuffle them into random order.
print(numbers)

secretNum = ''
for i in range(NUM_DIGITS):
    secretNum += str(numbers[i])
print(secretNum)

nums = [0,1,2,3,4,5,6,7,8,9]
random.shuffle(nums)
print(nums)
sNum = ''
for i in range(NUM_DIGITS):
    sNum += str(nums[i])

print(sNum)