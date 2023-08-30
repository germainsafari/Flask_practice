#zip(*iterables) = aggregates elements from two or more iterables(list,tuples,sets,etc)
country = ["Rwanda","Germany","Russia","Poland"]
city = ("Kigali","Berlin","Moscow","Warsaw")
cw = zip(country,city)
for i in cw:
    print(i)