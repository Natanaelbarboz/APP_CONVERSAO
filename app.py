import flet as ft

# Função para realizar as conversões
def converter(valor, de, para):
    conversoes = {
        "km": {"m": 1000, "mi": 0.621371},
        "m": {"km": 0.001, "mi": 0.000621371},
        "mi": {"km": 1.60934, "m": 1609.34},
    }
    if de == para:
        return round(valor, 2)
    return valor * conversoes[de][para]

def main(page: ft.Page):
    page.title = "Conversor de Unidades"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 60
    page.scroll = "adaptive"

    page.appbar = ft.AppBar(
        title=ft.Text(
            "CONVERSOS DE MEDIDAS", 
            size=24, 
            weight=ft.FontWeight.BOLD, 
            color=ft.colors.WHITE  # Define a cor do texto como branco
        ),
        center_title=True,
        bgcolor=ft.colors.BLUE_400,  # Cor de fundo opcional
    )

    # Opções de unidades
    unidades = ["km", "m", "mi"]

    # Elementos do app
    input_valor = ft.TextField(
        label="Valor",
        keyboard_type=ft.KeyboardType.NUMBER,
        expand=True,
    )
    dropdown_de = ft.Dropdown(
        label="De",
        options=[ft.dropdown.Option(u) for u in unidades],
        expand=True,
    )
    dropdown_para = ft.Dropdown(
        label="Para",
        options=[ft.dropdown.Option(u) for u in unidades],
        expand=True,
    )
    resultado = ft.Text(value="Resultado: ", size=24, weight=ft.FontWeight.BOLD)

    # Função chamada ao clicar no botão "Converter"
    def converter_click(e):
        try:
            valor = float(input_valor.value)
            de = dropdown_de.value
            para = dropdown_para.value

            if not de or not para:
                resultado.value = "Por favor, selecione as unidades."
            else:
                valor_convertido = converter(valor, de, para)
                resultado.value = f"Resultado: {valor_convertido} {para}"
        except ValueError:
            resultado.value = "Por favor, insira um valor numérico válido."
        page.update()

    # Função chamada ao clicar no botão "Reset"
    def reset_click(e):
        input_valor.value = ""
        dropdown_de.value = None
        dropdown_para.value = None
        resultado.value = "Resultado: "
        page.update()

    # botao_converter = ft.ElevatedButton("Converter", on_click=converter_click)
    # botao_reset = ft.OutlinedButton("Resetar", on_click=reset_click)

    botao_converter = ft.ElevatedButton(
        text="Converter",
        on_click=converter_click,
        width=150,  # Largura do botão
        height=50,  # Altura do botão
        bgcolor=ft.colors.BLUE,  # Cor de fundo
        color=ft.colors.WHITE,  # Cor do texto
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12)  # Cantos arredondados
        )
    )

    botao_reset = ft.OutlinedButton(
    text="Resetar",
    on_click=reset_click,
    width=150,  # Largura do botão
    height=50,  # Altura do botão
    style=ft.ButtonStyle(
        color=ft.colors.RED,  # Define a cor do texto
        shape=ft.RoundedRectangleBorder(radius=12),  # Cantos arredondados
        side=ft.BorderSide(1, ft.colors.RED),  # Cor e espessura da borda
    )

)



    # Adicionando os elementos à página
    page.add(
        ft.Column(
            [
                input_valor,
                ft.ResponsiveRow(
                    [
                        dropdown_de,
                        dropdown_para,
                    ],
                ),
                ft.ResponsiveRow(
                    [botao_converter, botao_reset],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=15,
                ),
                ft.Container(
                    resultado,
                    alignment=ft.alignment.center,
                    padding=15,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Rodar o app
ft.app(target=main)
