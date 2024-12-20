def sort_list_max_remove(lst):
    sorted_list = []
    while lst:
        max_elem = max(lst)
        sorted_list.append(max_elem)
        lst.remove(max_elem)
    return sorted_list

data_count = 0
kokugo_li = []
eng_li = []
math_li = []
stu_num_li = []
name_li = []
test_avg_li = []

while True:
    print(f"\n{'='*30}")
    print(" 1. 학생 성적 입력")
    print(" 2. 학생 목록 출력 (입력 순)")
    print(" 3. 프로그램 종료")
    print(f"\n 현재 입력된 데이터 수 : {len(kokugo_li)}")
    if len(test_avg_li) > 0:
        all_avg = sum(test_avg_li) / len(test_avg_li)
    else:
        all_avg = 0
    print(f" 잔류 학생 평균 점수 : {all_avg:.2f}")
    print("="*30)

    menu = int(input("메뉴를 선택하세요\n"))
    while not 1 <= menu <= 3:
        menu = int(input("1~3 사이에서 선택하세요\n"))

    if menu == 1:
        data_count += 1
        stu_num = int(input("학번을 입력하세요\n"))
        while not 1 <= stu_num <= 100:
            stu_num = int(input("학번을 입력하세요\n"))
        stu_num_li.append(stu_num)

        name = input("이름을 입력하세요\n")
        name_li.append(name)

        kokugo = int(input("국어 점수를 입력하세요\n"))
        kokugo_li.append(kokugo)

        eng = int(input("영어 점수를 입력하세요\n"))
        eng_li.append(eng)

        math = int(input("수학 점수를 입력하세요\n"))
        math_li.append(math)

        test_avg = (kokugo + eng + math) / 3
        test_avg_li.append(test_avg)

    elif menu == 2:
        if len(kokugo_li) == 0:
            print("입력된 데이터가 없습니다.")
        else:
            for i in range(len(kokugo_li)):
                print(f" ID : {stu_num_li[i]:02d}  이름 : {name_li[i]}  국어 : {kokugo_li[i]:3d}  영어 : {eng_li[i]:3d}  수학 : {math_li[i]:03d}  평균 : {test_avg_li[i]:.2f}")

    elif menu == 3:
        print("프로그램 종료")
        break
