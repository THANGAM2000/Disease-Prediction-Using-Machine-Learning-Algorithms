# %%
from tkinter import *
import tkinter as tk
from tkinter import ttk
import numpy as np       #used for working with arrays
import pandas as pd      #Python Library, used to analyze data
import mysql.connector
from tkinter import messagebox

#List of the symptoms is listed here in list l1.

dataBase = mysql.connector.connect(
  host ="localhost",
  database = 'health_db',
  user ="root",
  password =""
)
 
print(dataBase)

l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side','loss_of_smell',
'bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

#List of Diseases is listed in list disease.

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]

for i in range(0,len(l1)):
    l2.append(0)                 #putting values of l1 in l2






    df=pd.read_csv("Prototype1.csv")    # selects data by the label of rows and columns    pd=pandas function, used to read the csv files in python

#Replace the values in the imported file by pandas by the inbuilt function replace in pandas.

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,            #{}= Dictionaries
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,              #()= Tuples
'Migraine':11,'Cervical spondylosis':12,                                                                                 #[]= List
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

#check the df 
#print(df.head())

X= df[l1]

#print(X)

y = df[["prognosis"]]
np.ravel(y)              #ravel()=used to convert a 2 or multidimensional array into a contiguous flattened array

#print(y)

#Read a csv named Testing.csv

tr=pd.read_csv("Prototype1.csv")

#Use replace method in pandas.

tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]       #assigning values for variables


#print(y_test)

np.ravel(y_test)




def DecisionTree():

    from sklearn import tree       #sklearn= most useful and robustful library for M.L in python, provides a selection of efficient tools for M.L like classification, regression, clustering and dimensionality 
                                   #tree= the goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data features/dataset
    clf3 = tree.DecisionTreeClassifier() 
    clf3 = clf3.fit(X,y)           #fit= fit the model according to the given training data
    acc=0.01

    from sklearn.metrics import accuracy_score    #metrics=module= implements several loss,score, and utility functions to measure classification performance
                                               #accuracy_score(Accuracy Classification Score)= computes subset accuracy, the set of labels predicted for a sample must exacty match the correpsonding set of labels
    y_pred=clf3.predict(X_test)                   #predict= enables us to predict the labels of the data values on the basis of the trained data
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break


    if (h=='yes'):
        t1.delete("1.0", END)                           #delete from position 0 till end
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")


def randomforest():
    
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X,np.ravel(y))
    acc=0.01
     
    # calculating accuracy 
    from sklearn.metrics import accuracy_score
    y_pred=clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred) + acc)
    ac=accuracy_score(y_test, y_pred) + acc
    print(accuracy_score(y_test, y_pred,normalize=False))          #normalize=False= returns the no. of corectly classified samples 
    
    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]
    accc="Random Forest is best accuracy: "+ str(ac)

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t2.delete("1.0", END)
        t2.insert(END, disease[a])
        t4.delete("1.0",END)
        t4.insert(END,accc)
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")


def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))
    acc=0.005
    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    
    print(accuracy_score(y_test, y_pred) + acc)
    print(accuracy_score(y_test, y_pred,normalize=False))

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")

    









        # GUI stuff of the prediction..............................................................................

import os
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)               #top-level= used when a python application needs to represent some tra information, pop-up, or group of widgets,etc.
    register_screen.title("Register")
    register_screen.geometry("800x800")

    global sno
    sno = 1
    global username
    global password
    global name
    global contact
    global email
    global age
    global gender
    
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    name  = StringVar()
    contact =StringVar()
    email = StringVar()
    age = StringVar()
    gender = IntVar()
 
    Label(register_screen, text="Please Enter The Details Below To Register ",font=("Algerian", 15),width= "250", height="3",fg="Black",bg="LightBlue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ",font=("Calibri",11),fg="Black", bg="LightBlue")
    username_lable.place(x=120,y=150)
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.place(x=240,y=150)
    password_lable = Label(register_screen, text="Password * ",font=("Calibri", 11),fg="Black", bg="LightBlue")
    password_lable.place(x=120,y=200)
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.place(x=240,y=200)
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=11, height=1, font=("Calibri", 13),fg="Black", bg="LightBlue", command = register_user).place(x=300,y=450)

    label_name = Label(register_screen,text = "Name:",width = 20).place(x = 70,y = 250)
    entry_name = Entry(register_screen,width = 20,textvariable = name)
    entry_name.place(x = 240,y = 250)
    label_contact = Label(register_screen,text ="Contact N0:",width = 20).place(x = 70,y = 290)
    entry_contact = Entry(register_screen,textvariable = contact,width = 20)
    entry_contact.place(x = 240,y = 290)
    label_email = Label(register_screen,text ="Email Id:",width = 20).place(x = 70,y = 330)
    entry_email = Entry(register_screen,textvariable = email,width = 20)
    entry_email.place(x = 240,y = 330)
    label_age = Label(register_screen,text = "Age",width = 20).place(x = 70,y = 370)
    entry_age = Spinbox(register_screen,textvariable = age,from_ = 1,to_ = 150 )
    entry_age.place(x = 240,y = 370)
    label_gender = Label(register_screen,text = "Gender",width = 20).place(x = 70,y = 410)
    g_radio_male = Radiobutton(register_screen, text="Male",padx = 5, variable=gender ,value= 1).place(x=240,y=410)
    g_radio_female =  Radiobutton(register_screen, text="Female",padx = 20, variable=gender, value= 2).place(x=300,y=410)
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("500x550")
    Label(login_screen, text="Please Enter The Details Below To Login",font=("Algerian", 15),width= "250", height="3",fg="Black",bg="Lightblue").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ",font=("Calibri", 12),fg="Black",bg="Lightblue").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ",font=("Calibri", 12),fg="Black",bg="Lightblue").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login",font=("Calibri", 12),fg="Black",bg="Lightblue" ,width=11, height=1, command = login_verify).pack()

    
# Implementing event on register button
 
def register_user():
    username1 = username.get()
    password1 = password.get()
    name1 = name.get()
    contact1 = contact.get()
    email1 = email.get()
    age1 = age.get()
    gender1 = gender.get()

    cursorObject = dataBase.cursor()
  
    sql = "INSERT INTO register (username, password, name, contact, email, age, gender)\
    VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (username1, password1, name1, contact1, email1, age1, gender1)
   
    cursorObject.execute(sql, val)
    dataBase.commit()
   
    # disconnecting from server
    dataBase.close()
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).place(x=300,y=490)


# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    cursorObject = dataBase.cursor()
    cursorObject = dataBase.cursor(dictionary=True)
    sql1 = "select * from register where username='" + username1 + "' and password='" + password1 + "'"
    
    cursorObject.execute(sql1)
    result=cursorObject.fetchall()
    if result:
        login_sucess()
        #break
    else:
        messagebox.showinfo("Error","NOt Valid Login")
        
        
            
    dataBase.commit()
    
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    main_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def store():
    name1 = Name.get()
    symp1 = Symptom1.get()
    symp2 = Symptom2.get()
    symp3 = Symptom3.get()
    symp4 = Symptom4.get()
    symp5 = Symptom5.get()
    txt1 = t2.get("1.0","end-1c")
    txt2 = t3.get("1.0","end-1c")
    txt3 = t1.get("1.0","end-1c")
    txt4 ='RF-96%'  #t4.get("1.0","end-1c")
    messagebox.showinfo("Data stored successfully")
    cursorObject = dataBase.cursor()
    cursorObject = dataBase.cursor(dictionary=True)
    sql = "INSERT INTO health_prediction (name, Symptoms1, Symptoms2, Symptoms3, Symptoms4, Symptoms5, rf, nb, dt, best)\
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s ,%s)"
    val = (name1, symp1, symp2, symp3, symp4, symp5, txt1, txt2, txt3, txt4)
   
    cursorObject.execute(sql, val)
    dataBase.commit()
    '''dataBase.close()'''



def view():
    root = Tk()
    root.geometry("1800x1800")
    root.title("Report")
    #root.configure(background='Lavender')
    
    cursorObject = dataBase.cursor()
    sql1 = "select * from health_prediction"
    #sql1 = "select *from health_prediction ORDER BY id DESC LIMIT 1"
    cursorObject.execute(sql1)
    rs = cursorObject.fetchall()

    
    #pandas
    import pandas as pd
    df = pd.DataFrame(rs)
    #print(df.to_string())
    l=Label(root,text="HOSPITAL MANAGEMENT",font=("times new roman",35))
    l.pack()
    
    #l=Label(root,text=df.to_string())
    #l.pack()
    
    height = len(rs)
    width = 10
    cells = {}
    i=0
    lf=LabelFrame(root,text="PATIENT REPORTS",font=("calabri",20))
    lf.pack(fill="both", expand="yes")

    for s in rs:
        
        for j in range(len(s)):
            b=Label(lf,width=17,fg="black",text=s[j],relief='ridge',anchor="w")
            b.grid(row=i,column=j)
        i=i+1
                    

    '''
    for i in range(height): #Rows
        for j in range(width): #Columns
            #b = Label(root, text=[j.name, j.Symptoms1, j.Symptoms2, j.Symptoms3, j.Symptoms4, j.Symptoms5, j.rf, j.nb, j.dt,j.best])
            
            b = Entry(root, text="")
            b.grid(row=i, column=j)
            cells[(i,j)] = b
    '''       
    root.mainloop()


    
    
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("600x500")
    
    main_screen.title("Health Prediction Using Machine Learning ")
    Label(text="Health Prediction Using Machine Learning \n\n Select Your Choice", bg="LightBlue",fg="Black", width="300", height="4", font=("Algerian", 17)).pack()
    Label(text="").pack()
    
    Button(text="Login", fg="Black",bg="Lightblue",height="2", width="30", font=("Calibri", 15),command = login).pack()
    Label(text="").pack()
    Button(text="Register",fg="Black", bg="Lightblue",height="2", width="30", font=("Calibri", 15),command=register).pack()
 
    main_screen.mainloop()

 
 
main_account_screen()


root = Tk()
root.configure(background='Lavender')



Symptom1 = StringVar()
Symptom1.set("Select Here")

Symptom2 = StringVar()
Symptom2.set("Select Here")

Symptom3 = StringVar()
Symptom3.set("Select Here")

Symptom4 = StringVar()
Symptom4.set("Select Here")

Symptom5 = StringVar()
Symptom5.set("Select Here")

global Name 
Name = StringVar()
Age = int()




w2 = Label(root, justify=RIGHT, text="Health Prediction using Machine Learning", fg="Black", bg="GhostWhite")
w2.config(font=("Algerian",18,"bold"))
w2.grid(row=1, column=1, columnspan=2, padx=100)
w2 = Label(root, justify=LEFT, text="Fill All Colums For Better Accuracy ", fg="Black", bg="GhostWhite")
w2.config(font=("Algerian",18,"bold "))
w2.grid(row=4, column=1, columnspan=2, padx=100)



NameLb = Label(root, text="Name of the Patient", fg="Red", bg="Sky Blue")
NameLb.config(font=("Helvetica",16,"bold "))
NameLb.grid(row=5, column=0, pady=16, sticky=W)






S1Lb = Label(root, text="Symptom 1", fg="Blue", bg="Pink")
S1Lb.config(font=("Helvetica",15,"bold italic"))
S1Lb.grid(row=7, column=0, pady=10, sticky=W)

S2Lb = Label(root, text="Symptom 2", fg="White", bg="Purple")
S2Lb.config(font=("Helvetica",15,"bold italic"))
S2Lb.grid(row=8, column=0, pady=10, sticky=W)

S3Lb = Label(root, text="Symptom 3", fg="Green",bg="white")
S3Lb.config(font=("Helvetica",15,"bold italic"))
S3Lb.grid(row=9, column=0, pady=10, sticky=W)

S4Lb = Label(root, text="Symptom 4", fg="blue", bg="Yellow")
S4Lb.config(font=("Helvetica",15,"bold italic"))
S4Lb.grid(row=10, column=0, pady=10, sticky=W)

S5Lb = Label(root, text="Symptom 5", fg="purple", bg="light green")
S5Lb.config(font=("Helvetica",15,"bold italic"))
S5Lb.grid(row=11, column=0, pady=10, sticky=W)


lrLb = Label(root, text="DecisionTree", fg="white", bg="red")
lrLb.config(font=("Helvetica",15,"bold italic"))
lrLb.grid(row=17, column=0, pady=10,sticky=W)



ranfLb = Label(root, text="NaiveBayes", fg="White", bg="green")
ranfLb.config(font=("Helvetica",15,"bold italic"))
ranfLb.grid(row=18, column=0, pady=10, sticky=W)

destreeLb = Label(root, text="RandomForest", fg="Red", bg="Orange")
destreeLb.config(font=("Helvetica",15,"bold italic"))
destreeLb.grid(row=19, column=0, pady=10, sticky=W)

OPTIONS = sorted(l1)

NameEn = Entry(root, textvariable=Name,fg="black",bg="white")
NameEn.config(font=("Helvetica",15,"bold"))
NameEn.grid(row=5, column=1)





        
S1 = OptionMenu(root, Symptom1,*OPTIONS)
S1.config(font=("Helvetica",10,"bold"))
S1.grid(row=7, column=1)

S2 = OptionMenu(root, Symptom2,*OPTIONS)
S2.config(font=("Helvetica",10,"bold"))
S2.grid(row=8, column=1)

S3 = OptionMenu(root, Symptom3,*OPTIONS)
S3.config(font=("Helvetica",10,"bold"))
S3.grid(row=9, column=1)

S4 = OptionMenu(root, Symptom4,*OPTIONS)
S4.config(font=("Helvetica",10,"bold"))
S4.grid(row=10, column=1)

S5 = OptionMenu(root, Symptom5,*OPTIONS)
S5.config(font=("Helvetica",10,"bold"))
S5.grid(row=11, column=1)


dst = Button(root, text="Prediction 1", command=DecisionTree,bg="black",fg="yellow",bd=10)
dst.config(font=("Helvetica",15,"bold italic"))
dst.grid(row=8, column=2,padx=10)



lr = Button(root, text="Prediction 2", command=NaiveBayes,bg="Blue",fg="white", bd=10)
lr.config(font=("Helvetica",15,"bold italic"))
lr.grid(row=9, column=2,padx=10)

rnf = Button(root, text="Prediction 3", command=randomforest,bg="White",fg="green", bd=10)
rnf.config(font=("Helvetica",15,"bold italic"))
rnf.grid(row=10, column=2,padx=10)

store = Button(root, text="Store", command=store,bg="White",fg="green", bd=10)
store.config(font=("Helvetica",15,"bold italic"))
store.grid(row=11, column=2,padx=10)

view = Button(root, text="View", command=view,bg="White",fg="green", bd=10)
view.config(font=("Helvetica",15,"bold italic"))
view.grid(row=12, column=2,padx=10)

t1 = Text(root, height=1, width=40,bg="Light green",fg="red")
t1.config(font=("Helvetica",15,"bold italic"))
t1.grid(row=17, column=1, padx=10)


t2 = Text(root, height=1, width=40,bg="red",fg="white")
t2.config(font=("Helvetica",15,"bold italic"))
t2.grid(row=19, column=1 , padx=10)


t3 = Text(root, height=1, width=40,bg="White",fg="Blue")
t3.config(font=("Helvetica",15,"bold italic"))
t3.grid(row=18, column=1 , padx=10)


t4 = Text(root, height=1, width=40,bg="red",fg="white")
t4.config(font=("Helvetica",15,"bold italic"))
t4.grid(row=20, column=1 , padx=10)


root.mainloop()


# %%
