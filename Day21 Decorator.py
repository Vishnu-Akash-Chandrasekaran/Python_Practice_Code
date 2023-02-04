################with Decorator ############################
def decor_function(input_function):
    def inner():
        print("#"*10)
        print("Decoration wwith flowers")
        input_function()
        print("#"*10)
    return inner

@decor_function
def old_function():
    print("No decoration")

old_function()

################without Decorator ############################

def decor_function():
    def inner(input_function):
        print("#"*10)
        print("Decoration wwith flowers")
        input_function()
        print("#"*10)
    return inner

def old_function():
    print("No decoration")

returned_function= decor_function()
returned_function(old_function)
 
