class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)


class PersistenceManager:  # Separate class for handling file storage
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, "w") as file:
            file.write(str(journal))


j = Journal()
j.add_entry("Im happy today")
j.add_entry("Best day of my life")
print(f"Journal Entries: \n{j}")

file = r"journal.txt"
PersistenceManager.save_to_file(j, file)

with open(file, "r") as fh:
    print(fh.read())
