#main.py
#'D-PSR-APP-4IITEENS' developed by /Perspectilt/Kavirajar/ {^_^} 

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.base import runTouchApp
from kivy.clock import mainthread, Clock

try:
    import os
except:
    pass

#Global Variables
std = 11
school = ''
topic = ''
school_list = []
topics9_list = []
topics10_list = []
topics11_list = []
topics12_list = []

#The Class Screen 
class Class(Screen): 
    def next_screen(self,x):
    	global school, std
    	std = x
    	sm.current='School'
    	print('Class selected : ',std)
    	
    def about_screen(self):
        sm.current='About'

#The School Screen
class School(Screen):
    def __init__(self, **kwargs):
        super(School, self).__init__(**kwargs)
        self.name = 'School'
        self.add_widget(School_Display())
    
class School_Display(GridLayout):
    def __init__(self, **kwargs):        
        global school, std, school_list
        super(School_Display, self).__init__(**kwargs)
        self.rows = 10
        self.btn = {}
        
        try:
            file = open('schools.txt','r')
            
        except:
            file = open('schools.txt','w+')
            file = open('schools.txt','r+')

        while True:
            sc = file.readline()
            if sc != '':
                if sc[-1]=='\n':
                    sc = sc[:-1]
                school_list.append(sc)
            else:
                break

        Clock.schedule_interval(self.load_screen, 0.4)
        file.close()

    def load_screen(self,dt):
        global school_list    
        for key in self.btn:
            self.remove_widget(self.btn[key])

        self.btn = {}
        count = 0
        for i in school_list:
            self.btn[count] = Button(
                text = i,
                size_hint =(0.9, 0.1)
                )
            self.btn[count].bind(on_release=self.next_screen)
            self.add_widget(self.btn[count])
            count += 1
        else:
            self.btn[count+1] = Button(
                text = 'Edit',
                size_hint =(0.8, 0.05),
                background_color = (0, 0.3, 1, 1)
                )
            self.btn[count+1].bind(on_release=self.edit_screen)
            self.add_widget(self.btn[count+1])
            self.btn[count+2] = Button(
                text = 'Back',                
                size_hint =(0.8, 0.05),
                background_color = (1, 0, 0, 1)
                )
            self.btn[count+2].bind(on_release=self.prev_screen)
            self.add_widget(self.btn[count+2])
        
    def next_screen(self,ref):
        global school
        school = ref.text
        sm.transition.direction = 'left'
        sm.current='Topic'
        print('School selected: ',school)
        
    def prev_screen(self,ref):
        sm.transition.direction = 'right'
        sm.current='Class'
        
    def edit_screen(self,ref):
        sm.transition.direction = 'left'
        sm.current='School_Edit'
        #School_Edit()
    
class School_Edit(Screen):
    def content(self):
        try:
            Text = open('schools.txt','r+').read()
        except:
            Text = '^_^'
        return str(Text)

    def cancel(self):
        sm.current='School'
        
    def done(self, change):
        global school_list
        school_list = change.split('\n')
        while True:
            try:
                school_list.remove('')
            except:
                break
            
        file = open('schools.txt','w+')
        file.write(str(change))
        sm.current='School'


#The Topic Screen
class Topic(Screen):
    def __init__(self, **kwargs):
        super(Topic, self).__init__(**kwargs)
        self.name = 'Topic'
        self.add_widget(Topic_Display())
    
class Topic_Display(GridLayout):
    def __init__(self, **kwargs):        
        global school, std, school_list, topics9_list, topics10_list, topics11_list, topics12_list
        super(Topic_Display, self).__init__(**kwargs)
        self.rows = 16
        self.btn = {}

        topics9_list = self.load_topics('9')
        topics10_list = self.load_topics('10')
        topics11_list = self.load_topics('11')
        topics12_list = self.load_topics('12')
        
        Clock.schedule_interval(self.update, 0.4)

    def update(self, dt):
        global school, std, school_list, topics9_list, topics10_list, topics11_list, topics12_list
        if std == 9: topic_list = topics9_list
        elif std == 10: topic_list = topics10_list
        elif std == 11: topic_list = topics11_list
        elif std == 12: topic_list = topics12_list
        else: topic_list = []
    
        for key in self.btn:
            self.remove_widget(self.btn[key])

        self.btn = {}
        count = 0
        for i in topic_list:
            self.btn[count] = Button(
                text = i,
                size_hint =(0.9, 0.1)
                )
            self.btn[count].bind(on_release=self.next_screen)
            self.add_widget(self.btn[count])
            count += 1
        else:
            self.btn[count+1] = GridLayout(
                cols = 2,
                size_hint = (0.8, 0.05)
                )
            edit_btn = Button(
                text = 'Edit',
                size_hint =(0.8, 0.05),
                background_color = (0, 0.3, 1, 1)
                )
            back_btn = Button(
                text = 'Back',                
                size_hint =(0.8, 0.05),
                background_color = (1, 0, 0, 1)
                )
            back_btn.bind(on_release=self.prev_screen)
            edit_btn.bind(on_release=self.edit_screen)
            self.btn[count+1].add_widget(edit_btn)
            self.btn[count+1].add_widget(back_btn)
            self.add_widget(self.btn[count+1])
            
    def load_topics(self, x):
        temp_list = []
        try:
            file = open('topics'+x+'.txt','r')
        except:
            file = open('topics'+x+'.txt','w+')
            file = open('topics'+x+'.txt','r+')
        while True:
            tp = file.readline()
            if tp != '':
                if tp[-1]=='\n':
                    tp = tp[:-1]
                temp_list.append(tp)
            else:
                break
        file.close()
        return temp_list

    def next_screen(self,ref):
        global topic
        topic = ref.text
        sm.transition.direction = 'left'
        sm.current='Stat'
        print('Topic selected: ',topic)
        
    def prev_screen(self,ref):
        sm.transition.direction = 'right'
        sm.current='School'
        
    def edit_screen(self,ref):
        global std
        sm.transition.direction = 'left'
        if std == 9:
            sm.current='Topics9Edit'
        elif std == 10:
            sm.current='Topics10Edit'
        elif std == 11:
            sm.current='Topics11Edit'
        elif std == 12:
            sm.current='Topics12Edit'

class Topics9Edit(Screen):
    def content(self):
        try:
            Text = open('Topics9.txt','r+').read()
        except:
            Text = '^_^'
        return str(Text)

    def cancel(self):
        sm.current='Topic'
        
    def done(self, change):
        global topics9_list
        topics9_list = change.split('\n')
        while True:
            try:
                topics9_list.remove('')
            except:
                break
            
        file = open('topics9.txt','w+')
        file.write(str(change))
        sm.current='Topic'

class Topics10Edit(Screen):
    def content(self):
        try:
            Text = open('Topics10.txt','r+').read()
        except:
            Text = '^_^'
        return str(Text)

    def cancel(self):
        sm.current='Topic'
        
    def done(self, change):
        global topics10_list
        topics10_list = change.split('\n')
        while True:
            try:
                topics10_list.remove('')
            except:
                break
            
        file = open('topics10.txt','w+')
        file.write(str(change))
        sm.current='Topic'

class Topics11Edit(Screen):
    def content(self):
        try:
            Text = open('Topics11.txt','r+').read()
        except:
            Text = '^_^'
        return str(Text)

    def cancel(self):
        sm.current='Topic'
        
    def done(self, change):
        global topics11_list
        topics11_list = change.split('\n')
        while True:
            try:
                topics11_list.remove('')
            except:
                break
            
        file = open('topics11.txt','w+')
        file.write(str(change))
        sm.current='Topic'

class Topics12Edit(Screen):
    def content(self):
        try:
            Text = open('Topics12.txt','r+').read()
        except:
            Text = '^_^'
        return str(Text)

    def cancel(self):
        sm.current='Topic'
        
    def done(self, change):
        global topics12_list
        topics12_list = change.split('\n')
        while True:
            try:
                topics12_list.remove('')
            except:
                break
            
        file = open('topics12.txt','w+')
        file.write(str(change))
        sm.current='Topic'

class Stat(Screen):
    def __init__(self, **kwargs):
        super(Stat, self).__init__(**kwargs)
        self.name = 'Stat'
        self.add_widget(Stat_Display())
    
class Stat_Display(FloatLayout):
    def __init__(self, **kwargs):        
        global school, std, school_list, topics9_list, topics10_list, topics11_list, topics12_list
        super(Stat_Display, self).__init__(**kwargs)
        self.curr_topic = topic
        Clock.schedule_interval(self.refresh, 0.4)

    def refresh(self, dt):
        global topic
        if topic != self.curr_topic:
            self.update()
            
    def update(self):
        global topic, school, std
        self.curr_topic = topic
        try:
            self.remove_widget(self.title)
            self.remove_widget(self.lb0)
            self.remove_widget(self.lb1)
            self.remove_widget(self.lb2)
            self.remove_widget(self.lb3)
            self.remove_widget(self.lb4)
            self.remove_widget(self.ch0)
            self.remove_widget(self.ch1)
            self.remove_widget(self.ch2)
            self.remove_widget(self.ch3)
            self.remove_widget(self.ch4)
        except:
            pass
       
        self.title = Label(
            text = topic.upper(),
            pos_hint = {'x':0.45,'y':0.92},
            size_hint = (0.1,0.1),
            halign = 'justify'
            )
        self.lb0 = Label(
            text = 'Work Sheet',
            pos_hint = {'x':0.2,'y':0.85},
            size_hint = (0.1,0.1)
            )
        self.lb1 = Label(
            text = 'Synopsis',
            pos_hint = {'x':0.2,'y':0.77},
            size_hint = (0.1,0.1)
            )
        self.lb2 = Label(
            text = 'Discussion',
            pos_hint = {'x':0.2,'y':0.69},
            size_hint = (0.1,0.1)
            )
        self.lb3 = Label(
            text = 'Exam - Mains',
            pos_hint = {'x':0.2,'y':0.61},
            size_hint = (0.1,0.1)
            )
        self.lb4 = Label(
            text = 'Exam - Advanced',
            pos_hint = {'x':0.2,'y':0.53},
            size_hint = (0.1,0.1)
            )
        self.ch0 = CheckBox(
            pos_hint = {'x':0.6,'y':0.85},
            size_hint = (0.1,0.1),
            active = self.load(0)
            )
        self.ch0.bind(on_press = self.save)
        self.ch1 = CheckBox(
            pos_hint = {'x':0.6,'y':0.77},
            size_hint = (0.1,0.1),
            active = self.load(1)
            )
        self.ch1.bind(on_press = self.save)
        self.ch2 = CheckBox(
            pos_hint = {'x':0.6,'y':0.69},
            size_hint = (0.1,0.1),
            active = self.load(2)
            )
        self.ch2.bind(on_press = self.save)
        self.ch3 = CheckBox(
            pos_hint = {'x':0.6,'y':0.61},
            size_hint = (0.1,0.1),
            active = self.load(3)
            )
        self.ch3.bind(on_press = self.save)
        self.ch4 = CheckBox(
            pos_hint = {'x':0.6,'y':0.53},
            size_hint = (0.1,0.1),
            active = self.load(4)
            )
        self.ch4.bind(on_press = self.save)
        
        self.txtbox = TextInput(
            text = self.description(),
            pos_hint = {'x':0.1,'y':0.2},
            size_hint = (0.8,0.3)
            )
        self.back_btn = Button(
            text = 'Back',
            background_color = (1.0, 0.0, 0.0, 1),
            pos_hint = {'x':0.01, 'y': 0.02},
            size_hint = (0.49, 0.07)
            )
        self.back_btn.bind(on_release=self.cancel)
        self.done_btn = Button(
            text = 'Done',
            pos_hint = {'x':0.5, 'y': 0.02},
            size_hint = (0.49, 0.07)
            )
        self.done_btn.bind(on_release=self.done)
        
        self.add_widget(self.title)
        self.add_widget(self.lb0)
        self.add_widget(self.lb1)
        self.add_widget(self.lb2)
        self.add_widget(self.lb3)
        self.add_widget(self.lb4)
        self.add_widget(self.ch0)
        self.add_widget(self.ch1)
        self.add_widget(self.ch2)
        self.add_widget(self.ch3)
        self.add_widget(self.ch4)
        self.add_widget(self.txtbox)
        self.add_widget(self.back_btn)
        self.add_widget(self.done_btn)
        
    def description(self):
        global school, std, topic
        if school != '' and topic != '':
            try:
                file = open(str(std)+'-'+school+'-'+topic+'.txt','r')
            except:
                file = open(str(std)+'-'+school+'-'+topic+'.txt','w+')
                file = open(str(std)+'-'+school+'-'+topic+'.txt','r')
                
            data = file.readline()
            data = file.read()
            file.close()
            return data
        else:
            return ''
        
    def load(self, no):
        global school, topic, std
        if school != '' and topic != '':
            try:
                file = open(str(std)+'-'+school+'-'+topic+'.txt','r')
            except:
                file = open(str(std)+'-'+school+'-'+topic+'.txt','w+')
                file = open(str(std)+'-'+school+'-'+topic+'.txt','r+')
                
            data = file.readline()
            if data != '':
                try:
                    return bool(int(data[no]))
                except:
                    return False
            else:
                return False
            file.close()
        else:
            return False

    def save(self, ref):
        global school, topic, std
        if school != '' and topic != '':
            try:
                file = open(str(std)+'-'+school+'-'+topic+'.txt','r')
                data = file.readline()
                data = file.read()
            except:
                data = ''
                
            file = open(str(std)+'-'+school+'-'+topic+'.txt','w+')
            if data != '':
                new_data = str(int(self.ch0.active))+str(int(self.ch1.active))+str(int(self.ch2.active))+str(int(self.ch3.active))+str(int(self.ch4.active))+'\n'+data
            else:
                new_data = str(int(self.ch0.active))+str(int(self.ch1.active))+str(int(self.ch2.active))+str(int(self.ch3.active))+str(int(self.ch4.active))
            file.write(new_data)
            file.close()
            
    def cancel(self, ref):
        sm.current = 'Topic'
        sm.transition.direction = 'right'

    def done(self, ref):
        if school != '' and topic != '':
            file = open(str(std)+'-'+school+'-'+topic+'.txt','w+')
            data = self.txtbox.text      
            new_data = str(int(self.ch0.active))+str(int(self.ch1.active))+str(int(self.ch2.active))+str(int(self.ch3.active))+str(int(self.ch4.active))+'\n'+data
            file.write(new_data)
            file.close()
        sm.current = 'Topic'
        sm.transition.direction = 'right'

#The About Screen
class About(Screen):
    def next_screen(self):
        sm.current = 'Class'

    def save_reset(self):
        sm.current = 'Reset'
        
class Reset(Screen):    
    def cancel(self):
        sm.current = 'About'

    def confirm(self):
        print('Reseting...')
        try:
            files = [f for f in os.listdir('.') if os.path.isfile(f)]
            for f in files:
                if f not in ['main.py','design.kv','TheApp.py','schools.txt','topics10.txt','topics11.txt','topics12.txt','topics9.txt']:
                    if f[:1].isdigit():
                        os.remove(f)
            print('Reset Successful')
            
        except:
            print('Reset Unsuccessful')
            

kv = Builder.load_file("design.kv")
sm = ScreenManager()
screens = [Class(name='Class'), School(name='School'), School_Edit(name='School_Edit'), Topic(name='Topic'), Topics9Edit(name='Topics9Edit'), Topics10Edit(name='Topics10Edit'), Topics11Edit(name='Topics11Edit'), Topics12Edit(name='Topics12Edit'), Stat(name='Stat'), About(name='About'), Reset(name='Reset')]
for screen in screens:
    sm.add_widget(screen)
sm.current = "Class"

class MyApp(App):
    def build(self):
        self.title = 'PSR APP'
        return sm
    
MyApp().run()
