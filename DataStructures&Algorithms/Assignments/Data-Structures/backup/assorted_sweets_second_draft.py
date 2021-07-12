def best_assorted_rate(assort_num, icosts, dcosts):
    """
    finds the assortment with the best rate among all combinations, for 'assortNum' number of sweets.
    """

    # we are utilizing zip to form tuples of the lists, else we have to use (icosts[i], dcosts[i]) with range(i)
    # using zip improves the code readability, nothing more.
    input_values_tuples = list(zip(list(icosts), list(dcosts)))

    num_of_items = len(icosts)
    # print(input_values_tuples)

    item_sort = MaxHeap(num_of_items)
    item_sort.heapsort(icosts)
    print(icosts)
    print(list(item_sort.contents()))

    # d_costs = sorted(set(dcosts), reverse=True)
    # using heap sort with loops to insert only the unique elements, as opposed to using set.
    d_costs_uniq = MaxHeap(num_of_items)
    for x in dcosts:
        if x not in d_costs_uniq.heap_list:
            d_costs_uniq.enqueue(x)

    # print(d_costs.contents())
    details = list()
    max_heap = MaxHeap(num_of_items)

    for d_cost in d_costs_uniq.contents():
        max_queue = MaxHeap(num_of_items)

        for i_cost in input_values_tuples:
            if i_cost[1] >= d_cost:
                total = i_cost[0] + d_cost
                max_queue.enqueue(total)
                # print(f'{i_cost} ==> {total}')

        if max_queue.get_size() >= assort_num:
            list_out = max_queue.n_list(assort_num)
            summation = sum(list_out)
            max_heap.enqueue(summation)
            # additional details
            details.append([summation , [(i - d_cost, d_cost) for i in list_out]])
            # print(f'{my_list} : {sum(list_out)}')

    rated_list = [i for i in details if i[0] == max_heap.peek()][0]
    # print(rated_list)

    return rated_list


class MaxHeap:

    def __init__(self, capacity=10):
        """
        The constructor is assigned a default capacity 10 to avoid failure upon insertion without heap creation.
        This value automatically gets overwritten on heap creation.
        """
        self.capacity = capacity
        self.heap_list = [None]  # None is a placeholder! it helps with indexing so that the root is at index 1.

    def enqueue(self, item):
        """
        inserts elements into the heap, returns true if successful,
         returns false if it exceeds heap capacity (default = 10).
        """
        successful = True
        if item is None:
            return not successful
        if self.get_size() + 1 <= self.capacity:
            self.heap_list.append(item)
            self.bubble_up(self.get_size())
            return successful
        else:
            return not successful

    def peek(self):
        """
        returns the maximum value at the root, without changing the heap, returns None if the heap is empty
        """
        if self.is_empty():
            return None
        return self.heap_list[1]

    def dequeue(self):
        """
        returns the maximum and removes it from the heap and restores the heap property
        returns None if the heap is empty
        """
        if self.is_empty():
            return None
        maxima = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1]  # swap with last element.
        self.heap_list = self.heap_list[:-1]  # shrink the size of the heap.
        self.bubble_down(1)
        return maxima

    def contents(self):
        """
        returns the `linear` list of contents stored in the `non linear` heap.
        """
        if self.is_empty():
            return []
        return self.heap_list[1:]

    def heapsort(self, alist):
        """
        creates a heap from the items in the list parameter using the BOTTOM-UP heapification method.
        ie. performs an "bubble_down" operation BOTTOM-UP - from leaves of the tree to the root
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased
        """

        i = len(alist) // 2
        self.heap_list = [None] + alist
        while i > 0:
            self.bubble_down(i)
            i -= 1

    def swap(self, index, swapped_index):
        """
        swaps the element in the first argument with the element in the second argument and returns the swapped index
        """
        self.heap_list[index] = self.heap_list[swapped_index]
        return swapped_index

    def bubble_down(self, i):
        """
        bubble_down moves the element stored at index i to its proper place in the heap rearranging elements,
         as it compares and swaps the node with one of its children
        """

        if not self.is_empty():
            heap = self.heap_list

            temp = heap[i]
            while i * 2 <= self.get_size():  # checks if there is a left in the tree
                if i * 2 + 1 <= self.get_size():  # checks for right child and sets the maximum of the left and right if True
                    max_child = max(heap[i * 2], heap[i * 2 + 1])
                    is_right = True
                else:
                    max_child = heap[i * 2]
                    is_right = False
                if max_child > temp:
                    if is_right and max_child == heap[ i * 2 + 1]:  # checks for right child and if the maximum is the right child
                        i = self.swap(i, i * 2 + 1)  # swaps with left and return index
                    else:
                        i = self.swap(i, i * 2)  # swapped and returns the swapped index
                else:
                    heap[i] = temp
                    break
            heap[i] = temp

    def bubble_up(self, i):
        """
        bubble_up moves the element stored at index i to its proper place in the heap rearranging elements,
         as it compares and swaps the node with its parent.
        """
        heap = self.heap_list

        if not self.is_empty():
            temp = heap[i]
            while i > 1 and temp > heap[i // 2]:
                heap[i] = heap[i // 2]
                i = i // 2
            heap[i] = temp

    def n_list(self, num):
        """
        grabs the top N elements in the heap based on the priority
        """
        arr = []
        for _ in range(num):
            if self.get_size() <= 0:
                return arr
            else:
                arr.append(self.dequeue())
        return arr

    def get_size(self):
        """
        number of elements in the heap occupying the array
        """
        return len(self.heap_list) - 1

    def is_empty(self):
        """
        returns True if the heap is empty, else false
        """
        return self.heap_list == [None]

    def is_full(self):
        """
        returns True if the heap is full, else false
        """
        return len(self.heap_list) - 1 == self.capacity

    def get_capacity(self):
        """
        this is the maximum number of a entries the heap can hold
        capacity of heap = original array size - 1
        """
        return self.capacity


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
    chunks = [test_inputs[x:x + 3] for x in range(0, len(test_inputs), 3) if x < num_tests * 3]

    # warning message in-case the test number is greater than the inputs. The code still executes with the Tests present.
    if num_tests > len(chunks):
        print(f"\x1b[2;31m[WARN] The number of tests [{num_tests}] specified was greater than the inputs [{len(chunks)}] present.\x1b[0;0m")

    for test in chunks:
        totalN, assortN = [int(x) for x in test[0].split() if len(test[0].split()) == 2]
        item_costs = [int(x) for x in test[1].split()]
        delivery_costs = [int(x) for x in test[2].split()]

        # print(totalN, assortN)

        test_no += 1

        if (len(item_costs) == len(delivery_costs)  == totalN):
            assorted_max, assorted_list = best_assorted_rate(assortN, item_costs, delivery_costs)
            # print(f"Test Number {test_no} : {output[0]} ==> {output[1]}")
            output_list.append(f"Test Number {test_no} : {assorted_max} ==> {assorted_list}")
        else:
            raise Exception(f"{test}: elements don't match the number specified")

    file = 'outputPS9.txt'
    with open(file, 'w') as out_file:
        out = out_file.write('\n'.join(output_list))
        if out > 0:
            print("[outputPS9.txt] written.")
