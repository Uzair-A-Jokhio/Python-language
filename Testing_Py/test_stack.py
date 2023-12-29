from my_stack import stack

def stack_empty_stack():
    s1 = stack()
    assert s1.is_empty() is True

def test_pop_push():
    c1 = stack()
    c1.push(2)
    c1.push(3)
    assert c1.pop() == 3
    assert c1.pop() == 2

def test_push_peek():
    c1 = stack()
    c1.push(5)
    assert c1.peek() == 5
    assert c1.is_empty() is False
    


