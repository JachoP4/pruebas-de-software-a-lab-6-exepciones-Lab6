class MyException(Exception):
    pass

class ExceptionsDemo:
    
    def divide(self, a, b):
        result = a / b
        print("Division result:", result)
    
    def access_list(self, lst, index):
        print("Element:", lst[index])
    
    def access_dict(self, dic, key):
        print("Value:", dic[key])
    
    def read_file(self, filename):
        with open(filename, "r") as f:
            content = f.read()
            print(content)
    
    def access_attribute(self, obj):
        print(obj.tnonexistent_attribue)
    
    def check_positive(self, number):
        if number < 0:
            raise MyException("The number must be positive.")
        else:
            print("Valid number:", number)

class MyException(Exception):
    pass