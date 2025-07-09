var1 = "25"           # string
var2 = 100            # integer
var3 = 45.6           # float
var4 = True           # boolean
var5 = 4 + 3j         # complex

print("Original Types:")
print(type(var1), type(var2), type(var3), type(var4), type(var5))

# Try converting and printing new types
print("\nConverted Types:")
try:
    print(int(var1))  # string to int
except:
    print("Can't convert var1 to int")

try:
    print(str(var2))  # int to string
except:
    print("Can't convert var2 to string")

try:
    print(int(var3))  # float to int
except:
    print("Can't convert var3 to int")

try:
    print(int(var4))  # boolean to int (True = 1)
except:
    print("Can't convert var4 to int")

try:
    print(str(var5))  # complex to string
except:
    print("Can't convert var5 to string")
