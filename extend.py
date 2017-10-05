class Hello:
    hey = "hey"
    def hello(self):
        print(self.hey)

class Say(Hello):
    pass

say = Say()
say.hello()
