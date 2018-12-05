from collections import defaultdict
filepath = 'input.txt'

santa_path = ''

with open(filepath, 'r') as f:
	santa_path = f.read()
	f.close()
N = defaultdict(int)
x = 0
y = 0
x_min = 0
x_max = 0
y_min = 0
y_max = 0
N[(0,0)] += 1
houses = 0
# print "Start, at (0,0); min/max x: (0,0 y:(0,0)"
for step in santa_path:
	if step == "^":
		y += 1
		if y > y_max:
			y_max = y
		# print "Move N, now (" + str(x) + "," + str(y) + "); min/max x: (" + str(x_min) + "," + str(x_max) + ") y: (" + str(y_min) + "," + str(y_max) + ")"
	if step == "v":
		y -= 1
		if y < y_min:
			y_min = y
		# print "Move S, now (" + str(x) + "," + str(y) + "); min/max x: (" + str(x_min) + "," + str(x_max) + ") y: (" + str(y_min) + "," + str(y_max) + ")"
	if step == "<":
		x -= 1
		if x < x_min:
			x_min = x
		# print "Move W, now (" + str(x) + "," + str(y) + "); min/max x: (" + str(x_min) + "," + str(x_max) + ") y: (" + str(y_min) + "," + str(y_max) + ")"
	if step == ">":
		x += 1
		if x > x_max:
			x_max = x
		# print "Move E, now (" + str(x) + "," + str(y) + "); min/max x: (" + str(x_min) + "," + str(x_max) + ") y: (" + str(y_min) + "," + str(y_max) + ")"
	# print "New location: (" + str(x) + "," + str(y) + ")"
	N[(x,y)] += 1

for dx in range(x_min, x_max+1):
	row = ''
	for dy in range(y_min, y_max+1):
		row += str(N[(dx,dy)])
		if N[(dx,dy)] >= 1:
			houses += 1
	print row + " | " + str(len(row))

print "# of houses: " + str(houses)