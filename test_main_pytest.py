from main import Greeter


def test_hello_world():
    g = Greeter()
    result = g.greet()
    assert result == "Hello world!"


def test_hello_name():
    g = Greeter()
    result = g.greet(who="John")
    assert result == "Hello John!"
