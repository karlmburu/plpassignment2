listnum = input("Enter a list of numbers separated by commas: ")
numbers = listnum.split(",")  #split the input string into a list
numbers = [int(num) for num in numbers] #convert each string in the list to an integer
sum_numbers = sum(numbers)
print(sum_numbers)