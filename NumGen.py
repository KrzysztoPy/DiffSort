import math
import random
import sys
import time


class NumGen:
    num_of_test = 6
    range = [10, 20, 1000, 10000, 100000]
    # ,100000 , 1000000
    range_tests = [(0, range[0]), (0, range[1]), (0, range[2]), (0, range[3]), (0, range[4])]
    #  , (0, range[5])
    samples = []
    sort_samples = []
    time_and_result = []

    # code sort name/ num elem / time / sorting elem
    list_with_results = []

    def get_interval(self):
        self.setting_tests(self.internal_or_external())

        print(self.num_of_test)
        print(self.range_tests)

    def internal_or_external(self):
        while True:
            answer = input("You want choice internal range? Y/N  ")
            if answer == "Y" or answer == "y" or answer == "N" or answer == "n":
                if answer == "N" or answer == "n":
                    self.range_test()
                else:
                    self.sorting()
                break
            else:
                print("You must choice option Y or N. Try again.")

    def setting_tests(self):
        self.internal_or_external()

    def number_tests(self) -> int:

        self.range_tests.clear()
        while True:
            try:
                self.num_of_test = int(input("How many you want make a tests: "))
                if self.num_of_test > 0 and self.num_of_test != "":
                    return self.num_of_test
                else:
                    print("Number of test must be greater from 0. Please try again.")
            except ValueError:
                print("You must give a number! Try again. ")

    def range_test(self):
        while True:
            for i in range(1, self.number_tests() + 1):
                while True:
                    while True:
                        try:
                            since = (int(input("Range test number {} from: ".format(i))))
                            break
                        except ValueError:
                            print("You must give a number! Try again. ")

                    while True:
                        try:
                            to = (int(input("Range test number {} to: ".format(i))))
                            break
                        except ValueError:
                            print("You must give a number! Try again. ")
                    if to > since:
                        self.range_tests.append((since, to))
                        break
                    elif to == "":
                        print("'to' can't be empty.")
                    else:
                        print("Range 'from': {} can't be greater since 'to': {}. Try again.  ".format(since, to))

            self.sorting()
            break

    def sorting(self):
        while True:
            try:
                choice_sort = int(input(
                    "Which sort choice? \n 1.insertion \n 2.selection \n 3.bubble \n 4.shell \n 5.merge \n 6.heap"
                    " \n 7.quick \n 8.quick3 \n choice: "))
                if choice_sort < 1 or choice_sort > 8:
                    print("\nYou must choice number 1-8. Try again.\n")
                else:
                    self.create_of_samples()
                    break
            except ValueError:
                print("\nYou must choice number 1-8. Try again.\n")

        if choice_sort == 1:
            self.insertion()
        elif choice_sort == 2:
            self.selection()
        elif choice_sort == 3:
            self.bubble()
        # self.shell()
        # self.merge()
        # self.heap()
        # self.quick()
        # self.quick3()

    def create_of_samples(self):
        tmp_table = []
        for t, i in self.range_tests:
            for j in range(t, i):
                tmp_table.append(random.randint(t, i))
            self.samples.append(tmp_table.copy())
            tmp_table.clear()

    def insertion(self):
        sorted_list = []
        list_with_biggest = []

        for part_sample in self.samples:
            start = time.time()
            for unsort in part_sample:

                if sorted_list.__len__() == 0:
                    sorted_list.append(unsort)

                elif unsort > sorted_list[sorted_list.__len__() - 1]:
                    sorted_list.append(unsort)

                elif unsort == sorted_list[sorted_list.__len__() - 1]:
                    sorted_list.append(unsort)

                elif unsort < sorted_list[sorted_list.__len__() - 1]:
                    list_with_biggest.append(sorted_list[sorted_list.__len__() - 1])
                    sorted_list.pop()

                    if sorted_list.__len__() == 0:
                        sorted_list.append(unsort)
                        list_with_biggest.reverse()
                        sorted_list.extend(list_with_biggest.copy())
                        list_with_biggest.clear()

                    else:
                        for sort in sorted_list[::-1]:
                            if sort > unsort:
                                list_with_biggest.append(sort)
                                sorted_list.pop()
                                if sorted_list.__len__() == 0:
                                    sorted_list.append(unsort)
                                    list_with_biggest.reverse()
                                    sorted_list.extend(list_with_biggest.copy())
                                    list_with_biggest.clear()

                            elif sort == unsort:
                                sorted_list.append(unsort)
                                list_with_biggest.reverse()
                                sorted_list.extend(list_with_biggest.copy())
                                list_with_biggest.clear()
                                break

                            elif sort < unsort:
                                sorted_list.append(unsort)
                                list_with_biggest.reverse()
                                sorted_list.extend(list_with_biggest.copy())
                                list_with_biggest.clear()
                                break
            stop = time.time()
            data_after_sort = [sys._getframe().f_code.co_name, sorted_list.__len__(), stop - start, sorted_list.copy()]
            self.list_with_results.append(data_after_sort.copy())
            data_after_sort.clear()
            sorted_list.clear()

    def selection(self):
        tmp_smaller = None
        the_same_smallest = None
        sorted_list = []
        tmp_sample_list = self.samples.copy()

        for separated_samples in tmp_sample_list:
            print("Start sorting. Number of samples: {}".format(separated_samples.__len__))
            start = time.time()
            for separated_list in range(0, separated_samples.__len__()):
                for unsort in separated_samples:
                    if tmp_smaller is None:
                        tmp_smaller = unsort
                    else:
                        if unsort < tmp_smaller:
                            tmp_smaller = unsort
                        elif unsort == tmp_smaller:
                            the_same_smallest = unsort
                            pass
                if the_same_smallest is not None:
                    sorted_list.append(tmp_smaller)
                    the_same_smallest = None
                    separated_samples.remove(tmp_smaller)
                    tmp_smaller = None
                else:
                    sorted_list.append(tmp_smaller)
                    separated_samples.remove(tmp_smaller)
                    tmp_smaller = None
            stop = time.time()
            data_after_sort = [sys._getframe().f_code.co_name, sorted_list.__len__(), stop - start, sorted_list.copy()]
            self.list_with_results.append(data_after_sort.copy())
            data_after_sort.clear()

    def bubble(self):

        # table = [0, 1, 1, 2, 1, 3, 3, 1, 1, 5]
        # tmp_sample_list = table.copy()
        tmp_sample_list = self.samples.copy()

        check_revers = False
        for separated_samples in tmp_sample_list:
            print("Start sorting {} . Number of samples: {}".format(sys._getframe().f_code.co_name,
                                                                    len(separated_samples)))
            start = time.time()
            while True:
                for index in range(len(separated_samples)):
                    if index != 0:
                        if separated_samples[index] < separated_samples[index - 1]:
                            tmp_bigger = separated_samples[index]
                            separated_samples[index] = separated_samples[index - 1]
                            separated_samples[index - 1] = tmp_bigger
                            check_revers = True
                if check_revers is False:
                    break
                else:
                    check_revers = False
            stop = time.time()

            data_after_sort = [sys._getframe().f_code.co_name, separated_samples.__len__(), stop - start,
                               separated_samples.copy()]
            # separated_samples.clear()
            self.list_with_results.append(data_after_sort.copy())

    def shell(self):
        table = [0, 1, 1, 2, 1, 3, 3, 1, 1, 5]

        divi = math.floor(math.sqrt(table ^ (4 / 3)))
        pass

    def get_sort_data(self):

        for general_data in self.list_with_results:
            print(
                "\n Sort type: {} \n Number elements: {} \n Sort time: {} \n Element sorts: {} ".format(general_data[0],
                                                                                                        general_data[1],
                                                                                                        general_data[2],
                                                                                                        general_data[
                                                                                                            3]))

    def tests(self):
        table = [0, 1, 1, 2, 1, 3, 3, 1, 5, 1]
        k = [n for n in table]
        print(math.floor(math.pow(4, (4 / 3))))
        print(math.floor(6.9999))
        # print(table)


def reverse(self):
    self.range.reverse()
    self.range_tests.reverse()


def menu():
    num_gen = NumGen()
    # num_gen.setting_tests()
    # num_gen.create_of_samples()
    # num_gen.sorting()
    # num_gen.reverse()

    # num_gen.insertion()
    num_gen.tests()
    # num_gen.bubble()
    # num_gen.selection()
    # num_gen.get_sort_data()


menu()
