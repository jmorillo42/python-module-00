import sys

sys.tracebacklimit = 0
if len(sys.argv) == 1:
    sys.exit()
if len(sys.argv) > 2:
    raise AssertionError('more than one argument are provided')
try:
    num = int(sys.argv[1])
except ValueError:
    raise AssertionError('argument is not an integer') from None

if int(sys.argv[1]) == 0:
    print('I\'m Zero.')
elif not int(sys.argv[1]) % 2:
    print('I\'m Even.')
elif int(sys.argv[1]) % 2:
    print('I\'m Odd.')
