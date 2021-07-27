from main_imports import MDDialog, MDScreen, MDRaisedButton,BoxLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivymd.uix.button import MDRaisedButton
# from kivymd.uix.dialog import MDDialog

from libs.applibs import utils
utils.load_kv("home.kv")


class Content(BoxLayout):
    pass

class Home_Screen(MDScreen):
    dialog = None
    call = 0
    def show_confirmation_dialog(self,title_msg):
        print(title_msg,self.call)
        if self.call != 0:
            self.dialog.title = title_msg+" "+"-"+" 125"
            # self.dialog.dismiss()
        self.call = self.call + 1
        if not self.dialog:
            self.dialog = MDDialog(
                title=title_msg+" "+"-"+" 125",
                type="custom",
                content_cls=Content(),
            )
        self.dialog.open()
    def click(self,text):
        # self.ids.rv.data = [] # clear search historic results
        self.ids.rv.data.append({"image": "assets\img\profile.jpg","text":text})
    def download(self,one,two,name):
        print(one,two)
        self.parent.get_screen("download").download_start(name,40)
        self.dialog.dismiss()
