from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.camera import Camera
from rembg import remove
import os
import cv2
import numpy as np
import random as rand
class AddApparelView(Screen):
    #===========INITIALIZATION======================================
    
    def __init__(self, screen_manager, **kwargs):
        super(AddApparelView, self).__init__(**kwargs)
        self.screen_manager = screen_manager

        # Static Variables
        button_height = 44
        
        #======= PUBLIC VARIABLES =====================================
        chosen_category = None
        
        #======= CAMERA ===============================================
        # Create a camera object
        self.camera = Camera(play=True, resolution=(640, 480))
        
        #====== METHODS ===============================================
        def remove_background():
            input_path = 'images/selfie.png'
            output_path = 'selfie.png'
            with open(input_path, 'rb') as i:
                with open(output_path, 'wb') as o:
                    input = i.read()
                    output = remove(input)
                    o.write(output)
                

       
        
        #========== DROPDOWN MENU ==============================

        # Create a list of options
        options = ["Top", "Pants", "Shoes"]

        # Create a dropdown with buttons for each option
        dropdown = DropDown(auto_width=False, width=150)
        for option in options:
            btn = Button(text=option, size_hint_y=None, height=40, text_size=(None, None))
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        # Create a main button
        mainbutton = Button(text='Select Category', size_hint=(None, None), pos_hint={'x': .1, 'y': .2}, text_size=(None, None), width=150, height=button_height)

        # Show the dropdown menu when the main button is released
        mainbutton.bind(on_release=dropdown.open)

        # Modify the on_select callback to print a message based on the selected option
        def on_select_callback(instance, value):
            mainbutton.text=value
            chosen_category = value

            # You can perform additional actions based on the selected value here

        dropdown.bind(on_select=on_select_callback)

        #======= IMPORT BUTTON ========================================

        btn_upload = Button(text="Upload Photo", size_hint_y=None, height=button_height, text_size=(None, None), size_hint_x=0.2, pos_hint={'x': .7, 'y': .2}) 

        #======= CONFIRM BUTTON =======================================
        btn_confirm = Button(text="Add to Closet", size_hint_y=None, height=button_height, text_size=(None, None), size_hint_x=0.2, pos_hint={'x': .4, 'y': 0.05})
        def PlaceInfolder(self):
            incrament = rand.randint(0,10000)
            if mainbutton.text == "Top":
                os.rename('images/selfie.png', 'images/'+ mainbutton.text + f'/Top{incrament}.png')
            elif mainbutton.text == "Pants":
                os.rename('images/selfie.png','images/'+ mainbutton.text + f'/Pants{incrament}.png')
            else:
                os.rename('images/selfie.png','images/'+ mainbutton.text + f'/Shoes{incrament}.png')
            
        btn_confirm.bind(on_press=PlaceInfolder)
        
       #======= TAKE PHOTO BUTTON ====================================
        btn_take_photo = Button(text="Take Photo", size_hint_y=None, height=button_height, text_size=(None, None), size_hint_x=0.2, pos_hint={'x': .5, 'y': .5})
        btn_take_photo.bind(on_press=self.onCameraClick)

        #====== ADD WIDGETS ===========================================
        self.add_widget(mainbutton)
        self.add_widget(btn_upload)
        self.add_widget(btn_confirm)
        self.add_widget(self.camera)
        self.add_widget(btn_take_photo)
    def onCameraClick(self, instance):
        self.camera.export_to_png('images/selfie.png')

