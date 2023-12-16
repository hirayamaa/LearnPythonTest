from cards import Card


def test_equality_fail():
    c1 = Card('sit there', 'Brian')
    c2 = Card('do something', 'okken')
    assert c1 == c2


# pytestからでなくpythonから直接テストを実行できる
if __name__ == '__main__':
    test_equality_fail()
