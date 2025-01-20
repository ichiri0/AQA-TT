import pytest
from app.sol_2 import generate_request, parse_highlight, split_ignore_brackets

class TestSol2:

    def test_split_ignore_brackets(self):
        test_input = 'a,b,c,(d,e,f),g,h'
        expected_output = ['a', 'b', 'c', '(d,e,f)', 'g', 'h']
        result = split_ignore_brackets(test_input)
        assert result == expected_output

        test_input_no_brackets = 'a,b,c,d,e'
        expected_output_no_brackets = ['a', 'b', 'c', 'd', 'e']
        result_no_brackets = split_ignore_brackets(test_input_no_brackets)
        assert result_no_brackets == expected_output_no_brackets

    def test_parse_highlight(self):
        test_input = 'equals=S110=rgba(172,86,86,1),equals=S111'
        expected_output = [
            {'type': 'equals', 'value': 'S110', 'color': 'rgba(172,86,86,1)'},
            {'type': 'equals', 'value': 'S111', 'color': ''}
        ]
        result = parse_highlight(test_input)
        assert result == expected_output

        test_input_no_color = 'equals=S110,equals=S111'
        expected_output_no_color = [
            {'type': 'equals', 'value': 'S110', 'color': ''},
            {'type': 'equals', 'value': 'S111', 'color': ''}
        ]
        result_no_color = parse_highlight(test_input_no_color)
        assert result_no_color == expected_output_no_color

if __name__ == '__main__':
    pytest.main()
