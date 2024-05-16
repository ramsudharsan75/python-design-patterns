class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text="") -> None:
        self.name = name
        self.text = text
        self.elements = []


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))

    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))
        return self

    def __str__(self) -> str:
        return str(self.__root)

    @staticmethod
    def create(root_name):
        return HtmlBuilder(root_name)


builder = HtmlBuilder.create("ul")
builder.add_child_fluent("li", "hello")
builder.add_child_fluent("li", "world")
print("Ordinary builder:")
print(builder)
