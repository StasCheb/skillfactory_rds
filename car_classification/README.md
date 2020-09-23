# Task
You need to classify the car by photo.
Build your own image classifier. The data has already been collected and contains 10 types of car models.
This project was completed as part of the training competition Data Science Specialization Skillfactory https://www.kaggle.com/c/sf-dl-car-classification
### Have been tested:
- different State of the Art (SOTA)-models. 
- TTA (Test Time Augmentation).
- different Learning Rate techniques. 
- advanced image augmentation libraries.

### Description of the project files

- *car_class_EfficientNetB7* - 
Experimental notebook for the selection of LR, Batch size, epochs and the size of images with limited RAM. Training to use TTA and advanced augmentation.
using Albumentations for augmentation, the base model EfficientNetB7, ReduceLROnPlateau, and TTA.

- *car_class_Xception* - 
using ImageDataGenerator for augmentation and base model Xception
__________________________________________________________
Due to time constraints on kaggle and colab, GeForce GTX 2060 6Gb computer was mostly used.
__________________________________________________________
Kaggle: Stas(https://www.kaggle.com/stanislav8) 0.97213

 

