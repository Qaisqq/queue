from queue_1 import Queue

def test_en_queue():
    queue = Queue()
    queue.en_queue(1)
    queue.en_queue(2)
    queue.en_queue(3)
    assert queue.queList == [1, 2, 3]

def test_de_queue():
    queue = Queue()
    queue.en_queue(1)
    queue.en_queue(2)
    queue.en_queue(3)
    assert queue.de_queue() == 1
    assert queue.queList == [2, 3]

def test_is_empty():
    queue = Queue()
    assert queue.is_empty() == True
    queue.en_queue(1)
    assert queue.is_empty() == False
    queue.de_queue()
    assert queue.is_empty() == True

if __name__ == "__main__":
    test_en_queue()
    test_de_queue()
    test_is_empty()