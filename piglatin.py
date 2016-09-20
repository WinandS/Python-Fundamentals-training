def to_piglatin(word):
    i = 0
    dot = ''
    if word[-1] == '.':
        word = word[:-1]
        dot = '.'
    while word[i] not in "aeuio":
        i += 1
    piglatin = "{a}-{b}ay{c}".format(a=word[i:], b=word[:i], c=dot)
    return piglatin


def from_piglatin(piglatin):
    index_end = piglatin.index("-")
    index_middle = piglatin.index("ay", index_end)
    end = piglatin[:index_end]
    start = piglatin[index_end+1:index_middle]
    piglatin = "{start}{end}".format(start=start, end=end)

    return piglatin


if __name__ == "__main__":
    def main(input_file, output_file):
        with open(input_file, 'r') as inf:
            with open(output_file, 'w+') as outf:
                for line in inf:
                    for word in line.split():
                        outf.write(to_piglatin(word)+" ")
                    outf.write("\n")

    main("piglatin_input.txt", "piglatin_output.txt")
