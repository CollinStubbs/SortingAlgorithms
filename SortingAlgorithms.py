class Sorting_algorithm:
    def bubblesort(self, ul):
        leng = len(ul)
        for x in range(leng, 0, -1):
            for y in range(leng, 0, -1):
                if(ul[x-1] > ul[y-1]):
                    holder = ul[x-1]
                    ul[x-1] = ul[y-1]
                    ul[y-1] = holder

                


newList = [1,3,5,4,6,2,7,9,8]

sorter = Sorting_algorithm()
sorter.bubblesort(newList)