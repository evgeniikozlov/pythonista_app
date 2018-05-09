import ui, dialogs, datetime


class CalculationApp:
    content_map = [{
        "header": "На местности",
        "options": ["В укрытии", "В землянке"]
    }, {
        "header": "В технике",
        "options": ["Автомобиль", "Танк", "Вертолет"]
    }, {
        "header": "В городе",
        "options": ["Жилой высотный дом", "Жилой малоэтажный дом"]
    }, {
        "header": "group 4",
        "options": ["opt7", "opt8", "opt9"]
    }, {
        "header": "group 5",
        "options": ["opt7", "opt8", "opt9"]
    }, {
        "header": "group 6",
        "options": ["opt7", "opt8", "opt9"]
    }, {
        "header": "group 7",
        "options": ["opt7", "opt8", "opt9"]
    }, {
        "header": "group 8",
        "options": ["opt7", "opt8", "opt9"]
    }]

    def calculate_pressed(self, sender):
        result = self.calculate_results()
        self.history[datetime.datetime.now()] = result
        self.result_textfield.text = str(result)

    def switch_pressed(self, sender):
        self.textfields[sender.name].enabled = sender.value

    def calculate_results(self):
        result = 0
        for input in self.textfields.values():
            if not input.enabled:
                input_value = 0
            else:
                try:
                    input_value = float(input.text)
                except:
                    input_value = 0
            result += input_value
        return result

    def clear_inputs(self, sender):
        for input in self.textfields.values():
            input.text = ""
            input.enabled = False
        for switch in self.switches.values():
            switch.value = False
        self.result_textfield.text = ""

    def show_history(self, sender):
        items = []
        for date, result in self.history.items():
            items.append({
                "title": "{}: {}".format(date.strftime("%Y-%m-%d %H:%M:%S"), result),
            })

        dialogs.list_dialog(title="История", items=items, multiple=False)

    def testf(self, tableview, section, row):
        dialogs.text_dialog(text="{}_{}_{}".format(tableview, section, row))

    # def fill_inputs(self, history):
    #     if history is not None:
    #         self.result_textfield.text = str(history)

    def generate_height(self):
        self.row_count = 0
        self.row_height = 40
        self.row_start = 10
        while True:
            yield self.row_start + self.row_count * self.row_height
            self.row_count += 1

    def __init__(self):
        self.textfields = {}
        self.switches = {}
        self.history = {}

        screen_width, screen_height = ui.get_screen_size()
        view = ui.View(frame=(0, 0, screen_width, screen_height), name='Расчет укрытий', background_color='white')
        height_gen = self.generate_height()
        scroll_view_width = screen_width * 2 / 3 - 10
        scroll_view = ui.ScrollView(frame=(10, 10, scroll_view_width, screen_height - 90),
                                    border_width=1,
                                    border_color="lightgrey",
                                    corner_radius=5)
        view.add_subview(scroll_view)

        group_label_width = screen_width * 2 / 3 - 20
        option_label_width = screen_width * 2 / 3 - 130

        for content in self.content_map:
            group_label = ui.Label(text=content["header"],
                                   font=('<system-bold>', 17),
                                   frame=(10, next(height_gen), group_label_width, 30))
            scroll_view.add_subview(group_label)

            for option in content["options"]:
                height = next(height_gen)
                name = "{}_{}".format(content["header"], option)

                switch = ui.Switch(value=False,
                                   name=name,
                                   action=self.switch_pressed,
                                   frame=(10, height, 50, 30))
                scroll_view.add_subview(switch)
                self.switches[name] = switch

                textfield = ui.TextField(enabled=False,
                                         name=name,
                                         frame=(70, height, 50, 30))
                scroll_view.add_subview(textfield)
                self.textfields[name] = textfield

                label = ui.Label(text=option,
                                 frame=(130, height, option_label_width, 30))
                scroll_view.add_subview(label)

        scroll_view.content_size = (scroll_view_width, next(height_gen))

        controls_x = screen_width * 2 / 3 + 10
        controls_width = screen_width * 1 / 3 - 20

        result_button = ui.Button(title='Расчет',
                                  frame=(controls_x, 10, controls_width, 50),
                                  border_width=1,
                                  border_color="lightgrey",
                                  corner_radius=5,
                                  action=self.calculate_pressed,
                                  flex="W")
        result_button.width = controls_width
        result_button.height = 50
        view.add_subview(result_button)

        self.result_textfield = ui.TextField(enabled=True,
                                             name="result",
                                             text="",
                                             frame=(controls_x, 70, controls_width, 50),
                                             flex="W")
        view.add_subview(self.result_textfield)

        clear_button = ui.Button(title='Очистить',
                                 frame=(controls_x, 180, controls_width, 50),
                                 border_width=1,
                                 border_color="lightgrey",
                                 corner_radius=5,
                                 action=self.clear_inputs,
                                 flex="W")
        clear_button.width = controls_width
        clear_button.height = 50
        view.add_subview(clear_button)

        history_button = ui.Button(title='История',
                                   frame=(controls_x, 240, controls_width, 50),
                                   border_width=1,
                                   border_color="lightgrey",
                                   corner_radius=5,
                                   action=self.show_history,
                                   flex="W")
        history_button.width = controls_width
        history_button.height = 50
        view.add_subview(history_button)

        view.present('full_screen', orientations=['portrait'])


if __name__ == "__main__":
    app = CalculationApp()
