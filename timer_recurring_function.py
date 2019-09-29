import timeit
from recurring_string import repeated_character


timeit.Timer("for x in range(100): repeated_character(x)", "gc.enable()").timeit()
