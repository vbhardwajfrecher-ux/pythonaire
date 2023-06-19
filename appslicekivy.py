import kivy
kivy.require("1.11.1")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout


class InputFormatterApp(App):
    def format_input(self, button):
        input_text = self.input_textinput.text.strip()
        numbers = input_text.split("\n")
        formatted_output = ",".join(f"'{number}'" for number in numbers)
        self.output_label.text = formatted_output
    
    def build(self):
        # Create the main layout
        main_layout = BoxLayout(orientation="vertical")

        # Create the input layout
        input_layout = GridLayout(cols=1, size_hint=(1, 0.3))
        input_layout.add_widget(Label(text="Input:", font_size="20sp"))
        self.input_textinput = TextInput(font_size="16sp")
        input_layout.add_widget(self.input_textinput)

        # Create the output layout
        output_layout = GridLayout(cols=1, size_hint=(1, 0.3))
        output_layout.add_widget(Label(text="Output:", font_size="20sp"))
        self.output_label = Label(font_size="16sp")

        # Create the scroll view for the output
        output_scrollview = ScrollView(size_hint=(1, None), size=(800, 400))
        output_scrollview.add_widget(self.output_label)
        output_layout.add_widget(output_scrollview)

        # Create the process button
        process_button = Button(text="Process", font_size="20sp")
        process_button.bind(on_release=self.format_input)

        # Add the layouts and button to the main layout
        main_layout.add_widget(input_layout)
        main_layout.add_widget(output_layout)
        main_layout.add_widget(process_button)

        return main_layout


if __name__ == "__main__":
    InputFormatterApp().run()
