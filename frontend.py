from tkinter import *
from backend import TaskManager


class TaskManagerFrontend(TaskManager):
    def __init__(self):
        super(TaskManagerFrontend, self).__init__()
        self.base()

    def test(self):
        try:
            print(self.task_list.get(0,END)[self.task_list.curselection()[0]])
        except IndexError:
            pass


    def _init_buttons(self):
        add = Button(text="Добавить задачу", width=20, height=2, command=self.add)
        add.place(x=375, y=470)

        delete = Button(text="Удалить задачу", width=20, height=2,command=self.delete)
        delete.place(x=205, y=470,)

        update = Button(text="Обновить задачу", width=20, height=2,command=self.update)
        update.place(x=35, y=470)

        static = Button(text="Статистика", width=20, height=2, command=self.test)
        static.place(x=375, y=520)

        description = Button(text="Описание задачи", width=20, height=2)
        description.place(x=205, y=520)

        out = Button(text="Выход", width=20, height=2)
        out.place(x=35, y=520)

        search=Button(text='Поиск', width=20, height=1, command=self.search)
        search.place(x=373, y=20)

    def _init_tasks(self):

        self.task_list = Listbox(width=65, height=22)


        for i in self.sql.execute("SELECT task_name FROM task"):
            self.task_list.insert(END,i)

        self.task_list.place(x=37, y=55)

    def base(self):
        self.window = Tk()
        self.window.title('Task manager')
        self.window.geometry('600x600')
        wind1=Entry(self.window,width= 40)
        wind1.place(x=38, y=30)



        self._init_tasks()

        self._init_buttons()

        self.window.resizable(False, False)
        self.window.mainloop()


app = TaskManagerFrontend()
