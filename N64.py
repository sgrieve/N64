# -*- coding: utf-8 -*-

with open('N64_wiki.csv', 'r') as f:
    headers = f.readline()
    lines = f.readlines()

output = []
PALname = []
ALTname = []

for line in lines:
    tmp = []
    output.append(','.join(line.split(',')[1:]))
    if '•' in line:
        splits = line.split(',')[0].split(' •')
        for split in splits:
            if 'PAL' in split:
                PALname.append(split.strip('\"').split('PAL')[0].split('NA')[0].split('JP')[0].split('FRA')[0].split('GER')[0].split('AUS')[0].split('BRZ')[0].split('UK')[0])
            else:
                tmp.append(split.strip('\"').split('PAL')[0].split('NA')[0].split('JP')[0].split('FRA')[0].split('GER')[0].split('AUS')[0].split('BRZ')[0].split('UK')[0])

        if not any('PAL' in word for word in splits):
            PALname.append(splits[0].strip('\"').split('PAL')[0].split('NA')[0].split('JP')[0].split('FRA')[0].split('GER')[0].split('AUS')[0].split('BRZ')[0].split('UK')[0])

        ALTname.append(tmp)
    else:
        PALname.append(line.split(',')[0].strip('\"').split('PAL')[0].split('NA')[0].split('JP')[0].split('FRA')[0].split('GER')[0].split('AUS')[0].split('BRZ')[0].split('UK')[0])
        ALTname.append(['-'])

with open('N64_cleaned.csv', 'w') as w:

    w.write(headers.split(',')[0] + ',\"Alternative title(s)\",' + ','.join(headers.split(',')[1:]))
    for p, a, o in zip(PALname, ALTname, output):
        w.write(('{0},{1},{2}').format(p, ' | '.join(a), o))
