import socket as s
import time
import ipaddress

def sep(length) :
	print("=" * length)

def ui() :
	sep(26)
	print("Port Scanner".center(26, " "))
	sep(26)

def get_int(msg) :
	while True :
		try :
			return int(input(msg).strip())
			
		except ValueError :
			print("Type a valid value")
	
def get_info() :
	while True :
		ip = input("IP: ").strip()
	
		try :
			ipaddress.IPv4Address(ip)
			break
			
		except ipaddress.AddressValueError :
			print("Invalid IP address")
			sep(26)
			continue
	
	while True :
		
		sep(26)

		start = get_int("Scan starts from: ")
		end = get_int("Scan ends at: ")
	
		if start >= end :
			print("Invalid range!")
			sep(26)
			continue
			
		else :
			sep(26)
			print(f"Scanning ports between {start} and {end}....")
			break
			
	return ip, start, end
					
def main() :
	ip, start, end = get_info()
	
	ports = []
	
	start_time = time.time()
	
	for port in range(start, end + 1) :
		
		sock = s.socket()
		
		try :
			sock.settimeout(0.5)
			res = sock.connect_ex((ip, port))
		
			if res == 0 :
		  	  ports.append(port)

		finally :
			sock.close()

	end_time = time.time()
	
	scan_time = end_time - start_time
	
	return ports, scan_time	


def result() :
	
	ports, scan_time = main()
	
	amount = len(ports)
	
	sep(17)
	print(f"Scan took {scan_time:.1f}s")
	sep(17)
	
	if amount == 0 :
		print("No Ports Found")
		
	elif amount == 1 :
		print("1 Port Found")
		
	else :
		print(f"{amount} Ports Found")

	for p in ports :
		try :
			service = s.getservbyport(p)
		
		except OSError :
			service = "Unknown"
		
		print(f"Port: {p} ({service})")

ui()		
result()
