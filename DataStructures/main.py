from LinkedList import LinkedList

linkedList = LinkedList(2)
linkedList.append(3)
linkedList.append(4)
linkedList.append(11)

linkedList.prepend(9)

linkedList.delete_last()

linkedList.append(12)
linkedList.prepend(45)
linkedList.append(8)
linkedList.prepend(10)

# linkedList.delete_first()

linkedList.get_head()
linkedList.get_tail()
linkedList.get_length()

linkedList.print_list()