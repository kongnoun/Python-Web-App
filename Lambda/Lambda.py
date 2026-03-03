def add(x, y):
    return x + y
# Lambda equivialent
add_lambda = lambda x, y: x + y
print(add(5, 3)) # This will print 8
print(add_lambda(5, 3)) # This will also print 8

minus_lambda = lambda x, y: x - y
print(minus_lambda(5, 3)) # This will print 2
multiply_lambda = lambda x, y: x * y