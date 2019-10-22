a = 1
b = 12
assert a == 0, "Man you trying to divide by Zero"
print("Man you trying to divide by Zero")

try:
    assert a == 0, "Man you trying to divide by Zero"
except:
    print("I am in the excpet ")

