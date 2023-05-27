import sys

sys.tracebacklimit = 0
if len(sys.argv) == 1:
    print('''Usage: python operations.py <number1> <number2>
Example:
   python operations.py 10 3''')
    sys.exit()
if len(sys.argv) != 3:
    raise AssertionError('number of arguments other than two are provided')

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except ValueError:
    raise AssertionError('only integers') from None

print(f'Sum:        {a + b}')
print(f'Difference: {a - b}')
print(f'Product:    {a * b}')
print(f'Quotient:   {a / b if b else "ERROR (division by zero)"}')
print(f'Remainder:  {a % b if b else "ERROR (modulo by zero)"}')
