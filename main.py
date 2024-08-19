import tkinter as tk
import numpy as np

class MatrixOperationsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Матричные операции")

        self.create_widgets()

    def create_widgets(self):
        # Размерность первой матрицы
        self.label_matrix1 = tk.Label(self.master, text="Размерность первой матрицы (строки столбцы):")
        self.label_matrix1.grid(row=0, column=0, padx=5, pady=5)

        self.entry_rows1 = tk.Entry(self.master, width=5)
        self.entry_rows1.grid(row=0, column=1, padx=5, pady=5)

        self.entry_cols1 = tk.Entry(self.master, width=5)
        self.entry_cols1.grid(row=0, column=2, padx=5, pady=5)

        # Ввод первой матрицы
        self.label_input_matrix1 = tk.Label(self.master, text="Введите первую матрицу:")
        self.label_input_matrix1.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.text_matrix1 = tk.Text(self.master, height=5, width=30)
        self.text_matrix1.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        # Размерность второй матрицы
        self.label_matrix2 = tk.Label(self.master, text="Размерность второй матрицы (строки столбцы):")
        self.label_matrix2.grid(row=3, column=0, padx=5, pady=5)

        self.entry_rows2 = tk.Entry(self.master, width=5)
        self.entry_rows2.grid(row=3, column=1, padx=5, pady=5)

        self.entry_cols2 = tk.Entry(self.master, width=5)
        self.entry_cols2.grid(row=3, column=2, padx=5, pady=5)

        # Ввод второй матрицы
        self.label_input_matrix2 = tk.Label(self.master, text="Введите вторую матрицу:")
        self.label_input_matrix2.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

        self.text_matrix2 = tk.Text(self.master, height=5, width=30)
        self.text_matrix2.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

        # Выбор операции
        self.label_operation = tk.Label(self.master, text="Выберите операцию:")
        self.label_operation.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

        self.operation_var = tk.StringVar(self.master)
        self.operation_var.set("Сложение")
        self.operations = ["Сложение", "Вычитание", "Умножение", "Транспонирование"]
        self.option_menu = tk.OptionMenu(self.master, self.operation_var, *self.operations)
        self.option_menu.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

        # Кнопка для выполнения операции
        self.button_execute = tk.Button(self.master, text="Выполнить", command=self.execute_operation)
        self.button_execute.grid(row=8, column=0, columnspan=3, padx=5, pady=5)

        # Результат
        self.label_result = tk.Label(self.master, text="Результат:")
        self.label_result.grid(row=9, column=0, columnspan=3, padx=5, pady=5)

        self.text_result = tk.Text(self.master, height=5, width=30)
        self.text_result.grid(row=10, column=0, columnspan=3, padx=5, pady=5)

    def execute_operation(self):
        operation = self.operation_var.get()
        matrix1_rows = int(self.entry_rows1.get())
        matrix1_cols = int(self.entry_cols1.get())
        matrix1_text = self.text_matrix1.get("1.0", tk.END).strip()

        # Определяем операцию транспонирования
        if operation == "Транспонирование":
            matrix1 = np.array([list(map(int, row.split())) for row in matrix1_text.split('\n')])
            result = matrix1.T
            result_str = "\n".join(" ".join(str(cell) for cell in row) for row in result)
            self.text_result.delete("1.0", tk.END)
            self.text_result.insert(tk.END, result_str)
            return  # Завершаем выполнение метода после транспонирования

        matrix2_rows = int(self.entry_rows2.get())
        matrix2_cols = int(self.entry_cols2.get())
        matrix2_text = self.text_matrix2.get("1.0", tk.END).strip()

        matrix1 = np.array([list(map(int, row.split())) for row in matrix1_text.split('\n')])
        matrix2 = np.array([list(map(int, row.split())) for row in matrix2_text.split('\n')])

        if operation == "Сложение":
            result = matrix1 + matrix2
        elif operation == "Вычитание":
            result = matrix1 - matrix2
        elif operation == "Умножение":
            result = np.dot(matrix1, matrix2)

        result_str = "\n".join(" ".join(str(cell) for cell in row) for row in result)
        self.text_result.delete("1.0", tk.END)
        self.text_result.insert(tk.END, result_str)


def main():
    root = tk.Tk()
    app = MatrixOperationsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
