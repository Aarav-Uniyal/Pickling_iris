import pickle

def pickler(text):
    with open(text) as iris:
        string = iris.read()

    list1 = string.split("\n")
    list2 = [item.split(",") for item in list1 if len(item) != 0]
    with open("Ex10(Test).pkl","wb") as file1:
        pickle.dump(list2, file1)
    pass

def depickler():
    with open("Ex10(Test).pkl","rb") as file2:
        text = pickle.load(file2)
        print(text)
    pass

if __name__ == '__main__':
    file = "iris.data"
    pickler(file)
    depickler()




