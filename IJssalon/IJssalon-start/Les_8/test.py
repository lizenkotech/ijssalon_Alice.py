def print_10():
    for i in range(10):
        print (i + 1)

print_10()

'''
def ongeveer_pi():
    return 3.1415

print(ongeveer_pi())


def tel_op(a,b):
    return a + b
totaal = tel_op(5,10)
print (totaal)
'''
'''
def info(naam, leeftijd, in_dienst):
    if in_dienst:
        text_1 = "en nog altijd in dienst van onze firma."
    else:
        text_1 = "en niet meer bij ons in dienst."

    uitvoer = f"Beste {naam}, u bent {leeftijd} jaar " + text_1
    return uitvoer

print(info("Harry", 54, True))
print(info ("Magda", 73, False))
'''
def tel_op (a=1,b=2):
    return a + b
totaal = tel_op()

print (totaal)
