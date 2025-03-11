# Fix the code below, so it returns the expected output. Submit the fixed code to the judge system.
# input             output
# global            global
# outer: local      outer: local
# inner: nonlocal   inner: nonlocal
# outer: local      outer: nonlocal
# global            global: changed!

x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)
