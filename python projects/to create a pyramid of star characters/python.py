no = int(input("Type a no."))
# *******
#  *****
#   ***
#    *
character = "*"
space = " "


def pyramid_maker(x):
    no_of_spaces = 1
    no_of_char = 1
    i = 1
    while i <= x:
        print(space * (x - no_of_spaces), character * no_of_char)
        i += 1
        no_of_char += 2
        no_of_spaces += 1
    i = 1
    no_of_char -= 2
    no_of_spaces = no_of_char
    while i <= x:
        print(space * (no_of_spaces), character * no_of_char)
        i += 1
        no_of_char -= 2
        no_of_spaces += 1


pyramid_maker(no)
