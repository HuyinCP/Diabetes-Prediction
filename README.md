# Diabetes Prediction using Support Vector Machine (SVM)

This project uses a Support Vector Machine (SVM) classification model to predict whether an individual has diabetes based on biological features.

## 📊 Dataset

The dataset used is the [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database), which includes medical diagnostic measurements such as:

- Number of pregnancies
- Glucose level
- Blood pressure
- Skin thickness
- Insulin level
- BMI (Body Mass Index)
- Diabetes pedigree function
- Age

## ⚙️ Technologies and Libraries

- Python
- Pandas
- ydata-profiling
- scikit-learn (SVM, preprocessing, evaluation)

## 🚀 How It Works

1. **Data Loading**  
   Load the dataset from a CSV file.

2. **(Optional) Data Profiling**  
   Use `ydata-profiling` to generate a report for exploring data statistics and distributions.

3. **Data Splitting**  
   Split the dataset into training and testing sets (80%/20%).

4. **Feature Scaling**  
   Normalize the input features using `StandardScaler` to improve SVM performance.

5. **Model Training**  
   Train a Support Vector Machine (SVC) classifier on the training data.

6. **Evaluation**  
   Evaluate the model using classification metrics: precision, recall, f1-score, and accuracy.

## 🧪 Sample Output

```

```
          precision    recall  f1-score   support

       0       0.79      0.90      0.84       XXX
       1       0.71      0.52      0.60       XXX

accuracy                           0.77       XXX
```

macro avg       0.75      0.71      0.72       XXX
weighted avg       0.76      0.77      0.76       XXX

```

(*Numbers vary depending on the dataset split*)

## 📁 Project Structure

```

.
├── Datasets/
│   └── diabetes.csv
├── main.py
├── Diabetes.html       
└── README.md

````

## ✅ How to Run

1. Clone this repo
2. Install the required libraries:
   ```bash
   pip install pandas ydata-profiling scikit-learn
````

3. Run the script:

   ```bash
   python main.py
   ```

## ✍️ Author

Nghiêm Quang Huy
AI/Machine Learning Project – 2025
