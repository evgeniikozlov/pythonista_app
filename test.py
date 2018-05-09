import ui, dialogs, datetime


class CalculationApp:
    content_map = [{
        "header": "group 1",
        "options": ["opt1", "opt2", "opt3"]
    }, {
        "header": "group 2",
        "options": ["opt4", "opt5", "opt6"]
    }, {
        "header": "group 3",
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
        # items_titles = ["{}: {}".format(date, result) for (date, result) in self.history.items()]
        items = []
        for date, result in self.history.items():
            items.append({
                "title": "{}: {}".format(date.strftime("%Y-%m-%d %H:%M:%S"), result),
                "accessory_type": "detail_button"
            })

        history = dialogs.list_dialog(title="История", items=items, multiple=False)
        self.fill_inputs(history)

    def testf(self, tableview, section, row):
        dialogs.text_dialog(text="{}_{}_{}".format(tableview, section, row))

    def fill_inputs(self, history):
        if history is not None:
            self.result_textfield.text = str(history)

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
        start_column = 20
        scroll_view = ui.ScrollView(frame=(10, 10, 400, 480),
                                    border_width=1,
                                    border_color="lightgrey",
                                    corner_radius=5)
        view.add_subview(scroll_view)

        for content in self.content_map:
            group_label = ui.Label(text=content["header"],
                                   font=('<system-bold>', 17),
                                   frame=(start_column, next(height_gen), 120, 30))
            scroll_view.add_subview(group_label)

            for option in content["options"]:
                height = next(height_gen)
                name = "{}_{}".format(content["header"], option)

                switch = ui.Switch(value=False,
                                   name=name,
                                   action=self.switch_pressed,
                                   frame=(start_column, height, 50, 30))
                scroll_view.add_subview(switch)
                self.switches[name] = switch

                textfield = ui.TextField(enabled=False,
                                         name=name,
                                         frame=(start_column + 60, height, 50, 30))
                scroll_view.add_subview(textfield)
                self.textfields[name] = textfield

                label = ui.Label(text=option,
                                 frame=(start_column + 120, height, 100, 30))
                scroll_view.add_subview(label)

        scroll_view.content_size = (400, next(height_gen))

        result_button = ui.Button(title='Расчет',
                                  frame=(500, 50, 180, 40),
                                  border_width=1,
                                  border_color="lightgrey",
                                  corner_radius=5,
                                  action=self.calculate_pressed)
        view.add_subview(result_button)

        clear_button = ui.Button(title='Очистить',
                                 frame=(500, 150, 180, 40),
                                 border_width=1,
                                 border_color="lightgrey",
                                 corner_radius=5,
                                 action=self.clear_inputs)
        view.add_subview(clear_button)

        self.result_textfield = ui.TextField(enabled=True,
                                             name="result",
                                             text="empty",
                                             frame=(500, 250, 180, 40))
        view.add_subview(self.result_textfield)

        history_button = ui.Button(title='История',
                                 frame=(500, 350, 180, 40),
                                 border_width=1,
                                 border_color="lightgrey",
                                 corner_radius=5,
                                 action=self.show_history)
        view.add_subview(history_button)

        view.present('full_screen')


# class HistoryDialogDelegate():
#     def tableview_accessory_button_tapped(self, scrollview):
#         # You can use the content_offset attribute to determine the current scroll position
#         pass


if __name__ == "__main__":
    app = CalculationApp()
