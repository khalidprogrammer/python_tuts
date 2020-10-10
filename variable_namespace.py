# def outer_function():
#     b = 20
#     print("b", b)
#
#     def inner_func():
#         c = 30
#         print("c", c)
#
#     return inner_func()
#
#
# a = 10
#
# outer_function()
#
# print(a)

def outer_function():
    global a
    a = 20

    def inner_function():
        global a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a10 =', a)




