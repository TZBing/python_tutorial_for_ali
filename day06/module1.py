def f1(s):
    print("f1:" + s)


def f2(s):
    print("f2:" + s)


print("value of __name__ in module1: " + __name__)
f1("hello")

if __name__ == "__main__":
    f2("just for test")
