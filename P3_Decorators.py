# g(x) = 2x + 3
# f(x) = x * g(x) + 2

def g_fn(x):
    def my_inner_decorator(inner_fn):
        def callable_fn():
            return inner_fn((2 * x) + 3)
        return callable_fn
    return my_inner_decorator
    
x = 5

@g_fn(x)
def f_fn(g_value):
    return (x * (g_value) + 2)

print(f_fn())