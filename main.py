import bson

def my_test():

    for x in range(2, 10):
        print("------------------")
        for y in range(1, 10):
            print(x, "X", y, "=", x * y)
    print("---------------------")


print(my_test())
