def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
test_function()

# inner_function() -  если вызывать "inner_function()"
# вне функции "test_function()" будет выходить ошибка