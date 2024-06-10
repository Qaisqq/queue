from queue_1 import Queue

def test_en_queue():
    que = Queue()
    que.en_queue(1)
    que.en_queue(2)
    que.en_queue(3)
    que.en_queue(4)
    print(que.queList)

def test_de_queue():
    que = Queue()
    que.en_queue(1)
    que.en_queue(2)
    x = que.de_queue()
    print(x)
    x = que.de_queue()  
    print(x)
    print(que.queList)

if __name__ == "__main__":
    test_en_queue()
    test_de_queue()