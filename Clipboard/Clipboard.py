import sys
import clipboard
import json

MyFile = "new.json"
def save_items(filepath,data):
    with open(filepath, "w") as f:
        json.dump(data,f)
def load_items(filepath):
    try:
        with open(filepath,"r") as r:
            data=json.load(r)
            return data
    except:
        return {}


if len(sys.argv)==2:
    command = sys.argv[1]
    data = load_items(MyFile) #This is important because we will overwrite the json file, this will collect all the previous
                              #Json data and store it in data variable to which we will append the new Key:data values
    if command =="save":
        key = input("Enter a key to store the data corresponding to : \n")
        data[key] = clipboard.paste()
        save_items(MyFile,data)
        print("Thank you for saving your data with us \n")

    elif command =="load":
        key = input("Enter the key you want the value for\n")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("Data does not exist")

    elif command == "list":
        print(data)
    else:
        print("Unknown Command")

