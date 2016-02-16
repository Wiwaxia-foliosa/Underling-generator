# If you want to modify this generator for a different SBURB session:
#    - rewrite the gristList and prototypingList lists in the Underling class
#    - rewrite the addPrototypeSpells, prototype and getGrist functions to apply the effects of your new prototypings and grists
#    - ensure that any new tactics labels are added to tacticsBucket by prototype or getGrist, are checked for by sortTactics
#         in approptiate order of priotity and have an appropriate description inserted into tactics by sortTactics
#
#
# If you want to add new Underling types/subclasses:
#    - assign name and level appropriate values
#    - override rollHd with the correct size of die/dice to roll for hp per level
#    - override fillStats to assign the default values for your new Underling type to the fields created in __init__
#    - if your new Underling type is prototyped abnormally, override callPrototyping
#    - ensure that any new tactics labels are added to tacticsBucket by prototype or getGrist, are checked for by sortTactics
#         in approptiate order of priotity and have an appropriate description inserted into tactics by sortTactics
#    - DO NOT override __init__

from Underling_types import *
import random
import sys
        

def getInt(input_string,prompt_message,error_message="Please enter an integer value in the appropriate range",minimum=0,maximum=None,reprompt=True):
    value=None
    #allow 'no maximum value' as default
    def inRange(arg):
        try:
            bool_result = minimum<arg<maximum
        except TypeError:
            bool_result = minimum<arg
        return bool_result

    #continue to query user for input until told to quit or given a valid value
    if reprompt:
        try:
            value=int(input_string)
        except ValueError:
            value=None
        except TypeError:
            value=None

        while not type(value) is int or not inRange(value):
            #report error
            print (error_message)
            #prompt for new input string
            input_string=input(prompt_message+"\n'q' to quit\n > ").strip().lower()
            if input_string == 'q':
                print('quitting... \n')
                return
            elif input_string.isdigit():
                value = int(input_string)

    #just raise an exception if given an invalid value    
    else:
        if inRange(int(input_string)):
            value = int(input_string)
        else:
            raise ValueError ("Converted value is outside specified range")
    return value
           
def makeEncounterTable(filename):
    import collections
    encounter_table= collections.defaultdict(dict)
    with open(filename, 'r') as input_file:
        for line in input_file:
            land,underling_name,underling_type,grist = line.split(",")
            #ensure input strings are properly formatted
            land=land.strip().upper()
            underling_name=underling_name.strip().capitalize()
            underling_type=underling_type.strip().capitalize()            
            #pass over empty or irrelevant lines in the input file
            if land == '0' and grist.strip()== '0':
                pass
            elif underling_type not in Underling.types():
                raise ValueError( underling_type+" not a valid subclass of underling.")
            else:
                level=eval(underling_type).level
                gristTypes=grist.split('/')
                for i in range(0,len(gristTypes)):
                    gristTypes[i]=gristTypes[i].lower().strip()
                    if gristTypes[i] not in Underling.gristList:
                        raise ValueError (grist+" not found in gristList.")
                encounter_table[land][underling_name+' '+underling_type]= {'name':underling_name, 'level':level,'type': underling_type, 'grist': gristTypes}
    return encounter_table

def rollEncounterTable(table,land,key,value):
    if land=="DERSE":
        landList= []
        for each in table.keys():
            landList.append(each)
        land=landList[random.randint(0,len(landList)-1)]
        
    possible_results=[]
    for each in table[land]:
        if table[land][each][key]==value:
            possible_results.append(table[land][each])
            
    return possible_results[random.randint(0,len(possible_results)-1)]

def buildEncounter(table,land,totalHd=0,maxHd=0):
    #input and error checking
    if type(totalHd) is not int or totalHd <= 0:
        totalHd=getInt(totalHd,"What is the total level or HD of the encounter?",'Please enter a positive integer value',0,100)
    #quit this function if getInt was quit
    if totalHd==None:
        return
    if type(maxHd) is not int or maxHd <= 0:
        maxHd=getInt(maxHd,"What is the maximum level or HD of any single Underling?",'Please enter a positive integer value')
    #quit this function if getInt was quit
    if maxHd==None:
        return
    #ensure that the maximum possible hd does not exceed the highest level of availiable Underling
    levelCap=0
    for each in Underling.__subclasses__():
        if each.level > levelCap:
            levelCap=each.level
    maxHd=min(levelCap,int(maxHd))

    encounter_list=[]
    #ensure that loop never runs forever
    governor = 200
    while totalHd>0 and governor:
        governor-=1
        grabHd=random.randint(1,min(totalHd,maxHd))
        try:
            result=rollEncounterTable(table,land,"level",grabHd)
            number=eval(result['type']).numberOccurring
            if number-1>encounter_list.count(result):
                grabHd=grabHd*number
                result=[result]
                for i in range(number-1):
                    result.append(result[0])
            #ensure that the produced underlings do not overbudget totalHd
            if totalHd-grabHd>=0:
                totalHd-=grabHd
                encounter_list.append(result)
        except ValueError:
            #if getHd rolls a value for which there are zero options, keep calm and roll again
            pass
        
    return encounter_list


def main():
    input_filename = 'underling_encounter_table.csv'
    encounterTable = makeEncounterTable(input_filename)
    landList= []
    for each in encounterTable.keys():
        landList.append(each)
    underlingTypes=Underling.types()
    encounter=[]

    land=0
    while land not in landList:
        land = input("What land?\npress 'o' for a list of options or 'q' to quit\n > ").strip().upper()
        if land in landList:
            pass
        elif land == "DERSE":
            break
        elif land == 'O':
            print (landList+["DERSE"])
        elif land == 'Q':
            print('quiting... \n')
            return
        else:
            print ('Unrecognized')
        
    whatUnderling=''    
    
    while whatUnderling not in underlingTypes:
        whatUnderling= input("what kind of underling? enter 'r' for a random assortment.\n press 'o' for a list of options or 'q' to quit\n > ").strip().capitalize()
        if whatUnderling=='Random' or whatUnderling=='R':
            encounter=buildEncounter(encounterTable,land)
            break
        elif whatUnderling in underlingTypes:
            count=input('How many? \n > ')
            count=getInt(count,'How many Underlings?','Please enter a positive integer below 100',minimum=0,maximum=100)

            while count:
                encounter.append(rollEncounterTable(encounterTable,land,"type",whatUnderling))
                count-=1
            prompt=input("any other types of underling? y/n\n > ").lower().strip()
            if prompt in ["y","yes","yep"]:
                whatUnderling=''
            else:
                break
        elif whatUnderling == 'O':
            print (underlingTypes)
        elif whatUnderling == 'Q':
            print ('quitting... \n')
            return
        else:
            print ('Unrecognized')
            
            
    


    file=sys.stdout
    output = input('Where should the results be printed? \n Press \'e\' to print to Encounter.txt, \'o\' to print elsewhere, or any other key to print to the shell.\n').strip().capitalize()
    if output=='E':
        file=open('Encounter.txt',mode='w')
    elif output=='O':
        filename=input('Write name of file: >')
        if filename[-4:]!='.txt':
            filename=filename+'.txt'
        file=open(filename, mode='w')

    for each in encounter:
        underling_type=eval(each['type'])
        name=each['name']
        grist = each['grist'][0]
        alsoDrops=each['grist'][1:]
        make=underling_type(name,grist,alsoDrops)#,prototyping)
        make.printout(file)
        

main()
