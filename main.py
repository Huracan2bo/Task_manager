

# crud - create read update delete

# Task manager

task_list = ["Вынести мусор", "Помыть пол", "Сходить в магазин"]

task_dickt = {
    "Вынести мусор" :"Взять мусор из корзины и выкинуть его",
    "Помыть пол": "Взять ведро и помыть полы",
    "Сходить в магазин" :"Выйти на улицу, дойти до магазина и купить продукты"
}


def add_task(task_title, description_task): # заголов и описание
    task_dickt[task_title] = description_task

def delete_task(task_title): # заголовок
    try:
        task_dickt.pop(task_title)
    except:
        print('Ошибка. Введите корректный заголовок задачи.')


def show_all_tasks(task_dickt):
    task_index = 1
    for i in task_dickt:
        print(f"{task_index}. {i}")
        task_index = task_index + 1


def update_task(task_title, new_description):
    task_dickt.update([(task_title ,new_description)])


what_to_do = ""
while what_to_do is not "Выход":
    print()
    print("Task manager\n"
          "\n"
          "Выберите действие:\n"
          "1.Добавить\n"
          "2.Удалить\n"
          "3.Обновить\n"
          "4.Все задачи\n"
          "5.Выход")
    what_to_do = input()

    if what_to_do == 'Выход':
        break

    elif what_to_do == 'Добавить':
        task_title = input("Введите заголовк задачи:")
        description_task = input("Введите описание задачи:")

        add_task(task_title, description_task)

    elif what_to_do == 'Удалить':

        task_title = input("Введите заголовк задачи:")
        if task_title == '':
            print('Пустая строка. Введите значения!')
        else:
            print('Выберите задачу :')
            delete_task(task_title)

    elif what_to_do == 'Обновить':
        task_title = input('Заголовок задачи:')
        if task_title =='':
            print('Ошибка.Строка пуста.Вы ничего не ввели.')
        else:
            new_description = input('new_description:')
            update_task(task_title, new_description)
            show_all_tasks(task_dickt)

    elif what_to_do == 'Все задачи':

        show_all_tasks(task_dickt)
    
    
    
    
        
 
        
        
        
    
    