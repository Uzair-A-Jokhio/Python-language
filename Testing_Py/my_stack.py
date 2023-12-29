class stack():
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except Exception as e:
            print("Error: " , e)
    
    def peek(self):
        try:
            return self.items[-1]
        except IndexError as e:
            print("Error" , e)


