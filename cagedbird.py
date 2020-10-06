from random import sample

caged_bird = "poem.txt"
infile = open("poem.txt", "r")
infile.readlines(caged_bird)

def get_file_lines(caged_bird):
    lines_list = ["caged_bird"]
    return lines_list

def lines_printed_backward(caged_bird):
    lines_list = ["caged_bird"]
    return lines_list[::,-1]

def lines_printed_random(caged_bird):
    lines_list = "poem.txt" 
    lines = open(lines_list, "r").read().splitlines()

    for i in sample(lines, i=len(lines)):
        return lines

def lines_printed_custom(caged_bird):
    lines_list = ["caged_bird"]
    return lines_list


print(get_file_lines(caged_bird))

print(lines_printed_backward)

print(lines_printed_random)

print str(lines_printed_custom[9:12, 21:24, 32:34, 39:43]))