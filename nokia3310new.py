def menu():
	print('''
	--------Welcome to Nokia 3310--------
	
		1 -> Phone Book
		2 -> Message
		3 -> Chat
		4 -> Call Register
		5 -> Tones
		6 -> Settings
		7 -> Call Divert
		8 -> Games
		9 -> Calculator 
		10 -> Remainder
		11 -> Clock
		12 -> Profiles
		13 -> SIM Services
		0 -> Exit the App
	
	''')



def message():
	print(''' 
		----Message Menu----
		
		1 -> Write Message 
		2 -> Inbox
		3 -> Outbox  
		4 -> Picture Messages
		5 -> Templates
		6 -> Smileys
		7 -> Message Settings
		8 -> Info Service
		9 -> Voice Mailbox Number
		10 -> Service Command Editor
		0 -> Back to previous Menu
		
		''')

phonebook = int(input("select an option:"))
match phonebook: 
	case 1:
		menu()
	case 2: 
		message()
	case 3:
		print("Chat")
	case 4:  
		call_register()
	case 5:
		tones()
	case 6:
		settings()
	case 7:
		print("Call Divert")
	case 8:  
		print("Games")
	case 9:
		print("Calculator")
	case 10:
		print("Remainders")
	case 11: 
		clock()
	case 12: 
		print("Profiles")
	case 13: 
		print("SIM Service")
	case 0:  
		exit()
	case _:  
		print("Invalid Input Try Again")
	
def phonebook_menu():
	print('''
		-----Phone Book Menu-----		
		1 -> Search
		2 -> Service Nos
		3 -> Add Name
		4 -> Erase
		5 -> Edit
		6 -> Assign Tone
		7 -> Send b'card
		8 -> Options
		9 -> Speed Dials
		10 -> Voice Tags
		0 -> Back to previous Menu
		
		''')
phone_book_userinput = int(input("Select an option: "))
match phone_book_userinput:
	case 1:
		print("Search")
	case 2:
		print("Service Nos.")
	case 3:
		print("Add Name")
	case 4:
		print("Erase")
	case 5:
		print("Edit")
	case 6:
		print("Assign Tone")
	case 7:
		print("Send b'card")
	case 8:
		options()
	case 9: 
		print("Speed Dials")
	case 10:
		print("Voice Tags")
	case 0:
		menu()
	case _:
		print("Invalid Input Try Again")

message_userinput = int(input("Select an option: "))
match message_userinput:
	case 1: 
		print("Write a Message")
	case 2:
		print("Inbox")
	case 3:
		print("Outbox")
	case 4:
		print("Picture Messages")
	case 5: 
		print("Templates")
	case 6:
		print("Smileys")
	case 7:
		message_settings()
	case 8: 
		print("Info Service")
	case 9:
		print("Voice Mailbox Number")
	case 10:
		print("Service Command Editor")
	case 0: 
		menu()
	case _:
		print("Invalid Input Try Again")

def call_register():
	print(''' 
		 ----Call Register Menu----
		
		1 -> Missed Calls
		2 -> Received Calls
		3 -> Dialled Numbers  
		4 -> Erase Recent Call Lists
		5 -> Show Call Duration
		6 -> Show Call Cost
		7 -> Call Cost Settings
		8 -> Prepaid Credit
		9 -> Back to Previous Menu
		 
		''')
call_register_userinput = int(input("Select an option: "))
match call_register_userinput:
	case 1:
		print("Missed Calls")
	case 2: 
		print("Received Calls")
	case 3:
		print("Dialled Numbers")
	case 4: 
		print("Erase Recent Call Lists")
	case 5: 
		show_call_duration()
	case 6: 
		show_call_cost()
	case 7:
		call_cost_settings()
	case 8:
		print("Prepaid Credit")
	case 9:
		menu()
	case _:
		print("Invalid Input Try Again")


def tones():
	print(''' 
		----Tones Menu----
		
		1 -> Ringing Tone
		2 -> Ringing Volume
		3 -> Incoming Call Alert  
		4 -> Composer
		5 -> Message Alert Tone
		6 -> Keypad Tones
		7 -> Warning And Game Tones
		8 -> Vibrating Alert
		9 -> Screen Saver
		10 -> Back to Previous Menu
		
		''')
	tones_userinput = int(input("Select an option: "))
	match tones_userinput:
	case 1:
		print("Ringing Tone")
	case 2: 
		print("Ringing Volume")
	case 3:
		print("Incoming Call Alert ")
	case 4: 
		print("Composer")
	case 5: 
		print("Message Alert Tone")
	case 6:
		print("Keypad Tones")
	case 7:
		print("Warning And Game Tones")
	case 8: 
		print("Vibrating Alert")
	case 9:
		print("Screen Saver")
	case 10:
		menu()
	case _:
		print("Invalid Input Try Again")


def settings():
	print(''' 
		----Settings Menu----
		
		1 -> Call Settings
		2 -> Phone Settings
		3 -> Security Settings  
		4 -> Restore Factory Settings
		5 -> Back to Previous Menu
		 
		''')
	settings_userinput = int(input("Select an option: "))
	match settings_userinput:
	case 1:
		call_settings()
	case 2:
		phone_settings()
	case 3:
		security_settings()
	case 4:
		print("Restore Factory Settings")
	case 5: 
		menu()
	case _:
		print("Invalid Input Try Again")

def clock():
	print(''' 
		----Clock Menu----
		
		1 -> Alarm Clock
		2 -> Clock Settings
		3 -> Date Setting 
		4 -> Stopwatch
		5 -> Countdown Timer
		6 -> Auto Update Of Time And Date
		7 -> Back to Previous Menu
		 
		''')
	clock_userinput = int(input("Select an option: "))
	match clock_userinput:
	case 1:
		print("Alarm Clock")
	case 2:
		print("Clock Settings")
	case 3:
		print("Date Setting")
	case 4: 
		print("Stopwatch")
	case 5:
		print("Countdown Timer")
	case 6: 
		print("Auto Update Of Time And Date")
	case 7: 
		menu()
	case _: 
		print("Invalid Input Try Again")

def options():
	print(''' 
		Welcome to the Options Menu!
		-----------------------------------
		1 >>> Type of View
		2 >>> Memory Status
		3 >>> Back to Previous Menu
		4 >>> Back to Main Menu
		----------------------------------- 
		''')
	options_userinput = int(input("Enter from number 1 to 4: "))
	match options_userinput:
	case 1: 
		print("Type of View")
	case 2:
		print("Memory Status")
	case 3:
		phone_book_menu()
	case 4:
		menu()
	case _:
		print("Invalid Input Try Again")



def message_settings():
	print(''' 
		Welcome to the Message Settings Menu!
		-------------------------------------
		1 >>> Set 1
		2 >>> Common
		3 >>> Back to Previous Menu
		-------------------------------------
		''')
	message_settings_userinput = int(input("Enter from number 1 to 3: "))
	match message_settings_userinput:
	case 1:
		set1()
	case 2: 
		common()
	case 3:
		message()
	case _:
		print("Invalid Input Try Again")


def set1():
	print(''' 
		Welcome to the Set 1 Menu!
		-------------------------------------
		1 >>> Message Centre Number
		2 >>> Message Sent As
		3 >>> Message Validity
		4 >>> Back to Previous Menu
		-------------------------------------
		''')
	set1_userinput = int(input("Enter from number 1 to 4: "))
	match set1_userinput:
	case 1:
		print("Message Centre Number")
	case 2:
		print("Message Sent As")
	case 3:
		print("Message Validity")
	case 4: 
		message_settings()
	case _: 
		print("Invalid Input Try Again")

def common():
	print(''' 
		Welcome to the Common Menu!
		-------------------------------------
		1 >>> Delivery Reports
		2 >>> Reply Via Same Centre
		3 >>> Character Support
		4 >>> Back to Previous Menu
		-------------------------------------
		''')
	common_userinput = int(input("Enter from number 1 to 4: "))
	match common_userinput:
		case 1: print("Delivery Reports")
		case 2: print("Reply Via Same Centre")
		case 3: print("Character Support")
		case 4: message_settings()
		case _: print("Invalid Input Try Again")



def show_call_duration():
	print(''' 
		Welcome to the Show Call Duration Menu!
		-------------------------------------
		1 >>> Last Call Duration
		2 >>> All Calls' Duration
		3 >>> Received Calls' Duration
		4 >>> Dialled Calls' Duration
		5 >>> Clear Timers
		6 >>> Back to Previous Menu
		-------------------------------------
		''')
	show_call_duration_userinput = int(input("Enter from number 1 to 4: "))
	match show_call_duration_userinput:
	case 1: 
		print("Last Call Duration")
	case 2:
		print("All Calls' Duration")
	case 3:
		print("Received Calls' Duration")
	case 4: 
		print("Dialled Calls' Duration")
	case 5:
		print("Clear Timers")
	case 6: 
		call_register()
	case _:
		print("Invalid Input Try Again")

		
def show_call_cost():
	print(''' 
		Welcome to the Show Call Cost Menu!
		-------------------------------------
		1 >>> Last Call Cost
		2 >>> All Calls' Cost
		3 >>> Clear Counters
		4 >>> Back to Previous Menu
		-------------------------------------
		''')
	show_call_cost_userinput = int(input("Enter from number 1 to 4: "))
	match show_call_cost_userinput:
	case 1:
		print("Last Call Cost")
	case 2:
		print("All Calls' Cost")
	case 3: 
		print("Clear Counters")
	case 4:
		call_register()
	case _:
		print("Invalid Input Try Again")


def call_cost_settings():
	print(''' 
		Welcome to the Call Cost Settings Menu!
		-------------------------------------
		1 >>> Call Cost Limit
		2 >>> Show Costs In
		3 >>> Back to Previous Menu
		-------------------------------------
		''')
call_cost_settings_userinput = int(input("Enter from number 1 to 3: "))
match call_cost_settings_userinput:
	case 1: 
		print("Call Cost Limit")
	case 2:
		print("Show Costs In")
	case 3: 
		call_register()
	case _:
		print("Invalid Input Try Again")



def call_settings():
	print(''' 
		Welcome to the Call Settings Menu!
		-----------------------------------
		1 >>> Automatic Redial
		2 >>> Speed Dialling
		3 >>> Call Waiting Options  
		4 >>> Own Number Sending
		5 >>> Phone Line In Use
		6 >>> Automatic Answer
		7 >>> Back to Previous Menu
		----------------------------------- 
		''')
	call_settings_userinput = int(input("Enter from number 1 to 7: "))
	match call_settings_userinput:
	case 1:
		print("Automatic Redial")
	case 2: 
		print("Speed Dialling")
	case 3:
		print("Call Waiting Options")
	case 4:
		print("Own Number Sending")
	case 5:
		print("Phone Line In Use")
	case 6:
		print("Automatic Answer")
	case 7:
		settings()
	case _: 
		print("Invalid Input Try Again")



def phone_settings():
	print(''' 
		Welcome to the Phone Settings Menu!
		-----------------------------------
		1 >>> Language
		2 >>> Cell Info Display
		3 >>> Welcome Note 
		4 >>> Network Selection
		5 >>> Lights
		6 >>> Confirm SIM Service Actions
		7 >>> Back to Previous Menu
		----------------------------------- 
		''')
	phone_settings_userinput = int(input("Enter from number 1 to 7: "))
	match phone_settings_userinput:
	case 1:
		print("Language")
	case 2:
		print("Cell Info Display")
	case 3:
		print("Welcome Note ")
	case 4: 
		print("Network Selection")
	case 5:
		print("Lights")
	case 6: 
		print("Confirm SIM Service Actions")
	case 7: 
		settings()
	case _: 
		print("Invalid Input Try Again")



def security_settings():
	print(''' 
		Welcome to the Security Settings Menu!
		-----------------------------------
		1 >>> PIN Code Requests
		2 >>> Call Barring Service
		3 >>> Fixed Dialling
		4 >>> Closed User Group
		5 >>> Phone Security
		6 >>> Change Access Codes
		7 >>> Back to Previous Menu
		----------------------------------- 
		''')
	security_settings_userinput = int(input("Enter from number 1 to 7: "))
	match security_settings_userinput:
	case 1: 
		print("PIN Code Requests")
	case 2:
		print("Call Barring Service")
	case 3:
		print("Fixed Dialling")
	case 4:
		print("Closed User Group")
	case 5: 
		print("Phone Security")
	case 6: 
		print("Change Access Codes")
	case 7:
		settings()
	case _: 
		print("Invalid Input Try Again")


def exit():
	print(''' 
		Exiting the App...
	+++++++++++++++++++++++++++++++++++

	Thank you for choosing Nokia 3310

	''')



menu()
