#Fairus De La Cruz, Writng to text notes
import csv
"""
r = to read the file
w = write on the file
(replaces the old file)
W+ = read and write
a = append (adds tp the files doesn't delete them)
x = create the file
a+ = append and read the file
"""
#with open("Example file", "a") as file:
    #file.write("I am here for ever")
    #print(file.read())

data= [
    {"username": "someone", "color": "blue"},
    {"username": "username", "color": "yellow"},
    {"username": "rainbow", "color": "red"},
    {"username": "you", "color": "brown"},
    {"username": "yuareyu", "color": "black"},
    {"username": "missisippi", "color": "white"},
    {"username": "someone_1", "color": "pink"},
]
with open("Notes/Class CSV sample - Sheet1.csv", "a", newline= "") as file:
    fieldnames = ["username", "color"]
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow(data)
    
with open("Notes\Class CSV sample - Sheet1.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"user name: {row[0]} color: {row[1]}")