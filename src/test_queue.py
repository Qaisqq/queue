from queue_scratch import Queue
from queue_list import QueueList
from queue_linked_list import QueueLinkedList
## UNIT TESTS FOR QUEUE_SCRATCH ##
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

## UNIT TESTS FOR QUEUE_LIST ##
def test_en_queueL():
    initial_list = [1, 2, 3]
    queue = QueueList(initial_list)
    additional_elements = [4, 5, 6]
    for element in additional_elements:
        queue.en_queue(element)
    expected_list = initial_list + additional_elements
    assert queue.queList == expected_list

## UNIT TESTS FOR QUEUE_LINKED_LIST ##
def test_en_queueLL():
    queue = QueueLinkedList()
    queue.en_queue(1)
    assert queue.LL.head.value == 1
    assert queue.LL.count == 1

def test_de_queueLL():
    queue = QueueLinkedList()
    queue.en_queue(1)
    queue.en_queue(2)
    assert queue.de_queue() == 1
    assert queue.LL.head.value == 2
    assert queue.LL.count == 1

def test_is_emptyLL():
    queue = QueueLinkedList()
    assert queue.is_empty() == True
    queue.en_queue(1)
    assert queue.is_empty() == False

def test_sizeLL():
    queue = QueueLinkedList()
    assert queue.size() == 0
    queue.en_queue(1)
    assert queue.size() == 1
    queue.en_queue(2)
    assert queue.size() == 2

def test_peekLL():
    queue = QueueLinkedList()
    queue.en_queue(1)
    queue.en_queue(2)
    assert queue.peek() == 1
    queue.de_queue()
    assert queue.peek() == 2

if __name__ == "__main__":
    test_en_queue()
    test_de_queue()
    test_is_empty()
    test_calc_size()
    test_peek()
    test_en_queueL()
    test_en_queueLL()
    test_de_queueLL()
    test_is_emptyLL()
    test_sizeLL()
    test_peekLL()