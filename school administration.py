import csv 

def write_into_csv(info_list):
    with open('student_info.cvs','a',newline='')as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(("name"," age"," contact_no","email_id"))
    
        writer.writerow(info_list)
        
if __name__ == '__main__':
    status = True
    student_num=1
  
    while(status):
            student_info = input("enter the student information in a name age contact_number and e-mail id format:")
           
            
            
            student_info_list=student_info.split(' ')
            print("\n The entered information is \n Name:{}\n Age:{} \n Contact Number:{} \nE-Mail:{}"
                  .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
            choice_check = input("is the entered information correct?(yes/no)")
            
            if choice_check == "yes":
                write_into_csv(student_info_list)
            
            
            
                status_check = input("Do you want to continue ?(yes/no): ")
                if status_check =="yes":
                    status = True
                elif status_check== "no":
                    status = False

            elif choice_check == "no":
                 print("\n please enter the data again correctly")
   
      
    
    
