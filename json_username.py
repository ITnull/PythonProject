import json
filename="username.json"
try:
    with open(filename,'r') as f_obj:
        username=json.load(f_obj)
except:
    username=input('what is your name?')
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("we will remeber you when you come back,"+username + "!")
else:
    print("welcome back,"+username+"!")
