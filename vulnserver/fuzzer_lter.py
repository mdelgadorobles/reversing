#!/usr/bin/env python
# Designed for use with boofuzz v0.0.9
from boofuzz import *


def main():
	_host = "192.168.236.153"
	_port = 9999

	session = Session(
		target=Target(
			connection=SocketConnection(_host, _port, proto='tcp')
			),
		)

	s_initialize("Request")

	s_string("LTER", fuzzable = False)
	s_delim(" ", fuzzable = False, name = 'space-1')
	s_string("fuzzme")

	session.connect(s_get("Request"))
	session.fuzz()


if __name__ == "__main__":
    main()
