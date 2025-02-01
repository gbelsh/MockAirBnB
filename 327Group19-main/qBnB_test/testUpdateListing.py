from qBnB.backend import updateListings


# (id, title, description, price):
def test_r5_1_update_listings():
    # attempt to update row data with id....
    # to the new title ...
    assert updateListings('sajfb', 'coolNewBook',
                          'description', 4000) is True

    # return false caused id dont exist ...
    assert updateListings('thisiddoesntexist', 'coolNewBook', 
                          'description', 4000) is False


def test_r5_2_update_listings():
    # attempt to update row data with
    # id.... to the new title ...
    assert updateListings('kdnksdnksn', 'morethen20characterslong', 
                          'coolNewBook', 4000) is True

    # return false cause too short
    assert updateListings('shshsghs', 'tooshort', 
                          'coolNewBook', 4000) is False


def test_r5_3_update_listings():
    # attempt to update row data
    # with id.... to the new price ...
    assert updateListings('nsknald', 'coolNewBook', 
                          'description', 4000) is True

    # return false cause the price of
    # listing too small
    assert updateListings('ksndksnksnds', 'coolNewBook', 
                          'description', 5) is False

    # return false cause new price is
    # not greater then old price
    assert updateListings('sjdnsnskdn', 'coolNewBook', 
                          'description', 2000) is False




