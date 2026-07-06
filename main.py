from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.clock import Clock

# ==========================================
# LÓGICA MATEMÁTICA
# ==========================================
class ControladorCalculadora:
    def __init__(self):
        self.num1 = ""
        self.op = None
        self.nuevo_numero = False

    def presionar_digito(self, texto_actual, digito):
        if texto_actual == "0" or self.nuevo_numero or texto_actual == "Error":
            self.nuevo_numero = False
            return digito
        return texto_actual + digito

    def presionar_operacion(self, texto_actual, operacion):
        self.num1 = texto_actual
        self.op = operacion
        self.nuevo_numero = True
        return texto_actual

    def presionar_c(self):
        self.num1 = ""
        self.op = None
        self.nuevo_numero = False
        return "0"

    def presionar_igual(self, texto_actual):
        if self.op is None or self.num1 == "":
            return texto_actual
        try:
            val1 = float(self.num1)
            val2 = float(texto_actual)
            if self.op == '+': res = val1 + val2
            elif self.op == '-': res = val1 - val2
            elif self.op == '*': res = val1 * val2
            elif self.op == '/': res = "Error" if val2 == 0 else val1 / val2
            
            if isinstance(res, float) and res.is_integer():
                res = int(res)
            self.op = None
            self.num1 = ""
            self.nuevo_numero = True
            return str(res)
        except:
            self.op = None
            self.num1 = ""
            self.nuevo_numero = True
            return "Error"

# ==========================================
# INTERFAZ GRÁFICA NATIVA
# ==========================================
class PantallaInicio(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 0.92, 0.94, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.actualizar_fondo, size=self.actualizar_fondo)
        
        self.logo = Label(
            text="Calculadora\ndel Yavirac",
            font_size='32sp',  
            color=(0.85, 0.35, 0.45, 1),
            bold=True,
            halign='center'
        )
        self.add_widget(self.logo)

    def actualizar_fondo(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_enter(self, *args):
        # Programación segura para evitar congelamientos en el teléfono
        Clock.schedule_once(self.cambiar_pantalla, 2.0)

    def cambiar_pantalla(self, dt):
        if self.manager:
            self.manager.current = 'calculadora'

class BotonLindo(Button):
    def __init__(self, texto, color_fondo, **kwargs):
        super().__init__(**kwargs)
        self.text = texto
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (0, 0, 0, 0)
        self.font_size = '22sp'
        self.bold = True
        self.color = (1, 1, 1, 1)
        self.color_base = color_fondo
        
        with self.canvas.before:
            self.color_canvas = Color(*self.color_base)
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[15])
        self.bind(pos=self.actualizar_geom, size=self.actualizar_geom)

    def actualizar_geom(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    def on_state(self, instance, value):
        if value == 'down':
            self.color_canvas.rgba = [c * 0.8 for c in self.color_base[:3]] + [1]
        else:
            self.color_canvas.rgba = self.color_base

class Calculadora(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 8
        self.controlador = ControladorCalculadora()
        
        with self.canvas.before:
            Color(1, 0.94, 0.96, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.actualizar_fondo, size=self.actualizar_fondo)

        self.pantalla = TextInput(
            text='0', font_size='36sp', halign='right', readonly=True,
            size_hint_y=0.18, foreground_color=(0.85, 0.35, 0.45, 1),
            background_color=(1, 1, 1, 1), multiline=False
        )
        self.add_widget(self.pantballa if hasattr(self, 'pantballa') else self.pantalla)

        rejilla = GridLayout(cols=4, spacing=6)
        botones = [
            ('7', (1, 0.72, 0.77, 1), 'num'), ('8', (1, 0.72, 0.77, 1), 'num'), ('9', (1, 0.72, 0.77, 1), 'num'), ('+', (0.9, 0.45, 0.55, 1), 'op'),
            ('4', (1, 0.72, 0.77, 1), 'num'), ('5', (1, 0.72, 0.77, 1), 'num'), ('6', (1, 0.72, 0.77, 1), 'num'), ('-', (0.9, 0.45, 0.55, 1), 'op'),
            ('1', (1, 0.72, 0.77, 1), 'num'), ('2', (1, 0.72, 0.77, 1), 'num'), ('3', (1, 0.72, 0.77, 1), 'num'), ('x', (0.9, 0.45, 0.55, 1), '*'),
            ('C', (0.8, 0.35, 0.4, 1), 'c'), ('0', (1, 0.72, 0.77, 1), 'num'), ('=', (0.85, 0.35, 0.45, 1), 'igual'), ('/', (0.9, 0.45, 0.55, 1), '/')
        ]

        for texto, color, tipo in botones:
            btn = BotonLindo(texto=texto, color_fondo=color)
            if tipo == 'num': btn.bind(on_press=lambda val=texto, b=btn: self.press_num(texto))
            elif tipo == 'op' or tipo == '*': btn.bind(on_press=lambda val=texto, b=btn: self.press_op('*' if texto=='x' else texto))
            elif tipo == 'c': btn.bind(on_press=lambda b=btn: self.press_c())
            elif tipo == 'igual': btn.bind(on_press=lambda b=btn: self.press_igual())
            rejilla.add_widget(btn)

        self.add_widget(rejilla)

    def actualizar_fondo(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def press_num(self, d): self.pantalla.text = self.controlador.presionar_digito(self.pantalla.text, d)
    def press_op(self, o): self.pantalla.text = self.controlador.presionar_operacion(self.pantalla.text, o)
    def press_c(self): self.pantalla.text = self.controlador.presionar_c()
    def press_igual(self): self.pantalla.text = self.controlador.presionar_igual(self.pantalla.text)

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PantallaInicio(name='inicio'))
        sm.add_widget(Screen(name='calculadora'))
        sm.get_screen('calculadora').add_widget(Calculadora())
        return sm

if __name__ == '__main__':
    MainApp().run()
