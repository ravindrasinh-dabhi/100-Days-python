# Problem Statement:
# You are managing an electrical maintenance department's
# equipment inventory. Your task is to organize equipment IDs,
# remove unavailable equipment, identify duplicates and sort
# the inventory using Python list methods.

# Initial Data:
# equipment = [105, 102, 108, 102, 110, 104, 108]
#
# Tasks:
# 1. Add equipment ID 112 at the end using append().
# 2. Insert equipment ID 101 at index 0 using insert().
# 3. Remove the equipment at index 3 using pop().
# 4. Remove the first occurrence of equipment ID 108
#    using remove().
# 5. Sort all equipment IDs in ascending order using sort().
# 6. Count how many times equipment ID 102 appears
#    using count().
# 7. Find the index of equipment ID 110 using index().
# 8. Reverse the sorted inventory using reverse().
# Requirements:
# - Use all eight list methods.
# - Print the inventory after each major modification.
# - Do not manually create the expected output.
# - Generate all results using Python operations.

equipment = [105, 102, 108, 102, 110, 104, 108]
print(f"in starting inventory : {equipment}")
equipment.append(112)
print(f"After appending 112  : {equipment}")
equipment.insert(0,101)
print(f"added 101 at index 0 : {equipment}")
equipment.pop(3)
print(f"after removing equipment at index 3 : {equipment}")
equipment.remove(108)
print(equipment)
equipment.sort()
print(equipment)
print(equipment.count(102))
print(equipment.index(110))
equipment.reverse()
print(equipment)

