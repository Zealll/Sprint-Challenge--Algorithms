class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        self.set_light_on()
        # Make our light as a turning on/off switch for our loops


        if self._item == None:
            self.swap_item()
        # This swaps the 0th index with whatever we are holding at the very beginning,
        # which is `None`.
        # We could have nested it inside of the while loop, and done this every time
        # the loop started, but it is not necessary, because we will need to switch
        # the item on the 0th index each time, so performing this at the very 
        # beginning of the whole function is more efficient.

        while self.light_is_on():
            # As I said, light will be a switch for the function itself, so the parent while loop
            # will look at that.


            self.set_light_off()
            # When the while loop runs, we shut the light off right away. It prevents are from Anno 1800
            # infinite loop. How the while loop will re-activate, will be descussed below.


            # Even tho we shut of the light, these two children while loops will activate no matter what
            while self.can_move_right():
            # This activates if we aren't on the end of the array, so we start by moving from left to right
                self.move_right()
                # The reason we want to move right at the very beginning of the while loop is because,
                # at the very beginning of the function we did a swap on the 0th index:
                #                         # if self._item == None:
                #                         #     self.swap_item()
                # as discussed, these two lines swapped the first element with `None`
                # so when we start the child while loop, we don't care about the 0th index, because we know that
                # it's None. So we move to the right, and then do a check below


                if self.compare_item() == -1:
                    self.swap_item()
                # If what we are holding is less than the value that's on the current index, than swap that item,
                # so that we grab a larger item, and do this till we reach the end of the array. This will ensure that
                # when we reach the end of the array for the first time, we have are HOLDING the biggest element, However,
                # this will not replace the item on the last element, because our condition says to only switch it when 
                # we are holding an item that is LESS than what's located on the current index. And, since we are at the end
                # of the array, it will exit the first child while loop, and move to the second one.


            while self.can_move_left():
            # Now since we are at the end of the array, that means we can move left, so this loop will activate.

                if self.compare_item() == 1:
                    self.swap_item()
                # Remeber how I said that by the time we get to the last index in the previous loop, we are HOLDING the
                # largest item, but it won't replace it? Well this is where that issue is being taken care of.
                # Now, in the first while loop, we are moving to the right at the beginning, and THEN we are running
                # our "if" conditional. However, we aren't moving left first in THIS while loop, because, since the 
                # last while loop didn't replace the last element with the largest item that we were HOLDING, this loop
                # needs to start from the last index, and this time check whether the value that we are holding is 
                # GREATER than the value that is on the index, and since I said that we will be holding the largest
                # value by the time we get to the end of the array, the last element will be less than what we are holding.
                # So the Swap will activate, and we will place the largest element at the end of the array.

                elif self.compare_item() == -1:
                    self.set_light_on()
                # Now this here is how we re-activate our parent while loop. If we come across a vallue that is greater than the 
                # item that we are holding, that means that the item is not sorted yet, because we are coming from backwards, so if 
                # we pick up a zero at the end of the array, and we come across a number bigger than zero, that means that it is not sorted
                # so we re-run the big while loop
                

                self.move_left()
                # And finally we move one step to the left, and we continue this proccess until we reach the index 0 again. But since we are moving
                # AFTER our if conditionals, we never run that "if" conditional at the 0th index, so the 0th index never gets swapped in any of the children while loops.
                # So None will be the value of the 0th index. So these two loops will always sort from index 1 up to/including the last index. 
                # And when it is sorted `self.set_light_on()` will never activate, and we will exit the parent while loop, which brings us to the last line of code...
        
        self.swap_item()
        # And this is the last line of code. This code runs after the Parent while loop stops. Since we exited the parent while loop, that means that everything
        # from index 1 to the last index is sorted, and we are holding an item that should be on the 0th index. So we do the final swap, since the last line of code
        # put us on 0th index.
        # We could have done this inside of the parent for loop, but it will do the same thing over and over again, and is not gonna make any difference. So for then
        # code efficiency, it's better to put it after the parent while loop is done
        # return self._list


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)