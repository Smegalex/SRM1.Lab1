import math

#1.
def rectangle_square_and_perimeter (a, b): 
    s = a * b;
    p = 2 * (a + b)
    print (f"Площа прямокутника зі сторонами {a} і {b} дорівнює {s}.\nПериметр цього прямокутника дорівнює {p}.")

#2.
def average_geometric (a, b):
    print (f'Середнє геометричне чисел {a} і {b} дорівнює {round(math.sqrt(a * b),5)}.')

#3.
v1=[]
v2=[]
def rectangle_sq_and_per_by_vertex (v1, v2):
    a = abs (v2[0] - v1[0])
    b = abs (v2[1] - v1[1])
    rectangle_square_and_perimeter (a, b)

#4.
def is_even (a):
    if a % 2 == 0:
        print (f"Число {a} є парним.")
    else:
        print (f"Число {a} є непарним.")

#5.
def abc_quest (a, b, c):
    abc_in_growth = a < b < c
    abc_at_least_one_is_positive = a > 0 or b > 0 or c > 0
    abc_only_one_is_positive = (a > 0 and b <= 0 and c <= 0) or (a <= 0 and b > 0 and c <= 0) or (a <= 0 and b <= 0 and c > 0)
    if abc_in_growth:
        print (f"Для даних чисел справджується рівність {a} < {b} < {c}.")
    else:
        print ("Дані числа не задовольняють рівність a < b < c.")
    if abc_at_least_one_is_positive:
        if abc_only_one_is_positive:
            print (f"Тільки одне з чисел {a}, {b} і {c} є додатним")
            return 0;
        print (f"Як мінімум два числа з {a}, {b}, {c} є додатними.")
    else:
        print ("Усі дані числа - від'ємні.")

#6.
def chess_check_color (x, y): #(1, 1) is a black
    col = False #True == white, False == black.
    if x%2 == 0:
        if y%2 == 0:
            col = False #black
        else:
            col = True #white
    else:
        if y%2 == 0:
            col = True #white
        else: 
            col = False #black
    if col:
        print (f"Клітинка з координатами ({x}, {y}) є білою.")
    else:
        print (f"Клітинка з координатами ({x}, {y}) є чорною.")

#7.
sp1 = []
sp2 = []
def queen_can_move (sp1, sp2):
    orthogonal = (sp1[0] == sp2[0]) or (sp1[1] == sp2[1])
    diagonal = abs(sp1[0] - sp2[0]) == abs(sp1[1] - sp2[1])
    if orthogonal:
        print (f"Ферзь може походити з точки ({sp1[0]}, {sp1[1]}) у точку ({sp2[0]}, {sp2[1]}) ортогонально.")
    elif diagonal:
        print (f"Ферзь може походити з точки ({sp1[0]}, {sp1[1]}) у точку ({sp2[0]}, {sp2[1]}) діагонально.")
    else:
        print (f"Ферзь не може за один хід перейти з точки ({sp1[0]}, {sp1[1]}) у точку ({sp2[0]}, {sp2[1]}).")

#8.
growing = []
def range_in_growing (A, B):
    if A < B:
        for i in range(B-A+1):
            growing.append(A+i)
    else:
        for i in range(A-B+1):
            growing.append(B+i)
    print (f"Усі цілі числа у порядку зростання від A = {A} до B = {B} включно:\n{growing}\nУсього таких чисел {len(growing)}.")

#9.
reverse_numbers = []
def right_to_left_number (N):
    save_start = N
    for i in range (len(str(N))):
        reverse_numbers.append(str(N % 10))
        N = N // 10
    print (f"Число {save_start} записане справа наліво це {''.join(reverse_numbers)}")

#10.
arr = []
def greater_than_average_punishment (arr):
    average = 0
    for i in arr:
        average += int(i)
    average = average/len(arr)
    for i in range(len(arr)):
        if int(arr[i]) > average:
            arr[i] = int(arr[i]) - 18
        else: arr[i] = int(arr[i])
    print (f"Новий масив виглядає наступним чином:\n{arr}")

#11.
def is_prime_number (N):
    dividers_count = 0
    dividers = []
    for i in range (2, N):
        if N % i == 0: 
            dividers_count += 1
            dividers.append(i)
    if dividers_count == 0:
        print (f"Число {N} є простим (ділиться націло тільки на одиницю і саме на себе).")
    else:
        print(f"Число {N} не є простим, і має {dividers_count} дільників {dividers} окрім одиниці та самого себе.")

#12. завдання 24 зі списку
def counting_function_result():
    a = round(math.pow((25+math.sqrt(8.5)+8), (1/4)), 10)
    print (f"Результат даної функції, округлений до 10 знаків після коми, при X = 8, Y = 25, Z = 8.5 становить {a}.")

#13.
def fields_filling (i, name, surname, phone_number):
    match i: 
        case 1:
            #13.1. => all fields must be filled
            if not(name) or not(surname) or not(phone_number):
                print("Не залишайте жодного поля порожнім.")
            else:
                print("Спасибі.")
        case 2:
            #13.2. => at least one field should be filled
            if not(name) and not(surname) and not(phone_number):
                print("Не залишайте всі поля порожніми.")
            else:
                print("Спасибі.")
        case 3:
            #13.3. => name and surname must be filled
            if name == "" or surname == "":
                print("Ви зобов'язані ввести своє ім'я та прізвище для продовження.")
            else:
                print("Спасибі.")
        case _:
            print("Немає такого варіанту завдання.")

#14.
def five_tries_to_guess():
    for i in range(1, 6):
        if int(input(f"Спроба {i}: ")) == 5:
            print("Ви відгадали число. Цим числом було 5.")
            return 0
    print("На жаль, ви не відгадали число за 5 спроб.")

#15.
all_dividing_13_arr = []
def fifteen():
    for i in range(13, 101, 13):
        all_dividing_13_arr.append(i)
    print(f"Усі числа від 1 до 100, що діляться на 13 націло:\n{all_dividing_13_arr}")

#16.
def text_operations():
    text1 = "Lorem ipsum dolor et ali. "
    text2 = "Groli moli stu ra loni." 
    print (f"Текст 1 -'{text1}'")
    print (f"Текст 2 -'{text2}'")

    #16.1.
    text_combined = text1 + text2
    print (f"Текст 1 об'єднаний з текстом 2: \n{text_combined}")

    #16.2.
    text_multiplied = text1 * 10
    print (f"Текст 1 розмножений 10 разів:\n{text_multiplied}")

    #16.3.
    text1_array = [*text1]
    text1_array.insert(11, ",")
    new_text1 = "".join(text1_array)
    print(text1 + "\n" + new_text1)

    #16.4.
    text2_array = [*text2]
    text2_array[6] = "s"
    new_text2 = "".join(text2_array)
    print(text2 + "\n" + new_text2)


def tasks_call (i): 
    match i:
        case 1:
            print("Завдання 1:\nОберіть натуральні числа a та b")
            rectangle_square_and_perimeter(int(input("a = ")), int(input("b = "))) ,
        case 2:
            print("Завдання 2:\nОберіть числа a та b")
            average_geometric(int(input("a = ")), int(input("b = "))) 
        case 3:
            print("Завдання 3:\nОберіть координати точок A (x1, y1) та B (x2, y2)")
            v1.append(int(input("x1 = ")))
            v1.append(int(input("y1 = ")))
            v2.append(int(input("x2 = ")))
            v2.append(int(input("y2 = ")))
            rectangle_sq_and_per_by_vertex (v1, v2) 
        case 4:
            print("Завдання 4:\nОберіть число a")
            is_even(int(input("a = "))) 
        case 5:
            print("Завдання 5:\nОберіть числа a, b і c")
            abc_quest(int(input("a = ")), int(input("b = ")), int(input("c = "))) 
        case 6:
            print("Завдання 6:\nОберіть координати x та y (від 1 до 8).\nЗа цими координатами буде визначено колір клітинки шахової дошки,\nякщо вважати, що клітинка (1,1) є чорною.")
            chess_check_color(int(input("x = ")), int(input("y = ")))
        case 7:
            print("Завдання 7:\nОберіть координати точок A (x1, y1) та B (x2, y2).\nЗавдяки обчисленням, програма скаже, чи може\n ферзь переміститись з A у B за 1 хід.")
            sp1.append(int(input("x1 = ")))
            sp1.append(int(input("y1 = ")))
            sp2.append(int(input("x2 = ")))
            sp2.append(int(input("y2 = ")))
            queen_can_move (sp1, sp2) 
        case 8:
            print("Завдання 8:\nОберіть числа A та B")
            range_in_growing(int(input("A = ")), int(input("B = "))) 
        case 9: 
            print("Завдання 9:\nОберіть число N")
            right_to_left_number(int(input("N = "))) 
        case 10:
            print("Завдання 10:\nЗадайте масив будь-яких цілих чисел, записуючи їх через пропуск.\nДля даних чисел буде вираховано середнє значення та від\nусіх чисел, що вище середнього буде віднято 18.")
            greater_than_average_punishment(input().split())
        case 11:
            print("Завдання 11:\nОберіть число N")
            is_prime_number(int(input("N = ")))
        case 12:
            print("Завдання 12:")
            counting_function_result()
        case 13:
            print("Завдання 13.")
            fields_filling (int(input('Оберіть варіант завдання, який хочете виконати (1-3): ')), input("Введіть своє ім'я: "), input("Введіть своє прізвище: "), input("Введіть свій номер телефону: "))
        case 14:
            print("Завдання 14.")
            five_tries_to_guess()
        case 15:
            print("Завдання 15.")
            fifteen()
        case 16:
            print("Завдання 16.")
            text_operations()
        case _:
            print("Немає завдання з таким номером.")


print("Оберіть номер завдання, яке хочете запустити (1-16): ")

tasks_call(int(input()))
