import time
import socket
import sys
import config

def run():
	buffer = getfuzz(config.fuzzer_start, config.fuzzer_step, config.fuzzer_iterations)
	runfuzz(config.target_ip, config.target_port, config.timeout, config.prefix, buffer)


def runfuzz(ip, port, timeout, prefix, buffer):
	for string in buffer:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(timeout)
			s.connect((ip, port))
			print("Fuzzing with %s bytes" % len(string))
			s.send(prefix + string + "\r\n")
			s.recv(1024)
			s.close()
		except:
			print("Could not connect to " + ip + ":" + str(port))
			sys.exit(0)

		time.sleep(1)
	

def getfuzz(counter, step, iterations):
	buffer = []
	while len(buffer) < iterations:
		buffer.append("A" * counter)
		counter += step

	return buffer


run()