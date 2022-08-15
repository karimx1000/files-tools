with open('cleaned_file.txt') as f:
    read = [i.strip() for i in f.readlines()]
with open('cleaned_file.txt', 'w') as f:
    f.write('\n'.join(read))
