import pytest

import schemas.search


def test_search_base_validate_criteria_no_value_with_regnum():
    try:
        schemas.search.SearchBase(criteria={}, type=schemas.search.SearchType.REGISTRATION_NUMBER.name)
    except ValueError:
        pass
    else:
        pytest.fail('A validation error was expected since there was no value field in the criteria')


def test_search_base_validate_criteria_when_value_not_alphanumeric_regnum():
    try:
        schemas.search.SearchBase(criteria={'value': '123_56A'},
                                  type=schemas.search.SearchType.REGISTRATION_NUMBER.name)
    except ValueError:
        pass
    else:
        pytest.fail('A validation error was expected since the registration number has an invalid format')


def test_search_base_validate_criteria_when_valid_with_regnum():
    search = schemas.search.SearchBase(criteria={'value': '123456A'},
                                       type=schemas.search.SearchType.REGISTRATION_NUMBER.name)
    assert search.criteria == {'value': '123456A'}


def test_search_base_validate_type_when_invalid():
    try:
        schemas.search.SearchBase(type='INVALID_ENUM', criteria={'value': '1234567'})
    except ValueError:
        pass
    else:
        pytest.fail('A validation error was expected since type was invalid')


def test_search_base_validate_type_when_valid_enum_name():
    search = schemas.search.SearchBase(type=schemas.search.SearchType.AIRCRAFT_DOT.name, criteria={'value': '1234567'})
    assert search.type == schemas.search.SearchType.AIRCRAFT_DOT.name


def test_search_base_validate_when_type_invalid_and_criteria_empty():
    try:
        schemas.search.SearchBase(type='INVALID_ENUM', criteria={})
    except ValueError:
        pass
    else:
        pytest.fail('A validation error was expected since the input was invalid')


def test_search_result_validate_type_when_exact():
    search = schemas.search.SearchResult(type='EXACT', financingStatement=None)
    assert search.type == schemas.search.SearchResultType.EXACT.name


def test_search_result_validate_type_when_invalid():
    try:
        schemas.search.SearchResult(type='INVALID_ENUM_NAME', financingStatement=None)
    except ValueError:
        pass
    else:
        pytest.fail('A validation error was expected since type was invalid')