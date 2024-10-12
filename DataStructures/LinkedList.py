from Node import Node

class LinkedList:    
    def __init__(self,value):
        newNode = Node(value)
        self.__head = newNode
        self.__tail = newNode
        self.__length = 1

    def print_list(self):
        temp = self.__head
        while temp != None:
            print(f'{temp.value}->',end="")
            temp = temp.next
        print('None')

    def append(self, value):
        newNode = Node(value)
        if self.__head == None:
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.next = newNode
            self.__tail = newNode
        self.__length += 1
    
    def prepend(self, value):
        newNode = Node(value)
        if self.__head == None:
            self.__head = newNode
            self.__tail = newNode
        else:
            newNode.next = self.__head
            self.__head = newNode
        self.__length += 1

    def delete_first(self):
        temp = self.__head
        if self.__length == 0 or temp == None:
            return 
        else:
            self.__head = self.__head.next
        self.__length -= 1

    def delete_last(self):
        temp = self.__head
        pre = None
        if self.__length == 0 or self.__head == None: 
            return
        else:
            while temp.next != None:
                pre = temp
                temp = temp.next
        self.__tail = pre
        self.__tail.next = None
        self.__length -= 1
        del temp

    def get_head(self) -> None:
        print(F'Head: {self.__head.value}')

    def get_tail(self) -> None:
        print(F'Tail: {self.__tail.value}')

    def get_length(self) -> None:
        print(F'Length: { self.__length }')
