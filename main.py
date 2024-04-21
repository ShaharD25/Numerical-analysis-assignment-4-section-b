
#Date:21.4.24
#Group members: Andrey Romanchuk 323694059;Shahar Dahan 207336355;Maya Rozenberg 313381600
#Private Git: https://github.com/ShaharD25/Numerical-analysis-assignment-4-section-b.git
#Name: shahar dahan



import math

def trapezoidal_method(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result

def sin_function(x):
    return math.sin(x)

# Define the bounds of integration
a = 0
b = math.pi

# Number of segments
n = 4

# Calculate the integral using the trapezoidal method
integral_approximation = trapezoidal_method(sin_function, a, b, n)

# Known solution for comparison
known_solution = 2

# Calculate the error
error = abs(known_solution - integral_approximation)

print("Approximate Integral:", integral_approximation)
print("Known Solution:", known_solution)
print("Error:", error)