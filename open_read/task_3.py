def sort_files(files_path):
    dict_file = {}
    for file in files_path:
        with open(file, encoding='utf-8') as f:
            dict_file[file] = len(f.readlines())
    sorted_files = sorted(dict_file.items(), key=lambda x: x[1])

    with open('final.txt', 'a+', encoding='utf-8') as f:
        for file in sorted_files:
            with open(file[0], encoding='utf-8') as g:
                f.write(f'{file[0]}\n{file[1]}\n')
                for line in g:
                    f.write(line)
                f.write('\n')


sort_files(['1.txt', '2.txt', '3.txt'])
