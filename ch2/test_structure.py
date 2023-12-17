from cards import Card


def test_to_dict():
    # GIVEN
    # （前提：既知の値が設定されたCardオブジェクトが与えられたとすれば）
    c1 = Card('something', 'brian', 'todo', 123)

    # WHEN
    # （もし：このオブジェクトでto_dict()を呼び出したときに）
    c2 = c1.to_dict()

    # THEN
    # （ならば：既知の値が設定されたディクショナリが返される）
    c2_expected = {
        'summary': 'something',
        'owner': 'brian',
        'state': 'todo',
        'id': 123,
    }
    assert c2 == c2_expected
