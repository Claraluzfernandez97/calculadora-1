from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window

# Configurar un tamaño de ventana estándar para pruebas en PC (opcional)
Window.size = (360, 640)

class CalculadoraScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Layout principal vertical
        layout_principal = MDBoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Pantalla de visualización de texto
        self.pantalla = MDTextField(
            text="0",
            halign="right",
            font_size="32sp",
            readonly=True,
            mode="fill",
            fill_color_normal=(0.95, 0.95, 0.95, 1)
        )
        layout_principal.add_widget(self.pantalla)
        
        # Grid para los botones (4 columnas)
        grid_botones = MDGridLayout(cols=4, spacing=10, size_hint_y=0.8)
        
        # Lista de botones a crear
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        for texto in botones:
            boton = MDRoundFlatButton(
                text=texto,
                font_size="24sp",
                size_hint=(1, 1),
                on_press=self.al_presionar_boton
            )
            grid_botones.add_widget(boton)
            
        layout_principal.add_widget(grid_botones)
        self.add_widget(layout_principal)

    def al_presionar_boton(self, instancia):
        texto_boton = instancia.text
        texto_actual = self.pantalla.text

        if texto_boton == 'C':
            self.pantalla.text = '0'
        elif texto_boton == '=':
            try:
                # Evalúa la expresión matemática de forma segura
                resultado = str(eval(texto_actual))
                self.pantalla.text = resultado
            except Exception:
                self.pantalla.text = 'Error'
        else:
            if texto_actual == '0' or texto_actual == 'Error':
                self.pantalla.text = texto_boton
            else:
                self.pantalla.text += texto_boton


class CalculadoraApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return CalculadoraScreen()


if __name__ == '__main__':
    CalculadoraApp().run()
