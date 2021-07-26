#More excersizes on Variables and Naming conventions

name = "Habibi The Isle"
age = 43
height = 189 #cantimeteres
height_inches = 189 * 0.3937008
weight = 90 #kilos
weight_pounds = weight * 2.20
eyes = "Purple"
teeth = "Respectable"
hair = "Groomed"

print ("Let us talk about my good friend %s" %name)
print ("He's %d cantimeteres tall, equivelent to %d inches" %(height, height_inches))
print ("And weights %d kilos, which is %d in pounds" %(weight, weight_pounds))
print ("He has really interesting %s eyes and %s hair" %(eyes, hair))
print ("His teeth are %s" %teeth)

#Here comes the tricky line :b ;D
print ("If I add %d, %d and %d I get %d." %(age, height, weight, age + height + weight))
