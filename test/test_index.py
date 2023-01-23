import pytest
from index.IndexFile import index

Index_test=index("crawled_urls_test.json")

def test_extract_file():
    resu="Karine Lacombe — Wikipédia"
    assert resu == Index_test.extract_title(Index_test.data[0])

def test_tokensized_title():
    resu=["Karine","Lacombe","—", "Wikipédia"]
    Index_test.count_response-=1
    assert resu == Index_test.tokenized_title("Karine Lacombe — Wikipédia")

def test_token_dictonnary():
    resu={"Karine": {"1": 1}, "Lacombe": {"1": 1}, "—": {"1": 1}, "Wikipédia": {"1": 1}}
    Index_test.count =1
    Index_test.token_dictonnary("Karine Lacombe — Wikipédia")
    assert resu == Index_test.index

def test_stat_length():
    assert 1 == Index_test.stat_length()

def test_stat_length_token():
    assert 4== Index_test.stat_length_token()

def test_stat_lenght_response():
    assert 1== Index_test.stat_length_repsonse()

def test_stat_mean_token():
    assert 4 == Index_test.stat_mean()

