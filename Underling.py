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

#we gonna be rolling a lot of virtual dice here
import random
#for default printout
import sys
#import the Grist and Prototyping classes and subclasses for easy access
from Grist import *
from Prototyping import *

class Underling:
    name = 'Underling'
    level=0
    #for printout purposes. ensure that this matches rollHd in subclasses
    hd='0d0'
    #minimum number of a type that can show up at once. should usually be 1
    numberOccurring=1

    gristList = Grist.getList()
    prototypingList=Prototyping.getList()
##    gristList = ('plush','dust','cobalt','mahogany','amber','bismuth',
##                 'cotton','loam','indigo','ebony','copper','phosphorus',
##                 'wool','sandstone','woad','ash','glass','rust',
##                 'polyester','clay','azurite','wax','magnetite','aluminum',
##                 'linen','cobble','lampblack','rosewood','vinyl','ink',
##                 'velvet','humus','turquoise','redwood','quartz','silver',
##                 'silk','opal','ultramarine','fiddleback','ferrofluid','fulgurite',
##                 'zillium','uranium','alkahest','quintessence','illiaster','orichalcum')
##    #assign sections of gristList to smaller tuples by rarity for use in drop methods
##    #ENSURE THAT THE LENGTH OF THESE SECTIONS IS MODIFIED TO MATCH ANY MODIFICATIONS TO gristList
##    associatedGrist=gristList[0:6]
##    commonGrist=gristList[6:18]
##    goodGrist=gristList[18:30]
##    greatGrist=gristList[30:36]
##    capstoneGrist=gristList[36:42]
##    exoticGrist=gristList[42:48]
##
##    prototypingList = ('nessie_fins','nessie_neck','racoon_skull','racoon_paws',
##                       'flag_standard','flag_castle','leopard_spots','leopard_face',
##                       'vine_leaves','vine_tendrils','onryou_hair','onryou_kimono',
##                       'character_eyes','character_garb')
##
    def types():
        subclasses=Underling.__subclasses__()
        underlingTypes = []
        for each in subclasses:
            each=str(each)
            discard, name = each.split(".")
            name, discard = name.split("'")
            underlingTypes.append(name)
        return underlingTypes
       
#
#           
#      HP ROLLING METHODS
#
#
    def rollHd(self):
        #this method is overridden in subclasses of Underling to roll the correct size HD (by mass)
        return 0

    def rollHp(self,lvl):
        while lvl:
            #roll hit dice and add to hp
            self.hp+=self.rollHd()
            lvl-=1

#
#
#       PROTOTYPING METHODS
#
#
    def auraSize(self):
        if self.level<=5:
            aura=1
        elif self.level<=9:
            aura=3
        else:
            aura=5
        return aura


    def basicDamage(self,string=True):
        if string:
            if self.level<=5:    
                die='1d4'
            elif self.level<=9:
                die='2d10'
            else:
                die= '3d8'
            return die
        else:
            if self.level<=5:    
                dice=1
                size=4
            elif self.level<=9:
                dice=1
                size=10
            else:
                dice=3
                size=8
            return dice,size

    def baseAttk(self):
        if self.level<3:
            attk=0
        elif self.level<5:
            attk=1
        elif self.level<7:
            attk=3
        elif self.level<10:
            attk=5
        elif self.level <12:
            attk=8
        elif self.level<14:
            attk=9
        else:
            attk=10
        return attk

    def modify(self,modifierObject):
        def error(want,field,modifierObject=modifierObject):
            return "Expected {} for {} in {}".format(str(want),str(field),str(type(modifierObject)))
        def integerFields(field,name):
            if field:
                if type(field) == int:
                    return field
                else:
                    raise TypeError(error(int,name))
            else:
                return 0
    
        
        self.hp += integerFields(modifierObject.addHp,'addHP')
        self.defence += integerFields(modifierObject.addDefence,'addDefence')
        self.protection += integerFields(modifierObject.addProtection,'addProtection')
        self.fortSave += integerFields(modifierObject.addFortSave,'addFortSave')
        self.refSave += integerFields(modifierObject.addRefSave,'addRefSave')
        self.willSave += integerFields(modifierObject.addWillSave,'addWillSave')
        self.speed += integerFields(modifierObject.addSpeed,'addSpeed')
        self.dropWorth += integerFields(modifierObject.addDropWorth,'addDropWorth')

##        def (self,field,expected,name):
##            if field:
##                if type(field)==int:
##                    self
        
        if modifierObject.addTactics:
            pass
        
        
        
        
        
            
            
            
    
##    #EDIT THIS
##    #
##    def addPrototypeSpells(self,prototyping):
##        if prototyping not in self.prototypingList:
##            prototyping= self.prototypingList[random.randint(0,len(self.prototypingList)-1)]
##    
    #EDIT THIS
    #
    def prototype(self,prototyping=''):
##        #prototyping variable will be defined in an if/else as random if !manual or user input if manual
##        #either way, test that protoyping is both valid and not done yet before moving on
##        if prototyping not in self.prototypingList:
##            prototyping= self.prototypingList[random.randint(0,len(self.prototypingList)-1)]
##        if prototyping not in self.prototypedWith:
##            #add to prototypedWith to prevent duplicate prototypings
##            self.prototypedWith.add(prototyping)
##
##            #if this underling type gets a spell from their first prototyping, determine spell and add
##            if self.prototypingSpells:
##                #ensure only the first prototyping grants a spell
##                self.prototypingSpells=False
##                self.addPrototypeSpells(prototyping)
        pass


    def callPrototyping(self,prototyping=''):
        #initialization calls placed in a function outside of __init__
        #so underlings that are prototyped abnormally can override this function instead of __init__

        #prototype with given prototyping, if any
        self.prototype(prototyping)
        self.prototype()
        
        #50% chance of third prototyping, 25% chance of fourth, etc.
        prototypingLoopGovernor=random.randint(0,1)
        #keep exploding prototyping loop from running indefinitely
        #adjust for number of prototypings possible!
        loopStop=10
        while prototypingLoopGovernor and loopStop:
            #add additional prototype
            self.prototype()
            #check if you will prototype again
            prototypingLoopGovernor=random.randint(0,1)
            #increment loopStop
            loopStop-=1

#
#
#       INITIALIZATION METHODS
#
#

    def incidental(self,number):
        self.special.add('50% chance of 1d'+str(number)+' incidental damage to everything adjacent.')

    def fillStats(self):
        #this method does nothing in Underling
        #subclasses of Underling override it to fill in the default values for that type of underling
        #so __init__ does not have to be overriden and risk unexpected errors
        #rolls HP
        #sets defence, protection, fortSave, refSave, willSave, speed (in meters/round), size, dropWorth
        #basic attacks, basic spells (if any), and special abilities common to the underling type to the appropriate lists/sets
        pass
    
    def sortTactics(self):
        tacticsAddendum=set()
        strongestTactics=[]
        priorityCounter=0
        for tacticsObject in self.tacticsBucket:
            if tacticsObject.priority==0:
                tacticsAddendum.add(tacticsObject)
            elif tacticsObject.priority>priorityCounter:
                #throw out all the previous content of lower priority
                strongestTactics=[tacticsObject]
                priorityCounter=tacticsObject.priority
            elif tacticsObject.priority==priorityCounter:
                #add tactics of equal priority to the list
                strongestTactics.append(tacticsObject)
        #multiple identical tactics from different sources are counted seperately
        #and are thus weighted heavier in random selection
        finalTactic=strongestTactics[random.randint(1,len(strongestTactics))-1]
        for each in tacticsAddendum:
            finalTactic+="\n"+each
        return finalTactic

        
    def printout(self,file=sys.stdout):
        file.write('{} {}\n'.format(self.adj.capitalize(),self.name.capitalize()))
        file.write('Speed: {}m/round   Size: {}\n'.format(self.speed,self.size))
        file.write('Defenses: {} HP  [{},{}]  Saves:({}f/{}r/{}w)\n'.format(self.hp,self.defence,self.protection,self.fortSave,self.refSave,self.willSave))
        file.write('Attacks: ')
        for each in self.attacks:
            file.write('({})'.format(each))
        if self.spells != []:
            file.write('\nSpells: ')
            for each in self.spells:
                file.write('- {}\n         '.format(each))
        file.write('\nSpecial: ')
        for each in self.special:
            file.write('- {}\n         '.format(each))
        if self.prototypedWith != set():
            file.write('\nPrototypings: {}\n'.format(self.prototypedWith))
        file.write('Tactics: - {}'.format(self.tactics))
        file.write('\nDrops: {}'.format( self.loot))
        file.write('\n\n\n')

    def __init__(self, descriptor, gristType, alsoDrops=None, prototyping=''):
        #create instance-specific stat variables
        self.adj=descriptor
        self.hp=0
        self.defence=0
        self.protection=0
        self.fortSave=0
        self.refSave=0
        self.willSave=0
        self.speed=0
        self.size=''
        self.tactics='Attack closest enemies or enemies that most recently attacked them. Like to bunch up and try to avoid entering chokepoints.\n           Will not pursue fleeing enemies unless very confident.\n           Do not ambush; generally mill around, destroy surroundings or wander aimlessly if not engaged.'

        #controls grist and health drops
        self.dropWorth=0
        #controls if prototypings add spells
        self.prototypingSpells=False
        
        #lists and sets to hold information about the underling
        self.attacks=[]
        self.spells=[]
        self.special=set()
        self.loot=[]
        #used to hold the possible tactics of this underling
        #self.sortTactics() is then used to apply the order of precedence and write the final tactics in self.tactics
        self.tacticsBucket=[]
        #used to ensure an underling is not prototyped with the same thing twice
        self.prototypedWith=set()

        #call functions to fill stats and descriptive lists with appropriate values
        
        #this method is overridden in Underling subclasses
        #to populate the above variables with the default values for the type of underling
        #so __init__ can be used as inherited
        self.fillStats()
        #call the prototype method an appropriate amount of times
        #this method may be overridden in Underling subclasses that are prototyped abnormally
        self.callPrototyping(prototyping)
        
        #ensure that grist is of a valid type
        gristType=gristType.capitalize().strip()
        while(gristType not in self.gristList):
              #if grist is invalid, prompt for replacement
              print('Invalid grist type. Enter grist type or enter 'r' for random. /n')
              #get and format input
              gristType = input('> ').lower().strip()
              if gristType == 'r':
                  #pick a random grist type from gristList
                  gristType = random.sample(self.gristList,1)
                  
        gristObject=gristList[gristType]["class"](self.level)
        self.modify(gristObject)
        self.loot=gristObject.dropGrist(self.dropWorth,otherGrists=alsoDrops)
        if self.tacticsBucket:
            self.sortTactics()
##        #move this call to main once troubleshooting is done
##        self.printout(sys.stdout)
