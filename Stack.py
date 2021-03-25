class Stack: # Class for operations related to stack.

    def __init__(self) -> None:
        self.stack = [] # Initialise empty stack.

    def push(self, data) -> None:
        # Method to add elements at the top of the queue.
        self.stack.append(data)

    def pop(self) -> None:
        # Method to deletes the top most element of the stack.
        if len(self.stack) <= 0:
            raise IndexError("No element in the queue")
        else:
            self.stack.pop()

    def display(self) -> list:
        # Mehtod to return stack.
        return self.stack

    def size(self) -> int:
        # Method to return size of the queue.
        return len(self.stack)

def main():
    s = Stack()
    s.push("Tim")
    s.push("Sadra")
    s.push("Benjamin")
    s.pop()
    print(s.size())
    print(s.display())

if __name__ == "__main__":
    main()