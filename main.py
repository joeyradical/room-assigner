import sys
import random
import time
import copy
from constants import *

class Person:
	def __init__(self, name, rooms):
		self.name = name
		self.rooms = rooms
		
	def get_name(self):
		return self.name
		
	def get_rooms(self):
		return self.rooms
		
	def add_room(self, room):
		self.rooms.append(room)

def read(db_name):
	people = []
	file = open(db_name, 'r')
	for line in file:
		temp = line.split(';')
		name = temp[0]
		rooms = []
		for room in temp[1:]:
			room2 = int(room)
			rooms.append(room2)
		people.append(Person(name, rooms))
	file.close()
	return people
	
def shuffle(list):
	indexes = []
	new_list = []
	for i in range(0,len(list)):
		indexes.append(i)
		
	for i in range(0, len(list)):
		index = random.choice(indexes)
		indexes.remove(index)
		new_list.append(list[index])
	return new_list
	
def generate_rooms(people):
	busy_rooms = []
	people_tmp = []
	for person in people:
		person_tmp = copy.deepcopy(person)
		rooms = person_tmp.get_rooms()
		room = rooms[-1]
		cnt = 0
		while (room in rooms):
			temp = random.randint(1, len(people))
			if temp not in busy_rooms:
				room = temp
			if cnt > 50:
				cnt = 0
				time.sleep(1)
				return False
			cnt += 1
		busy_rooms.append(room)
		person_tmp.add_room(room)
		people_tmp.append(person_tmp)
	return people_tmp
		
def write(people, path):
	file = open(path, 'w')
	for person in people:
		file.write(person.get_name() + ';')
		rooms = person.get_rooms()
		for room in rooms:
			file.write(str(room))
			if rooms.index(room) != (len(rooms)-1):
				file.write(';')
		file.write('\n')
	file.close()
	
def print_results(people):
	print "GENERATION RESULTS: "
	for person in people:
		print "-------------------------"
		print person.get_name() + ": " + ROOMS_DICT[person.get_rooms()[-1]]
		
			

if __name__ == "__main__":
	if len(sys.argv) == 2:
		people = read(sys.argv[1])
		people_s = shuffle(people)
		result = None
		while not result:
			result = generate_rooms(people_s)
			people_s = shuffle(people)
		write(result, sys.argv[1])
		print_results(result)
		sys.exit(1)
		
	else:
		print "Invalid number of arguments"
		sys.exit(-1)