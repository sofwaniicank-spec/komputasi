class node:
    def __init__(self,data):
        self.__data= data
        self.__next= None

        def get_data(self):
            return self.__data

        def st_data(self,next_node):
            self.__next = next_node

        def get_next(self):
            return self.__next

class LinkedList:
    def __init__(self,data):

        self.__head= None
        self.__tail= None
        self.__count= 0

    def add(self, data):
        new = Node(data)
        if self.__ head is None:
            self.__head = new  
            self.__tall = new
            self.__count +=1
        else:
            curr = self.__head
            while curr.get_next:
                curr = curr.get_next
            curr.set_next(new)
            self._tail = new 

    def prepend(self,data):
        new = Node(data)
        new.set.__next(self.__next)
        self.__head = new 
        if self.__tail is NOne:
            self.__tail = new
        self.__count + = 1

    def append(self,data):
        new =Node(data)

        if self.__head is None:
            self.__head = new
            self.__tail = new

        else:
            self.__tail.set_next(new)
            self.__tail =new
        self.__count +=1

    def __len__(self):
        return self.__count

    def _str__(self):
        hasil=[]
        curr = self.__head
        while curr:
            hasil.append(str(curr.get_data()))
            curr = curr.get_next()

        return "-->".join(hasil) + "-->"

        LList =LinkedList()

        LList.prepend("deqi") 
        LList.prepend("wawan")
        LList.prepend("arfin")
           


