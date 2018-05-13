# !/usr/bin/env python
# _*_ coding: utf8 _*_

# Read lines as a list
with open("Prices/ANIUS.txt", "r") as ANIUS_price:
	lines = ANIUS_price.readlines()
	ANIUS_price.close()

# Weed out blank lines with filter
lines = filter(lambda x: not x.isspace(), lines)

# Write
ANIUS_price = open("output", "w")
ANIUS_price.write("".join(lines))

# should also work instead of joining the list:
# ANIUS_price.writelines(lines)
ANIUS_price.close()