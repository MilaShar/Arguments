# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet (name_patient, name = "Doc" ):
    print ("Hello " + name + "!")
    print ("What's up " + name_patient + "!")

greet("Bob")

def force(mass, body="earth"):
    force = mass * round(planets[body],1)
    print(force)


planets = {"sun": 274,
           "jupiter": 24.92,
           "neptune": 11.15,
           "saturn": 10.44,
           "earth": 9.798,
           "uranus": 8.87,
           "venus": 8.87,
           "mars": 3.71,
           "mercury": 3.7,
           "moon": 1.62,
           "pluto": 0.58}


#for item in planets:
#   print (item, ":" ,planets[item])#prints keys and value

#for item in  planets:
    #print (item)#prints key
    #print (planets[item])#prints value

force (2, "moon")

def pull (m1, m2, d2):
    g = 6.674*(10**-11)

    m = (m1 * m2)
    md = m /d2**2
    #print (md)

    f = g * md
    print (round(f,2))
    return

pull(0.1, 5.972*(10**24), 6.371*(10**6))

