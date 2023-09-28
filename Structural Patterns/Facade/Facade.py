class Buffer:
    def __init__(self, width=30, height=20) -> None:
        self.width = width
        self.height = height
        self.buffer = [" "] * (width * height)

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text


class ViewPort:
    def __init__(self, buffer=Buffer()) -> None:
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[index + self.offset]

    def append(self, text):
        self.buffer.write(text)


class Console:  # Facade
    def __init__(self):
        b = Buffer()
        self.current_viewport = ViewPort(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    def write(self, text):  # high level write
        self.current_viewport.buffer.write(text)

    def get_char_at(self, index):  # expose low level methods
        return self.current_viewport.get_char_at(index)


if __name__ == "__main__":
    c = Console()
    c.write("Hello")
    ch = c.get_char_at(-1)
