
# Goated GPA Calculator
# Last revised 12/1/2021

grade = ''
lastGrade = ''
uw = 0.0
w = 0.0
numCounted = 0.0
done = False
weighted = 0.0 
fail = 0.0

gpaTable = {'A+' : 4.33,
            'A'  : 4.00,
            'A-' : 3.67,
            'B+' : 3.33,
            'B'  : 3.00,
            'B-' : 2.67,
            'C+' : 2.33,
            'C'  : 2.00,
            'C-' : 1.67,
            'D+' : 1.33,
            'D'  : 1.00,
            'D-' : 0.67,
            'F'  : 0.00}

print ()
print ('----')
print ('Goated GPA Calculator')
print ()
print ("This calculator uses Francis Parker's GPA scale:")
print ('A+/4.33, A/4.00, A-/3.67, B+/3.33, B/3.00, B-/2.67,')
print ('C+/2.33, C/2.00, C-/1.67, D+/1.33, D/1.00, D-/0.67, F/0.00')
print ('Grades of C- and above in weighted classes earn an extra point (A+ = 5.33, for example).')
print ()
print ("If you would like to use Westview's GPA scale, simply omit pluses and minuses.")
print ('If you enter a grade incorrectly, enter "undo".') 
print ('When you are done entering grades, enter "done".')
print ('----')
print ()

def parseGrade ():
    global grade, lastGrade, uw, w, numCounted, done, weighted, fail
    if (grade == 'done' or grade == 'undo') and numCounted == 0:
        print ('Enter at least one grade first.')
        print ()
    elif grade == 'done':
        done = True
    elif grade == 'undo':
        uw -= gpaTable [lastGrade]
        numCounted -= 1.0
        print ('Undid previous entry.')
        print ()
    else:
        checkGrade ()

def checkGrade ():
    global grade, lastGrade, uw, w, numCounted, done, weighted, fail
    while True:
        try:
            uw += gpaTable [grade]
            numCounted += 1.0
            lastGrade = grade
            print ('Entered ' + grade + ' for GPA ' + str (gpaTable [grade]))
            print ()
            break
        except KeyError:
            print ('Enter a valid grade, "undo," or "done".')
            print ()
            break

while done == False:
    grade = input ('Enter grade: ')
    parseGrade ()

w = uw

def checkWeighted ():
    global grade, lastGrade, uw, w, numCounted, done, weighted, fail
    try:
        i = int (input ('If this is correct, enter "1"; otherwise, enter "0": '))
        if i == 0:
            getWeighted ()
        elif i == 1:
            w += weighted
        else:
            checkWeighted ()
    except ValueError:
        checkWeighted ()

def getWeighted ():
    global grade, lastGrade, uw, w, numCounted, done, weighted, fail
    try:
        weighted = float (input ('Enter the number of grades earned in weighted courses: '))
        if weighted < 0.0:
            print ('Enter a number ≥ 0.')
            print ()
            getWeighted ()
        elif weighted > numCounted:
            print ('This number cannot exceed the total number of grades.')
            print ('You entered ' + str (int (numCounted)) + ' total grade(s).')
            print ()
            getWeighted ()
        else:
            print ('Entered ' + str (int (weighted)) + '.')
            print ()
            checkWeighted ()
    except ValueError:
        print ('Enter a number ≥ 0.')
        print ()
        getWeighted ()

getWeighted ()

def checkFail ():
    global grade, lastGrade, uw, w, numCounted, done, weighted, fail
    try:
        i = int (input ('If this is correct, enter "1"; otherwise, enter "0": '))
        if i == 0:
            getFail ()
        elif i == 1:
            w -= fail
        else:
            checkFail ()
    except ValueError:
        checkFail ()

def getFail ():
    global grade, lastGrade, uw, w, numCounted, done, weighted, fail
    try:
        fail = float (input ('Enter the number of grades below C- earned in weighted courses: '))
        if fail < 0.0:
            print ('Enter a number ≥ 0.')
            print ()
            getFail ()
        elif fail > weighted:
            print ('This number cannot exceed the total number of grades earned in weighted courses.')
            print ('You entered ' + str (int (weighted)) + ' grade(s) in weighted courses.')
            print ()
            getFail ()
        else:
            print ('Entered ' + str (int (fail)) + '.')
            print ()
            checkFail ()
    except ValueError:
        print ('Enter a number ≥ 0.')
        print ()
        getFail ()

getFail ()

print ('----')
print ('Unweighted GPA: ' + str ((uw/numCounted)))
print ('Weighted GPA: ' + str ((w/numCounted)))
print ()
print ('Number of grades counted: ' + str (int (numCounted)))
print ('Number of grades in weighted courses counted: ' + str (int (weighted)))
print ('Number of grades below C- in weighted courses counted: ' + str (int (fail)))
print ('----')

