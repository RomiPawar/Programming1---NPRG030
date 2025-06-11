import sys
def convert_to_base(num, base):
    digits = "01234567898abcdefghijklmnopqrstuvwxyz"
    result = " "
    while num > 0:
        remainder = num % base
        result = digits[remainder] + result
        num //= base
    return result if result else "0"
current_conversion = None
for line in sys.stdin:
    line = line.strip()
    if ">" in line:
        current_conversion = list(map(int, line.split(">")))
    else:
        if current_conversion:
            initial_base, final_base = current_conversion
            decimal_num = int(line, initial_base)
            convert_num = convert_to_base(decimal_num, final_base)
            print(convert_num)
