from datetime import datetime

class To_do_list:

    def __init__(self, name, description, tdate):
        self.name = name
        self.description = description
        self.tdate = tdate

    def __str__(self):
        return f"{self.name};{self.description};{self.tdate}"
    
    @classmethod
    def data_string(cls, data_str):
        name , description , tdate = data_str.split(';')
        return cls(name , description , tdate)
    
    @classmethod
    def todo_time(cls , date_str):
        pass

def save_task(todo , filename = "todo.txt"):
    try:
        with open(filename , 'a') as file:
            file.write(str(todo) + "\n")
    except Exception as e:
        print("Error saving credentials:", e)

def load_tast( filename = "todo.txt"):
    todolist = []
    try:
        with open(filename , 'r') as file:
            for line in file :
                todolist.append(To_do_list.data_string(line))
    except FileNotFoundError:
        open(filename, 'w').close()
    except Exception as e:
        print("Error saving credentials:", e)
    return todolist

def delete_tast(index ,filename= "todo.txt"):
    tododlist = load_tast(filename)
    try:
        tododlist.pop(index)
        with open(filename , 'w') as file:
            for tast in tododlist:
                file.write(str(tast) + "\n")
    except IndexError:
        print("Invalid index.")
    except Exception as e:
        print("Error deleting task:", e)
def timer_todo():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    pass
def display_menu():
    print("\n=== ENTER A NUMBER ===")
    print("1. Add New task")
    print("2. View All tasks")
    print("3. Delete a task")
    print("4. Exit")
    
def main ():
    while True:
        display_menu()
        choice = int(input("enter a number: "))
        if choice == 1:
            name = input("the name of the task: ")
            description = input("the description: ")
            time = timer_todo()
            tast = To_do_list(name, description, time)
            save_task(tast)
        elif choice == 2 :
            tast = load_tast()
            if not tast:
                print("there is not tasts.")
            else:
                for idx ,cred in enumerate(tast):
                        print(f"{idx}. task: {cred.name}, desc: {cred.description}, time: {cred.tdate}")
        elif choice == 3:
            tast = load_tast()
            for idx , tass in enumerate(tast):
                print(f"{idx}: {tass.name}")
            try:
                  del_index = int(input("Enter index to delete: "))
                  delete_tast(del_index)
            except ValueError:
                    print("Invalid input. Please enter a number.")
        elif choice == 4:
            print("Exiting from task.")
            break
        else:
            print("Invalid option. Try again.")
    

if __name__ == "__main__":
    main()
    

    
