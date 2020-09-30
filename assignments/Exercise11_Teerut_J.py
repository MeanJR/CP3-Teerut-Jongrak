rowStar = int(input("Please input number of row :"))
numStar = ""
rePyramid = ""
for pyramid in range(rowStar):
    numStar += "*"
    rePyramid = (rowStar - pyramid)-1
    print(" "*rePyramid+numStar+"*"*pyramid)
