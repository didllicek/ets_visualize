from process import *
from merge import *


def main():
    #1.copy the head of .csv file
    csv_header = 'Date,Time,uSec,F63 (Hz ),V63 (Volt),I63 (Amp),P63 (kW),RP63 (kvar),Eimp63 (kWh),Eimp63T (kWh),F64 (Hz),V64 (Volt),I64 (Amp),P64 (kW),RP64 (kvar),Eimp64 (kWh),Eimp64T (kWh),H64 Din T (degC)'

    #2.name of the output file
    csv_out = 'D:/energy_data/merged_data.csv'

    #3. write down absolute path to files with .csv files - as many as necessary
    csv_dir1='D:/belfast_ulster/DT85'
    csv_dir2='D:/belfast_ulster/2017'


    #4. write down time period you want to process
    start='2017/08/01'
    end='2018/07/31'

    #5. write down header name of the column with energy consumption data - as many as necessary
    column_name1='Eimp63 (kWh)'
    column_name2='Eimp64 (kWh)'


    #6. write down the limits for real consumption in an hour
    up_limit=1000
    down_limit=0


    #7. the code to create new merged file
    #merge_data(csv_header, start, end, csv_out, csv_dir1)


    #8. process data
    process_data(up_limit,down_limit,csv_out,column_name1,column_name2)

if __name__ == '__main__':
    main()

