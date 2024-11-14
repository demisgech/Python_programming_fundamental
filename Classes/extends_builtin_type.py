class Text(str):
    def duplicate(self):
        return self + self
    
obj = Text("Python")

capitalized = obj.capitalize()
print(capitalized)
print(obj.duplicate())
print(obj.lower())
print(obj.upper())


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)

trackableObject = TrackableList(["First","Second","Third"])
trackableObject.append("Four")
for trackable in trackableObject:
    print(trackable)

class TrackableTuple(tuple):
    def count(self, value):
        print("Count called")
        return super().count(value)


trackableTuple = TrackableTuple((1,2,3))
countedValue = trackableTuple.count(1)
print(countedValue)
for trackable in trackableTuple:
    print(trackable)

