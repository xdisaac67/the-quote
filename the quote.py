import flet as ft
def main(page:ft.Page):

#funtion
    def change_text(e):
        normal.value = language.value

#text
    normal = ft.Text(value="What will u have after 500 years",size=20,font_family = "Nunito")
#buttons
    language = ft.RadioGroup(
        on_change = change_text,
    content=ft.Row(controls=[
        ft.Radio(value = "what will you have after 500 years!", label="english"),
        ft.Radio(value = "O que você terá daqui a 500 anos!", label="portuguese"),
        ft.Radio(value = "Que restera-t-il après 500 ans!", label= "french" ),
        ft.Radio(value = "¿Qué tendrás dentro de 500 años", label = "spanish"),]))
    
    omnimen = ft.Image(src = "images/thinking.png",height = 600, width = 600)

    the_language = ft.Row(controls=[language,normal], alignment=ft.MainAxisAlignment.CENTER)
    omniman = ft.Row(controls=[omnimen])

    the_omnimen = ft.Column(controls=[omniman],alignment=ft.MainAxisAlignment.END, 
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,expand=True)

    page.add(the_language,the_omnimen)

ft.run(main=main, assets_dir="assets")