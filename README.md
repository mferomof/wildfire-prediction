# Wildfire Prediction

### Overview
This project is about implementing a deep learning model, **VGG19**, to process satellite images and predict the occurrence of wildfires.

### Features
* **Data Preprocessing:** Defines the transformations applied to satellite images, including resizing, normalization, and converting to a tensor, to prepare them as input for the VGG19 model defined in PyTorch.
* **Model Implementation:** The model is a **VGG19** architecture that will be trained from scratch for this specific classification task. The implementation is based on the seminal paper by K. Simonyan and A. Zisserman, "Very deep convolutional networks for large-scale image recognition" (2015), 1409.1556.
* **Image Classification:** Utilizes the VGG19 model to classify satellite images as either **wildfire** or **no wildfire**.

### Data
The dataset used in this project can be found here: A. Aaba, “Wildfire Prediction Dataset (Satellite Images),” 2022. [Online]. Available: `https://www.kaggle.com/datasets/abdelghaniaaba/wildfire-prediction-dataset?select=valid`.

To set up the data:
1.  Download the **training**, **validation**, and **test** sets as a single `.zip` file from the provided link.
2.  Unzip the downloaded file and place the `train`, `valid`, and `test` folders directly into the project's root directory, maintaining the `nowildfire` and `wildfire` subfolder structure within each.

**Important:** The dataset is large. It's recommended to use a **GPU** for training to avoid memory overload and reduce processing time.

### How to Run
1.  **Clone the repository:** `git clone https://github.com/mferomof/wildfire-prediction.git`
2.  **Navigate to the project folder:** ex. `cd wildfire-prediction`
3.  **Install the dependencies:** `pip install -r requirements.txt`
4.  **Run the main script:** `Wildfire_Prediction.ipynb`
    * The `load_dataset.py` file is a utility module used by the main notebook. Please keep it in the same directory.

### Contact
https://github.com/mferomof
