#ZIP FUNCTION
import itertools

counter = itertools.count()

data = [100, 200, 300, 400]
daily_data = list(zip(itertools.count(), data))

print(daily_data)

#prints:[(0, 100), (1, 200), (2, 300), (3, 400)]
