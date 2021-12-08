def count_names(name_list):
    count1=0
    count2=0
    for i in name_list:
        if ((i[0]>'a' and i[0]<'z') or (i[0]>'A' and i[0]<'Z')) and i.endswith("at"):
            count1+=1
        if "at" in i:
            count2+=1
    print("_at -> ",count1)
    print("%at% -> ",count2)
    
#Provide different names in the list and test your program
name_list=["Hat","Cat","rabbit","matter"]
count_names(name_list)
