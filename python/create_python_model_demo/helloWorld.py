

class HelloWorld(object):
    def __init__(self):
        self.__github="https://github.com/Jiangxumin"
    
    def printf(self):
        print("Hello World")

    def printGithub(self):
        print self.__github


if __name__ == "__main__":
    hello = HelloWorld()
    hello.printf()
    hello.printGithub()
