# --CHALLENGE PREFACE--
# Connect over TCP to the following server: 'localhost', 10000
# Initiate communication with 'GET' to retrieve the encrypted messages.
# Then return the messages decrypted to the server,
# taking care to ensure each message is split on to a newline
# 
# --COMMENTS--
# This code works most of the time, I didnt have the ability in the CyberStart interface to check against a dictionary of words as easily. 
# The file it is pulling lines from is an Aladdin story, so I suggest changing the words it checks against and just running it multiple times
# Until the roll of the dice picks sentences with those words. 
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 10000))

s.send(b'GET')
out = s.recv(1024)


def getoffset(input):
	# Try an offset of every possibility from 0 to 25
	for i in range(0, 26):
		output = ""
		# For every character in the provided input
		for j in range(len(input)):
			char = input[j]
			# Move the character along by the offset
			if (ord(char) != 32):
				newChar = chr((ord(char) + i - 65) % 26 + 65)
				output += newChar
			else:
				output += " "
		print("Combination " + str(i) + " = " + output)
		if (output.find("THE") != -1 or output.find(" OF ") != -1) :
			print(i)
			return i


def crack(input, val):
	output = ""
	for j in range(len(input)):
		char = input[j]
		if (ord(char) != 32):
			newChar = chr((ord(char) + int(val) - 65) % 26 + 65)
			output += newChar
		else:
			output += " "
	print(output)
	return output


out = str(out, 'utf-8')
print(out)
list = out.split('\n')

offsets = [0]

separator = '\n'
res = []

for i in range(1, 4):
	offsets.append(getoffset(list[i]))
for i in range(1, 4):
	res.append(crack(list[i], offsets[i]))
result = separator.join(res)

s.send(result.encode('utf-8')) #Sending the results to the socket server
flag = str(s.recv(1024), 'utf-8')
print(flag) 
