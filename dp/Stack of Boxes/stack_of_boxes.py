'''
Stack of Boxes: You have a stack of n boxes, with widths wi, heights h , and depths d • The boxes 11
cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly 
larger than the box above it in width, height, and depth. Implement a method to compute the height of 
the tallest possible stack. The height of a stack is the sum of the heights of each box.

#155 Will sorting the boxes help in any way?
#194 We can sort the boxes by any dimension in descending order. This will give us a partial
        order for the boxes, in that boxes later in the array must appear before boxes earlier in the array
#214 Try to break it down into sub problems.
#260 Think about the first decision you have to make. The first decision is which box will be at the bottom.
#322 Once we pick the box on the bottom, we need to pick the second box. Then the third box.
#368 Once you have a basic recursive algorithm implemented, think about if you can optimize it. Are there any repeated sub problems?
#378 Alternatively, we can think about the repeated choices as: Does the first box go on the stack? Does the second box go on the stack? And so on.

'''