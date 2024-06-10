from queue_scratch import Queue
from queue_list import QueueList

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

def test_calc_size():
    queue = Queue()
    assert queue.calc_size() == 0
    queue.en_queue(1)
    queue.en_queue(2)
    queue.en_queue(3)
    assert queue.calc_size() == 3
    queue.de_queue()
    assert queue.calc_size() == 2
    queue.en_queue(4)
    queue.en_queue(5)
    queue.en_queue(5)
    assert queue.calc_size() == 5

def test_peek():
    queue = Queue()
    queue.en_queue(1)
    queue.en_queue(2)
    queue.en_queue(3)
    assert queue.peek() == 1
    queue.de_queue()
    assert queue.peek() == 2

def test_en_queue_with_list():
    initial_list = [1, 2, 3]
    queue = QueueList(initial_list)
    additional_elements = [4, 5, 6]
    for element in additional_elements:
        queue.en_queue(element)
    expected_list = initial_list + additional_elements
    assert queue.queList == expected_list

if __name__ == "__main__":
    test_en_queue()
    test_de_queue()
    test_is_empty()
    test_calc_size()
    test_peek()
    test_en_queue_with_list()