# GAN_Clothing_mnist

This repository contains an implementation of a Generative Adversarial Network (GAN) trained on the Clothing MNIST dataset. The GAN is designed to generate new images of clothing items such as t-shirts.

## Repository Files

- `.gitattributes`: Specifies Git attributes for the repository.
- `.gitignore`: Lists files and directories to be ignored by Git version control.
- `README.md`: This file, providing an overview of the repository.
- `cgan_generator.h5`: Pre-trained generator model for the GAN in HDF5 format.
- `create_generator_model.py`: Python script to create and train the generator model.
- `generated_images.png`: Sample of generated images from the GAN.
- `generated_tshirts.png`: Sample of generated t-shirt images.
- `img_generator_ui.py`: Python script for a user interface to generate images using the trained model.
- `install_requirements.py`: Python script to install the required dependencies.
- `requirements.txt`: Text file listing the required Python libraries and their versions.

## Downloading the Repository

To download this repository, you have a few options:

### Option 1: Clone the Repository

You can clone this repository using the following command:

```shell
git clone https://github.com/masanbasa3k/GAN_Clothing_mnist.git
```

### Option 2: Download as ZIP

You can download the repository as a ZIP file by clicking on the green "Code" button at the top of the repository page and selecting "Download ZIP". After downloading, extract the ZIP file to your desired location.

## Usage

To use this repository, follow these steps:

1. Install the required dependencies by running `python install_requirements.py`.
2. Execute the `create_generator_model.py` script to train the GAN model or use the pre-trained `cgan_generator.h5` model.
3. Use the `img_generator_ui.py` script to interact with the trained model and generate new clothing images.
4. View the generated images in the `generated_images.png` and `generated_tshirts.png` files.

## Contributing

Contributions to this repository are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

<img width="227" alt="Screenshot 2023-07-14 at 3 00 22 PM" src="https://github.com/masanbasa3k/CGAN_Clothing_mnist/assets/66223190/eceba429-39b2-4ad0-b9eb-e004e3830df6">
<img width="225" alt="Screenshot 2023-07-14 at 3 01 13 PM" src="https://github.com/masanbasa3k/CGAN_Clothing_mnist/assets/66223190/65906846-1d97-414e-bd87-c28683511921">

