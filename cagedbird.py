def get_file_lines(filename):
    in_file = open(filename, 'r')
    lines = in_file.readlines()
    in_file.close()
    return lines

def lines_printed_backwards(lines_list):
    lines_list.reverse()
    lines_length = len(lines_list)
    for i in range(lines_length):
        line = lines_list[i]
        line_num = lines_length - i
        print(f"{line_num} {line}")

from random import choice
def lines_printed_random(lines_list):
    for _ in lines_list:
        print(choice(lines_list))

def lines_printed_custom(lines_list):
    in_file = open(lines_list,'r')
    lines = in_file.readlines()
    lines.sort
    for _ in range(len(lines_list)):
        print(lines_list)
        
        

print(get_file_lines("poem.txt"))

poem_lines = get_file_lines('poem.txt')

lines_printed_backwards(poem_lines)

lines_printed_random(poem_lines)