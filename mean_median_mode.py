import statistics


def mean_median_mode(list_1):
    return [statistics.mean(list_1), statistics.median(list_1), statistics.mode(list_1)]
    # the return values will be stored in a tuple or a list when indicated


print(mean_median_mode([34, 78, 12, 10, 34, 63, 88, 12, 34]))
mean_0, median_0, mode_0 = mean_median_mode([34, 78, 12, 10, 34, 63, 88, 12, 34])
print(mean_0)
print(median_0)
print(mode_0)


def add_0(a, b):
    if a == 0 and b == 0:
        return
    else:
        return a + b


var_1 = int(input("Enter first number: \n"))
var_2 = int(input("Enter second number: \n"))
result = add_0(var_1, var_2)
print(f"The result is {result}")
