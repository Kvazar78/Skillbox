class Stack:
    __stack_list = []

    def get_stack(self):
        return self.__stack_list

    def add_item(self, item):
        self.__stack_list.append(item)

    def del_item(self):
        return self.__stack_list.pop()

    def get_info(self):
        return self.__stack_list


class TaskManager:

    def __init__(self):
        self.__tm_stack = Stack()

    def new_task(self, task, priority):
        self.__task_flag = False
        self.temp_dict = {}
        self.__task = task
        self._set_priority(priority)
        if len(self.__tm_stack.get_stack()) != 0:
            for i_key, i_val in self._gen_dict_from_stack().items():
                if i_key == task and i_val == priority:
                    self.__task_flag = True
        if not self.__task_flag:
            self.temp_dict[task] = priority
            self._set_stack(self.temp_dict)
        else:
            print(f'Задача {task.upper()} с приоритетом {priority} уже существует и не будет внесена повторно!')

    def _set_priority(self, priority):
        if isinstance(priority, int):
            self.__priority = priority
        else:
            raise ValueError(f'Ошибка ввода приоритета: {priority} - не число!')

    def _set_stack(self, task_dict):
        self.__tm_stack.add_item(task_dict)

    def get_stack_info(self):
        return self.__tm_stack.get_info()

    def _gen_dict_from_stack(self):
        self.__dict_stack = {key: val for i_elem in self.__tm_stack.get_stack() for key, val in i_elem.items()}
        return self.__dict_stack

    def get_task_info(self):
        self.__hist_dict = dict()
        for i_key in self._gen_dict_from_stack():
            if self._gen_dict_from_stack()[i_key] in self.__hist_dict:
                self.__hist_dict[self._gen_dict_from_stack()[i_key]].append(i_key)
            else:
                self.__hist_dict[self._gen_dict_from_stack()[i_key]] = [i_key]
        for i_key, i_elem in self.__hist_dict.items():
            print(f'{i_key}:', end=' ')
            for i in i_elem:
                print(f'{i}, ', end='')
            print()

    def del_task_lifo(self):
        print(f'Удалена задача {self.__tm_stack.del_item()}')


tm = TaskManager()
tm.new_task('встать', 1)
tm.new_task('умыться', 2)
tm.new_task('позавтракать', 2)
tm.new_task('умыться', 2)
tm.new_task('погулять с собакой', 2)

tm.get_task_info()
for i in tm.get_stack_info():
    print(i)

tm.del_task_lifo()

for i in tm.get_stack_info():
    print(i)
