import os
import json
import numpy as np
import pandas as pd
import cv2
import flask
from flask import Flask, request,render_template,redirect,url_for,jsonify,json
import requests
import os
import glob
import pprint

main_dir = r'''C:\Users\aritra_chatterjee\richie's_kitchen'''
os.chdir(main_dir)
images_folder = os.path.join(main_dir,'images')
images_labels = os.listdir(images_folder)
with open('images_map.json','r') as readfile:
    image_map = json.load(readfile)

IMAGE_FOLDER = os.path.join('static', 'images')

text_folder = os.path.join(main_dir,'recipe_text')
text_files = os.listdir(text_folder)

with open(os.path.join(text_folder,text_files[0]),'r') as readfile:
    text = readfile.read()

# make the dataframe

image_ids = list(image_map.keys())
recipe = [image_map[key]['recipe_name'].lower() for key in
               list(image_map.keys())]

food_items = [image_map[key]['food_item'] for key in
               list(image_map.keys())]

columns = ['image_ids','recipe_name','food_items']
df = pd.DataFrame(columns = columns)
df['image_ids'] = image_ids
df['recipe_name'] = recipe
df['food_items'] = food_items

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER


@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        data = request.form
        print(data)
        recipe_name = data['hidden_recipe']
        image = df['image_ids'][df['recipe_name'] == recipe_name].values.tolist()[0]
        full_filename = os.path.join(app.config['IMAGE_FOLDER'], image)
        print(full_filename)
        recipe_list= [i.lower() for i in recipe]
        selected_value = data['hidden_recipe']
    else:
        recipe_list= [i.lower() for i in recipe]
        recipe_list.sort()
        image_list = list(image_map.keys())
        image_list.sort()
        img = image_list[0]
        full_filename = os.path.join(app.config['IMAGE_FOLDER'], img)
        print(full_filename)
        selected_value = 'coconut_chutney'
        
    return render_template('interface.html',recipe_list = recipe_list,
                           recipe_image = full_filename,
                           selected_value = selected_value)

@app.route('/update', methods = ['POST'])
def update():
    data = request.form
    print(data)
    return data


if __name__ == '__main__':
    app.run(debug=True)














