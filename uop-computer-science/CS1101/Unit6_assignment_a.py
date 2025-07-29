# Lists of 10 employees name
originalList = ["Sarah Kim", "Michael Johnson", "Priya Patel",
                "James Wilson", "Maria Garcia", "David Lee",
                "Emma Thompson", "Carlos Rodriguez", "Lisa Chen", "Ahmed Hassan"]

# Divide a list into two equal sublists of 5 names each.
subList1 = originalList[:5];
subList2 = originalList[5:];
print("Original SubList1:", subList1)
print("Original SubList2:", subList2)

# Add “Kriti Brown” in subList2.
subList2.append("Kriti Brown");
print("Updated SubList2:", subList2)

# Remove the second employee's name from subList1.
subList1.pop(1)
print("Updated SubList1:", subList1)

# Merge both the lists.
subList1.extend(subList2)
print("Merged List:", subList1)

# Give a rise of 4% to every employee and update the salaryList.
salaryList = [45000, 52000, 38000, 75000, 42000, 68000, 55000, 47000, 81000, 59000]
print("Original Salary List:", salaryList)

for i in range(len(salaryList)):
    salaryList[i] = int(salaryList[i] * 1.04)  # Increase each salary by 4%

print("Updated Salary List:", salaryList)
print(type(salaryList[0]))  # <class 'float'>

# Sort the salaryList in descending order and print the top 3 salaries.
salaryList.sort(reverse=True)  # Sort in descending order (highest first)
print("Top 3 Salaries:", salaryList[:3])
print("Sorted Salary List:", salaryList)