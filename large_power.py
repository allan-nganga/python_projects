def large_power(base, exponent):
    result = base ** exponent
    return result > 5000

#Test the function
print(large_power(10,2))#Output will be false
print(large_power(100, 2))#Output will be True