filepath = 'input.txt'

santa_path = ''
floor = 0
part2_trigger = False

with open(filepath, 'r') as f:
	santa_path = f.read()
	f.close()

for i, step in enumerate(santa_path,1):
	if step == '(':
		floor += 1
	else:
		if step == ')':
			floor -= 1
		else:
			print "LOL IDK"
	if not part2_trigger and (floor == -1):
		print ("First enters basement on step " + str(i))
		part2_trigger = True

print ("Final floor " + str(floor))