import employee_info as info

def test_get_employees_by_age_range():
    result = []
    test = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    result = info.get_employees_by_age_range(21,28)
    assert(result == test)

def test_calculate_average_salary():
    test = 60166.67
    result = info.calculate_average_salary()
    assert(result == test)

def test_get_employees_by_department():
    result = []
    test = [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    result = info.get_employees_by_dept("Engineering")

    assert (result == test)

