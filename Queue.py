from LinkedList import LinkedList

class Queue:
    def __init__(self):
        self.__length = 0
        self.__linked_list = LinkedList()

    def enqueue(self, data):
        self.__linked_list.add_last(data)
        self.__length += 1

    def dequeue(self):
        data = self.__linked_list.get_first()
        self.__linked_list.remove_first()
        if data != None:
            self.__length -= 1
        return data

    def peek(self):
        return self.__linked_list.get_first()

    def is_empty(self):
        return self.__length == 0

    def get_length(self):
        return self.__length

    def get_queue(self):
        return self.__linked_list.get_list()