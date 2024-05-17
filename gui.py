import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from decode import revenue_by_department, revenues_by_product, quantities, analyzer


class ChartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Услышь же мольбу мою ради Господа нашего")
        self.root.geometry("1050x710")

        self.label = None
        self.create_widgets()

    def create_widgets(self):
        # Фрейм для кнопок
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        # Фрейм для графиков
        self.charts_frame = tk.Frame(self.root)
        self.charts_frame.pack(fill=tk.BOTH, expand=True)

        # Кнопки
        button1 = tk.Button(
            button_frame,
            text="Показать статистику",
            command=self.create_charts,
            bd=0,
            fg="#fff",
            bg="#08f",
            underline=0,
            activebackground="#e6deff",
            activeforeground="#fff",
            cursor="hand2",
        )
        button1.pack(side=tk.LEFT, fill=tk.X, expand=True)

        button2 = tk.Button(
            button_frame,
            text="Запустить симуляцию",
            command=self.simulate,
            bd=0,
            fg="#fff",
            bg="#04f",
            underline=0,
            activebackground="#4169e1",
            activeforeground="#fff",
            cursor="hand2",
        )
        button2.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def create_collected_chart(self, s, labels, explode, chart_title, num_format=False):
        fig = Figure(figsize=(5, 3))
        ax = fig.add_subplot(111)

        if num_format:

            def autopct_format(values):
                def my_format(pct):
                    total = sum(values)
                    val = int(round(pct * total / 100.0))
                    return "{p:.1f}% \n- {v:d}".format(p=pct, v=val)

                return my_format

            autopct = autopct_format(s)
        else:
            autopct = "%1.1f%%"

        ax.pie(
            s,
            labels=labels,
            explode=explode,
            autopct=autopct,
            shadow=True,
            startangle=90,
        )
        ax.axis("equal")
        ax.set_title(chart_title)

        canvas = FigureCanvasTkAgg(fig, master=self.charts_frame)
        canvas.draw()
        widget = canvas.get_tk_widget()
        return widget

    def create_charts(self):
        # Очистка старых диаграмм
        for widget in self.charts_frame.winfo_children():
            widget.destroy()

        data = [
            (
                revenues_by_product,
                [0, 0, 0, 0.1, 0],
                "Продажи по стоимости (руб)",
                True,
            ),
            (quantities, [0.1, 0, 0, 0, 0], "Продажи по количеству (единиц)", True),
            (
                [(k, v) for k, v in revenue_by_department.items()],
                [0, 0.1],
                "Продажи по отделам (руб)",
                True,
            ),
        ]

        row = 0
        col = 0
        for items, explode, title, num_fmt in data:
            labels = [x[0] for x in items]
            sizes = [x[1] for x in items]
            widget = self.create_collected_chart(sizes, labels, explode, title, num_fmt)
            if col == 0 and row == 1:
                widget.grid(
                    row=row, column=col, padx=10, pady=10, sticky="nsew", columnspan=2
                )
            widget.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            col += 1
            if col > 1:
                col = 0
                row += 1
        from decode import TOTAL

        if self.label:
            self.label.destroy()
        self.label = tk.Label(
            text=f"Всего товаров на складе: {TOTAL}",
            font="Calibri",
            height=1,
            foreground="Blue",
        )
        self.label.pack()

    def simulate(self):
        analyzer.get_data()
        for widget in self.charts_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ChartApp(root)
    root.mainloop()
