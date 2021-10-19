from os import listdir
import xlwt
import xlrd

current = "19.10"
cols = ["Meno", "Priezvisko", "12.10", "19.10"]
dirname = '../fotky.tmp'
infile = 'tomi.xls'
outfile = 'tomi.xls'

def write_from_hashmap(hashmap):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Fotky')

    # Write header row
    row = ws.row(0)
    for i in range(len(cols)):
        row.write(i, cols[i])

    # Write other rows
    i = 1
    for key in hashmap:
        row = ws.row(i)
        print(key)
        name, surname = key.split(' ', maxsplit=1)
        row.write(0, name)
        row.write(1, surname)
        for idx, col in enumerate(cols):
            if idx < 2:
                continue
            if col in hashmap[key]:
                row.write(idx, "1")
        i += 1

    wb.save(outfile)

def read_to_hashmap():
    hashmap = {}
    wb = xlrd.open_workbook(infile)
    ws = wb.sheet_by_index(0)
    # get days from existing sheet
    days = []
    for i in range(2, ws.ncols):
        days.append(ws.cell(0, i).value)

    # map sheet names to hashmap
    for i in range(1, ws.nrows):
        name = ws.cell(i, 0).value
        surname = ws.cell(i, 1).value
        fullname = ' '.join([name, surname])
        hashmap[fullname] = []
        for j in range(2, ws.ncols):
            if ws.cell(i, j).value == "1":
                hashmap[fullname].append(days[j-2])
    return hashmap

def update_hashmap(hashmap):
    data = listdir(dirname)
    data = list(map(lambda x: x.split('.')[0], data))
    data = list(map(lambda x: [x.split(' ')[0], ' '.join(x.split(' ')[1:])], data))
    for i in range(len(data)):
        joined = ' '.join(data[i])
        if joined not in hashmap:
            hashmap[joined] = [current]
        else:
            hashmap[joined].append(current)
    return hashmap


hashmap = read_to_hashmap()
hashmap = update_hashmap(hashmap)
write_from_hashmap(hashmap)