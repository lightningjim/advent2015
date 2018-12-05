from collections import defaultdict
filepath = 'input.txt'

fill_path = ''
santa_path = ''
robo_path = ''

with open(filepath, 'r') as f:
	full_path = f.read()
	f.close()
N = defaultdict(int)
s_x = 0
s_y = 0
r_x = 0
r_y = 0
x_min = 0
x_max = 0
y_min = 0
y_max = 0
N[(0,0)] += 1
houses = 0
for i, step in enumerate(full_path,1):
	if not(i % 2):
		santa_path += step
	else:
		robo_path += step
# print "Start, at (0,0); min/max x: (0,0 y:(0,0)"
for step in santa_path:
	if step == "^":
		s_y += 1
		if s_y > y_max:
			y_max = s_y
		# print "Move N, now (" + str(x) + "," + str(y) + "); min/max x: (" + str(x_min) + "," + str(x_max) + ") y: (" + str(y_min) + "," + str(y_max) + ")"
	if step == "v":
		s_y -= 1
		if s_y < y_min:
			y_min = s_y
		# print "Move S, now (" + str(x) + "," + str(y) + "); min/max x: (" + str(x_min) + "," + str(x_max) + ") y: (" + str(y_min) + "," + str(y_max) + ")"
	if step == "<":
		s_x -= 1
		if s_x < x_min:
			x_min = s_x
		# print "Move W, now (" + str(x) + "," + str(y) + "); min/max x: (" + str(x_min) + "," + str(x_max) + ") y: (" + str(y_min) + "," + str(y_max) + ")"
	if step == ">":
		s_x += 1
		if s_x > x_max:
			x_max = s_x
		# print "Move E, now (" + str(x) + "," + str(y) + "); min/max x: (" + str(x_min) + "," + str(x_max) + ") y: (" + str(y_min) + "," + str(y_max) + ")"
	# print "New location: (" + str(x) + "," + str(y) + ")"
	N[(s_x,s_y)] += 1
# print "Start, at (0,0); min/max x: (0,0 y:(0,0)"
for step in robo_path:
	if step == "^":
		r_y += 1
		if r_y > y_max:
			y_max = r_y
		# print "Move N, now (" + str(x) + "," + str(y) + "); min/max x: (" + str(x_min) + "," + str(x_max) + ") y: (" + str(y_min) + "," + str(y_max) + ")"
	if step == "v":
		r_y -= 1
		if r_y < y_min:
			y_min = r_y
		# print "Move S, now (" + str(x) + "," + str(y) + "); min/max x: (" + str(x_min) + "," + str(x_max) + ") y: (" + str(y_min) + "," + str(y_max) + ")"
	if step == "<":
		r_x -= 1
		if r_x < x_min:
			x_min = r_x
		# print "Move W, now (" + str(x) + "," + str(y) + "); min/max x: (" + str(x_min) + "," + str(x_max) + ") y: (" + str(y_min) + "," + str(y_max) + ")"
	if step == ">":
		r_x += 1
		if r_x > x_max:
			x_max = r_x
		# print "Move E, now (" + str(x) + "," + str(y) + "); min/max x: (" + str(x_min) + "," + str(x_max) + ") y: (" + str(y_min) + "," + str(y_max) + ")"
	# print "New location: (" + str(x) + "," + str(y) + ")"
	N[(r_x,r_y)] += 1

for dx in range(x_min, x_max+1):
	row = ''
	for dy in range(y_min, y_max+1):
		row += str(N[(dx,dy)])
		if N[(dx,dy)] >= 1:
			houses += 1
	print row + " | " + str(len(row))

print "# of houses: " + str(houses)