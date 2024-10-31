# app.py
import streamlit as st
import pandas as pd
import joblib
st.set_page_config(
    page_title="Home",
    page_icon="🎗️",
)
# تحميل النموذج والبيانات
model = joblib.load('model.pkl')
df = pd.read_csv('breast-cancer.csv')

# إعداد اللغة
language = st.sidebar.selectbox("اختر اللغة | Choose Language", ("العربية", "English"))

# تعريف النصوص بناءً على اللغة
if language == "العربية":
    title = " تشخيص سرطان الثدي باستخدام التعلم الآلي"
    model_title = "تنبؤ النموذج"
    predict_button = "تشخيص"
    benign_text = "حميد"
    malignant_text = "خبيث"
    direction_css = "direction: rtl;"  # إضافة CSS لجهة النص
else:
    title = "Breast Cancer Diagnosis using Machine Learning"
    model_title = "Model Prediction"
    predict_button = "Diagnose"
    benign_text = "Benign"
    malignant_text = "Malignant"
    direction_css = "direction: ltr;"  # إضافة CSS لجهة النص

# كود CSS لتعيين اللون الخلفي
background_css = f"""
<style>
    .stApp {{
        background-color: #D5006D; /* لون خلفية وردي غامق */
        {direction_css}  /* تحديد اتجاه النص */
    }}
    
</style>
"""

# تطبيق CSS كخلفية
st.markdown(background_css, unsafe_allow_html=True)

# عرض العنوان
st.title(title)

# تنبؤ النموذج
st.subheader(model_title)

# إدخال بيانات جديدة للنموذج
input_data = {}
with st.expander("", expanded=True):
    for feature in df.columns[2:]:
        input_data[feature] = st.number_input(feature, value=float(df[feature].mean()))  # إزالة "ادخل قيمة"

# توقع النتيجة
if st.button(predict_button):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]
    diagnosis = malignant_text if prediction == 1 else benign_text
    st.write(diagnosis)

# تحسين ترتيب العناصر وإضافة تباعد
st.markdown("<br>", unsafe_allow_html=True)  # إضافة مسافة فارغة
