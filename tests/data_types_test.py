import os,sys,inspect
import pytest
import random

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import data_types

# VARIABLES TESTS
instructor_list = ['zakk', 'jimmy', 'hammad', 'erin']

def test_dictionary_classroom():
    assert data_types.dictionary_classroom == {
        "chairs": 35,
        "name": 'CR3',
        "windows_count": 8,
        "glare": True
    }

def test_dict_classroom_chairs():
    assert data_types.dictionary_classroom["chairs"] == 35, 'the chair count is off'

def test_dict_classroom_name():
    assert data_types.dictionary_classroom["name"] == "CR3", 'the name is incorrect'

def test_dict_classroom_windows_count():
    assert data_types.dictionary_classroom["windows_count"] == 8, 'the window count is not 8'

def test_dict_classroom_glare():
    assert data_types.dictionary_classroom["glare"] == True, 'the glare property is not true'

def test_num_list():
    assert data_types.num_list == [1, 2, 3, 4], 'list is not correct'

def test_teacher_list():
    assert data_types.teacher_list == instructor_list, 'the teachers_list does not contain the correct strings or the order is wrong'

def test_teacher_list_data_type():
    for teacher in data_types.teacher_list:
        assert type(teacher) == str, 'each item in the list is not a string'