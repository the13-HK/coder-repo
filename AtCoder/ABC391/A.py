D = input()

dict = {
    "N": "S",
    "S": "N",
    "W": "E",
    "E": "W"
}
output = ""
for i in D:
    output += dict[i]

print(output)