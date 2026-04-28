from app import get_random_quote, quotes


def test_get_random_quote_returns_string_from_quotes():
    result = get_random_quote()
    assert result in quotes, "Returned quote should be in the quotes list"


def test_quotes_list_is_not_empty():
    assert len(quotes) > 0, "Should have at least one quote"


def test_quotes_list_has_expected_minimum():
    assert len(quotes) >= 3, "Should have at least 3 quotes"


def test_this_should_fail_on_purpose():
    assert 1 == 1, "Math Works"