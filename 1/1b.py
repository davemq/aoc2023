# The newly-improved calibration document consists of lines of text;
# each line originally contained a specific calibration value that the
# Elves now need to recover. On each line, the calibration value can be
# found by combining the first digit and the last digit (in that order)
# to form a single two-digit number.
#
# For example:
#
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# In this example, the calibration values of these four lines are 12,
# 38, 15, and 77. Adding these together produces 142.
import re
import sys

r = re.compile("\d|one|two|three|four|five|six|seven|eight|nine")
sum = 0
for line in sys.stdin:
    line = line.rstrip()  # Remove \n
    print(line)
    cursor = 0
    m = r.search(line[cursor:])
    digits = []
    while m:
        digits.append(m.group(0))
        cursor += m.start() + 1
        m = r.search(line[cursor:])
    print(digits)

    for i, mult in [(0, 10), (-1, 1)]:
        match digits[i]:
            case "0":
                val = 0
            case "1" | "one":
                val = 1
            case "2" | "two":
                val = 2
            case "3" | "three":
                val = 3
            case "4" | "four":
                val = 4
            case "5" | "five":
                val = 5
            case "6" | "six":
                val = 6
            case "7" | "seven":
                val = 7
            case "8" | "eight":
                val = 8
            case "9" | "nine":
                val = 9
        print(val * mult)
        sum += val * mult

print(sum)
