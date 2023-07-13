import numpy as np
from numpy.random import randn
from keras.models import load_model
from PIL import Image, ImageTk
import tkinter as tk

# generate points in latent space as input for the generator
def generate_latent_points(latent_dim, n_samples, label):
    # generate points in the latent space
    z_input = randn(n_samples, latent_dim)
    # generate labels
    labels = np.full((n_samples,), label)
    return [z_input, labels]

# Load the generator model
model = load_model('cgan_generator.h5')

# List of available items
items = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Generate images of the chosen item
def generate_image():
    choice = item_listbox.curselection()[0]
    latent_points, labels = generate_latent_points(100, 1, choice)
    generated_image = model.predict([latent_points, labels])[0]
    generated_image = (generated_image + 1) * 127.5
    generated_image = generated_image.astype(np.uint8)
    generated_image = Image.fromarray(generated_image.reshape(28, 28))
    generated_image = generated_image.resize((112*2, 112*2))
    generated_image = ImageTk.PhotoImage(generated_image)
    image_label.config(image=generated_image)
    image_label.image = generated_image

# Create the UI
window = tk.Tk()
window.title("Fashion Item Generator")

# Item listbox
item_listbox = tk.Listbox(window, selectmode=tk.SINGLE)
for i, item in enumerate(items):
    item_listbox.insert(tk.END, item)
item_listbox.pack(pady=10)

# Generate button
generate_button = tk.Button(window, text="Generate", command=generate_image)
generate_button.pack(pady=10)

# Image label
image_label = tk.Label(window)
image_label.pack()

window.mainloop()
