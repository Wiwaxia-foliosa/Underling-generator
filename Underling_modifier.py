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
            self.playerList[name]=[]
            for grist in gristList:
                if gristList[grist]["player"]==name:
                    self.playerList[name].append(grist)
        for quality in qualities:
            self.qualityList[quality]=[]
            for grist in gristList:
                if gristList[grist]["quality"]==quality:
                    self.qualityList[quality].append(grist)
        print (self.playerList,self.qualityList, sep='\n')
##
##    def dropGrist(self, gristType, otherGrists):
##        nativeGrists=['build',gristType]
##        if otherGrists:
##            try:
##               nativeGrists=nativeGrists+otherGrists
##            except TypeError:
##                if type(otherGrists)is str:
##                    otherGrists=[otherGrists]
##                else:
##                    otherGrists=list(otherGrists)
##                nativeGrists=nativeGrists+otherGrists
##
##        print (nativeGrists)
##    
##        scaleFactor=round(self.dropWorth/10)
##        drops=0
##        #randomly vary exact size of dropWorth
##        if random.randint(0,1):
##            drops=self.dropWorth+random.randint(0,5)*scaleFactor
##        else:
##            drops=self.dropWorth-random.randint(0,5)*scaleFactor
##        while drops:
##            print(drops)
##            dropThis=random.randint(2, round(self.dropWorth*.6))
##            drops-=dropThis
##            #prevent overflow
##            if drops<0:
##                dropThis+=drops
##                drops=0
##            #randomly determines potential quality of drops
##            governor=random.randint(0,30)
##            if self.level>6 and governor < 2 and dropThis>50:
##                self.dropExotic(dropThis)
##            elif self.level>10 and governor < 4 and dropThis>50:
##                self.dropExotic(dropThis)
##            elif self.level>6 and dropThis>30 and governor<4:
##                self.dropGreat(dropThis)
##            elif self.level>6 and governor <8:
##                self.dropGood(dropThis)
##            elif self.level>1 and governor<10:
##                self.dropRelated(nativeGrists,dropThis)
##            elif drops>20 and governor<15:
##                self.dropHeal(dropThis)
##            elif self.level>4 and governor<15:
##                self.dropRandom(dropThis)
##            else:
##                self.dropNative(nativeGrists, dropThis)
##
##    def dropIt(self, grist, amount):
##        if grist=='build':
##            amount*=2
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


    
