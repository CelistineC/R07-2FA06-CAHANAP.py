scores = [85, 90, 78, 92, 88]

def show():
    print("\nScores:", scores)

def search():
    n = int(input("Search score: "))
    print("Found!" if n in scores else "Not found.")

def average():
    print("Average:", sum(scores) / len(scores))

def update():
    i = int(input("Index (0-4): "))
    scores[i] = int(input("New score: "))
    print("Updated!")

while True:
    print("\n=== Student Score Analyzer ===")
    print("1.Display  2.Search  3.Average  4.Update  5.Display Updated  6.Exit")
    c = input("Choice: ")
    if c == "1" or c == "5": show()
    elif c == "2": search()
    elif c == "3": average()
    elif c == "4": update()
    elif c == "6": break
    else: print("Invalid choice.")
print("Thank you! Program ended.")