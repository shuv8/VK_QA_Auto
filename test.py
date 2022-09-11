import pytest


class TestDict:
    def test_dict_1(self):
        test_dict = dict()
        test_dict.update([(0, 'null')])
        assert test_dict[0] == 'null'

    @pytest.mark.parametrize("test_input_key, test_input_value, test_expected",
                             [('one', 1, ('one', 1)), (0, 0, (0, 0)), (-3, -3, (-3, -3))])  # different types of keys
    def test_dict_2(self, test_input_key, test_input_value, test_expected):
        test_dict = dict.fromkeys([test_input_key], test_input_value)
        for a in test_dict.items():
            assert a == test_expected

    def test_dict_3(self):
        test_dict = {0: 'null'}
        try:
            assert test_dict['null'] == 0
        except KeyError:
            pass


class TestSet:
    def test_set_1(self):
        test_set = set()
        test_set.add(123)
        for a in test_set:
            assert a == 123

    @pytest.mark.parametrize("test_input, test_expected", [(3 - 5, -2), (2 + 4, 6), (6 * 7, 42)])
    def test_set_2(self, test_input, test_expected):
        test_set = {test_input}
        for a in test_set:
            assert a == test_expected

    def test_set_3(self):
        test_set = {123}
        try:
            assert test_set[0] == 123
        except TypeError:
            pass
