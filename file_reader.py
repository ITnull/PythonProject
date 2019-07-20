file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    for textline in file_object:
        print(textline.rstrip())
