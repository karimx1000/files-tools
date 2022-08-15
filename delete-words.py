infile = "combo.txt"
outfile = "cleaned_file.txt"

delete_list = ["Word1", "Word2", "Word3","Word4"]
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)
with open(outfile) as finn:
    for line in finn:
        line = line.rstrip()
        if line:
                print(line, end = '')
                fout.close()
