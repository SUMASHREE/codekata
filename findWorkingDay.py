    Workingday={}
    def findHoliday(day):
        Workingday['Monday']='true'
        Workingday['Tuesday']='true'
        Workingday['Wednesday']='true'
        Workingday['Thursday']='true'
        Workingday['Friday']='true'
        Workingday['Saturday']='true'
        Workingday['Sunday']='false'
        return Workingday[day]
    day=input("Enter the day:")
    wd=findHoliday(day)
    print(wd)
    if wd=='false':
        print(day+" is a holiday")
    else:
        print(day+" is a working day")
