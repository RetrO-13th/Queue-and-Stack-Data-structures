class Queue: # Class for operations related to queue.

    def __init__(self) -> None:
        self.queue = [] # Initialise empty stack.

    def push(self, data) -> None:
        # Method to add elements at the top of the queue.
        self.queue.append(data)

    def pop(self) -> None:
        # Method to deletes the down most element of the queue.
        if len(self.queue) <= 0:
            raise IndexError("No element in the queue")
        else:
            self.queue.pop(0)
        
    def display(self) -> list:
        # Mehtod to return queue.
        return self.queue

    def size(self) -> int:
        # Method to return size of the queue.
        return len(self.queue)

def main():
    q = Queue()
    q.push("Tim")
    q.push("Sadra")
    q.push("Benjamin")
    q.pop()
    print(q.size())
    print(q.display())

if __name__ == "__main__":
    main()