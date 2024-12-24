[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Y0oZyzHx)
# CV-Project
### README: AI’m Hungry App 🍴

---

## **Overview**
The Recipe Generator App is an innovative tool that combines cutting-edge computer vision and natural language processing technologies to provide personalized recipe recommendations. Using **YOLOv11**, the app detects food ingredients from uploaded images, and with the power of **GPT-4o Mini**, it generates delicious recipes tailored to the detected ingredients and the user's selected cuisine.

This project is perfect for food enthusiasts looking to explore creative culinary ideas with the help of AI!

---

## **Features**
- **Object Detection**: Identifies food ingredients in images using a trained YOLOv11 model.
- **Recipe Recommendation**: Generates personalized recipes based on detected ingredients using GPT-4 Mini.
- **Custom Dataset**: Built a unique dataset of food ingredients, annotated using Roboflow, and used it to train YOLOv8.
- **User-Friendly Interface**: Developed with Streamlit, providing an intuitive interface for uploading images, selecting cuisines, and viewing recipes.

---

## **Project Workflow**
1. **Dataset Collection**:
   - Gathered a dataset of 100+ images of food ingredients.
   - Annotated and preprocessed the dataset using **Roboflow**.

2. **Model Training**:
   - Trained a **YOLOv11** object detection model with the annotated dataset.
   - Fine-tuned the model for accurate ingredient detection.

3. **Recipe Recommendation**:
   - Integrated **GPT-4o Mini** to generate recipes dynamically.
   - Recipes are tailored to detected ingredients and user-selected cuisines.

4. **Deployment**:
   - Deployed a seamless **Streamlit** application for easy user interaction.
   - Users can upload images, detect ingredients, and receive recipes instantly.

---

## **How It Works**
1. Navigate to the **Generate Recipe** page from the app sidebar.
2. Upload an image of your food ingredients (e.g., tomato, cheese, basil).
3. Select a cuisine type (Saudi, Italian, Indian, or French).
4. The app will:
   - Detect the ingredients in your image.
   - Generate a recipe based on the detected ingredients and your selected cuisine.
5. View and enjoy your personalized recipe!

---

## **Requirements**
To run the app locally, ensure you have the following dependencies installed:

- **Python 3.8+**
- **Streamlit**
- **OpenAI Python API**
- **Pillow**
- **Ultralytics** (for YOLOv11)

Install the required dependencies using:
```bash
pip install streamlit openai pillow ultralytics
```

---

## **Usage**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/recipe-generator.git
   cd recipe-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Replace `your_openai_api_key_here` in the code with your OpenAI API key.

4. Download the trained YOLOv11 model (`best.pt`) and place it in the project directory.

5. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

6. Open the app in your browser and start exploring recipes!

---

## **Screenshots**
### **Introduction Page**
![streamlit1](https://github.com/user-attachments/assets/fb9c82a9-9dc9-410d-83e1-4570701847ba)


### **Generate Recipe Page**
![streamlit2](https://github.com/user-attachments/assets/6edeb45b-5720-4261-8ba7-57a8d8f90288)


---

## **Acknowledgements**
### **Special Thanks to Our Team**:
- **Sama**
- **Shaden**
- **Basel**
- **Nawaf**

### **Tools and Technologies**:
- [Streamlit](https://streamlit.io/)
- [OpenAI GPT](https://openai.com/)
- [YOLOv8 by Ultralytics](https://github.com/ultralytics/ultralytics)
- [Roboflow](https://roboflow.com/)

---

## **Future Enhancements**
- Add multi-language support for a global audience.
- Include additional cuisines and recipe categories.
- Enhance object detection capabilities with a larger dataset.



---

**Bon Appétit! 🍽️**



