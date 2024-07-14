import csv
from prettytable import PrettyTable
districts = {}


with open('2024_std_num_high_school.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["제외여부"] == "N":
            district = row['지역']
            if district not in districts:              
                districts[district] = {
                    '1학년(남)': 0, '1학년(여)': 0,
                    '2학년(남)': 0, '2학년(여)': 0,
                    '3학년(남)': 0, '3학년(여)': 0,
                    '1학년 전채 학생 수': 0, '2학년 전채 학생 수': 0, '3학년 전채 학생 수': 0,
                    '전채 학생 수': 0 
                }
            districts[district]['1학년(남)'] += int(row['1학년(남)'])
            districts[district]['1학년(여)'] += int(row['1학년(여)'])
            districts[district]['2학년(남)'] += int(row['2학년(남)'])
            districts[district]['2학년(여)'] += int(row['2학년(여)'])
            districts[district]['3학년(남)'] += int(row['3학년(남)'])
            districts[district]['3학년(여)'] += int(row['3학년(여)'])

    for district, data in districts.items():
        data['1학년 전채 학생 수'] = data['1학년(남)'] + data['1학년(여)']
        data['2학년 전채 학생 수'] = data['2학년(남)'] + data['2학년(여)']
        data['3학년 전채 학생 수'] = data['3학년(남)'] + data['3학년(여)']
        data['전채 학생 수'] = data['1학년 전채 학생 수'] + data['2학년 전채 학생 수'] + data['3학년 전채 학생 수']    

        if data['1학년 전채 학생 수'] != 0:
            data['1학년 남자 비율'] = data['1학년(남)'] / data['1학년 전채 학생 수'] * 100
            data['1학년 여자 비율'] = data['1학년(여)'] / data['1학년 전채 학생 수'] * 100
        else:
            data['1학년 남자 비율'] = data['1학년 여자 비율'] = 0

        if data['2학년 전채 학생 수'] != 0:
            data['2학년 남자 비율'] = data['2학년(남)'] / data['2학년 전채 학생 수'] * 100
            data['2학년 여자 비율'] = data['2학년(여)'] / data['2학년 전채 학생 수'] * 100
        else:
            data['2학년 남자 비율'] = data['2학년 여자 비율'] = 0

        if data['3학년 전채 학생 수'] != 0:
            data['3학년 남자 비율'] = data['3학년(남)'] / data['3학년 전채 학생 수'] * 100
            data['3학년 여자 비율'] = data['3학년(여)'] / data['3학년 전채 학생 수'] * 100
        else:
            data['3학년 남자 비율'] = data['3학년 여자 비율'] = 0

            
    table = PrettyTable()
    table.field_names = [
        '지역', '전채 학생 수',
        '1학년 전채 학생 수', '1학년(남)', '1학년(여)', '1학년 남자 비율', '1학년 여자 비율',
        '2학년 전채 학생 수', '2학년(남)', '2학년(여)', '2학년 남자 비율', '2학년 여자 비율',
        '3학년 전채 학생 수', '3학년(남)', '3학년(여)', '3학년 남자 비율', '3학년 여자 비율'
    ]
for district, data in sorted(districts.items(), key=lambda x: x[1]['전채 학생 수'], reverse=True)[:5]:
    table.add_row([
            district,
            f"{data['전채 학생 수']:,} 명",
            f"{data['1학년 전채 학생 수']:,} 명", f"{data['1학년(남)']:3d} 명", f"{data['1학년(여)']:3d} 명", f"{data['1학년 남자 비율']:.2f} %", f"{data['1학년 여자 비율']:.2f} %",
            f"{data['2학년 전채 학생 수']:,} 명", f"{data['2학년(남)']:3d} 명", f"{data['2학년(여)']:3d} 명", f"{data['2학년 남자 비율']:.2f} %", f"{data['2학년 여자 비율']:.2f} %",
            f"{data['3학년 전채 학생 수']:,} 명", f"{data['3학년(남)']:3d} 명", f"{data['3학년(여)']:3d} 명", f"{data['3학년 남자 비율']:.2f} %", f"{data['3학년 여자 비율']:.2f} %"
    ])
print(table)
#             school = {
#                 '학교명': row['학교명'],
#                 '1학년(남)': int(row['1학년(남)']),
#                 '1학년(여)': int(row['1학년(여)']),
#                 '2학년(남)': int(row['2학년(남)']),
#                 '2학년(여)': int(row['2학년(여)']),
#                 '3학년(남)': int(row['3학년(남)']),
#                 '3학년(여)': int(row['3학년(여)']),
#             }

#         school['1학년 전체 학생 수'] = school['1학년(남)'] + school['1학년(여)']
#         school['2학년 전체 학생 수'] = school['2학년(남)'] + school['2학년(여)']
#         school['3학년 전체 학생 수'] = school['3학년(남)'] + school['3학년(여)']
        
#         if school['1학년 전체 학생 수'] != 0 and school['2학년 전체 학생 수'] != 0 and school['3학년 전체 학생 수'] != 0:
#             school['1학년 남자 비율'] = school['1학년(남)'] / school['1학년 전체 학생 수'] * 100
#             school['2학년 남자 비율'] = school['2학년(남)'] / school['2학년 전체 학생 수'] * 100
#             school['3학년 남자 비율'] = school['3학년(남)'] / school['3학년 전체 학생 수'] * 100
#             school['1학년 여자 비율'] = school['1학년(여)'] / school['1학년 전체 학생 수'] * 100
#             school['2학년 여자 비율'] = school['2학년(여)'] / school['2학년 전체 학생 수'] * 100
#             school['3학년 여자 비율'] = school['3학년(여)'] / school['3학년 전체 학생 수'] * 100
#         school['전체 학생 수'] = school['1학년 전체 학생 수'] + school['2학년 전체 학생 수'] + school['3학년 전체 학생 수']
#         school_li.append(school)


# top5_schools = sorted(school_li, key=lambda x: x['전체 학생 수'], reverse=True)[:5]

# table = PrettyTable()
# table.field_names = ['학교명', '전체 학생 수', '1학년 전체 학생 수', '1학년(남)', '1학년(여)','1학년 남자 비율','1학년 여자 비율', '2학년 전체 학생 수', '2학년(남)', '2학년(여)','2학년 남자 비율', '2학년 여자 비율', '3학년 전체 학생 수', '3학년(남)', '3학년(여)','3학년 남자 비율', '3학년여자 비율']

# for school in top5_schools:
#     table.add_row([
#         school['학교명'],
#         f"{school['전체 학생 수']:,} 명",
#         f"{school['1학년 전체 학생 수']} 명",f"{school['1학년(남)']} 명",f"{school['1학년(여)']} 명",f"{school['1학년 남자 비율']:.2f} %",f"{school['1학년 여자 비율']:.2f} %",
#         f"{school['2학년 전체 학생 수']} 명",f"{school['2학년(남)']} 명",f"{school['2학년(여)']} 명",f"{school['2학년 남자 비율']:.2f} %",f"{school['2학년 여자 비율']:.2f} %",
#         f"{school['3학년 전체 학생 수']} 명",f"{school['3학년(남)']} 명",f"{school['3학년(여)']} 명",f"{school['3학년 남자 비율']:.2f} %",f"{school['3학년 여자 비율']:.2f} %"
#     ])
# print(table)