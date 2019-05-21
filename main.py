
class Greeter:

    def greet(self, who=None):
        if who:
            return "Hello " + who + "!"
        else:
            return "Hello world!"


if __name__ == '__main__':
    g = Greeter()
    msg = g.greet()
    print(msg)
