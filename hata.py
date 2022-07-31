from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

from kivymd.font_definitions import theme_font_styles

import webbrowser
import sqlite3
from kivymd.uix.list import TwoLineIconListItem

KV = '''
# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)
    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color
<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"
    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height
        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"
    MDLabel:
        text: app.title
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]
    MDLabel:
        text: app.by_who
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]
    ScrollView:
        MDList:
            OneLineIconListItem:
                text: "Главная"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "home scr"
                IconLeftWidgetWithoutTouch:
                    icon: "home"
            OneLineIconListItem:
                text: "Калькулятор"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "calculator scr"
                    
                IconLeftWidgetWithoutTouch:
                    icon: "calculator-variant"
            
            OneLineIconListItem:
                text: "Варианты"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "table scr"
                    app.createTable()
                    
                IconLeftWidgetWithoutTouch:
                    icon: "table-heart"
<ListItemWithIcon>:
    id: the_list_item
    
    on_release:
        print("Click")
        root.goToSas(the_list_item)
        #print(the_list_item)
    IconLeftWidgetWithoutTouch:
        icon: 'atom'
MDScreen:
    MDTopAppBar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
    MDNavigationLayout:
        x: toolbar.height
        ScreenManager:
            id: screen_manager
            MDScreen:
                name: "home scr"
                MDBoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: app.title
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["alien-outline", lambda x: app.on_alien_click()]]
                        md_bg_color: 0, 0, 0, 1
                    MDTabs:
                        id: android_tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        background_color: 0.1, 0.1, 0.1, 1
                        
                        Tab:
                            id: tab1 
                            text: "сначала сюда"
                            MDLabel:
                                text: "Привет! Мне нужно сказать вам кое-что неприятное..."
                                halign: "center"
                                font_style: "H6"
                                bold: True
                                x: "10dp"
                                y: "205dp"   
                            
                            MDLabel:
                                text: "Поэтому я решил написать мобилку для этого.\\nЕсли что это не что-то плохое, это скорее просьба\одолжение"
                                halign: "center"
                                font_style: "Body1"
                                #theme_text_color: "Secondary"
                                size_hint_y: None
                                height: self.texture_size[1]
                                x: "10dp"
                                y: "350dp" 
                            
                            MDIconButton:
                                icon: "arrow-right-bold-circle-outline"
                                user_font_size: "48sp"
                                pos_hint: {"center_x": .5, "center_y": .2}
                                on_release: app.switch_tab_by_object(*args)
                        Tab:
                            id: tab2
                            text: "потом сюда"
                            ScrollView:
                                MDGridLayout:
                                    id: box
                                    cols: 1
                                    spacing: "70dp"
                                    padding: "20dp"
                                    adaptive_height: True
                                    #adaptive_size: True
                                    MDLabel:
                                        text: "Что случилось?" 
                                        halign: "center"
                                        font_style: "H6"
                                        bold: True
                                        
                                    MDSmartTile:
                                        radius: 24
                                        box_radius: [0, 0, 24, 24]
                                        box_color: 0, 0, 0, .5
                                        #overlap: False
                                        source: "aquacry.png"
                                        #pos_hint: {"center_x": 5, "center_y": 1}
                                        size_hint: None, None
                                        size: "320dp", "320dp"
                                        MDLabel:
                                            text: "Аква плачет без денег("
                                            bold: True
                                            color: 1, 1, 1, 1
                                    
                                    MDLabel:
                                        text: "sdfdsfdsfоапрвапв\\ngkfgjdklhgd\\ndjgusguiewgueuwg\\neshdfuisudif\\ndfs" 
                                        halign: "center"
                                        font_style: "Body1"
                                        
                                    MDIconButton:
                                        icon: "arrow-right-bold-circle-outline"
                                        user_font_size: "48sp"
                                        
                                        #size_hint_y: 0.1
                                        size_hint_x: 0.7
                                        on_release: app.switch_tab_by_object_to_tab_3(*args)
                                
                        Tab:
                            id: tab3
                            name: "tab 3"
                            text: "затем сюда"
                            ScrollView:
                                MDGridLayout:
                                    id: box
                                    cols: 1
                                    spacing: "70dp"
                                    padding: "20dp"
                                    adaptive_height: True
                                    #adaptive_size: True
                                    MDLabel:
                                        text: "Почему ""Да""?" 
                                        halign: "center"
                                        font_style: "H6"
                                        bold: True
                                        size_hint_y: 0.99
                                        size_hint_x: 0.7
                                    MDLabel:
                                        text: "sdfdsfdsfоапрвапв\\ngkfgjdklhgd\\ndjgusguiewgueuwg\\neshdfuisudif\\ndfs" 
                                        halign: "center"
                                        font_style: "Body1"
                                        #source: "aquacry.png"
                                        
                                    MDSmartTile:
                                        radius: 24
                                        box_radius: [0, 0, 24, 24]
                                        box_color: 0, 0, 0, .5
                                        #overlap: False
                                        source: "123.png"
                                        #pos_hint: {"center_x": 5, "center_y": 1}
                                        size_hint: None, None
                                        size: "320dp", "320dp"
                                        MDLabel:
                                            text: "dfsfsfasdf"
                                            bold: True
                                            color: 1, 1, 1, 1
                                    MDSmartTile:
                                        radius: 24
                                        box_radius: [0, 0, 24, 24]
                                        box_color: 0, 0, 0, .5
                                        #overlap: False
                                        source: "aquacry.png"
                                        #pos_hint: {"center_x": 5, "center_y": 1}
                                        size_hint: None, None
                                        size: "320dp", "320dp"
                                        MDLabel:
                                            text: "Аква плачет без денег("
                                            bold: True
                                            color: 1, 1, 1, 1
                                    MDIconButton:
                                        icon: "home-circle-outline"
                                        user_font_size: "48sp"
                                        
                                        size_hint_y: None
                                        size_hint_x: 0.7
                                        on_release: app.switch_tab_by_object_to_tab_1(*args) 
            MDScreen:
                name: "calculator scr"
                MDBoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: app.title
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["alien-outline", lambda x: app.on_alien_click()]]
                        md_bg_color: 0, 0, 0, 1
                    MDTabs:
                        id: calcTab
                        text: "калькулятор"
                        background_color: 0.1, 0.1, 0.1, 1

                        Tab:
                            id: tab3
                            name: "tab 3"
                            text: "расчет расходов"

                            MDLabel:
                                text: "calculator Screen 2"
                                #halign: "center"
                                x: "10dp"
                                y: "205dp"

                            
                            MDTextField:
                                hint_text: "20000"
                                #mode: "rectangle"
                                fill_color: 0, 0, 0, .4
                                x: "10dp"
                                y: "100dp"
                                #size: "320dp", "320dp"
            MDScreen:
                name: "table scr"
                MDBoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: app.title
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["alien-outline", lambda x: app.on_alien_click()]]
                        md_bg_color: 0, 0, 0, 1
                    ScrollView:
                        MDList:
                            id: container
                    
                                     
            MDScreen:
                name: "pashalka"
                MDBoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "пасхалочка"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["alien-outline", lambda x: app.on_alien_click()]]
                        md_bg_color: 0, 0, 0, 1
                    MDLabel:
                        text: "ты нашел пасхалку, молодец"
                        halign: "center"                            
                         
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                screen_manager: screen_manager
                id: content_drawer
                nav_drawer: nav_drawer
'''

class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class Database:
    def __init__(self):
        self.con = sqlite3.connect('todo.db')
        self.cursor = self.con.cursor()
        self.create_task_table()

    def create_task_table(self):
       
        self.cursor.execute("CREATE TABLE IF NOT EXISTS flats(id integer PRIMARY KEY, description TEXT NOT NULL, price INT NOT NULL, url TEXT NOT NULL)")
        self.con.commit()

    def sasi(self):
        print("sasus")
    def get_flats(self):
        flats_list = self.cursor.execute("SELECT id, description, price FROM flats").fetchall()
        return flats_list
    def get_url_by_id(self, id):
        url = self.cursor.execute("SELECT url FROM flats WHERE id = ?", (id,)).fetchone()
        return url

class ListItemWithIcon(TwoLineIconListItem):
    def goToSas(self, the_list_item):
        db = Database()
        webbrowser.open(db.get_url_by_id(the_list_item.text[0])[0])


class help(MDApp):

    title = "noname"
    by_who = "я это сделал"

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        print("start")

        db = Database()
        flats_list = db.get_flats()

        for flat in flats_list:
            text = str(flat[0]) + " " + flat[1]
            stext = str(flat[2]) + "р"
            self.root.ids.container.add_widget(ListItemWithIcon(text=text, secondary_text = stext))

        #icons_item = {
        #    "home": "Главная",
        #    "calculator-variant": "Калькулятор",
        #}
        #for icon_name in icons_item.keys():
        #    self.root.ids.content_drawer.ids.md_list.add_widget(
        #        ItemDrawer(icon=icon_name, text=icons_item[icon_name])
        #    )
        #программная генерация закладок
        #tabs_item = ["сначала сюда",
        #             "потом сюда",
        #             "теперь вот тут",
        #]
        #for i in range(3):
        #    self.root.ids.android_tabs.add_widget(Tab(text=tabs_item[i]))

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text): 

        print(instance_tab_label)
        print(tab_text)


    def on_alien_click(self):
        self.root.ids.screen_manager.current = "pashalka"
    
    def switch_tab_by_object(self, *args):
        self.root.ids.android_tabs.switch_tab("потом сюда")

    def switch_tab_by_object_to_tab_3(self, *args):
        self.root.ids.android_tabs.switch_tab("затем сюда")

    def switch_tab_by_object_to_tab_1(self, *args):
        self.root.ids.android_tabs.switch_tab("сначала сюда")   

    def createTable(self):
        pass
 
   
help().run()