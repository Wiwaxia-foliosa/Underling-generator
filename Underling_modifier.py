import random

class Underling_modifier:
    """Create an object containing values to be used to modify an Underling object."""
    #these values will be accessed by an Underling object and used to modify the corresponding state variable within it
    #if any new variables are added here, be sure to modify Underling.modify to handle them
    addHp=None
    addDefence=None
    addProtection=None
    addFortSave=None
    addRefSave=None
    addWillSave=None
    addSpeed=None
    addMoveType=None
    addSize=None
    addTactics=None
    addDropWorth=None
    addAttacks=None
    addSpells=None
    addSpecial=None
    addLoot=None

    #The following methods define default values that can be used in ablities granted by
    #grist or prototypings, based on the level of the Underling (expected to be from 1 to 14)
    def auraSize(self, level):
        """Return an integer representing radius in meters.

        Keyword Arguments:
        level -- The level of an Underling. Determines the value returned. expected to be from 1 to 14
        """
        if level<=5:
            aura=1
        elif level<=9:
            aura=3
        else:
            aura=5
        return aura


    def basicDamage(self, level, string=True):
        """Return a string or pair of integers representing the dammage of an attack
        Keyword Arguments:
        level -- The level of an Underling. Determines the value returned. expected to be from 1 to 14
        string -- Determines whether a string or pair of integers is returned (Default: True)
        """ 
        if string:
            if level<=5:    
                die='1d4'
            elif level<=9:
                die='2d10'
            else:
                die= '3d8'
            return die
        else:
            if level<=5:    
                dice=1
                size=4
            elif level<=9:
                dice=1
                size=10
            else:
                dice=3
                size=8
            return dice,size

    def baseAttk(self, level):
        """Return an integer representing the attack bonus of an attack.

       Keyword Arguments:
       level -- The level of an Underling. Determines the value returned. expected to be from 1 to 14
       """
        if level<3:
            attk=0
        elif level<5:
            attk=1
        elif level<7:
            attk=3
        elif level<10:
            attk=5
        elif level <12:
            attk=8
        elif level<14:
            attk=9
        else:
            attk=10
        return attk

    def modifiers(self):
        #this class does nothing in Underling_modifier
        #it is overridden in subclasses to allow subclass-specific initialization details
        #without overriding __init__
        pass

    def __init__ (self, level):
        self.level=level
        self.modifiers()


class Tactics:
    """Contain a description of tatcics and a priority relative to other Tactics objects.
    

    """
    def __init__(self,description,priority):
        """Initialize self.

        Keyword arguments:
        description -- the description of tactics
        priority -- an int from 1 to 7. The Tatics object with the highest priority will be used.
        0 is a special case: description will be added as an addendum to the description of another Tactics object"""
        self.description=description
        if priority < 0 or priority > 7:
            raise ValueError('Out of bounds.')
        else:
            self.priority =priority

class Prototyping(Underling_modifier):
    "Contain methods concerning all Prototyping subclasses"

    def getList():
        """ Return a dictionary of the subclasses of Prototyping, keyed by name."""
        subclasses=Prototyping.__subclasses__()
        prototypingList = {}
        for each in subclasses:
            name=str(each)
            discard, name = name.split(".")
            name, discard = name.split("'")
            prototypingList[name]=each
        return prototypingList
    
    def random(create=True):
        """Select a random subclass of Prototyping.

        Keyword Arguments:
        create -- determine if an instance of the subclass will be created and returned (Default: True)"""
        subclasses=Prototyping.__subclasses__()
        choose=subclasses[random.randint(1,len(subclasses))]
        if create:
            prototypingObject=choose()
            return prototypingObject
        else:
            return choose

class Grist(Underling_modifier):
    "Contain methods concerning all Grist subclasses"

    def getList():
        """ Return a dictionary of the subclasses of Grist, and their orgaizational information, keyed by name."""
        subclasses=Grist.__subclasses__()
        gristList = {}
        for each in subclasses:
            name=str(each)
            discard, name = name.split(".")
            name, discard = name.split("'")
            gristList[name]={"player":each.player,"quality":each.quality,"class":each}
        return gristList
    
    def organize(self):
        """Create two dictionaries of Grist subclass names organized by player and quality.

        Used primarily for dropGrist and associated methods controlling underling loot.
        Could also provide a base for implementing a programmatic generator for underling_encounter_table.csv
        """
        
        gristList=Grist.getList()
        names=set()
        qualities=set()
        self.qualityList={}
        self.playerList={}
        for key in gristList:
            names.add(gristList[key]["player"])
            qualities.add(gristList[key]["quality"])
        for name in names:
            self.playerList[name]=dict()
            for grist in gristList:
                if gristList[grist]["player"]==name:
                    self.playerList[name][grist]=gristList[grist]["class"]
        for quality in qualities:
            self.qualityList[quality]=dict()
            for grist in gristList:
                if gristList[grist]["quality"]==quality:
                    self.qualityList[quality][grist]=gristList[grist]["class"]
#remove after testing
        print (self.playerList,self.qualityList, sep='\n')

    def dropGrist(self,dropWorth,gristType=None,otherGrists=None):
        dropList=[]
        if not gristType:
            gristType=self.__class__.__name__
        nativeGrists=['Build',gristType]
        if otherGrists:
            try:
               nativeGrists=nativeGrists+otherGrists
            except TypeError:
                if type(otherGrists)is str:
                    otherGrists=[otherGrists]
                else:
                    otherGrists=list(otherGrists)
                nativeGrists=nativeGrists+otherGrists

#remove after testing
        print (nativeGrists)

        def dropLoot(quality, amount, nativeGrists=nativeGrists, self=self):
            typeDropped=None
            gristList=Grist.getList()
            #a list of the rarest grists selected when quality is "exotic", which have no underlings with them as their native grist under normal circumstances
            exoticGrists=["Zillium","Uranium","Alkahest","Quintessence","Illiaster","Orichalcum"] 
            #modified by quality of grist to force better grist drops to be smaller

#remove after testing
            print(player)
            scaleFactor=1
            if quality in self.qualityList:
                typeDropped=random.sample(list(self.qualityList[quality].keys()),1)
            elif quality == "exotic":
                typeDropped=exoticGrists[random.randint(1,len(exoticGrists))-1]
            elif quality == "related":
                randomNativeGrist=nativeGrists[random.randint(1,len(nativeGrists)-1)] #not an off by one error on the randint range, deliberately excluding "Build" as nativeGrists[0]
                selectedQuality=gristList[randomNativeGrist]["quality"]
                selctedPlayer=gristList[randomNativeGrist]["player"]
                validQualities=None
                if selectedQuality == "great" or selectedQuality == "capstone":
                    validQualities == ["good","great","capstone"]
                elif selectedQuality == "good":
                    validQualities=["common","good","great"]
                else:
                    validQualities=["associated","common","good"]
                possibleTypes=[]
                for eachGrist in self.playerList[selectedPlayer]:
                    if eachGrist.quality in validQualities:
                        possibleTypes.append(eachGrist.__class__.__name__)
                typeDropped=possibleTypes[random.randint(1,len(possibleTypes))-1]
            elif quality == "random":
                typeDropped=random.sample(gristList.keys(),1)
            #if dropping "heal" the result is formatted differently, and returned directly out of the elif block
            #rather than bothering with scale factor and formatting at the end of the method
            elif quality == "heal":
                healingAmount="1"
                if amount<50:
                    healingAmount="1d6"
                elif amount<100:
                    healingAmount="2d6"
                elif amount<500:
                    healingAmount="4d4"
##                elif amount<1000:
##                    healingAmount=
##                elif amount<5000:
##                    healingAmount=
##                elif amount<10000:
##                    healingAmount=
                else:
                    return "healing gel flower for full restoration"
                return "healing gel cube for {}".format(healingAmount)

            else:
                typeDropped=nativeGrists[random.randint(1,len(nativeGrists))-1]

            if typeDropped == "Build":
                scaleFactor=2
            elif typeDropped in self.qualityList["associated"] or typeDropped in self.qualityList["common"]:
                scaleFactor=1
            elif typeDropped in self.qualityList["good"]:
                scaleFactor=0.8
            elif typeDropped in self.qualityList["great"]:
                scaleFactor=0.5
            elif typeDropped in self.qualityList["capstone"]:
                scaleFactor=0.1
            else:
                scaleFactor=0.01

            finalAmount=round(amount*scaleFactor)

            #gurantee at least 1 unit of grist, or two units for the best grists
            if finalAmount<2 and (typeDropped in exoticGrists or typeDropped in self.qualityList["capstone"]):
                finalAmount=2
            elif finalAmount<1:
                finalAmount=1

            return "{} {} Grist".format(finalAmount,typeDropped)
              

            
        #vary the actual amount dropped between 0.5 and 1.5 of dropWorth
        scaleFactor=round(dropWorth/10)
        #variabilityFactor is in terms of multiples of scaleFactor
        varibilityFactor=5
        dropsRemaining=0
        if random.randint(0,1):
            dropsRemaining=dropWorth+random.randint(0,variabilityFactor)*scaleFactor
        else:
            dropsRemaining=dropWorth-random.randint(0,variabilityFactor)*scaleFactor
        while dropsRemaining:

#remove after testing
            print(dropsRemaining)
            #determine a random amount up to 60% of the total dropWorth to put into a single loot drop
            individualDrop=random.randint(2, round(dropWorth*.6))
            #subtract the amount going into this loot drop from drops for the next loop
            dropsRemaining-=individualDrop
            #prevent dropping more loot than is in drops
            if dropsRemaining<0:
                individualDrop+=dropsRemaining
                dropsRemaining=0
            #determine potential quality of drops based on a random roll, the level of the Grist object, and the amount in a given drop
            governorRange=30
            governor=random.randint(0,governorRange)
            #the random results table decreases in quality with increasing random integers
            #if the generator rolls low, but additional conditions for that result are not met, the next best result is used, and so on

            
            #if the Grist object is level 7 or above and drop worth is greater than 50, there is a 1 in 30 chance of dropping the rarest grists
            if self.level>6 and governor < 2 and individualDrop>50:
                dropList.append(dropLoot("exotic",individualDrop))

            #if the Grist object is level 11 or above, the chance of dropping the rarest grist increases to 3 in 30
            elif self.level>10 and governor < 4 and individualDrop>50:
                dropList.append(dropLoot("exotic",individualDrop))
                
            #if the Grist level is too low to get exotic grist but still above 4, get capstone grist instead
            elif self.level>4 and governor < 2 and individualDrop>30:
                dropList.append(dropLoot("capstone",individualDrop))
                
            elif self.level>6 and governor < 3 and individualDrop>30:
                dropList.append(dropLoot("capstone",individualDrop))
                
            elif self.level>10 and governor < 5 and individualDrop>30:
                dropList.append(dropLoot("capstone",individualDrop))
                
            elif self.level>6 and governor<6 and individualDrop>30:
                dropList.append(dropLoot("great",individualDrop))
                
            elif self.level>6 and governor <8:
                dropList.append(dropLoot("good",individualDrop))
                
            #if the Grist object is level 1, only healing and native grists may be dropped
            elif self.level>1 and governor<11:
                dropList.append(dropLoot("related",individualDrop))
                
            #totally random grist drops are only avaliable for small quantities dropped, larger quantities will give healing instead
            elif individualDrop>20 and governor<16:
                dropList.append(dropLoot("heal",individualDrop))
                
            elif self.level>4 and governor<16:
                dropList.append(dropLoot("random",individualDrop))
                
            #for all levels, there is at least a flat 50% chance that the drop will be of a native grist type
            else:
                dropList.append(dropLoot("native",individualDrop))

            return dropList
##
## Deprecating
##
##    def dropIt(self, grist, amount):
##        if grist=='build':
#            amount*=2
##        elif grist in self.associatedGrist:
##            pass
##        elif grist in self.commonGrist:
##            pass
##        elif grist in self.goodGrist:
##            amount-=10
##            if amount<2:
##                amount=2
##
##        elif grist in self.greatGrist:
##            amount=amount//2
##            if not amount:
##                amount=2
##
##        elif grist in self.capstoneGrist:
##            amount=amount//10
##            if not amount:
##                amount=2
##
##        elif grist in self.exoticGrist:
##            amount= amount//100+1
##
##
##        self.loot.append(str(amount)+' '+grist+' grist')
##        
##    def dropNative(self, nativeGrists, amount):
##        choose=random.randint(0,len(nativeGrists)-1)
##        self.dropIt(nativeGrists[choose],amount)
##
##    def dropHeal(self, amount):
##        if amount<50:
##            self.loot.append('healing gel for 1d6')
##        elif amount<100:
##            self.loot.append('healing gel for 2d6')
##        else:
##            self.loot.append('healing gel for 4d4')
##
##    def dropRelated(self, grists, amount):
##        refGrist=grists[random.randint(1,len(grists)-1)]
##        reference = self.gristList.index(refGrist)
##        if random.randint(0,1):
##            newIndex=reference-6*random.randint(1,2)
##            if newIndex<0:
##                newIndex=reference-6
##                if newIndex<0:
##                    newIndex=reference
##        else:
##            newIndex=reference+6*random.randint(1,2)
##            if newIndex>41:
##                newIndex=reference+6
##                if newIndex>41:
##                    newIndex=reference
##        newGrist=self.gristList[newIndex]
##        self.dropIt(newGrist, amount)
##
##    def dropRandom(self, amount):
##        grist=self.gristList[random.randint(0,41)]
##        self.dropIt(grist,amount)
##
##    def dropGood(self, amount):
##        grist=self.goodGrist[random.randint(0,11)]
##        self.dropIt(grist,amount)
##
##    def dropGreat(self, amount):
##        if not random.randint(0,5):
##            grist=self.capstoneGrist[random.randint(0,5)]
##        else:
##            grist=self.greatGrist[random.randint(0,5)]
##        self.dropIt(grist,amount)
##
##    def dropExotic(self,amount):
##        grist=self.exoticGrist[random.randint(0,5)]
##        self.dropIt(grist,amount)


    
