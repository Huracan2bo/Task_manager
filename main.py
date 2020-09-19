class TaskManager:
    def __init__(self):
        self.FILE = 'task_name.txt'
        self.task_dickt = {
            "Вынести мусор": "Взять мусор из корзины и выкинуть его",
            "Помыть пол": "Взять ведро и помыть полы",
            "Сходить в магазин": "Выйти на улицу, дойти до магазина и купить продукты"
        }

        self.create_db()
        print()
        print("Task manager\n"
              "\n"
              "Выберите действие:\n"
              "1.Добавить\n"
              "2.Удалить\n"
              "3.Обновить\n"
              "4.Все задачи\n"
              "5.Описание задачи\n"
              "6.Поиск\n"
              "7.Статистика\n"
              "8.Выход")

    def create_db(self):
        try:
            file = open(self.FILE, 'r')
            file.close()
        except FileNotFoundError:
            file = open(self.FILE, 'w')
            file.close()

    def id(self, FILE):
        file = open(FILE, 'r')
        return len([i for i in file])

    def save(self, content):
        file = open('task_name.txt', 'w')
        [file.write(i) for i in content]
        file.close()

    def add(self, task_title, description_task):  # Добавить задачу
        file = open(self.FILE, 'a')
        file.write(f'{self.id(self.FILE)}#{task_title}#{description_task}\n')
        file.close()

    def all_task(self):  # Добавить задачу
        file = open(self.FILE, 'r')
        for i in file:
            print(f"Номер задачи:{int(i.split('#')[0]) + 1} "
                  f"Задача:{i.split('#')[1]} "
                  f"Описание:{i.split('#')[2]}")
        file.close()

    def delete(self, task_title):
        content = [i for i in open('task_name.txt', 'r')]

        [content.remove(i) for i in content if task_title in i]

        self.save(content)

    def update(self, task_title, new_description):
        content = [i for i in open('task_name.txt', 'r')]

        for i in content:
            if task_title in i:
                content.remove(i)

                content.append(f"{i.split('#')[0]}#{i.split('#')[1]}#{new_description}\n")

        self.save(content)

    def description_task(self,content):  # Переписать под файлы
         content=[i for i in open('task_name.txt','r')]
         task_title=input()
         if task_title in content:
            print(self.description_task)
            file.close()

            # def description_task(self,task_dict):  # Переписать под файлы
         #content=[i for i in open('task_name.txt','r')]
         #task_dict=input('Выберите задачу:')
         #if task_dict in content:
            #self.task_dict(description_task)
            #file.close()



    def search(self):  # Поиск
        try:
            search = input("Поиск:")
            print(f"Задача: '{search}', описание: '{self.task_dickt[search]}'")
        except:
            print(f"По запросу '{search}' ничего не найдено.")

    def statistic(self,task_dict):   # Переписать под файлы
        content=[i for i in open('task_name.txt','r')]
        self.task_dickt


    def run(self):
        what_to_do = input()
        if what_to_do == 'Добавить':
            task_title = input("Введите заголовк задачи:")
            description_task = input("Введите описание задачи:")

            self.add(task_title, description_task)

        elif what_to_do == 'Удалить':
            task_title = input("Введите заголовк задачи:")
            if task_title == '':
                print('Пустая строка. Введите значения!')
            else:
                self.delete(task_title)

        elif what_to_do == 'Обновить':
            task_title = input('Заголовок задачи:')
            if task_title == '':
                print('Ошибка.Строка пуста.Вы ничего не ввели.')
            else:
                new_description = input('Новое описание:')
                self.update(task_title, new_description)
                self.all_task()

        elif what_to_do == 'Все задачи':

            self.all_task()

        elif what_to_do == 'Описание задачи':

            self.description_task()

        elif what_to_do == 'Поиск':

            self.search()

        elif what_to_do == 'Статистика':

            self.statistic()


if __name__ == '__main__':
    TASK_MANAGER = TaskManager()
    TASK_MANAGER.run()


