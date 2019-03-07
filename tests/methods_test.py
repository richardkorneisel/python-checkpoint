import pytest
import os,sys,inspect
import pdb

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import methods as methods_module

# METHODS/Control Flow

def test_num_list_with_arg_name():
    assert "num_list_with_arg" in file_data, "the method num_list_with_arg is not defined"

def test_has_ruby_exp():
    assert methods_module.has_ruby_exp() == ['don', 'jimmy', 'zakk'], 'the method has_ruby_exp did not return the expected result'

def test_toggle_str_num():
    assert methods_module.toggle_str_num(3) == '3', 'the toggle str method did not successfully convert a number to a string'
    assert methods_module.toggle_str_num('3') == 3, 'the toggle str method did not successfully convert a string to a number'
    assert methods_module.toggle_str_num(True) == 'this is not a str or a int', 'the toggle str method did not successfully handle none string or integer data types'

def test_num_list_with_arg():
    assert methods_module.num_list_with_arg(1) == [], "the method num_list_with_arg(1) does not return the desired result."
    assert methods_module.num_list_with_arg(3) == [1, 2], "the method num_list_with_arg(3) does not return the desired result."
    assert methods_module.num_list_with_arg(5) == [1,2,3,4], "the method num_list_with_arg(5) does not return the desired result."
    assert methods_module.num_list_with_arg(6) == [1, 2, 3, 4, 5], "the method num_list_with_arg(6) does not return the desired result."
    assert methods_module.num_list_with_arg(15) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "the method num_list_with_arg(15) does not return the desired result."

### Data/File Tests

# def get_file_as_data():
with open(currentdir + '/../methods.py', 'r') as myfile:
    file_data=myfile.read().replace('\n', '')

def test_has_ruby_experience_append():
    assert "ruby_experience.append" in file_data, "the method has_ruby_exp does not append to the list, ruby_experience"

def test_has_ruby_exp_name():
    assert "has_ruby_exp" in file_data, "the method has_ruby_exp is not defined"

def test_toggle_str_num_name():
    assert "toggle_str_num" in file_data, "the method 'toggle_str_num' is not defined"