"""

"""

def underscorifySubstring(string, substring):
	locations = collapse(getLocations(string, substring))
	return underscorify(string, locations)


def getLocations(string, substring):
	locations = []
	startIndex = 0
	while startIndex < len(string):
		nextIndex = string.find(substring, startIndex)
		if nextIndex != -1:
			locations.append([nextIndex, nextIndex + len(substring)])
			startIndex = nextIndex + 1
		else:
			break
	return locations


def collapse(locations):
	if not len(locations):
		return locations
	newLocations = [locations[0]]
	previous = newLocations[0]
	for i in range(1, len(locations)):
		current = locations[i]
		if current[0] <= previous[1]:
			previous[1] = current[1]
		else:
			newLocations.append(current)
			previous = current
	return newLocations


def underscorify(string, locations):
	locationsIndex = 0
	stringIndex = 0
	betweenUnderscores = False
	finalChars = []
	i = 0
	while stringIndex < len(string) and locationsIndex < len(locations):
		if stringIndex == locations[locationsIndex][i]:
			finalChars.append('_')
			betweenUnderscores = not betweenUnderscores
			if not betweenUnderscores:
				locationsIndex += 1
			i = 0 if i == 1 else 1
		finalChars.append(string[stringIndex])
		stringIndex += 1
	if locationsIndex < len(locations):
		finalChars.append('_')
	elif stringIndex < len(string):
		finalChars.append(string[stringIndex:])
	return ''.join(finalChars)

if __name__ == "__main__":
	print(underscorifySubstring('testthis', 'test'))
