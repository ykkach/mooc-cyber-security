#!/usr/bin/env python3
import sys
import json


def get_vulnerabilities(name, db):
	vulnerabilities = []
	advisories = json.load(db)
	advisory = advisories.get(name)

	vulnerabilities = [(vuln["id"], vuln["v"], vuln["cve"]) for vuln in advisory]
	return vulnerabilities




def main(argv):
	name = sys.argv[1]
	db = open(sys.argv[2])
	vulnerabilities = get_vulnerabilities(name, db)
	for v in vulnerabilities:
		print('%s; %s; %s' % (v[0], v[1], v[2]))


if __name__ == "__main__": 
	if len(sys.argv) != 3:
		print('usage: python %s name db' % sys.argv[0])
	else:
		main(sys.argv)
