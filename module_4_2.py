
def test_function():

    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

test_function()
#inner_function()
# в данном случае функция не работает, так как не видит ее в глобальной
# области видимости, а ф-я находится локально.


