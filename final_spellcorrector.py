def min_edit_dist(word1,word2):
    len_1=len(word1)
    len_2=len(word2)
    x = [[0]*(len_2+1) for _ in range(len_1+1)]#the matrix whose last element ->edit distance
    for i in range(0,len_1+1):  
    #initialization of base case values
        x[i][0]=i
    for j in range(0,len_2+1):
         x[0][j]=j
    for i in range (1,len_1+1):
        for j in range(1,len_2+1):
            if word1[i-1]==word2[j-1]:
                x[i][j] = x[i-1][j-1]
            else :
                x[i][j]= min(x[i][j-1],x[i-1][j],x[i-1][j-1])+1
    return x[i][j]
from Tkinter import *
# Define input retrieve function for application input
def retrieve_text():
    text.config(state=NORMAL)
    global word1
    word1=(app_entry.get())
    path="C:\Users\ishaan\Desktop\Dictionary.txt"
    ffile=open(path,'r')
    lines=ffile.readlines()
    distance_list=[]
    #print "Suggestions coming right up count till 10"
    for i in range(0,58109):
        
       dist=min_edit_dist(word1,lines[i])
       distance_list.append(dist)
    for j in range(0,58109):
        
        if distance_list[j]<=2:
            
            
            text.insert('1.end',lines[j])
            text.insert('1.end',' \n')
    text.config(state=DISABLED)
            
        
    ffile.close()


if __name__ == "__main__":

    
    # Create window (or form)
    app_win = Tk()
    app_win.title("spell")

    # Create label
    app_label = Label(app_win, text="Enter the incorrect word")
    app_label.pack()

    # Create entry box
    app_entry = Entry(app_win)
    app_entry.pack()
    
    text=Text(app_win)
    text.pack()

    text.config(state=DISABLED)
    # Create button
    app_button = Button(app_win, text="Get Suggestions", command=retrieve_text)
    app_button.pack()

    # Initialize GUI loop
    app_win.mainloop()

