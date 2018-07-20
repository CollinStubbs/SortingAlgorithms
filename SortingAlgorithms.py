import datetime

class SortingAlgorithm:
    def linear_search(self, ul, start, end):
        num = ul[start]
        for x in range(start, end):
            if(ul[x] < num):
                num = ul[x]
        return num

    def bubble_sort(self, ul):
        leng = len(ul)
        for x in range(leng, 0, -1):
            for y in range(leng, 0, -1):
                if(ul[x-1] > ul[y-1]):
                    holder = ul[x-1]
                    ul[x-1] = ul[y-1]
                    ul[y-1] = holder

            print(ul)

    def selection_sort(self, ul):
        leng = len(ul)
        for x in range(0, leng-1):
            num = self.linear_search(ul, x, leng)
            index = ul.index(num)
            holder = ul[index]
            ul[index] = ul[x]
            ul[x] = holder

            print(ul)

    def insertion_sort(self, ul):
        leng = len(ul)
        for x in range(1, leng):
            num = ul[x]
            i = x
            while i>=1 and num < ul[i-1]:
                ul[i] = ul[i-1]
                i-=1
            ul[i] = num

            print(ul)










newList = [7,3,5,4,6,2,1,9,8]

sorter = SortingAlgorithm()
sorter.bubble_sort(newList)



