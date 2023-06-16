import Lab2.Lab2 as temp

def test_find_min_max():
    input_arr = [20,15,33,29,21,26]
    test = [15,33]
    result = temp.find_min_max(input_arr)

    assert(test == result)

def test_calc_average():
    input_arr = [20,15,33,29,21,26]
    result = temp.calc_average(input_arr)
    assert(result == 24)

def test_calc_median_temperature():

    input_arr = [20,15,33,29,21,26]
    sorted_list = temp.sort_temperature(input_arr)
    result = temp.calc_median_temperature(sorted_list)

    assert(result == 23.5)