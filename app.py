import streamlit as st
import openai
from PIL import Image
from ultralytics import YOLO

# إعداد مفتاح OpenAI API
openai.api_key = "Add your API"

# وظيفة لتحليل الصورة واستخراج المكونات باستخدام YOLOv8
def extract_ingredients_from_image(image_path):
    yolo_model = YOLO("best_ver2.pt")  # استبدل بمسار نموذج YOLO الخاص بك
    results = yolo_model.predict(source=image_path, conf=0.5)  # الكشف عن المكونات
    detections = results[0].boxes.data.cpu().numpy()  # استخراج البيانات
    ingredients = []

    for detection in detections:
        class_id = int(detection[5])  # class_id هو رقم الصنف
        confidence = detection[4]    # الثقة بالتنبؤ
        if confidence > 0.5:         # تصفية النتائج بناءً على الثقة
            ingredients.append(yolo_model.names[class_id])  # الحصول على اسم الصنف

    return list(set(ingredients))  # إزالة التكرارات وإرجاع القائمة

# وظيفة لجلب الوصفة والسعرات الحرارية باستخدام ChatGPT
def get_recipe_and_calories(ingredients, cuisine, meal_type):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful recipe generator and calorie calculator."},
                {"role": "user", "content": f"Create a {meal_type} recipe for {cuisine} cuisine using the following ingredients: {', '.join(ingredients)}. Also, provide the estimated calories per 100 grams for each ingredient in a clear format."}
            ],
            max_tokens=500
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"An error occurred while generating the recipe and calories: {str(e)}"

# إضافة خلفية مخصصة
def add_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# إعداد الصفحة
st.set_page_config(
    page_title="🍴 AI’m Hungry",
    page_icon="🍲",
    layout="centered"
)

# التنقل بين الصفحات
st.sidebar.title("🍽️ Navigation")
page = st.sidebar.radio("Go to", ["🏠 Introduction", "🍳 Generate Recipe", "👩‍🍳 Acknowledgements"])

# صفحة المقدمة
if page == "🏠 Introduction":
    add_background("https://source.unsplash.com/1600x900/?cooking,ingredients")
    st.title("🍴 Welcome to the AI’m Hungry App!")
    st.write("""
    Welcome to the **Recipe Generator App**! 🍲
    
    This app allows you to:
    - Upload an image of food ingredients 🍅🧀.
    - Detect ingredients using AI 🧠.
    - Choose your favorite cuisine (Saudi, Italian, Indian, French) 🌎.
    - Select a meal type (Breakfast, Lunch, Dinner) to tailor the recipe! 🕒

    **Bon Appétit! 🍽️**
    """)

# صفحة توليد الوصفات
elif page == "🍳 Generate Recipe":
    add_background("https://source.unsplash.com/1600x900/?recipes,food")
    st.title("🍳 Recipe Generator")
    st.write("### Upload your food ingredients and select a cuisine and meal type to get started! 🥗")

    # رفع الصورة
    uploaded_image = st.file_uploader(
        "Upload an image of your food ingredients (e.g., tomato, cheese, basil):",
        type=["png", "jpg", "jpeg"]
    )

    # اختيار المطبخ
    cuisine = st.selectbox(
        "🌎 Choose your cuisine",
        ["Saudi", "Italian", "Indian", "French"]
    )

    # اختيار نوع الوجبة
    meal_type = st.selectbox(
        "🍽️ Choose your meal type",
        ["Breakfast", "Lunch", "Dinner"]
    )

    # توليد الوصفة
    if uploaded_image:
        # عرض الصورة
        image = Image.open(uploaded_image)
        st.image(image, caption="Your Uploaded Image", use_column_width=True)
        st.write("🔍 Analyzing your image...")

        # حفظ الصورة مؤقتًا
        image_path = "temp_image.jpg"
        with open(image_path, "wb") as f:
            f.write(uploaded_image.getbuffer())

        # استخراج المكونات باستخدام YOLOv8
        detected_ingredients = extract_ingredients_from_image(image_path)
        st.write(f"✅ **Detected Ingredients:** {', '.join(detected_ingredients)}")

        # السماح بحذف المكونات غير المرغوب فيها
        final_ingredients = st.multiselect(
            "Select ingredients to keep:",
            options=detected_ingredients,
            default=detected_ingredients
        )

        # إضافة مكونات إضافية
        additional_ingredients = st.text_input(
            "Add additional ingredients (separated by commas):",
            placeholder="e.g., garlic, pepper, olive oil"
        )

        # دمج المكونات النهائية
        if st.button("Generate Recipe"):
            if additional_ingredients:
                additional_list = [item.strip() for item in additional_ingredients.split(",")]
                final_ingredients.extend(additional_list)
                final_ingredients = list(set(final_ingredients))  # إزالة التكرارات

            st.write(f"✅ **Final Ingredients List:** {', '.join(final_ingredients)}")

            # طلب الوصفة والسعرات الحرارية
            st.write(f"🍽️ Generating a **{meal_type}** recipe for **{cuisine}** cuisine...")
            recipe_and_calories = get_recipe_and_calories(final_ingredients, cuisine, meal_type)
            
            # فصل البيانات للعرض
            if "\n\n" in recipe_and_calories:
                recipe, calories_info = recipe_and_calories.split("\n\n", 1)
                st.write("### 🍲 Suggested Recipe:")
                st.write(recipe)
                st.write("### 🔢 Calorie Estimation (per 100g):")
                st.write(calories_info)
            else:
                st.write("### 🔍 Full Response:")
                st.write(recipe_and_calories)

# صفحة الشكر
elif page == "👩‍🍳 Acknowledgements":
    add_background("https://source.unsplash.com/1600x900/?team,thankyou")
    st.title("👩‍🍳 Acknowledgements")
    st.write("""
    ### Special Thanks to Our Team:
    - **Sama**
    - **Shaden**
    - **Basel**
    - **Nawaf**

    ### Thank You!
    Thank you for using our Recipe Generator App. We hope it helps inspire your culinary creativity!  
    **Bon Appétit! 🍽️**
    """)
