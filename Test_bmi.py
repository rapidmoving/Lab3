import Lab2.bmi as bmi

def test_bmi_normal_weight():
    test = 0
    result = bmi.calculate_bmi(1.75,62)

    assert(test == result)

def test_bmi_over_weight():
    test = 1
    result = bmi.calculate_bmi(1.75,90)

    assert (test == result)

def test_bmi_under_weight():
    test = -1
    result = bmi.calculate_bmi(1.75,50)
    assert (test == result)




