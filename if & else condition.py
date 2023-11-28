age=int(input("Enter the age:-"))
gender=str(input("Gender:")).upper()

if gender=='FEMALE':
    pass
elif gender =='MALE':
    pass
else:
    print("Enter Male and Female only")

if gender=='MALE' or gender =='FEMALE':
    if 0<=age <=5:
        print('You are not eligibal for education.')
    elif 5 <age<60:
        print('Now, You are eligibal for education.')
        if 5 < age <=21:
            dict1={
                6:'in 1 std',
                7:'in 2 std',
                8:'in 3 std',
                9:'in 4 std',
                10:'in 5 std',
                11:'in 6 std',
                12:'in 7 std',
                13:'in 8 std',
                14:'in 9 std',
                15:'in 10 std',
                16:'in 11 std',
                17:'in 12 std',
                18:'in 1st year of Graduation',
                19:'in 2ed year of Graduation',
                20:'in 3rd year of Graduation',
                21:'in 4th year of Graduation',
                }
            print(f"you are {dict1[age]}")

            if age>=18:
                print("you are eligibal for driving license & voting")
                if gender=="FEMALE":
                    print("you are eligible for marrige")
                if gender=="MALE" and age >=20:
                    print("not suicide.")
            elif age>=21:
                    print("if you are graduate then you are eligibal for competitive exam")
            elif age >=21 and gender=='MALE':
                 print('you are eligibale for marrige')
        elif 22< age <=30:
            if age>=23:
                        print("you are eligible to pursuing for master study ")
            if age>25:
                        print("you are eligible for to participate in Rajyasabha Election")
            if age>26:
                        print("You are eligible for Ph.D if master is done")
            if age>=30:
                        print("You are eligible for tp participate in loksabha election")
        elif age>=35:
                    print("Eligible to participate in election of President/Vice-President/Governor")
    elif age>=60:
                print("offical age for Retirment per labour law")
                if gender=='MALE':
                    print("Eligible for 10% benifit in tax")
                elif gender=='FEMALE':
                    print("Eligible for 20% benifit in tax")
    else:
         print("Insert Data Properly")