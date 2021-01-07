import kivymd
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.dialog import MDDialog
class Calculator(MDApp):
    dialog = None
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Syntax Error",
                text="Kindly check your expression !",
                size_hint=(0.75,0.3)
            )
        self.dialog.open()
    def build(self):
        def print_text(self):
            if(len(disp.text)>0 and disp.text[0]=='='):
                small_disp.text=""
                disp.text=disp.text[1:]
            disp.text+=self.text
        def all_clear(self):
            disp.text=""
            small_disp.text=""
        def clear(self):
            if small_disp.text=="":
                disp.text=disp.text[:-1]
            else:
                small_disp.text = ""
                disp.text=disp.text[1:len(disp.text)]
        def equal(self):
            try:
                temp=disp.text
                disp.text="="+str(eval(disp.text))
                small_disp.text += temp
            except SyntaxError:
                Calculator.show_alert_dialog(Calculator)
        calc = MDFloatLayout()
        btn_size=(0.15,0.075)
        small_disp=MDLabel(text="",halign="center",pos_hint={"center_y":0.85},font_style="H5")
        disp = MDLabel(text="",halign="center",pos_hint={"center_y":0.75},font_style="H4")
        calc.add_widget(MDToolbar(title="Calculator",pos_hint={"center_y":0.96},size_hint=(1,0.15)))
        calc.add_widget(disp)
        calc.add_widget(small_disp)
        element=["(",")","C","AC","1","2","3","+","4","5","6","-","7","8","9","*",".","0","=","/"]
        dif_func=["C","AC","="]
        y_margin=0.6
        y_spacing=0.1
        x_margin=0.2
        x_spacing=0.2
        count=0
        for i in element:
            if i not in dif_func:
                calc.add_widget(MDRoundFlatButton(text=i,pos_hint={"center_y":y_margin,"center_x":x_margin},size_hint=btn_size,on_press=print_text))
            else:
                if i=="C":
                    calc.add_widget(MDRoundFlatButton(text=i, pos_hint={"center_y": y_margin, "center_x": x_margin}, size_hint=btn_size,on_press=clear))
                elif i=="AC":
                    calc.add_widget(MDRoundFlatButton(text=i, pos_hint={"center_y": y_margin, "center_x": x_margin},size_hint=btn_size, on_press=all_clear))
                else:
                    calc.add_widget(MDRoundFlatButton(text=i, pos_hint={"center_y": y_margin, "center_x": x_margin},size_hint=btn_size, on_press=equal))
            count+=1
            x_margin+=x_spacing
            if count==4:
                count=0
                y_margin-=y_spacing
                x_margin=0.2
        return calc
Calculator().run()