
def validate(tag):
    validTagSet = set(['INDI','NAME','SEX','BIRT','DEAT','FAMC','FAMS','FAM','MARR','HUSB','WIFE','CHIL','DIV','DATE','HEAD','TRLR','NOTE'])
    if tag in validTagSet:
        return tag
    else:
        return 'Invalid Tag'   
    
def parse(inputFile):
    gedcomFile = open(inputFile)
    output_file = open("AchanVedant_P02_Output.txt", 'w+')
    for line in gedcomFile:       
        #Output Line1: The Line being parsed 
        print >> output_file, line.strip()

        word = line.strip().split(' ')
        if word[0].isdigit():

            #Output Line2: Level of the line being parsed
            print >> output_file, word[0]

        #Output Line2: Tag of the line being parsed
        if int(word[0]) == 0:
            if '@' in word[1]:
                print >> output_file,(validate(word[2]))
            else:
                print >> output_file,(validate(word[1]))
        else:
            print >> output_file,(validate(word[1]))
        print >> output_file

if __name__ == "__main__":
    parse('AchanVedant_P02_Input.ged')
    print "'AchanVedant_P02_Output.txt' created in the same directory. Open to view the output."