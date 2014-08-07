#create a mapping of state to abbreviation
states = ['Oregon': 'OR']
# create a basic set of states and some cities in them
cities = [
	'CA' = 'San Francisco',
	'MI' = 'Detroit',
	'FL' = 'Jacksonville'
]

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print out some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.item():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.item():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is %s" % city
