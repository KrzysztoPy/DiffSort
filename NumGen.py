import random


class NumGen:
    num_of_test = 6
    range = (10, 20)
    # ,1000, 10000, 100000, 1000000
    range_tests = [(0, range[0]), (0, range[1])]
    # , (0, range[2]), (0, range[3]), (0, range[4]), (0, range[5])
    samples = []

    def get_interval(self):
        self.setting_tests(self.internal_or_external())

        print(self.num_of_test)
        print(self.range_tests)

    def internal_or_external(self):
        while True:
            answer = input("You want choice internal range? Y/N  ")
            if answer == "Y" or answer == "y" or answer == "N" or answer == "n":
                if answer == "N" or answer == "n":
                    self.range_test(answer)
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

    def range_test(self, answer):
        while True:
            for i in range(1, self.number_tests() + 1):
                try:
                    since = (int(input("Range test number {} from: ".format(i))))
                except ValueError:
                    print("You must give a number! Try again. ")
                try:
                    while True:
                        to = (int(input("Range test number {} from: ".format(i))))
                        if to > since:
                            self.range_tests.append((since, to))
                            break
                        elif to == "":
                            print("'to' can't be empty.")
                        else:
                            print(
                                "Range 'from': {} can't be greater since 'to': {}. Try again.  ".format(since, to))

                except ValueError:
                    print("You must give a number! Try again. ")
            self.sorting()

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
                    pass
                    break
            except ValueError:
                print("\nYou must choice number 1-8. Try again.\n")
        # insertion()
        # selection()
        # bubble()
        # shell()
        # merge()
        # heap()
        # quick()
        # quick3()

    def create_of_samples(self):
        tmp_table = []
        for t, i in self.range_tests:
            for j in range(t, i):
                tmp_table.append(random.randint(t, i))
            self.samples.append(tmp_table.copy())
            tmp_table.clear()

        print("Star \n")
        print(self.samples)
        print(self.samples.__len__())
        print("Stop \n")


    def insertion(self):
        # test_list = [1, 2, 1, 1, 2]
        sorted_list = []
        list_with_biggest = []
        for unsort in self.samples:

            if sorted_list.__len__() == 0:
                sorted_list.append(unsort)

            elif unsort > sorted_list[sorted_list.__len__() - 1]:
                sorted_list.append(unsort)

            elif unsort == sorted_list[sorted_list.__len__() - 1]:
                sorted_list.append(unsort)

            elif unsort < sorted_list[sorted_list.__len__() - 1]:
                list_with_biggest.append(sorted_list[sorted_list.__len__() - 1])
                sorted_list.pop()

                for sort in range(sorted_list.__len__(), 0, -1):
                    if sort > unsort:
                        list_with_biggest.append(sorted_list[sorted_list.__len__() - 1])
                        sorted_list.pop()

                    elif sort == unsort:
                        sorted_list.append(unsort)
                        list_with_biggest.reverse()
                        sorted_list.extend(list_with_biggest.copy())
                        list_with_biggest.clear()
                        break
        print(sorted_list)


def menu():
    num_gen = NumGen()
    # num_gen.setting_tests()
    # num_gen.sorting()
    num_gen.create_of_samples()
    # num_gen.insertion()


menu()
