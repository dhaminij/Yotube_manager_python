file = open("test.py","w")

try:
    file.write('chai aur code')
finally:
    file.close()

with open('youtube.txt','w') as file:
    file.write('chai aur pyrthon')