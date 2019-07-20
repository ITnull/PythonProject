file_name='txt_analysis.txt'
try:
    with open(file_name) as file_object:
        contents=file_object.read()
except FileNotFoundError:
    print ('file not found')
words=contents.split()
print(words)
print (len(words))
