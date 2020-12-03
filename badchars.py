from __future__ import print_function
import config


def run():
	for x in range(0, 256):
		if chr(x) not in config.badchars:
			print("\\x" + "{:02x}".format(x), end='')

	print()

run()

