import os
import requests
import random

def create_emotions_dict(sheet_id, sheet_api_key):

	sheet_url = "https://sheets.googleapis.com/v4/spreadsheets/"+sheet_id+"/values/A:D?key="+sheet_api_key+"&majorDimension=columns"
	response = requests.get(sheet_url).json()
	emotions_dict = dict()

	for emotion_list in response["values"]:
		emotions_dict[emotion_list[0]] = emotion_list[1:]

	return emotions_dict

def get_wit(user_input, auth_key):

	encoded_input = requests.utils.quote(user_input, safe='')

	headers =  {"Authorization": "Bearer "+os.getenv("AUTH_KEY")}
	wit_url = "https://api.wit.ai/message?v=20200421&q="+encoded_input

	response = requests.get(wit_url, headers=headers)

	return response

# get responses
emotions_dict = create_emotions_dict(sheet_id=os.getenv("SHEET_ID"), sheet_api_key=os.getenv("SHEET_API_KEY"))

print("My name is superbot! Talk to me:)")
print()

while True:
	user_input = input("User: ")
	response = get_wit(user_input, os.getenv("AUTH_KEY")).json()

	# define goodbye
	if response["entities"].get("bye") is not None and response["entities"]["bye"][0]["confidence"] > 0.9:
		print("Goodbye!")
		break

	elif response["entities"].get("greetings") is not None and response["entities"]["greetings"][0]["confidence"] > 0.9:
		print("Hello there!")
			
	
	# define emotion response
	elif response["entities"].get("intent") is not None:
		intent = response["entities"]["intent"][0]["value"]
		print(random.choice(emotions_dict[intent]))
	
	else:
		print(random.choice(emotions_dict["not_recognized"]))
			
