class RingBuffer:
    def __init__(self, buffersize: int):
        self.buffer = []
        self.maxsize = buffersize
        self.tail = 0
        self.head = 0
        self.full = False

    def __getitem__(self, index: int):
        return self.buffer[index]

    def reset(self):
        self.tail = 0
        self.head = 0
        self.full = False

    def buffer_is_empty(self):
        return not self.full and self.head == self.tail

    def push(self, data: int):
        if not self.full:
            self.buffer.append(data)
        else:
            self.buffer[self.head] = data

        self.head = (self.head + 1) % self.maxsize
        self.full = (self.head == self.tail)

    def pop(self):
        if len(self.buffer) == 0:
            raise Exception("No data added to the buffer yet.")

        data = self.buffer[self.tail]

        self.tail = (self.tail + 1) % self.maxsize
        self.full = False

        return data
