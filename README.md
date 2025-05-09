# Crop Recommendation System using AI/ML 🌾🤖

This project is designed to provide **smart agricultural solutions** using machine learning techniques. By analyzing soil properties, weather conditions, and crop requirements, the system recommends the most suitable crops and fertilizers for optimal yield. It leverages data-driven insights to help farmers make informed decisions, aiming to improve productivity while promoting **sustainable farming practices**. 🌱🌍

### Key Features
- **Data Preprocessing**: The system starts by loading the crop and fertilizer datasets and checking for missing values and inconsistencies. The data is cleaned and preprocessed, with key features like **N, P, K**, **temperature**, **humidity**, **pH**, and **rainfall** being identified as critical factors for crop growth.
- **Data Visualization** 📊: Various visualizations like **histograms**, **scatter plots**, and **box plots** are used to understand the relationships between different features such as soil nutrient levels, temperature, humidity, and crop yield. Correlation **heatmaps** highlight which variables have strong dependencies, helping to identify the most influential factors for crop selection.
- **Feature Engineering**: Categorical variables are encoded, and numerical features are scaled to ensure the model can process the data effectively. 🧑‍💻

### Model Training & Evaluation
Once the data is processed, it is split into **training** and **testing** sets. The model is then trained on the training dataset, and its performance is evaluated using the test data. The accuracy of different models is compared to find the one that best predicts the optimal crops and fertilizers based on the input features. The system’s accuracy is evaluated to ensure reliable predictions. ✅

### Deployment 🚀
The trained model is integrated into a **Flask web application**, allowing users to input their soil and weather data through a simple interface. The **Flask backend** processes these inputs and provides real-time recommendations for crop and fertilizer choices. The frontend is designed using an **HTML page**, making it easy for farmers to interact with the system and access the recommendations. 🌾💻

### Technologies Used
- **Python**: For data analysis, machine learning, and backend development.
- **Flask**: For creating a web application to serve the model.
- **Seaborn/Matplotlib**: For data visualization (graphs, plots, and charts).
- **Scikit-Learn**: For machine learning model training, testing, and evaluation.

### How It Works
1. **User Input**: The user inputs data regarding soil nutrients, temperature, humidity, pH, and rainfall into the app.
2. **Model Prediction**: The backend Flask app processes the input and uses the trained model to predict the most suitable crop and fertilizer.
3. **Recommendations**: The user receives suggestions on the best crop to grow and the optimal fertilizer to use based on the analyzed data.

### Goal 🎯
The ultimate goal of this system is to help farmers improve their **crop yields**, **optimize fertilizer use**, and **boost productivity** while maintaining the health of their soil and ensuring sustainable farming practices. By utilizing AI/ML, the system provides **data-driven insights** to guide decisions in real-time, making agriculture more efficient and environmentally friendly. 🌍🚜

This project combines the power of machine learning with the real-world needs of agriculture, creating a tool that not only enhances crop selection but also contributes to a more sustainable future for farming. 🌱✨

## Screenshot
![Screenshot (3)]
