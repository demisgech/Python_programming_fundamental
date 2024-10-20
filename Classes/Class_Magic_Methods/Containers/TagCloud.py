class TagCloud:
    def __init__(self):
        self.tags = {}
    
    def add(self, tag):
        # self.tags[tag] = self.tags.get(tag, 0) + 1
        # Take care case-sensitivity
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    # get item using subscript opertator like obj[key]
    def __getitem__(self,tag):
        return self.tags.get(tag.lower(), 0)

    # set item using subscript operator like obj[key] = value
    # def __setitem__(self, key, value):
    #     self.tags[key] = value

    def __setitem__(self, tag, count):
        self.tags[tag] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)
    
    def __str__(self):
        return str(self.tags)
    

cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")


print(cloud.tags)

# get item
p = cloud["python"]
print(p)

# set item
cloud["JavaScript"] = 16
print(cloud.tags)

tag_list = cloud.tags

for tag_key in tag_list:
    print(tag_key, tag_list[tag_key])

# tuple style
for tag_key, tag_value in tag_list.items():
    print(tag_key, tag_value)

# list style
for [tag_key, tag_value] in tag_list.items():
    print(tag_key, tag_value)

# length
length = len(cloud)
print(f"Length: {length}")

iterable = cloud

for key in cloud:
    print(key, cloud[key])

print(cloud)