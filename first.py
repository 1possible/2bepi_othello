import Client
if __name__=="__main__":
    prems = Client.Client(8000,"prems",["12355", "67899"])
    dems = Client.Client(8880,"dems",["12345", "67890"])
    truc = input("hello")
    prems.fin()
    dems.fin()


def add(x,y):
    return x + y

