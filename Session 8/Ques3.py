class stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()
s=stack()
s.push(12)
s.push(13)
s.push(14)
print(s.pop())