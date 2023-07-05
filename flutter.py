import flet as flt
from flet import Page, TextField, Row, IconButton, icons
  
def myapp(page: flt.Page):
    page.theme_mode = flt.ThemeMode.LIGHT
    page.window_height = 400
    page.window_width = 500
    
    def button_clicked(e):
        if str(e).replace(" ","") != "":
            t.value = " Yo this Is Prakhar Guy is so coooll !!"
        page.update()
    
    t = TextField()

    
    
    tb2 = flt.TextField(label="With placeholder", hint_text="Please enter text here")

    b = flt.ElevatedButton(text="Submit", on_click=button_clicked)
    
    page.add( tb2,b,t)


  
flt.app(target=myapp)
