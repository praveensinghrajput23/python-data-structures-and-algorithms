import ctypes


class List:
    def __init__(self) -> None:
        self.size = 1
        self.n = 0

        # Create a C type array with size = self.size
        self.A = self.__make_array(self.size)

    def __make_array(self, capacity):
        # Create a C type array(static or fixed, referential) wth size capacity
        return (capacity * ctypes.py_object)()

    def __len__(self):
        return self.n

    def __resize(self, new_capacity):
        # create new array with new capacity
        new_array = self.__make_array(new_capacity)

        # assigning the size of the new array
        self.size = new_capacity

        # iterate over the n and assing the values of old array to new array
        for i in range(self.n):
            new_array[i] = self.A[i]

        # assign the old array as the new array
        self.A = new_array

    def __str__(self):
        # [1,2,3]
        result = ""
        for i in range(self.n):
            result += str(self.A[i]) + ","
        return "[" + result[:-1] + "]"

    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        return "IndexError: Index is out of range"

    def append(self, item):
        if self.n == self.size:
            # have to resize the array becuase there is no vacant space in the array\
            self.__resize(self.size + 8)

        # append if space is available
        self.A[self.n] = item
        self.n += 1  # self.n = self.n + 1

    def pop(self):
        if self.n == 0:
            return "Empty List"
        print(self.A[self.n - 1])
        self.n -= 1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return "ValueError: Not in list"

    def insert(self, pos, value):
        # check whether the size of list is equal to the total item present in the list
        if self.size == self.n:
            # resize the list is there is no space available
            self.__resize(self.size * 2)

        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i - 1]

        self.A[pos] = value
        self.n += 1

    def __delitem__(self, pos):
        if 0 < pos < self.n:
            for i in range(pos, self.n - 1):
                self.A[i] = self.A[i + 1]
            self.n -= 1

    def remove(self, item):
        index = self.find(item)
        if isinstance(index, int):
            self.__delitem__(index)
        else:
            return index

    def sort(self, reverse=None, key=None):
        # TODO: functionality for key arugument in list sort
        for i in range(self.n):
            if not self.__len__() - 1 == i:
                if reverse:
                    if self.A[i] < self.A[i + 1]:
                        self.A[i], self.A[i + 1] = self.A[i + 1], self.A[i]
                        self.sort(reverse=True)
                else:
                    if self.A[i] > self.A[i + 1]:
                        self.A[i], self.A[i + 1] = self.A[i + 1], self.A[i]
                        self.sort()
        return self

    def min(self):
        # TODO: currently work for list of integers
        sorted_list = self.sort(reverse=None)
        return sorted_list[0]

    def max(self):
        # TODO: currently work for list of integers
        sorted_list = self.sort(reverse=True)
        return sorted_list[0]

    def sum(self, start=None):
        result = 0
        for i in range(self.n):
            if isinstance(self.A[i], int):
                result += self.A[i]
            else:
                return "ValueError: all items should be integers"
        if start and isinstance(start, int):
            result += start
        return result


L = List()
L.append(1)
L.append(3)
L.append(-1)
L.append(23)
print(L)

L.sort(reverse=None)
print(L)

print(L.min())
print(L.max())
print(L.sum())
print(L.sum(start=20))

# # An object of Class List
# L = List()

# # Type of object
# print(type(L))


# # Length of List
# print(len(L))


# # append the items in new array
# L.append(1)
# L.append(2)
# L.append(1111)
# L.append(324)

# print(len(L))
# print(L)


# # Get the item from given index
# # item at index 2
# print(L[2])

# # when given index is out of ranges
# print(L[5])

# # pop item from list
# L.pop()
# print(L)


# # clear the list
# L.clear()
# print(L)

# # find the item in the list
# # append the items in new array
# L.append(1)
# L.append(2)
# L.append(1111)
# L.append(324)

# L.find(1111)
# print(L)


# # insert the item into the list

# L.insert(3, "ram")
# print(L)

# # delter the item from the list for given index

# del L[3]
# print(L)
# remove the item from the list
# print(L)
