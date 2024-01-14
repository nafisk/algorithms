'''
Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.

Write a program to move the disks from the first tower to the last using stacks.

Hints: #144: Try the Base Case and Build approach
#224: You can easily move the smallest disk from one tower to another. Ifs also pretty easy to move the smallest two disks from one tower to another. Can you move the smallest three disks?
#250: Think about moving the smallest disk from tower X=0 to tower Y=2 using tower Z=1 as a temporary holding spot as havingasolutionforf(l, X=0, Y=2, Z=l). Moving thesmallesttwodisksisf(2, X=0, Y=2, Z=l).Giventhatyouhaveasolutionfor f(l, X=0, Y=2, Z=l)andf(2, X=0, Y=2, Z=l),canyousolvef(3, X=0, Y=2, Z=l)?
#272: Observe that it doesn't really matter which tower is the source, destination, or buffer. Youcandof{3, X=0, Y=2, 2=1) byfirstdoingf(2, X=0, Y=l, 2=2) (moving two disks from tower Oto tower 1, using tower 2 as a buffer), then moving disk 3 from towerOtotower2,thendoingf(2, X=l, Y=2, 2=0) (movingtwodisksfromtower 1 to tower 2, using tower Oas a buffer). How does this process repeat?
, #318: If you're having trouble with recursion, then try trusting the recursive process more. Once you've figured out how to move the top two disks from tower Oto tower 2, trust that you have this working. When you need to move three disks, trustthat you can move two disks from one tower to another. Now, two disks have been moved. What do you do about the third 
'''

def tower_hanoi(n, a, b, c):
    if n == 1:
        print("move the 1st disc from ", a, "to ", c)
        return
    tower_hanoi(n - 1, a, c, b)
    print("move ", n, "th disk from ", a, " to ", c)
    tower_hanoi(n - 1, b, a, c)