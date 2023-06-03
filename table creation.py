passwordsql=str(input("Enter your password of MySql  - "))
import mysql.connector as sql
mycon=sql.connect(host='localhost',user='root',passwd=passwordsql)
if mycon.is_connected():
  print("\n")
  print('successfully connected to SQL')
  
cur=mycon.cursor()

###  cur.execute("drop database if exists aiims")
cur.execute(" Create Database if not exists aiims")
cur.close()
mycon.close()

mycon=sql.connect(host='localhost',user='root',passwd=passwordsql,database="aiims")
cur=mycon.cursor()
cur.execute("Create Table if not exists Patients_information(Patient_ID_number varchar(10) primary key,name_of_patient varchar(15),  disease varchar(15),patient_admitted_on date, patient_discharged_on date,total_amount int);")

cur.execute("create table if not exists doctor_information( doctor_id_no varchar(10) primary key,doctor_name varchar(20),department varchar(20),mob_no varchar(10));")
mycon.commit()
print("Succesfully created tables")

# DATA
insertcoms=("""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1001,"Aditya","Kidney Stone",'2020-04-20','2020-10-10',10000);"""
,"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1002,"Hardeep","Diabetes",'2020-05-19','2020-10-04',50000);"""
,"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1003,"Sunil","Chloera",'2020-07-19','2020-09-15',5000);"""
,"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1004,"Sunil","Pneumonia",'2020-08-16','2020-10-07',10000);"""
,"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1005,"raani","Anaemia",'2020-08-28','2020-10-10',2500);"""
,"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1006,"Gaurav","Rickets",'2020-03-28','2020-11-04',200000);"""
,"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1007,"Ryuzaki","Stroke",'2020-05-24','2020-11-02',50000);"""
,"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1008,"Lokhand","Kidney Failure",'2018-06-17','2019-11-10',850000);"""
,"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1009,"Rupa","Diabetes",'2018-02-23','2020-05-28',850012);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1010,"Suresh","Covid-19",'2018-02-23','2020-09-09',900000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1011,"Yagami","Tubercluosis",'2018-05-20','2020-11-14',95000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1012,"Simon","Diabetes",'2018-06-20','2020-09-10',1000000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1013,"Suresh","Cold",'2017-04-08','2017-05-31',500);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1015,"Nimala","Covid-19",'2020-08-05','2020-08-31',500000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1016,"saishri","Malaria",'2020-01-06','2020-02-28',90000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1017,"somya","Fungal",'2019-01-07','2019-03-25',75000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1018,"Sonny","Covid-19",'2020-10-07','2020-08-30',65000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1019,"Aman","Covid-19",'2019-01-15','2020-08-27',78900);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1020,"Aram","Alzheimer",'2019-01-30','2020-08-29',50200);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1021,"Virat","Depression",'2019-01-31','2020-03-31',8000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1022,"Ranveer","Fever&Cold",'2019-01-06','2020-02-28',4500);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1023,"Allu","Cataract",'2019-07-18','2019-11-11',10000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1024,"Naira","Covid-19",'2019-05-27','2020-08-28',200000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1025,"Mudit","Bone Fracture",'2020-01-21','2020-06-21',500000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1026,"Ayush","Inflammation",'2019-11-30','2020-02-25',5000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1027,"Anuja","Diabetes",'2019-08-19','2019-10-20',20000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1028,"Arjuna","Sinus",'2017-08-19','2018-11-21',18000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1029,"Sahil","Bloating",'2019-08-15','2020-10-13',15000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1030,"Suresh","tubercluosis",'2019-05-20','2020-05-18',44000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1031,"Pooja","Fever","2020-05-01","2020-05-10",5000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1032,"Kaashvi","Cold","2020-04-22","2020-04-26",2000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1033,"John","Fungal","2020-04-10","2020-04-20",7000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1034,"Jitender","Covid-19","2020-07-02","2020-08-05",20000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1035,"Girish","Diabetes","2020-03-25","2020-04-07",5000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1036,"Sanjay","Rickets","2020-05-17","2020-05-29",3500);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1037,"Kulbhusan","Malaria","2020-08-23","2020-09-13",6500);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1038,"Jatin","Tubercluosis","2020-09-12","2020-09-23",7000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1039,"Akki","Fever","2020-08-13","2020-08-16",2500);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1040,"Nikhil","AIDS","2020-07-03","2020-08-01",8000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1041,"Ethesh","Bloating","2020-08-10","2020-08-12",1500);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1042,"Prateek","Cold","2020-08-16","2020-08-27",4500);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1043,"Yashveer","Anaemia","2020-09-12","2020-09-24",6500);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1044,"Kashish","Stroke","2020-09-15","2020-09-30",8000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1045,"Harsh","Kidney stone","2020-09-09","2020-09-20",7500);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1046,"Komal","Malaria","2020-09-07","2020-09-21",5500);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1047,"Rahul","Chickengunia","2020-10-02","2020-10-25",8700);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1048,"Akshay","Eye infection","2020-09-15","2020-09-22",4500);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1049,"Balkishan","Rickets","2020-09-14","2020-09-30",6000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1050,"Harshita","Thyroid","2020-10-05","2020-11-21",45000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1051,"Surinder","Kidney stone","2020-10-04","2020-10-29",6000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1052,"Astha","Diabetes","2020-10-02","2020-10-26",12000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1053,"Sonam","Covid-19","2020-11-01","2020-11-10",4500);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1054,"Kamlesh","Flu","2020-10-08","2020-10-14",8000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1055,"Yogesh","Anaemia","2020-10-07","2020-10-14",5000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1056,"Kajal","Fever","2020-10-15","2020-10-27",10000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1057,"Chaman","Malaria","2020-10-07","2020-10-18",14000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1058,"Ayushi","Rickets","2020-11-09","2020-12-10",125000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1059,"Akashat","Covid-19","2020-10-13","2020-10-23",19000);""",
"""insert ignore into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(1060,"Minakshi","Bloating","2020-11-18","2020-11-29",30000);""" )        


for exe in insertcoms:
  cur.execute(exe)
mycon.commit()


insertcoms2=(""" insert ignore into doctor_information values(5001,"Akash","pulmonologists",9867574790);""",
""" insert ignore into doctor_information values(5002,"Anish","radiologists",9015023248);""",
""" insert ignore into doctor_information values(5003,"Mayank","pathologists","9684747442");""",
""" insert ignore into doctor_information values(5004,"Radhika","oncologists",9087524257);""",
""" insert ignore into doctor_information values(5005,"Rashmi","gynecologists",9483847837);""",
""" insert ignore into doctor_information values(5006,"Kaushal","neurologists",9573846748);""",
""" insert ignore into doctor_information values(5007,"Chandra","nephrologists",9685747377);""",
""" insert ignore into doctor_information values(5008,"Akash","internists",9873473548);""",
""" insert ignore into doctor_information values(5009,"Vivek","hematologists",9726740362);""",
""" insert ignore into doctor_information values(5010,"Mohit","gastroenterologists",9868537830);""",
""" insert ignore into doctor_information values(5011,"Madhu","dentalist",9634152829);""",
""" insert ignore into doctor_information values(5012,"Ravina","endocrilogists",9853480063);""",
""" insert ignore into doctor_information values(5013,"Bablu","surgeon",9542775688);""",
""" insert ignore into doctor_information values(5014,"Ankesh","anesthesiologist",9663576445);""",
""" insert ignore into doctor_information values(5015,"Rakesh","family_physicians",9768764678);""",
""" insert ignore into doctor_information values(5016,"Sonam","allergists",8751466830);""",
""" insert ignore into doctor_information values(5017,"Nidhi","dermatologists",9622369061);""",
""" insert ignore into doctor_information values(5018,"Devraj","cardiologists",9764639007);""",
""" insert ignore into doctor_information values(5019,"Sonu","urologists",9870680231);""",
""" insert ignore into doctor_information values(5020,"Purti","plastic_surgeon",9576001145);""",
""" insert ignore into doctor_information values(5021,"Archana","dentalist",8598319269);""",
""" insert ignore into doctor_information values(5022,"Satish","surgeon",8364748282);""",
""" insert ignore into doctor_information values(5023,"Sadhna","internists",9899948206);""",
""" insert ignore into doctor_information values(5024,"Pankaj","cardiologists",8948844017);""",
""" insert ignore into doctor_information values(5025,"khushi","pathologists",9863863106);""")

for exe in insertcoms2:
  cur.execute(exe)
mycon.commit()
