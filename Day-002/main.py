#You have recorded 10 voltage measurements during an electrical laboratory experiment.
#Your task is to analyse the measurements using Python indexing and slicing.
#voltage = [218, 220, 222, 225, 228, 230, 233, 235, 238, 240]
voltage = [218, 220, 222, 225, 228, 230, 233, 235, 238, 240]
# Print the first five voltage readings.
print(f"first five voltage reading : {voltage[0:5]}")


#Print the last three voltage readings.
print("Last three voltage reading : ", voltage[-3:])

#Extract readings from index 2 to index 6.
print(f"reading from index given range : {voltage[2:7]}")

#Print every alternate voltage reading.
print(voltage[::2])

# Reverse the complete list using slicing.
print(voltage[::-1])

#Print the third and second-last readings using negative and positive indexing.
print(voltage[2], voltage[-2])

#Extract the middle four readings.
print(f"middle four readings : {voltage[3:7]}")