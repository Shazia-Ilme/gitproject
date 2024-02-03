import mysql.connector as m
import numpy as np
import matplotlib.pyplot as plt

c = m.connect(host='localhost', user='root', passwd='23786@Ans')
cursor = c.cursor()
cursor.execute('drop database if exists yyes')
cursor.execute('create database yyes')
cursor.execute('use yyes')
cursor.execute('create table c19_vaccination(sno integer, city varchar(20), country varchar(20), affected int, vaccinated_1dose int, vaccinated_2dose int)')
c.commit()
c.close()

while True:
    print("WELCOME TO THE VACCINATION SURVEY!")
    print("1. add details of affected and vaccinated people")
    print("2. update details of affected and vaccinated people")
    print("3. display/search details of affected and vaccinated people")
    print("4. show the graph of affected and vaccinated people")
    print("5. exit")
    
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        c = m.connect(host='localhost', user='root', passwd='23786@Ans', database='yyes')
        cursor = c.cursor()
        sno = int(input("Enter serial no.: "))
        city = input("Enter city name: ")
        country = input("Enter the name of the country: ")
        affected = int(input("Enter no of people affected with covid: "))
        vaccinated_1dose = int(input("Enter no of people vaccinated with 1st dose: "))
        vaccinated_2dose = int(input("Enter the no. of people vaccinated with 2nd dose: "))
        cursor.execute('''
            insert into c19_vaccination values("%d","%s","%s","%d","%d","%d")
        ''' % (sno, city, country, affected, vaccinated_1dose, vaccinated_2dose))
        c.commit()
        c.close()
    
    elif ch == 2:
        c = m.connect(host='localhost', user='root', passwd='23786@Ans', database='yyes')
        cursor = c.cursor()
        print("1. update city ")
        print("2. update country")
        print("3. update no of people affected with covid")
        print("4. update no of people vaccinated with 1st dose")
        print("5. update no of people vaccinated with 2nd dose")
        print("6. exit")
        t = int(input("Enter your choice for 2nd choice: "))
        
        if t == 1:
            city = input("Enter the modified city name: ")
            sno = int(input("Enter the sno of the data to be modified: "))
            cursor.execute('''update c19_vaccination set city="%s" where sno="%d"''' % (city, sno))
            c.commit()
            print("Successfully updated!")
        
        elif t == 2:
            country = input("Enter the modified country name: ")
            sno = int(input("Enter the sno of the data to be modified: "))
            cursor.execute('''update c19_vaccination set country="%s" where sno="%s"''' % (country, sno))
            c.commit()
            print("Successfully updated!")
        
        elif t == 3:
            affected = int(input("Enter the modified no of affected people: "))
            sno = int(input("Enter the sno of the data to be modified: "))
            cursor.execute('''update c19_vaccination set affected="%d" where sno="%d"''' % (affected, sno))
            c.commit()
            print("Successfully updated!")
        
        elif t == 4:
            vaccinated_1dose = int(input("Enter the modified no. of vaccinated people with 1st dose: "))
            sno = int(input("Enter the sno of the data to be modified: "))
            cursor.execute('''update c19_vaccination set vaccinated_1dose="%d" where sno="%d"''' % (vaccinated_1dose, sno))
            c.commit()
            print("Successfully updated!")
        
        elif t == 5:
            vaccinated_2dose = int(input("Enter the modified no. of vaccinated people with 2nd dose: "))
            sno = int(input("Enter the sno of the data to be modified: "))
            cursor.execute('''update c19_vaccination set vaccinated_2dose="%d" where sno="%d"''' % (vaccinated_2dose, sno))
            c.commit()
            print("Successfully updated!")
        
        elif t == 6:
            pass  # You can add more options or exit logic here
        
        c.close()
    
    elif ch == 3:
        c = m.connect(host='localhost', user='root', passwd='23786@Ans', database='yyes')
        cursor = c.cursor()
        print("1. show all the details")
        print("2. show the details of a particular city")
        t = int(input("Enter your choice: "))
        
        if t == 1:
            cursor.execute('select * from c19_vaccination')
            a = cursor.fetchall()
            for i in a:
                print(i)
        
        elif t == 2:
            sno = int(input("Enter the serial no. whose details are to be displayed: "))
            cursor.execute('''select * from c19_vaccination where sno="%d"''' % (sno))
            a = cursor.fetchall()
            for i in a:
                print(i)
        
        else:
            print("Enter a proper choice")
        
        c.close()
    
    elif ch == 4:
        c = m.connect(host='localhost', user='root', passwd='23786@Ans', database='yyes')
        cursor = c.cursor()
        print("1. graph of people affected with covid ")
        print("2. graph of people vaccinated with 1st dose ")
        print("3. graph of people vaccinated with 2nd dose ")
        h = int(input("Enter your choice for 2nd choice: "))
        
        if h == 1:
            country = input("Enter the country whose covid positive cases graph is to be displayed: ")
            cursor.execute('''select affected from c19_vaccination where country="%s" ''' % (country))
            u = cursor.fetchall()
            x = np.array(u)
            x1 = []
            
            for i in x:
                for j in i:
                    x1.append(j)
            
            cursor.execute('''select city from c19_vaccination where country="%s"''' % (country))
            p = cursor.fetchall()
            y = np.array(p)
            y1 = []
            for i in y:
                for j in i:
                    y1.append(j)
            
            plt.bar(y1, x1, width=0.5, color='red')
            plt.xlabel('City')
            plt.ylabel('Affected')
            plt.show()
        
        elif h == 2:
            country = input("Enter the country whose 1st dose vaccination graph is to be displayed: ")
            cursor.execute('''select vaccinated_1dose from c19_vaccination where country="%s" ''' % (country))
            u = cursor.fetchall()
            x = np.array(u)
            x1 = []
            
            for i in x:
                for j in i:
                    x1.append(j)
            
            cursor.execute('''select city from c19_vaccination where country="%s"''' % (country))
            p = cursor.fetchall()
            y = np.array(p)
            y1 = []
            
            for i in y:
                for j in i:
                    y1.append(j)
            
            plt.bar(y1, x1, width=0.5, color='green')
            plt.xlabel('City')
            plt.ylabel('Vaccinated_1dose')
            plt.show()
        
        elif h == 3:
            country = input("Enter the country whose 2nd dose vaccination graph is to be displayed: ")
            cursor.execute('''select vaccinated_2dose from c19_vaccination where country="%s" ''' % (country))
            u = cursor.fetchall()
            x = np.array(u)
            x1 = []
            
            for i in x:
                for j in i:
                    x1.append(j)
            
            cursor.execute('''select city from c19_vaccination where country="%s"''' % (country))
            p = cursor.fetchall()
            y = np.array(p)
            y1 = []
            
            for i in y:
                for j in i:
                    y1.append(j)
            
            plt.bar(y1, x1, width=0.5, color='blue')
            plt.xlabel('City')
            plt.ylabel('Vaccinated_2dose')
            plt.show()
        
        c.close()
    elif ch == 5:
        break