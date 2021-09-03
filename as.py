import requests
import json
import datetime
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.OKBLUE}{bcolors.BOLD}")
t= datetime.datetime.now()
url = 'https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getUserInfobyNickname'
myobj = {'nickname':"circle"}




#use the 'headers' parameter to set the HTTP headers:
x = requests.post(url, data = myobj, headers = {"x-api-key": "1985106ddeaaccfc3a1bf1976c7cff70","x-app-key":"000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"})

#convert response to json format

#parse the json to get the service ticket
response= x.text
#the 'demopage.asp' prints all HTTP Headers
#8801147116455

json_object = json.loads(response)

json_formatted_str = json.dumps(json_object, indent=1)

# print(json_formatted_str)
# print(json_object)

# Input the key value that you want to search
keyVal = "data"

# load the json data
customer = json.loads(response)
# Search the key value using 'in' operator
i=0;
print("Auto Shout Blast")
name = input("Enter lkey: ")
#name2 = input("Enter nickname: ")
message = input("Enter Message: ")
if keyVal in customer:
    while 1:
        url2 = 'https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&action=kast'
        myobj0 = {'message':message}
        myobj1 = {'message':message}
        myobj2 = {'message':message}
        myobj3 = {'message':message}
        myobj4 = {'message':message}
        myobj5 = {'message':message}
        myobj6 = {'message':message}
        myobj7 = {'message':message}
        myobj8 = {'message':message}
        myobj9 = {'message':message}
        try:
            requests.post(url2, data = myobj0, headers = {"x-api-key": name,"x-app-key":"000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"})
            print("SMS to ",i)
            i=i+1
        except:
            print(f"{bcolors.FAIL}{bcolors.BOLD}")
            print("Server Error")
        try:
            requests.post(url2, data = myobj1, headers = {"x-api-key": name,"x-app-key":"000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"})
            print("SMS to ",i)
            i=i+1
        except:
            print(f"{bcolors.FAIL}{bcolors.BOLD}")
            print("Server Error")
        try:
            requests.post(url2, data = myobj2, headers = {"x-api-key": name,"x-app-key":"000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"})
            print("SMS to ",i)
            i=i+1
        except:
            print(f"{bcolors.FAIL}{bcolors.BOLD}")
            print("Server Error")
        try:
            requests.post(url2, data = myobj3, headers = {"x-api-key": name,"x-app-key":"000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"})
            print("SMS to ",i)
            i=i+1
        except:
            print(f"{bcolors.FAIL}{bcolors.BOLD}")
            print("Server Error")
        try:
            requests.post(url2, data = myobj4, headers = {"x-api-key": name,"x-app-key":"000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"})
            print("SMS to ",i)
            i=i+1
        except:
            print(f"{bcolors.FAIL}{bcolors.BOLD}")
            print("Server Error")
        try:
            requests.post(url2, data = myobj5, headers = {"x-api-key": name,"x-app-key":"000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"})
            print("SMS to ",i)
            i=i+1
        except:
            print(f"{bcolors.FAIL}{bcolors.BOLD}")
            print("Server Error")
        try:
            requests.post(url2, data = myobj6, headers = {"x-api-key": name,"x-app-key":"000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"})
            print("SMS to ",i)
            i=i+1
        except:
            print(f"{bcolors.FAIL}{bcolors.BOLD}")
            print("Server Error")
        try:
            requests.post(url2, data = myobj7, headers = {"x-api-key": name,"x-app-key":"000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"})
            print("SMS to ",i)
            i=i+1
        except:
            print(f"{bcolors.FAIL}{bcolors.BOLD}")
            print("Server Error")
        try:
            requests.post(url2, data = myobj8, headers = {"x-api-key": name,"x-app-key":"000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"})
            print("SMS to ",i)
            i=i+1
        except:
            print(f"{bcolors.FAIL}{bcolors.BOLD}")
            print("Server Error")
        try:
            requests.post(url2, data = myobj9, headers = {"x-api-key": name,"x-app-key":"000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"})
            print("SMS to ",i)
            i=i+1
        except:
            print(f"{bcolors.FAIL}{bcolors.BOLD}")
            print("Server Error")
else:
    # Print the message if the value does not exist
    print("SerVer Down!!!!")
