# Stacks -> Last In First Out === LIFO or 
# First In Last Out === FILO
#
borwsing_section = []

# Add item to the stack
borwsing_section.append("facebook.com/watch")
borwsing_section.append("facebook.com/videos")
borwsing_section.append("facebook.com/users")
borwsing_section.append("facebook.com/signup")

# print(borwsing_section)

# Remove item from the stack
last = borwsing_section.pop()
print(last)
# print(borwsing_section)
print("redirect to ",borwsing_section)

borwsing_section.pop()
borwsing_section.pop()
borwsing_section.pop()

print("redirect to ",borwsing_section)

# If browsing_section is not []
if not borwsing_section: 
    print("Disabled")

# Accessing the last item of the stack if it is not empty
last 
if not borwsing_section:

    last = borwsing_section[-1]