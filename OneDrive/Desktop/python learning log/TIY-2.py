places=['tokyo','la','berlin','oslo']

print("Places I want to visit:",places)

print("Sorted places I want to visit:",sorted(places))

print("original places list",places)

print("alphabetically reverse sorted places I want to visit:",sorted(places,reverse=True))

print("original places list",places)

places.reverse()
print("reverse order of the places I want to visit:",places)
print("original places order:",places)

places.sort()
print("permanent sorting of the places:",places)

places.sort(reverse=True)
print("reverse permanent sorting of the places:",places)
