# Disease Prediction System using Machine Learning

This project implements a disease prediction system using various machine learning algorithms. Users can input a set of symptoms, and the system will predict potential diseases based on trained models. The application also includes a user registration and login system.

## Features

* **Symptom-based Disease Prediction:** Predicts diseases based on 5 user-selected symptoms.
* **Multiple Machine Learning Models:** Utilizes Decision Tree, Random Forest, and Naive Bayes algorithms for prediction.
* **User Authentication:** Includes a registration and login system for users.
* **Graphical User Interface (GUI):** Built with `tkinter` for an interactive user experience.

## Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository (or download the files):**
    ```bash
    git clone <your-repository-url>
    cd disease-prediction-system
    ```

2.  **Create the required CSV files:**
    You need two CSV files: `Prototype.csv` (for training data) and `Prototype1.csv` (for testing data). These files should contain symptoms as columns and diseases as the target variable. The symptom names in the CSV files must exactly match the symptom list `l1` in the `Disease_prediction.ipynb` file. The disease names must match the `disease` list.

    **Example `Prototype.csv` structure:**

    ```csv
    Symptom1,Symptom2,Symptom3,Symptom4,Symptom5,prognosis
    itching,skin_rash,nodal_skin_eruptions,dischromic _patches,,Fungal infection
    skin_rash,patches_in_throat,high_fever,,Gastroenteritis
    # ... more data
    ```

    **Example `Prototype1.csv` structure (similar to Prototype.csv):**

    ```csv
    Symptom1,Symptom2,Symptom3,Symptom4,Symptom5,prognosis
    chills,vomiting,diarrhoea,,Typhoid
    muscle_pain,joint_pain,fever,weakness_in_limbs,,Malaria
    # ... more data
    ```
    * **Note:** The provided Jupyter notebook expects specific symptom and disease names. Ensure your CSV files align with these lists for the models to train correctly.

3.  **Install the necessary Python libraries:**
    ```bash
    pip install pandas numpy scikit-learn tkinter
    ```
    *(Note: `tkinter` is usually included with Python installations, but it's listed here for completeness.)*

## Usage

1.  **Run the application:**
    ```bash
    python Disease_prediction.ipynb
    ```
    *(Alternatively, you can run the code directly from a Jupyter environment.)*

2.  **Main Screen:**
    Upon running, a "Medical Diagnosis System" window will appear with options to "Login" or "Register".

3.  **Register:**
    * Click "Register".
    * Fill in the registration details (Username, Password, Name, Contact No, Email Id, Age, Gender).
    * Click "Register" to create an account. A confirmation message "Registration Success" will appear.

4.  **Login:**
    * Return to the main screen and click "Login".
    * Enter your registered username and password.
    * Click "Login". If successful, a "Login Success" pop-up will appear. Click "OK".

5.  **Disease Prediction Interface:**
    After successful login, the main disease prediction GUI will open.
    * Enter the "Name of the Patient".
    * Select 5 symptoms from the dropdown menus.
    * Click on "Prediction 1" (Decision Tree), "Prediction 2" (Random Forest), or "Prediction 3" (Naive Bayes) to see the predicted disease by each model. The predicted disease will appear in the respective text boxes.

## Code Structure

* **Symptom and Disease Lists:** `l1` contains a comprehensive list of symptoms, and `disease` contains the list of possible diseases.
* **Data Loading and Preprocessing:**
    * `pandas` is used to read `Prototype.csv` (training data) and `Prototype1.csv` (testing data).
    * Disease names in the datasets are replaced with numerical labels for model training.
    * `X` and `y` represent the features (symptoms) and target (prognosis) for training.
    * `X_test` and `y_test` are used for evaluating the models.
* **Machine Learning Models:**
    * `DecisionTree()`: Implements a Decision Tree Classifier using `sklearn.tree.DecisionTreeClassifier`.
    * `randomforest()`: Implements a Random Forest Classifier using `sklearn.ensemble.RandomForestClassifier`.
    * `NaiveBayes()`: Implements a Gaussian Naive Bayes Classifier using `sklearn.naive_bayes.GaussianNB`.
    * Each prediction function calculates and prints the accuracy of the model on the test data.
    * For user input, symptoms are converted into a numerical input vector (`l2`) before prediction.
* **GUI Implementation (`tkinter`):**
    * `main_account_screen()`: Creates the initial login/register screen.
    * `register()`: Handles user registration, saving credentials to a file.
    * `login()`: Handles user login, verifying credentials against saved files.
    * `login_verify()`, `register_user()`, `login_sucess()`, `password_not_recognised()`, `user_not_found()`: Functions for handling login/registration logic and pop-up messages.
    * The main `tkinter` root window sets up the symptom selection dropdowns, input fields, and prediction buttons.

## Dependencies

* `tkinter`
* `numpy`
* `pandas`
* `scikit-learn`


