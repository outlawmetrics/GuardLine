from src.scanners.secrets.entropy import calculate_entropy

def test_empty_string():
    assert calculate_entropy("") == 0.0
    
def test_repeated_char():
    assert calculate_entropy("aaaaa") == 0.0

def test_random_string():
    assert calculate_entropy("a8Kf2x9Qm4Lp7Wd") >= 3.9

