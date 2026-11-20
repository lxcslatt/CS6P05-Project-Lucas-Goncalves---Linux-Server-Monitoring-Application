log_lines = [
    "Failed password for admin from 203.0.113.5",
    "Accepted password for lucy from 192.0.2.10",
    "Failed password for root from 203.0.113.5",
    "Failed password for root from 198.51.100.7",
    "Failed password for admin from 203.0.113.5",
    "Accepted password for lucy from 192.0.2.10",
]

failed_attempts = {}

def failed_login_counter(line):
	for line in log_lines:
		if "Failed" in line:
			word = line.split()
			ip_add = word[-1]
			if ip_add in failed_attempts:
				failed_attempts[ip_add] += 1
			else:
				failed_attempts[ip_add] = 1

failed_login_counter(log_lines)
for ip, attempts in failed_attempts.items():
	if attempts > 1:
		print(f"IP address : {ip} has entered an incorrect password {attempts} times")
	else:
		print(f"IP address : {ip} has entered an incorrect password {attempts} time")
