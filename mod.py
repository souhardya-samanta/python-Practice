import converters
from converters import to_sec
sec=int(input("Enter time in seconds"))
print("Time in minutes", converters.to_min(sec),end="\n")
m=int(input("Input time in minutes"))
print("Time in seconds ", to_sec(m))