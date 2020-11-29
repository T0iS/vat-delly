import glob
import os
import csv
import sys

arr = []
keyword = ""

def load_scheme(inp_filename):   
        global arr
        global keyword
        with open(inp_filename, 'r') as f:
            text = f.readlines()
            keyword = text[0].strip() 
            for line in text[1:]:
                line = line.strip().split(",")
                if(arr[int(line[1])] == 999):
                    arr[int(line[1])] = int(line[0])
                else:
                    print("DUPLICITA VE SCHEMATU")

                #index je nove, value je puvodni

def def_input():
    global arr
    inp = " "
    while True:

        inp = input("Vlozte mapovani ve formatu\nPUVODNI NOVE:\n")
        if inp is "":
            break
        print(inp)
        inp = inp.split(" ")
        arr[int(inp[1])] = int(inp[0])
        inp = " "

          
def conf():
    print("Ulozit nove mapovani?\n")
    for i in range(0,86):
        print(i, " ", end = '')
    print("\n")
    print(arr)


    inp = input("Y pro povrzeni N pro opravu\n")
    if inp is "Y":
        inp = input("Vlozte nazev mapovani:\n")
        inp2=input("Vlozte klicove slovo pro rozliseni souboru: \n")
        keyword = inp2
        with open(inp, 'w+') as scheme_file:  
            scheme_file.write(keyword + "\n")
            for i in range(len(arr)):
                if arr[i] is not 999:
                    scheme_file.write(str(i))
                    scheme_file.write(",")
                    scheme_file.write(str(arr[i]))
                    scheme_file.write("\n")
        return True
    else:
        return False

def create_scheme():
    

    
    inp = input("Chcete nacist stavajici schema? Y|N\n")
    if inp is "Y":
        inp = input("Zadejte nazev schematu v teto slozce: ")
        load_scheme(inp)
    print(keyword)
    def_input()
    while conf() == False:                
        def_input()
        conf()



def script_one(filename):
    with open(filename, 'r') as f:
        text = f.readlines()
        not_found = []
        used = []
        for line in text[6:]:
            idx =  text.index(line)
            if ',' in line:
                line = line.split(',')
                try:
                    line[0] = str(arr.index(int(line[0])))
                    used.append(arr.index(int(line[0])))
                except ValueError:
                    not_found.append(idx)

                line = "".join(line[0]+","+line[1])
                text[idx] = line

        for n in not_found:
            line = text[n]
            line = line.split(',')
            for a in reversed(arr):
                if a not in used:
                    line[0] = a
                    line = "".join(line[0]+","+line[1])
                    text[n] = line


    save_script(filename.replace(".txt", "-DELLY.txt"),text)
    




def script_multi(src_folder=os.getcwd()):

    if not os.path.exists(src_folder):
        print("SOURCE DIR NOT CORRECT")
        main()
    dest_folder = os.path.join(src_folder, "DELLY_URC_files")
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)
    
    for root, dirs, files in os.walk(src_folder):
        for filename in files:
        
            if keyword in filename and "DELLY" not in filename:
                with open(os.path.join(root,filename), 'r') as f:
                    text = f.readlines()
                    not_found = []
                    used = []
                    for line in text[6:]:
                        idx =  text.index(line)
                        if ',' in line:
                            line = line.split(',')
                            try:
                                used.append(arr.index(int(line[0])))
                                line[0] = str(arr.index(int(line[0])))
                                
                                                                    
                            except ValueError:
                                not_found.append(idx)

                            
                            line[1] = line[1].replace("0005","0051")
                            line = "".join(line[0]+","+line[1])
                            text[idx] = line

                            
                for n in not_found:
                    line = text[n]
                    line = line.split(',')
                    for a in reversed(arr):
                        if (arr.index(a) not in used) or a == 999:
                            
                            line[0] = arr.index(a)
                            
                            line = "".join(str(line[0])+","+line[1])
                            text[n] = line
                            used.append(arr.index(a))
                            arr[arr.index(a)] = 888
                            break
           
                name = filename.replace(".txt", "-DELLY.txt")
                save_script(os.path.join(dest_folder, name),text)



def save_script(filename, text):
    with open(filename, 'w+') as script_file: 
        script_file.writelines(text)

def main():

    global arr
    for i in range(0,86):
        arr.append(999)
    

    inp = input("Vlozte cislo pro pozadovanou akci\n1) Uprava schematu\n2) Spustit script na jeden soubor\n3) Spustit script na soucasnou slozku.\n")
    if int(inp) == 1:
        create_scheme()
    elif int(inp) == 2:
        inp = input("Vlozte nazev souboru\n")
        inp_scheme = input("Vlozte nazev schematu\n")
        load_scheme(inp_scheme)
        script_one(inp)
    elif int(inp) == 3:
        inp = input("Vlozte zdrojovou slozku, nebo nechte prazdne\n")
        inp_scheme = input("Vlozte nazev schematu\n")
        load_scheme(inp_scheme)
        if inp == "":
            script_multi()
        else:
            script_multi(inp)

if __name__ == "__main__":
    main()