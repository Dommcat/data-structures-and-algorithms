# Python 401: Code Challenge Class 11

## stack-queue-pseudo

### Feature Tasks

Create a new class called pseudo queue.

Do not use an existing Queue.

Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below),
Internally, utilize 2 Stack instances to create and manage the queue
Methods:

enqueue
Arguments: value
Inserts a value into the PseudoQueue, using a first-in, first-out approach.

dequeue
Arguments: none
Extracts a value from the PseudoQueue, using a first-in, first-out approach.

NOTE: The Stack instances have only push, pop, and peek methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.




[WhiteBoard](/python/code_challenges/stack_queue_pseudo_file/CC11%20WB.png)


## Solution Code:
<!-- Show how to run your code, and examples of it in action -->

[Code Challenge 11 - Code Example](/python/code_challenges/stack_queue_pseudo_file/stack_queue_pseudo.py)

## Code Re/Sources Used:

ChatGPT

Class Demo File


## Testing:

Unit Tests:

- `test_enqueue_one()`: Test case to verify enqueueing a single element into an empty queue and dequeuing it results in the expected value.

- `test_enqueue_two()`: Test case to verify enqueueing two elements into an empty queue and dequeuing them in order results in the expected values.

- `test_enqueue_dequeue_enqueue_dequeue()`: Test case to verify enqueueing and dequeueing multiple elements into and from the queue, in a specific order, results in the expected values.


All tests passing
