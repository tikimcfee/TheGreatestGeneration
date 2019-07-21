# import only system from os 
from os import system, name
from time import sleep

# -------------------------------
# --- ShipOS System State ---
# -------------------------------

# main control switch
system_switch = True

# main system logs. we need to make this better!
system_logs = []
critical_logs = []

def __super_secret(target, log, show):
	target.append(log)
	if show:
		print(log)

def WRITE(log, show = True):
	global system_logs
	__super_secret(system_logs, log, show)

def WRITE_CRIT(log, show = True):
	global critical_logs
	__super_secret(critical_logs, log, show)

def READ():
	global system_logs
	for log in system_logs:
		print(log) 

# -------------------------------
# --- ShipOS System Functions ---
# -------------------------------

def clear():
	system('clear')

def welcome_user():
	# Welcome the user to the system
	WRITE("*****************")
	WRITE("Welcome to ShipOS")
	WRITE("*****************")
	WRITE("")
	WRITE("")

def say_goodbye():
	# Display system-close stats
	WRITE("")
	WRITE("")
	WRITE("**************************")
	WRITE("Thank you for using ShipOS")
	WRITE("**************************")
	WRITE("")
	WRITE("")

	WRITE("-- If you see this shutdown prompt, your life support systems have likely failed. --")
	WRITE("-- Please be advised you have no recorse for action, and are likely 'boned'. --")
	WRITE("-- Have a great day! --")
	WRITE("-- Moving on in sleep(10)! --")
	sleep(10)
	

def display_environment_stats():
	# This will be our ship state object. Very exciting.
	ship_name = "The Good Ship Ship"
	ship_current_occupant_count = 7522
	ship_features = [
		"Transporter",
		"Room for a pony",
		"Sauna",
		"Full complement of weaponry, standard issue",
		"AM/FM Tuner"
	]

def deploy_critical_subsystems():
	print("-!- ...")
	print("-!- Critical Subsystems deployed somehow. Good to go. -!-")
	print("-!- ...")

def stop_system():
	global system_switch
	system_switch = False

def tell_joke():
	print("Humor module not installed. Try again later.")
	sleep(3)
	
def default():
	WRITE("Incorrect operation executed. Shutting down ShipOS and related subsystems.")
	say_goodbye()
	stop_system()

# -- Core system code. Don't munge it up. --

def BOOTUP():
	clear()
	welcome_user()
	sleep(1)
	display_environment_stats()
	sleep(1)
	deploy_critical_subsystems()
	print()

def SHUTDOWN():
	clear()

def SYSTEM_LOOP():

	def handle_command(command):
		if not command:
			print("Stop breaking the function, human.")
			stop_system()
			return

		if command == "stop":
			stop_system()
		elif command == "tell me a joke":
			tell_joke()
		else:
			default()

	while system_switch == True:
		print("... Please enter a command: ", end ="")
		command = input()
		print("\n\n")
		handle_command(command)
		clear()
		READ()

		

# -------------------------------
# -------------------------------
# -------------------------------


# Initial bootup and wait process for generational ship
BOOTUP()
SYSTEM_LOOP()
SHUTDOWN()
