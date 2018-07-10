from random import randint
def shuffle(the_list):

    # if it's 1 or 0 items, just return
    if len(the_list) <= 1:
        return the_list

    last_index_in_the_list = len(the_list) - 1

    # walk through from beginning to end
    for index_we_are_choosing_for in xrange(0, len(the_list)):

        # choose a random not-yet-placed item to place there
        # (could also be the item currently in that spot)
        # must be an item AFTER the current item, because the stuff
        # before has all already been placed
        random_choice_index = randint(index_we_are_choosing_for, last_index_in_the_list)

        # place our random choice in the spot by swapping
        the_list[index_we_are_choosing_for], the_list[random_choice_index] = the_list[random_choice_index], the_list[index_we_are_choosing_for]
