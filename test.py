import sys
from main import *

if len(sys.argv) != 2:
	print "Invalid amount of arguments"
	sys.exit(-1)

try:
	people = read(sys.argv[1])
	
except IOError:
	print "File failed to open"
	sys.exit(-1)
	
# Check if person has duplicate rooms	
for person in people:
	rooms = person.get_rooms()
	for i in range(1, len(rooms)):
		if rooms.count(i) > 1:
			print person.get_name() + " has the same room twice."
	
# Check if several people are staying in the same room at once	
for i in range(1, len(rooms)):
	test = []
	for person in people:
		test.append(person.get_rooms()[i])
	for i in test:
		if test.count(i) > 1:
			print "Several people are staying in the same room at once"

			