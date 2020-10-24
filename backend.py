import sqlite3


from tkinter import *

class TaskManager:
    def __init__(self):
        self.db=sqlite3.connect("task.db")
        self.sql=self.db.cursor()

        self.create_db()

    def create_db(self):
       self.sql.execute("""CREATE TABLE IF NOT EXISTS task(
                                            task_name TEXT NOT NULL,
                                            description TEXT,
                                            id INTEGER PRIMARY KEY)""")


    def save(self, content):
        file = open('task_name.txt', 'w')
        [file.write(i) for i in content]
        file.close()

    def add_task(self):
        self.sql.execute("INSERT INTO task (task_name,description) VALUES(?,?)",
                         (self.title.get(), self.description.get("1.0", END)))
        self.db.commit()


    def add(self):
        window_add = Tk()
        window_add.title('Добавление задачи')
        window_add.geometry('400x400')
        self.title=Label(window_add,text='Введите название задачи :')
        self.title.place(x=38,y=12)
        self.title = Entry(master=window_add, width=40)
        self.title.place(x=40, y=30)

        self.description=Label(window_add,text='Описание задачи :')
        self.description.place(x=38,y=52)
        self.description = Text(master=window_add, width=40, height=15)
        self.description.place(x=40, y=70)

        add = Button(text="Добавить", master=window_add,bg='blue', width=16, height=1, command=self.add_task)
        add.place(x=210, y=340)
        add_1 = Button(master=window_add, text='Отмена', bg='red', width=16, height=1)
        add_1.place(x=40, y=340)
        window_add.resizable(False, False)
        window_add.mainloop()

    def delete(self):

        delete_window=Tk()
        delete_window.title('Удаление задачи')
        delete_window.geometry('400x400')
        self.del_list = Label(delete_window, text='Выберите задачу :')
        self.del_list.place(x=30, y=12)
        self.del_list=Listbox(delete_window,width=42, height=15)
        self.del_list.place(x=30,y=30)
        for i in self.sql.execute("SELECT task_name FROM task"):
            self.del_list.insert(END, i)
        del_button=Button(delete_window,text='Удалить задачу',width=15,height=1,bg='red',fg='gold',
                          command=self.delete_button)
        del_button.place(x=220,y=330)
        del_button_1 = Button(delete_window, text='Отмена',bg='blue',fg='orange', width=15, height=1)
        del_button_1.place(x=220, y=360)
        delete_window.resizable(False,False)
        delete_window.mainloop()

    def delete_button(self):

        id = [i[0] for i in self.sql.execute("SELECT id FROM task")][self.del_list.curselection()[0]]
        self.sql.execute(f"DELETE FROM task WHERE id = {id}")
        self.db.commit()
        self.del_list.delete(0,END)
        for i in self.sql.execute("SELECT task_name FROM task"):
            self.del_list.insert(END, i)






    def update(self):

        update_window=Tk()
        update_window.title('Обновить')
        update_window.geometry('400x400')
        up_label = Label(update_window, text='Введите обновление задачи :')
        up_label.place(x=30, y=20)
        self.text_b = Text(update_window, width=40, height=17)
        self.text_b.place(x=35, y=55)
        up_button=Button(update_window, text='Обновить',bg='green',fg='yellow',width=13,    height=1)
        up_button.place(x=230, y=355, )
        self.up_button_1 = Button(update_window, text='Отмена', bg='silver', fg='gold', width=13, height=1,
                             command=self.update_button)
        self.up_button_1.place(x=90, y=355)
        update_window.resizable(False,False)
        update_window.mainloop()

    def update_button(self):
        id = [i[0] for i in self.sql.execute("SELECT id FROM task")][self.task_list.curselection()[0]]
        self.sql.execute(f"UPDATE FROM task WHERE id = {id}")
        self.bd.commit()

        for i in self.sql.execute("SELECT task_name FROM task"):
            self.up_label.update(END, i)

    def description_task(self):  # Переписать под файлы
        self.all_task()
        try:
            description = input("Описание какой задачи хотите просмотреть?:")
            print(f"Описание к задаче '{description}': {self.task_dickt[description]}")
        except:
            print(f"Ошибка. Нет такой задачи: '{description}'.")

    def search(self):  # Поиск
        search_window=Tk()
        search_window.title('Поиск задачи :')
        search_window.geometry('400x400')
        search_button = Button(search_window, text='Поиск', width=13, height=1)
        search_button.place(x=230, y=355)
        search_button_1=Entry(search_button,width=20, bg='red')
        search_button_1.place(x=180,y=355)




        search_window.resizable(False,False)
        search_window.mainloop()

    def statistic(self):   # Переписать под файлы
        print(f"Всего задач: {len(self.task_dickt)}")
        print()
        max_task = []
        for i in self.task_dickt:
            max_task.append(i)

        print(f"Самое длинное название: '{max(max_task)}'.\n"
              f"Общая длина символов: '{len(max(max_task))}'.")
        print()
        print(f"Самое корткое название: '{min(max_task)}'.\n"
              f"Общая длина символов: '{len(min(max_task))}'.")





if __name__ == '__main__':
    TASK_MANAGER = TaskManager()
    TASK_MANAGER.run()


