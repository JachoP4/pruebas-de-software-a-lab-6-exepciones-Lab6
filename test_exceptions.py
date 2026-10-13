import pytest
from Exceptions import ExceptionsDemo, MyException  

@pytest.mark.unit
def test_div_zero():
    demo = ExceptionsDemo()
    with pytest.raises(ZeroDivisionError):
        demo.divide(10,0)

@pytest.mark.unit
def test_type_error():
    demo = ExceptionsDemo()
    with pytest.raises(TypeError):
        demo.divide('Tamaulipas',0)

@pytest.mark.unit
def test_index_error():
    demo = ExceptionsDemo()
    with pytest.raises(IndexError):
        demo.access_list([1,2,3], 100)

#@pytest.mark.unit
#def test_index_type_error():
    #demo = ExceptionsDemo()
    #with pytest.raises(TypeError, IndexError):
        #demo.access_list([1,2,3], 1)
        #demo.access_list([1,2,3], 100)
        #demo.access_list([1,2,3], "caca")

@pytest.mark.unit
def test_file_error():
    demo = ExceptionsDemo()
    with pytest.raises(FileNotFoundError):
        demo.read_file('caca.txt')

@pytest.mark.unit
def test_acces_attribute():
    demo = ExceptionsDemo()
    with pytest.raises(AttributeError):
        demo.access_attribute(demo.caca())

@pytest.mark.unit
def test_my_exeption():
    demo = ExceptionsDemo()
    with pytest.raises(MyException):
        demo.check_positive(-3)