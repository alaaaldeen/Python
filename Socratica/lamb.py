"""
def f(x):
    return 3*x + 1

print f(2)


d = lambda x: 3*x + 1
print d(2)


full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print full_name("   leonardo", "DAVINCI")
"""

geometric_mean = lambda x, y: (x*y)**0.5

harmonic_mean = lambda x, y, z: 3/(1.0/x + 1.0/y + 1.0/z)

print geometric_mean(4, 9)
print harmonic_mean(3, 3, 3)
