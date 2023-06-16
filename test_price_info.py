import price_info as price

def test_total_cost_shopping():
    result = price.total_cost_shopping()
    answer = 46.75
    assert(result == answer)

def test_cost_of_fruits():
    result = price.cost_of_fruits('apple',10)
    answer = 12
    assert (result == answer)

