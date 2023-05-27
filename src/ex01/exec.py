import sys


if len(sys.argv) > 1:
	print(' '.join(map(str.swapcase, sys.argv[1:]))[::-1])
