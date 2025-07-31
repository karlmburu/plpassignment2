set1_input = input("Enter integers for the first set,separated by commas: ")
set1 = set(int(x) for x in set1_input.split(","))

set2_input = input("Enter integers for the second set, separated by commas: ")
set2 = set(int(x) for x in set2_input.split(","))

common_elements = set1.intersection(set2)

print("\nFirst set:", set1)
print("Second set:", set2)
print("Common elements:", common_elements)
