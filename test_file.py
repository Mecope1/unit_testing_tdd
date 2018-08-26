from pytest import raises


def test_it():
    assert True


def test_it2():
    assert False


def raises_value_exception():
    # pass
    raise ValueError


def test_exception():
    with raises(ValueError):
        raises_value_exception()


