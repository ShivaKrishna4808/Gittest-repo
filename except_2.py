def check_age(age):
    try:
        if age<18:
            raise Exception("age must be 18 or above")
        
        print("Eliigble for voting")

    except Exception as e:
        print("Exception:", e)


check_age(21)
check_age(15)