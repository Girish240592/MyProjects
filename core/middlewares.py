# This is my first middleware
# Middeleware view (Function Based) start
def my_middleware1(get_response):
    print("Welcome to first time running code")
    def my_fun(request):
        print("Welcome to the code running before the view function")
        response=get_response(request)
        print("This code will run after the view file")
        return response
    return my_fun

def my_middleware2(get_response):
    print("Welcome to Second time running code")
    def my_fun2(request):
        print("Welcome to the code running before the view function")
        response=get_response(request)
        print("This code will run after the view file")
        return response
    return my_fun2
# Middeleware view function based end

# Middeleware view Class based Start
class My_middleware():
    def __init__(self, get_response):
        self.get_response=get_response
        print("One time class based middleware running code")
        
    def __call__(self, request):
        print("THis will running before cb views function")
        response=self.get_response(request)
        print('This will run after cb view function')
        return response
    
# Middeleware view Class based end