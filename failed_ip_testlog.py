#This is my first prototype of a failed ip login counter.
#log_lines is representing data that would in a live environment be pulled from a file stored on the linux server.
#The code below demonstrates the logic of checking if a ip address is incorrect and if its possible that might malicious intent

log_lines = [
    "Failed password for admin from 203.0.113.5",
    "Accepted password for lucy from 192.0.2.10",
    "Failed password for root from 203.0.113.5",
    "Failed password for root from 198.51.100.7",
    "Failed password for admin from 203.0.113.5",
    "Accepted password for lucy from 192.0.2.10",
]


#This function checks for a word equating to failure and then stores the ip and the amount of times in failed_attempts
def failed_login_counter(lines):
	failed_attempts = {}
	for line in lines:
		if "Failed" in line:
			word = line.split()
			ip_add = word[-1]
			if ip_add in failed_attempts:
				failed_attempts[ip_add] += 1
			else:
				failed_attempts[ip_add] = 1
	return failed_attempts
		
#The amount we define is a potential risk to our network
THRESHOLD = 3 
#This variable holds the result of log_lines going through the logic of our function above
failed_attempts = failed_login_counter(log_lines)

#This prints out the function response and formats in a readable and formal style. 
for ip, attempts in failed_attempts.items():
	if attempts > 1:
		print(f"IP address :{ip} has entered an incorrect password {attempts} times")
	else:
		print(f"IP address :{ip} has entered an incorrect password {attempts} time")
	if attempts >= THRESHOLD:
		print(f"WARNING: {ip} reached {THRESHOLD} or more failed logins")

