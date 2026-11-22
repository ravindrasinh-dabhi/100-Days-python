#You are recording current measurements from an electrical laboratory experiment. Some readings need correction, 
#a new reading arrives, and one measurement is invalid.
#Your job is to create a Python program that manages and analyses these readings using a list.
# readings = [2.1, 2.4, 2.2, 2.8, 2.5]
#Step-by-step requirements
#1. Print the first and last readings.
#2. Update the third reading from 2.2 to 2.3.
#3. Add a new reading of 2.6 to the list.
#4. Remove the invalid reading 2.8.
#5. Print the final list and its length.
#6. Calculate the total of all readings using a for loop.
#7. Calculate the average current.
#8. Count how many readings are greater than 2.4.

readings = [2.1, 2.4, 2.2, 2.8, 2.5]
print(f"first reading = {readings[0]}")
print("last reading = ",readings[-1])
readings[2]=2.3
readings.append(2.6)
readings.remove(2.8)
print(readings)
print(f"Total reading : ",len(readings))

sum=0
for i in readings:
    sum=sum+i

tootal_of_all_reading=sum
print(f"total current = {sum:.2f}")

average_current=tootal_of_all_reading/len(readings)

print(f" average_current = {average_current}")

count=0
for i in readings :
    if i > 2.4 :
        count=count+1


print(f"{count} readings are greater than 2.4 ")