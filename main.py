from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle, RoundedRectangle

class CalculadoraApp(App):
    def build(self):
        # Contenedor principal
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Fondo estético
        with main_layout.canvas.before:
            Color(1, 0.94, 0.96, 1)
            self.rect = Rectangle(size=main_layout.size, pos=main_layout.pos)
        main_layout.bind(size=self._update_rect, pos=self._update_rect)

        # Pantalla de resultados
        self.pantalla = TextInput(
            text='0', font_size='40sp', halign='right', readonly=True,
            size_hint_y=0.2, foreground_color=(0.85, 0.35, 0.45, 1),
            background_color=(1, 1, 1, 1), multiline=False
        )
        main_layout.add_widget(self.pantalla)

        # Rejilla de botones
        grid = GridLayout(cols=4, spacing=8)
        botones = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            'C', '0', '=', '/'
        ]

        for texto in botones:
            # Asignar colores según el tipo de botón
            if texto == 'C':
                color_btn = (0.8, 0.35, 0.4, 1)
            elif texto in ['+', '-', '*', '/', '=']:
                color_btn = (0.9, 0.45, 0.55, 1)
            else:
                color_btn = (1, 0.72, 0.77, 1)

            btn = Button(
                text=texto, font_size='26sp', bold=True,
                background_normal='', background_color=color_btn,
                color=(1, 1, 1, 1)
            )
            btn.bind(on_press=self.on_key_press)
            grid.add_widget(btn)

        main_layout.add_widget(grid)
        self.valores_iniciales()
        return main_layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def valores_iniciales(self):
        self.num1 = ""
        self.op = None
        self.nuevo_numero = False

    def on_key_press(self, instance):
        texto = instance.text
        actual = self.pantalla.text

        if texto == 'C':
            self.pantalla.text = '0'
            self.valores_iniciales()
        elif texto in ['+', '-', '*', '/']:
            self.num1 = actual
            self.op = texto
            self.nuevo_numero = True
        elif texto == '=':
            if self.op and self.num1:
                try:
                    v1 = float(self.num1)
                    v2 = float(actual)
                    if self.op == '+': res = v1 + v2
                    elif self.op == '-': res = v1 - v2
                    elif self.op == '*': res = v1 * v2
                    elif self.op == '/': res = "Error" if v2 == 0 else v1 / v2
                    
                    if isinstance(res, float) and res.is_integer():
                        res = int(res)
                    
                    self.pantalla.text = str(res)
                except:
                    self.pantalla.text = 'Error'
                self.valores_iniciales()
                self.nuevo_numero = True
        else:
            if actual == '0' or self.nuevo_numero or actual == 'Error':
                self.pantalla.text = texto
                self.nuevo_numero = False
            else:
                self.pantalla.text = actual + texto

if __name__ == '__main__':
    CalculadoraApp().run()
