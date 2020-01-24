#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    Since we have n * n * n, it is the same thing as n^3, so it would start with O(n^3), however, in the while loop, we are adding a + n * n and we are restarting the loop
    that is the asme thing as n^2. Take out n^2 out of n^3 and we are left with ```O(n)```

b)
    sum = 0
    for i in range(n):      O(n) - Since this loop will run up to as many times as `n` 
      j = 1
      while j < n:          O(log n) - Since it will go up to the `n` but at since we have a line of j*=2 it will not increment 1 by 1, therefore it will get to `n` much faster
        j *= 2
        sum += 1
    
    Since the while loop is nested inside of the for loop, and it will perform the same amount of operations each time the for loop runs, the function will be ```O(n log n)```
    
    for example, n = 10
    the for loop will run 10 times which is O(n)
    the while loop will activate 10 times, but every time it loops, J will start from 1 and it will increase by 2 times, so first we have 1 * 2 = 2, then 2*2 = 4, then 4*2 = 8, then 8*2 = 16 which is larger than `n` at this point and the while loop will stop, so it didn't run 10 times within each for loop, therefore we cannot say the whole function is O(n^2)


c)
    def bunnyEars(bunnies):
        if bunnies == 0:
            return 0

        return 2 + bunnyEars(bunnies-1)        O(n) - because once bunnies will get down to zero, it will start returning. The 2 at the beginning doesn't affect anything, because it doesn't get added until the depth of the recursion reches it's bottom
        For example:
            If bunnies equals 10 at the beginnig, each time recursion occurs, it will decrement until it reaches 0, which makes the depth in this case 10. Then 2 is gonna get added up to itself 10 times, and it will give us 20, but the recursion depth was still the same number as bunnies, therefore it's ```O(n)```

## Exercise II

Floors are ordered, so we don't need to sort them.

We will take an `n` number of floors, and drop an egg from each floor. Starting from the first floor
and going up to the last floor. Since we are dropping an egg from each floor, we will determine which one is the first floor that the egg breaks from, and we will take that number as our reesult

EX:

for floor_num in range(1, n + 1):  
                                    Since range only goes UP to the specified number, but not including that number, that'w why we add +1 to `n`
    if egg-drop == egg-break:
        return floor_num            
                                    `egg-drop` and `egg-break` are arbitrary key words representing drop and a break of an egg
    return None
                                    If an egg doesn't break from any floor, than it fill return None

Since this is a for loop, it will run as many times as there are `n` number of Floors in the buildngs, so the Time Complexity would be ```O(n)```


