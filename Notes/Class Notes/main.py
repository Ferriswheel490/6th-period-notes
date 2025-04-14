class subject:
    def __init__(self, content, period, teacher, room):
        self.content = content
        self.period = period
        self.teacher = teacher
        self.room = room

first = subject("chemestry", 1, "Jo")
second = subject("Art", 2, "hudson")

print(first)
print(second)