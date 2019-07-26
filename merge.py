import os
import datetime as dt

def merge_data(csv_header, start, end, csv_out, *csv_dirs):

    start_date = dt.datetime.strptime(start, '%Y/%m/%d')
    end_date = dt.datetime.strptime(end, '%Y/%m/%d')
    csv_merge = open(csv_out, 'w')
    csv_merge.write(csv_header)
    csv_merge.write('\n')

    for csv_dir in csv_dirs:
        dir_tree = os.walk(csv_dir)
        for dirpath, dirnames, filenames in dir_tree:
            for f in filenames:
                file=os.path.abspath(os.path.join(dirpath, f))
                if (file.endswith('A.csv')):
                    csv_in = open(file)
                    for line in csv_in:
                        if (line.startswith(csv_header)):
                            pass
                        else:
                            tokens = [t.strip() for t in line.split(",")]
                            date = tokens[0]
                            try:
                                d = dt.datetime.strptime(date, '%Y/%m/%d')
                                if ((d <= end_date) and (d >= start_date)):
                                    csv_merge.write(line)
                            except:
                                pass
                    csv_in.close()

    csv_merge.close()

    file=open(csv_out)
    n=1
    d={}
    dates=open('dates.txt','w')
    for line in file:
        if(n>1):
            tokens = [t.strip() for t in line.split(",")]
            date=tokens[0]
            try:
                [year,month,day]=[t.strip() for t in date.split("/")]
                if(date in d):
                    d[date]+=1
                else:
                    d[date]=1
            except:
                pass
        else:
            n+=1
    sorted_d=sorted(d.items())
    for item in sorted_d:
        dates.write(str(item)+'\n')

    print('Verify consolidated CSV file : ' + csv_out)
