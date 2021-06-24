
class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.capacity = capacity
        self.heap_list = [None]

    def enqueue(self, item):
        """inserts "item" into the heap, returns true if successful, false if there is no room in the heap"""
        successful = True
        if item is None:
            return not successful
        if self.get_size() + 1 <= self.capacity:
            self.heap_list.append(item)
            self.perc_up(self.get_size())
            return successful
        else:
            return not successful

    def peek(self):
        """returns max without changing the heap, returns None if the heap is empty"""
        if self.is_empty():
            return None
        return self.heap_list[1]

    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty"""
        if self.is_empty():
            return None
        max = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1]
        self.heap_list = self.heap_list[:-1]
        self.perc_down(1)
        return max

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)"""
        if self.is_empty():
            return []
        return self.heap_list[1:]

    def build_heap(self, alist):
        """Builds a heap from the items in alist and builds a heap using the bottom up method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased"""

        i = len(alist) // 2
        self.heap_list = [None] + alist
        while i > 0:
            self.perc_down(i)
            i -= 1

    def is_empty(self):
        """returns True if the heap is empty, false otherwise"""
        return self.heap_list == [None]

    def is_full(self):
        """returns True if the heap is full, false otherwise"""
        return len(self.heap_list) - 1 == self.capacity

    def get_capacity(self):
        """this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return self.capacity

    def get_size(self):
        """the actual number of elements in the heap, not the capacity"""
        return len(self.heap_list) - 1

    def perc_down(self, i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""

        if not self.is_empty():
            heap = self.heap_list

            temp = heap[i]
            while i * 2 <= self.get_size():  # checks if there is a left in the tree
                if i * 2 + 1 <= self.get_size():  # checks for right child and sets the max of the left and right if True
                    max_child = max(heap[i * 2], heap[i * 2 + 1])
                    is_right = True
                else:
                    max_child = heap[i * 2]
                    is_right = False
                if max_child > temp:
                    if is_right and max_child == heap[
                        i * 2 + 1]:  # checks for right child and if the max is the right child
                        i = self.swap(i, i * 2 + 1)  # swaps with left and return index
                    else:
                        i = self.swap(i, i * 2)  # swapped and returns the swapped index
                else:
                    heap[i] = temp
                    break
            heap[i] = temp

    def swap(self, index, swapped_index):
        self.heap_list[index] = self.heap_list[swapped_index]
        return swapped_index

    def perc_up(self, i):
        heap = self.heap_list
        tempIndex = None
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""

        if not self.is_empty():
            temp = heap[i]
            while i > 1 and temp > heap[i // 2]:
                heap[i] = heap[i // 2]
                i = i // 2
            heap[i] = temp

    def n_list(self, n):
        arr = []
        for i in range(n):
            if self.get_size() <= 0:
                return arr
            else:
                arr.append(self.dequeue())
        return arr

def best_rate(n, item_costs, delivery_costs):

    # we are utilizing zip to form tuples of the lists, else we have to use (item_costs[i], delivery_costs[i])
    # using zip improves the code readability, nothing more.
    input_values_tuples = list(zip(list(item_costs), list(delivery_costs)))

    # print(input_values_tuples)

    d_costs = sorted(set(delivery_costs), reverse=True)
    # sorted_delivery_heap = MaxHeap(len(delivery_costs));
    # sorted_delivery_heap.build_heap(delivery_costs);
    # d_costs = sorted_delivery_heap.contents()

    maxHeap = MaxHeap()
    lister = []
    # print(d_costs)

    for d_cost in d_costs:
        # print(d_cost)
        max_queue = MaxHeap(len(input_values_tuples))
        for i_cost in input_values_tuples:
            if i_cost[1] >= d_cost:
                total = i_cost[0] + d_cost
                # print(f'{i_cost} ==> {total}')
                max_queue.enqueue(total)
        if max_queue.get_size() >= n:
            list_out = max_queue.n_list(n)
            my_list = [(i - d_cost, d_cost) for i in list_out]
            summation = sum(list_out)
            lister.append([summation , my_list])
            maxHeap.enqueue(summation)  #
            # print(f'{my_list} : {sum(list_out)}')

    print(lister)

    highest_price = maxHeap.peek()
    return ([i[1] for i in lister if i[0] == highest_price][0], highest_price)

# Driver Code
if __name__ == "__main__":

    input_file = open('inputPS9.txt')
    num_tests = int(input_file.readline().rstrip())
    test_inputs = [i.rstrip() for i in input_file.readlines()]
    # print(test_inputs[:])
    input_file.close()

    test_no = 0
    output_list = []
# The if condition at the end is to limit the number of tests to the number specified up top.
    chunks = [test_inputs[x:x+3] for x in range(0, len(test_inputs), 3) if x < num_tests*3]

    # warning message in-case the test number is greater than the inputs.
    if num_tests > len(chunks):
        print(f"\x1b[2;31m[WARN] The number of tests [{num_tests}] specified was greater than the inputs [{len(chunks)}] present.\x1b[0;0m")

    for n in chunks:
        n1 = [int(x) for x in n[0].split()]
        item_costs = [int(x) for x in n[1].split()]
        delivery_costs = [int(x) for x in n[2].split()]

        test_no += 1

        if(len(item_costs) == len(item_costs) == n1[0]):
            output = best_rate(n1[1], item_costs, delivery_costs)
            # print(f"Test Number {test_no} : {output[0]} ==> {output[1]}")
            output_list.append(f"Test Number {test_no} : {output[0]} ==> {output[1]}")
        else:
            raise Exception(f"{n}: elements don't match the number specified")

    file = 'outputPS9.txt'
    with open(file, 'w') as out_file:
        out = out_file.write('\n'.join(output_list))
        if out > 0:
            print("[outputPS9.txt] written.")