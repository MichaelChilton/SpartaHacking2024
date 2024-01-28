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
from PIL import Image
class AddApparelView(Screen):
    #===========INITIALIZATION======================================
    
    def __init__(self, screen_manager, **kwargs):
        super(AddApparelView, self).__init__(**kwargs)
        self.screen_manager = screen_manager

        # Static Variables
        button_height = 60
        size_standard = .5
       
        
        #======= CAMERA ===============================================
        # Create a camera object
        self.camera = Camera(play=True, index=2,resolution=(640, 480))


        #====== LOOKNICE ===============================================
        
        horizontal_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        
       
        
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

        btn_upload = Button(text="Upload Photo", size_hint_y=None, height=button_height, text_size=(None, None), size_hint_x=size_standard)

        #======= CONFIRM BUTTON =======================================
        btn_confirm = Button(text="Add to Closet", size_hint_y=None, height=button_height, text_size=(None, None), size_hint_x=size_standard)
        
        def remove_background():
            input_path = 'images/selfie.png'
            output_path = 'images/selfie.png'
            input_image = cv2.imread(input_path)
            output_image = remove(input_image, alpha=0)
            cv2.imwrite(output_path, output_image)
        def crop():
            # Open the captured image
            im = Image.open('images/selfie.png')
            # Define the region to crop based on the camera resolution
            camera_resolution = (640, 480)  # Resolution used for the camera
            crop_left = (im.width - camera_resolution[0]) // 2
            crop_top = (im.height - camera_resolution[1]) // 2
            crop_right = crop_left + camera_resolution[0]
            crop_bottom = crop_top + camera_resolution[1]
            # Crop the image
            im_cropped = im.crop((crop_left, crop_top, crop_right, crop_bottom))
            # Save the cropped image
            im_cropped.save('images/selfie.png')
        def PlaceInfolder(self):
            crop()
            remove_background()
            incrament = rand.randint(0,10000)
            if mainbutton.text == "Top":
                os.rename('images/selfie.png', 'images/'+ mainbutton.text + f'/Top{incrament}.png')
            elif mainbutton.text == "Pants":
                os.rename('images/selfie.png','images/'+ mainbutton.text + f'/Pants{incrament}.png')
            else:
                os.rename('images/selfie.png','images/'+ mainbutton.text + f'/Shoes{incrament}.png')
            
        btn_confirm.bind(on_press=PlaceInfolder)
        
       #======= TAKE PHOTO BUTTON ====================================
        btn_take_photo = Button(text="Take Photo", size_hint_y=None, height=button_height, text_size=(None, None), size_hint_x=0.2)
        btn_take_photo.bind(on_press=self.onCameraClick)

        #====== ADD WIDGETS ===========================================
   
        horizontal_layout.add_widget(btn_upload)
        horizontal_layout.add_widget(btn_take_photo)
        horizontal_layout.add_widget(btn_confirm)
        
        
        
        horizontal_layout.pos_hint = {'bottom': 4}
        self.add_widget(horizontal_layout)
        self.add_widget(mainbutton)
        self.add_widget(self.camera)
    def onCameraClick(self, instance):
        self.camera.export_to_png('images/selfie.png')

