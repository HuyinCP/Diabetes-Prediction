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

| Class        | Precision | Recall | F1-Score | Support |
|--------------|-----------|--------|----------|---------|
| **0**        | 0.77      | 0.83   | 0.80     | 99      |
| **1**        | 0.65      | 0.56   | 0.60     | 55      |
| **Accuracy** |           |        | 0.73     | 154     |
| **Macro avg**| 0.71      | 0.70   | 0.70     | 154     |
| **Weighted avg** | 0.73  | 0.73   | 0.73     | 154     |

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
