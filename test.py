import ui


class CalculationApp:
    content_map = [{
        "header": "group 1",
        "options": ["opt1", "opt2", "opt3"]
    }, {
        "header": "group 2",
        "options": ["opt4", "opt5", "opt6"]
    }]

    def calculate_pressed(self, sender):
        result = self.calculate_results()
        self.result_textfield.text = result

    def switch_pressed(self, sender):
        pass

    def textfield_changed(self, sender):
        self.inputs[sender.name] = sender.text

    def calculate_results(self):
        return 1

    def clear_inputs(self, sender):
        pass

    def generate_height(self):
        self.row_count = 0
        self.row_height = 10
        while True:
            yield 5 + self.row_count * self.row_height
            self.row_count += 1

    def __init__(self):
        self.inputs = {}

        view = ui.View(frame=(0, 0, 700, 500), name='Расчет укрытий', background_color='white')
        height = self.generate_height()
        start_column = 30

        for content in self.content_map:
            label = ui.Label(text=content["header"])
            label.center = (start_column, next(height))
            view.add_subview(label)
            for option in content["options"]:
                switch = ui.Switch(value=False, name="{}_{}".format(content["header"], option), action=self.switch_pressed)
                switch.center = (start_column, next(height))
                view.add_subview(switch)
                textfield = ui.TextField(enabled=True, name="{}_{}".format(content["header"], option))
                textfield.center = (start_column + 50, next(height))
                view.add_subview(textfield)
                label = ui.Label(text=option)
                label.center = (start_column + 100, next(height))
                view.add_subview(label)
        button = ui.Button(title='Расчет')
        button.center = (500, 50)
        button.action = self.calculate_pressed
        view.add_subview(button)

        button = ui.Button(title='Очистить')
        button.center = (500, 150)
        button.action = self.clear_inputs
        view.add_subview(button)

        self.result_textfield = ui.TextField(enabled=True, name="result", text="empty")
        self.result_textfield.center = (500, 250)
        view.add_subview(self.result_textfield)

        view.present('sheet')


if __name__ == "__main__":
    app = CalculationApp()
