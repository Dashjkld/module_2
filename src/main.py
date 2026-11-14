""""
расчет заработка за смену
автор: [Балкабеков Олжас]
"""

# параметр расчёта
NORMAL_HOURS = 8;
OVERTIME_RATE = 1.5;
MAX_HOURS = 12;

"запрашивает имя работника и почасовую ставку, возвращает введённые данные."
def get_shift_data():
    name = input("Введите имя работника: ").strip().capitalize();
    rate = float(input("Введите почасовую ставку: "))
    while rate <=0:
        rate = float(input("Ставка должна быть больше нуля: "))
    return name, rate;

"запрашивает продолжительность смены, проверяет её и возвращает корректное значение."
def get_shift_hours():
    shift_duration = float(input("Введите продолжительность смены: "));
    while shift_duration <= 0 or shift_duration > MAX_HOURS:
        shift_duration = float(input("Продолжительность должна быть в диапазоне от больше 0 и не превышать 12 часов: "));
    return shift_duration;

"рассчитывает сверхурочные часы, оплату сверхурочных часов а также общий заработок"
def calculate_salary(rate, shift_duration):
    if shift_duration > NORMAL_HOURS:
        overtime_hours = shift_duration - NORMAL_HOURS;
    else:
        overtime_hours = 0;
    overtime_payment = overtime_hours * rate * OVERTIME_RATE;
    total_salary = min(shift_duration, NORMAL_HOURS) * rate + overtime_payment;
    return overtime_hours, overtime_payment, total_salary

"определяет категорию смены по её продолжительности и возвращает нужное название."
def get_shift_category(shift_duration):
    if shift_duration < NORMAL_HOURS:
        return "Неполная смена";
    elif shift_duration == NORMAL_HOURS:
        return "Обычная смена";
    else:
        return "Сверхурочная работа";

def main():
    name, rate = get_shift_data();
    shift_duration = get_shift_hours();
    overtime_hours, overtime_payment, total_salary = calculate_salary(rate, shift_duration);
    category = get_shift_category(shift_duration);

    print();
    print(f"{'ОТЧЁТ О ЗАРАБОТКЕ':^60}");
    print("-" * 60);
    print(f"{'Имя работника:':<35}{name:>25}");
    print(f"{'Продолжительность смены:':<35}{f'{shift_duration:.2f} ч':>25}");
    print(f"{'Почасовая ставка:':<35}{f'{rate:.2f} тг/ч':>25}");
    print(f"{'Сверхурочные часы:':<35}{f'{overtime_hours:.2f} ч':>25}");
    print(f"{'Оплата сверхурочной части:':<35}{f'{overtime_payment:.2f} тг':>25}");
    print(f"{'Общий заработок:':<35}{f'{total_salary:.2f} тг':>25}");
    print(f"{'Категория смены:':<35}{category:>25}");
    print("-" * 60);

    print();
    print(f"{'ТАБЛИЦА ЗАРАБОТКА':^60}");
    print("-" * 60);
    print(f"{'Часы':<35}{'Заработок, тг':>25}");
    print("-" * 60);

    for hours in range(6, 11):
        overtime_hours, overtime_payment, total_salary = calculate_salary(rate, hours);
        print(f"{hours:02d}{' ' * 33}{total_salary:>25.2f}");
    print("-" * 60);


while True:
    main();
    answer = input("Рассчитать другую смену? (да/нет): ").strip().lower();
    while answer != "да" and answer != "нет":
        answer = input("Введите «да» или «нет»: ").strip().lower();
    if answer == "нет":
        print("Работа программы завершена");
        break;

