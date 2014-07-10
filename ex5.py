name = 'Zed A Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_in_feet = 0
height_in_cm = 0 

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usally %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# Study Drill 
# Convert inches to feet and centimeters
height_in_feet = float(height / 12.0)
print "%s 's height in feet is %d" % (name, height_in_feet)

height_in_cm = float(height * 2.54)
print "%s 's height in centimeters is %d" % (name, height_in_cm)