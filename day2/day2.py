filepath = 'input.txt'

boxes = file(filepath).readlines()
total_area_box = 0
total_ribbon_length = 0

for dimensions in boxes:
	smallest_area = 0
	dim = map(int,dimensions.split("x"))
	# The 2 smaller sides are always the smallest area
	dim.sort()
	# print dim
	total_area_box += 3*dim[0]*dim[1] + 2*dim[0]*dim[2] + 2*dim[1]*dim[2]
	total_ribbon_length += 2*dim[0] + 2*dim[1] + dim[0]*dim[1]*dim[2]


print "Total wrapping paper area is " + str(total_area_box) + " sq ft"
print "Total ribbon length is " + str(total_ribbon_length) + " ft"