import unittest

from src.maxHeap import *


class TestHeap(unittest.TestCase):

    def test_01_enqueue(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertTrue(insert)
        self.assertEqual(test_heap.contents(), [10, 6, 9, 2, 5, 7, 8])

        test_heap = MaxHeap(10)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertTrue(insert)
        self.assertEqual(test_heap.contents(), [10, 6, 9, 2, 5, 7, 8])
        insert = test_heap.enqueue(10)
        self.assertEqual(test_heap.contents(), [10, 10, 9, 6, 5, 7, 8, 2])

        test_heap = MaxHeap(6)  # no room in the list
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        original_heap = test_heap.contents()
        insert = test_heap.enqueue(10)
        self.assertFalse(insert)
        self.assertEqual(test_heap.contents(), original_heap)  # heap shouldn't be modified from the original

        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(None)
        original_heap = test_heap.contents()
        self.assertFalse(insert)
        self.assertEqual(test_heap.contents(), original_heap)

    def test_02_dequeue(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.dequeue(), 9)
        self.assertEqual(test_heap.get_size(), 5)
        self.assertEqual(test_heap.contents(), [8, 6, 7, 2, 5])

        self.assertEqual(test_heap.dequeue(), 8)
        self.assertEqual(test_heap.dequeue(), 7)
        self.assertEqual(test_heap.dequeue(), 6)
        self.assertEqual(test_heap.dequeue(), 5)
        self.assertEqual(test_heap.dequeue(), 2)

        self.assertEqual(test_heap.contents(), [])

        print(test_heap.dequeue())

    #
    def test_03_heap_contents(self):
        test_heap = MaxHeap(8)
        test_heap.build_heap([1, 2, 3])
        self.assertEqual(test_heap.contents(), [3, 2, 1])

    # #
    def test_04_build_heap(self):
        test_heap = MaxHeap(8)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

        test_heap = MaxHeap(8)
        test_heap.build_heap([])
        self.assertEqual(test_heap.contents(), [])

    def test_peek(self):
        test_heap = MaxHeap(10)
        self.assertEqual(test_heap.peek(), None)
        test_heap.enqueue(10)
        self.assertEqual(test_heap.peek(), 10)

    # #
    def test_05_is_empty(self):
        test_heap = MaxHeap(5)
        self.assertTrue(test_heap.is_empty())

        test_heap = MaxHeap(5)
        test_heap.enqueue(4)
        self.assertFalse(test_heap.is_empty())

        test_heap = MaxHeap(0)
        # test_heap.enqueue(4)
        self.assertTrue(test_heap.is_empty())

    def test_06_is_full(self):
        test_heap = MaxHeap(5)
        built = test_heap.build_heap([1, 2, 3, 4, 5])
        self.assertTrue(test_heap.is_full())

        test_heap = MaxHeap(0)
        built = test_heap.build_heap([])
        self.assertTrue(test_heap.is_full())

    def test_07_get_heap_cap(self):
        test_heap = MaxHeap()
        self.assertEqual(test_heap.get_capacity(), 50)
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertEqual(test_heap.get_capacity(), 7)

    def test_08_get_size(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.get_size(), 6)
        test_heap.enqueue(10)
        self.assertEqual(test_heap.get_size(), 7)
        test_heap.build_heap([])
        self.assertEqual(test_heap.get_size(), 0)

    def test_09_perc_down(self):  # tested without build heap but works for basic left and right perc
        test_heap = MaxHeap(5)
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        self.assertTrue(test_heap.contents(), [9, 6, 8, 2, 5, 7])
        test_heap.perc_down(1)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

        test_heap.heap_list = [None, 2, 6, 8, 9, 5, 7]
        test_heap.perc_down(1)
        self.assertEqual(test_heap.contents(), [8, 6, 7, 9, 5, 2])

        test_heap.build_heap([1])
        test_heap.perc_down(1)
        self.assertEqual(test_heap.contents(), [1])

        test_heap.build_heap([])
        test_heap.perc_down(1)
        self.assertEqual(test_heap.contents(), [])

    def test_10_perc_up(self):  # passes prelim tests and works so far
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_up(5)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])  # tested on [None, 60, 90, 80, 70, 100, 50, 40]

    def test_11_heap_sort_ascending(self):
        test_heap = MaxHeap(5)
        test_heap.build_heap([5, 4, 3, 2, 1])
        self.assertEqual(test_heap.contents(), [5, 4, 3, 2, 1])

        list1 = [2, 9, 7, 6, 5, 8]
        test_heap.heap_sort_ascending(list1)
        self.assertEqual(list1, [2, 5, 6, 7, 8, 9])


if __name__ == "__main__":
    unittest.main()