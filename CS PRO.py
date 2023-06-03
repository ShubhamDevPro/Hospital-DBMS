passwordsql=str(input("Enter your password of MySql  - "))
import mysql.connector as sql
mycon=sql.connect(host='localhost',user='root',passwd=passwordsql,database='AIIMS')
if mycon.is_connected():
  print("\n")
  print('successfully connected to Hospitals MySQL Database')
  
cur=mycon.cursor()

print("\n"* 2)

print("Welcome To All India Institute Of Medical Science")

print("\n"* 2)

print('"Get Well Soon "')

print("\n"* 2)

def choices():
  choice=str(input("Do you want to login(yes/no): "))
  if choice=="yes":
    uname=input("Enter username:")
    pwd=input("Enter password:")
    if uname=="cs" and pwd=="project":
      print("\n"* 2)

      print("Database can be accessed now")
      
      print("\n"* 2)
        
      print("What do you need ?")
      
      print("\n")
        
      print("1. Admit Patient")
  
      print("\n")
        
      print("2. Update patient info")
        
      print("\n")

      print("3. New Doctor details")

      print("\n")

      print("4. Close")

    else:
      print("\n")
      
      print("Wrong password or username. TRY AGAIN")
      choices()
    print("\n"*2)
    need=str(input("What do you want to do ? Enter option no.  =  "))
    if need=="1":
      print("Admit Patient")

      print("\n")
      
      patid=str(input("Enter Unique ID No. :    "))

      print("\n")
      name=str(input("Name  :"))

      print("\n")

      di=str(input("Disease:   "))

      print("\n")

      c=str(input("Admision date:  "))

      print("\n")

      d=str(input("Enter Discharge Date:   "))

      print("\n")
      total=str(input("Enter Total Amount Due"))

      print("\n")
      cur.execute("insert into patients_information(Patient_ID_number,name_of_patient,disease,patient_admitted_on,patient_discharged_on,total_amount) values(  "+patid+" , "+name+"  , " +di+"  ,"+ c+",   "+d+"   , "+total+");")
      #cur.execute(exe)
      mycon.commit()
      cur.close()
      mycon.close()
      print("data entered succefully")
      choices()
    elif need=="2":
      print("Update Patient Info")
      print(" What do you want to update ? " )
      print(" 1. Patient Id")
      print(" 2. Name of Patient")
      print(" 3.Disease")
      print(" 4. Admission Date")
      print("5. Discharge Date" )
      print(" 6. Total Amount Due")
      update= "" # BCZ update was not defined Error
      CHOICE=str(input( "Enter Choice Number :"))
      if CHOICE=="1":
        pidu=str(input("Enter Existing Patient Id  : "))
        colu=str(input("Enter New Patient Id : "))
        cur.execute(" update patients_information set Patient_ID_number= "+colu+" where Patient_ID_Number= "+pidu+" ;")
      elif CHOICE=="2":
        pidu=str(input("Enter Patient's ID number  : "))
        colu=str(input("Enter Corrected Name of Patient  :  "))
        cur.execute(" update patients_information set name_of_patient="+colu+" where Patient_ID_number="+pidu+" ;")
      elif CHOICE=="3":
        pidu=str(input("Enter Patient's ID number : "))
        colu=str(input("Enter New Symptoms/Disease :  "))
        cur.execute(" update patients_information set disease="+colu+" where Patient_ID_number="+pidu+";")
      elif CHOICE=="4":
        pidu=str(input("Enter Patient's ID number : "))
        colu=str(input("Enter Corrected Admission Date :  "))
        cur.execute(" update patients_information set patient_admitted_on="+colu+" where Patient_ID_number="+pidu+";")
      elif CHOICE=="5":
        pidu=str(input("Enter Patient's ID number :"))
        colu=str(input("Enter Corrected Admission Date :  "))
        update=" update patients_information set patient_discharged_on="+colu+" where Patient_ID_number="+pidu+";"
      elif CHOICE=="6":
        pidu=str(input("Enter Patient's ID number :"))
        colu=str(input("Enter Total Amount Due  "))
        cur.execute(" update patients_information set total_amount="+colu+" where Patient_ID_number="+pidu+";")
      else:
            print("Incorrect Option")
      print("INFORMATION UPDATED")
      choices()
    
    elif need=="3":
      print("Enter Newly appointed Doctor Details")
      choices()
    elif need=="4":
      print("Closing Program")
      choices()
    else:
        print("Invalid Choice")
        choices()
        
choices()
mycon.close()

