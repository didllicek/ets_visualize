import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt


def prepare_dictionary(up_limit,down_limit,csv_out,column_names):
    file = open(csv_out)
    days_of_year=[{},{}]
    n=1
    for line in file:
        if(n==1):
            index0=0
            index1=0
            tokens = [t.strip() for t in line.split(",")]
            for token in tokens:
                if(token==column_names[0]): break;
                index0 += 1
            for token in tokens:
                if(token==column_names[1]): break;
                index1 += 1
        else:
            tokens = [t.strip() for t in line.split(",")]
            date=tokens[0]
            date_comp=dt.datetime.strptime(date, '%Y/%m/%d')
            if date_comp in days_of_year[0]:
                hours_of_day=[(days_of_year[0])[date_comp],(days_of_year[1])[date_comp]]
            else:
                hours_of_day=[{},{}]
                for i in range(0,24):
                    (hours_of_day[0])[i]=0
                    (hours_of_day[1])[i] = 0

            time=tokens[1]
            hour=int(time.split(':')[0])
            consumption=[float(tokens[index0]),float(tokens[index1])]
            for i in range(0,2):
                if ((consumption[i]>=down_limit) and (consumption[i]<=up_limit)):
                    (hours_of_day[i])[hour] += consumption[i]
                (days_of_year[i])[date_comp]= hours_of_day[i];
        n += 1;
    file.close()
    sorted_days_of_year0=dict(sorted((days_of_year[0]).items()))
    sorted_days_of_year1 = dict(sorted((days_of_year[1]).items()))
    return [sorted_days_of_year0,sorted_days_of_year1]


def vizualize_data(days_of_year,column_name):
    plt.figure(num=1, figsize=(10, 10), dpi=160, facecolor='w', edgecolor='k')
    colors = iter(plt.cm.rainbow(np.linspace(0, 1, len(days_of_year.keys()))))
    print(len(days_of_year.items()))
    frames=[]
    for day in days_of_year.keys():
        k = []
        # day="2018/02/09";
        energy_comsupted_hour_per_day = days_of_year[day]
        sorted_energy_comsupted_hour_per_day = sorted(energy_comsupted_hour_per_day.items())
        s = pd.DataFrame(sorted_energy_comsupted_hour_per_day, columns=['Time [h]', 'Energy Consumption [kWh]'+column_name])
        for i in range(0,24):
            k.append(day)
        #print(len(k))
        #print(day)
        s.insert(loc=0,value=k,column='Date',allow_duplicates=True)
        frames.append(s)
        plt.plot('Time [h]', 'Energy Consumption [kWh]'+column_name, data=s, color=next(colors), label=day)
        plt.gca().set_xlim([0, 23])
        plt.xlabel('Time [h]', fontsize=16)
        plt.ylabel('Energy Consumption [kWh]', fontsize=16)

    plt.savefig('plot' + column_name + '.png')
    plt.close()
    return frames

#def process_to_file(column_name):




def process_data(up_limit,down_limit,csv_out,*column_names):
    results={}
    ind=0;
    days_of_year = prepare_dictionary(up_limit, down_limit, csv_out, column_names)
    for column_name in column_names:
        frames=vizualize_data(days_of_year[ind],column_name)
        result=pd.concat(frames,ignore_index=True)
        results[column_name]=result
        ind+=1
        #print(result)

    #df=pd.merge(results[0], results[1], left_on='Date', right_on='Time')
    #df=pd.merge(results[0],results[1],suffixes=column_names)
    #df.to_csv('results.csv')

    #results[column_names[1]].drop('Time')
    #results[column_names[1]].index = results[column_names[0]].index

    (results[column_names[0]])['Energy Consumption [kWh]'+column_names[1]] = (results[column_names[1]])['Energy Consumption [kWh]'+column_names[1]]

    (results[column_names[0]]).to_csv('results.csv',index_label='index')







