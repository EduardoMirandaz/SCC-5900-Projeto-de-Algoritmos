import sys

def build_lps(pattern):
    lps = [0] * len(pattern)

    prefix_length = 0
    current_position = 1

    while current_position < len(pattern):
        if pattern[current_position] == pattern[prefix_length]:
            prefix_length += 1
            lps[current_position] = prefix_length
            current_position += 1

        elif prefix_length > 0:
            prefix_length = lps[prefix_length - 1]

        else:
            lps[current_position] = 0
            current_position += 1

    return lps


def kmp_search(pattern, text):
    lps = build_lps(pattern)

    pattern_index = 0
    text_index = 0

    while text_index < len(text):

        if pattern[pattern_index] == text[text_index]:
            pattern_index += 1
            text_index += 1

        if pattern_index == len(pattern):
            print(text_index - pattern_index)
            pattern_index = lps[pattern_index - 1]

        elif text_index < len(text) and pattern[pattern_index] != text[text_index]:

            if pattern_index > 0:
                pattern_index = lps[pattern_index - 1]
            else:
                text_index += 1


all_lines = sys.stdin.readlines()

current_line = 0

while current_line < len(all_lines):

    while current_line < len(all_lines) and all_lines[current_line].strip() == "":
        current_line += 1

    if current_line >= len(all_lines):
        break

    pattern_length = int(all_lines[current_line].strip())
    current_line += 1

    pattern = all_lines[current_line].rstrip("\n")
    current_line += 1

    text = all_lines[current_line].rstrip("\n")
    current_line += 1

    kmp_search(pattern, text)

    print()