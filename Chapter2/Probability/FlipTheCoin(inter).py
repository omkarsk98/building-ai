def count11(seq):
   # define this function and return the number of occurrences as a number
   cnt = 0
   for i in range(0, len(seq) - 1):
        print("index:", i)
        if seq[i] == 1 and seq[i + 1] == 1:
            print("Found at index:", i)
            cnt += 1
   return cnt

print(count11([0, 0, 1, 1, 1, 0])) # this should print 2
