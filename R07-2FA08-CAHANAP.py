items = ["Notebook", "Pen", "Calculator", "Laptop", "Book"]
print("Original:", items)

i = int(input("Index to Update: "))
new = input("New Value: ")

s = input("Slice Range (start:end): ")
a, b = map(int, s.split(":"))
sliced = items[a:b]
print(f"Sliced ({a}:{b}):", sliced)

search = input("Search Item: ")
print("Found in sliced list!" if search in sliced else "Not found in sliced list.")

items[i] = new
print("Updated:", items)
