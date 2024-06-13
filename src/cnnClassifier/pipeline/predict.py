import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import json
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)



class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        imagename = self.filename
        train_generator = train_datagen.flow_from_directory(
            os.path.join("artifacts", "data_ingestion", "asl_dataset"),
            target_size=(224, 224),
            batch_size=32,
            class_mode='categorical'
        )
        # Assuming 'train_generator' is the generator you used during model.fit()
        class_labels = list(train_generator.class_indices.keys())
        test_image = image.load_img(imagename, target_size = (224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis = 1)
        print('result: ' + str(class_labels[result[0]]))

        return [{"image" : str(class_labels[result[0]])}]