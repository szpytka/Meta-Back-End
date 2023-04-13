# global scope
my_global = 10


def fn1():
    enclosed_v = 8

    def fn2():
        local_v = 5
        print("Access to Global", my_global)
        print("Access to Enclosed", enclosed_v)

    fn2()


fn1()
