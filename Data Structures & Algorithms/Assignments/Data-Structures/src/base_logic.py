class MaxHeap:
    def __init__(self):
        self.maxHeap = []

    def get_length(self):
        return len(self.maxHeap)

    def put(self, item):
        self.maxHeap.append(item)
        self.bubble_up()

    def pop(self):
        if self.get_length() == 0:
            raise Exception('Empty heap')
        if self.get_length() == 1:
            return self.maxHeap.pop()
        max = self.maxHeap[0]
        self.maxHeap[0] = self.maxHeap.pop()
        self.bubble_down()
        return max

    def buildHeap(self, list=[]):
        self.maxHeap = list
        index = self.get_length() // 2 - 1
        while index >= 0:
            self.bubble_down(index)
            index -= 1

    def bubble_up(self):
        child = self.get_length() - 1
        parent = self.get_parent(child)
        while child > 0 and self.maxHeap[parent] < self.maxHeap[child]:
            self.swap(parent, child)
            child = parent
            parent = self.get_parent(child)

    def bubble_down(self, parent=0):
        left, right = self.get_children(parent)
        max_child = self.max_child(left, right)
        while max_child > 0 and self.maxHeap[parent] > self.maxHeap[max_child]:
            self.swap(max_child, parent)
            parent = max_child
            left, right = self.get_children(parent)
            max_child = self.max_child(left, right)

    def max_child(self, left, right):
        if left < self.get_length() and right < self.get_length():
            if self.maxHeap[left] > self.maxHeap[right]:
                return left
            else:
                return right
        elif left < self.get_length():
            return left
        else:
            return -1

    def swap(self, i, j):
        self.maxHeap[i], self.maxHeap[j] = self.maxHeap[j], self.maxHeap[i]

    def get_parent(self, child):
        if child % 2 != 0:
            return (child - 1) // 2
        else:
            return (child - 2) // 2

    def get_children(self, parent):
        left = 2 * parent + 1
        right = 2 * parent + 2
        return left, right

    def getNitems_inOrder(self, n):
        arr = []
        for i in range(n):
            if self.get_length() <= 0:
                return arr
            else:
                arr.append(self.pop())
        return arr

    def peek_at_root(self):
        root = self.maxHeap[0]
        return root

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

    def size(self):
        return len(self.queue)

    def n_list(self, n):
        arr = []
        for i in range(n):
            if len(self.queue) <= 0:
                return arr
            else:
                arr.append(self.delete())
        return arr


# Driver Code
if __name__ == "__main__":
    '''     
            Sample input
            1
            5 3
            8 7 2 6 10
            1 5 8 4 8

  Hint: The idea of this solution is to first sort the data based on delivery costs, 
  Pickup m-1 items with the highest prices using a heap. 
  And then select one item based on delivery cost + price that maximizes the total cost. 
  If value is repeated, select that only one item

    '''
    n = 3
    # (item,delivery)

    item_costs = [8, 7, 2, 6, 10, 13, 14, 22, 30]
    delivery_costs = [1, 5, 8, 4, 8, 3, 2, 1, 2]

    input_values_tuples = [(8, 1), (7, 5), (2, 8), (6, 4), (10, 8), (13, 3), (14, 2), (22, 1), (30, 2)]

    d_costs = sorted(set(delivery_costs), reverse=True)
    maxHeap = MaxHeap()
    lister = []
    print(d_costs)

    for d_cost in d_costs:
        print(d_cost)
        max_queue = PriorityQueue()
        for i_cost in input_values_tuples:
            if i_cost[1] >= d_cost:
                total = i_cost[0] + d_cost
                # print(f'{i_cost} ==> {total}')
                max_queue.insert(total)
        if max_queue.size() >= n:
            list_out = max_queue.n_list(n)
            my_list = [(i - d_cost, d_cost) for i in list_out]
            summation = sum(list_out)
            lister.append([summation , my_list])
            maxHeap.put(summation)
            # print(f'{my_list} : {sum(list_out)}')

    print(maxHeap.peek_at_root())
    print([i[1] for i in lister if i[0] == maxHeap.peek_at_root()])