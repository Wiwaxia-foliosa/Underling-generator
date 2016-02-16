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

class Underling:
    name = 'Underling'
    level=0
    #for printout purposes. ensure that this matches rollHd in subclasses
    hd='0d0'
    #minimum number of a type that can show up at once. should usually be 1
    numberOccurring=1
    gristList = ('plush','dust','cobalt','mahogany','amber','bismuth',
                 'cotton','loam','indigo','ebony','copper','phosphorus',
                 'wool','sandstone','woad','ash','glass','rust',
                 'polyester','clay','azurite','wax','magnetite','aluminum',
                 'linen','cobble','lampblack','rosewood','vinyl','ink',
                 'velvet','humus','turquoise','redwood','quartz','silver',
                 'silk','opal','ultramarine','fiddleback','ferrofluid','fulgurite',
                 'zillium','uranium','alkahest','quintessence','illiaster','orichalcum')
    #assign sections of gristList to smaller tuples by rarity for use in drop methods
    #ENSURE THAT THE LENGTH OF THESE SECTIONS IS MODIFIED TO MATCH ANY MODIFICATIONS TO gristList
    associatedGrist=gristList[0:6]
    commonGrist=gristList[6:18]
    goodGrist=gristList[18:30]
    greatGrist=gristList[30:36]
    capstoneGrist=gristList[36:42]
    exoticGrist=gristList[42:48]

    prototypingList = ('nessie_fins','nessie_neck','racoon_skull','racoon_paws',
                       'flag_standard','flag_castle','leopard_spots','leopard_face',
                       'vine_leaves','vine_tendrils','onryou_hair','onryou_kimono',
                       'character_eyes','character_garb')

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
                die=''
            else:
                die= ''
            return die
        else:
            if self.level<=5:    
                dice=1
                size=4
            elif self.level<=9:
                dice=0
                size=0
            else:
                dice=0
                size=0
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
        
    
    #EDIT THIS
    #
    def addPrototypeSpells(self,prototyping):
        pass
    
    #EDIT THIS
    #
    def prototype(self,prototyping=''):
        if prototyping not in self.prototypingList:
            #IF YOU ARE EDITING ENSURE THAT THE RANGE OF THE RANDOM NUMBER GENERATED MATCHES THE LENGTH OF prototypingList
            prototyping= self.prototypingList[random.randint(0,len(self.prototypingList)-1)]
        if prototyping in self.prototypedWith:
            return
        else:
            #add to prototypedWith to prevent duplicate prototypings
            self.prototypedWith.add(prototyping)

            #if this underling type gets a spell from their first prototyping, determine spell and add
            if self.prototypingSpells:
                #ensure only the first prototyping grants a spell
                self.prototypingSpells=False
                self.addPrototypeSpells(prototyping)
            
            #nessie fins --> can swim
            if prototyping == self.prototypingList[0]:
                self.special.add('Swim speed')
            #nessie long neck --> 
            elif prototyping == self.prototypingList[1]:
                self.special.add('Can make bite atacks at an extra meter reach.')
                self.attacks.append('1 bite, +'+str(self.baseAttk())+', '+self.basicDamage())
            #raccoon skull --> opportunity attacks
            elif prototyping == self.prototypingList[2]:
                self.special.add('Gets immediate free attack on opponents moving away.')
            #racoon paws --> can climb
            elif prototyping == self.prototypingList[3]:
                self.special.add('Climb speed equal to normal speed, needs no checks to climb.')
            #standard bearer --> aids nearby Underlings
            elif prototyping == self.prototypingList[4]:
                aura=self.auraSize()
                heal=self.basicDamage()
                self.special.add('Underlings within '+str(aura)+' meters get a +1 bonus to all rolls and heal '+heal+' HP per round')
            #castle blazon --> gets bonus protection when remaining still
            elif prototyping == self.prototypingList[5]:
                if self.level<=7:
                    bonus=2
                else:
                    bonus=4
                self.special.add('Gets '+str(bonus)+' bonus protection if it didn\'t move last round and doesn\'t move this round.')
            #leopard spots --> pounce to grapple w/out provoking attack,
            #can leap over things from standstill, ambush predator tactics
            elif prototyping == self.prototypingList[6]:
                self.special.add('Can pounce onto targets. (charge attack, immediate grapple on hit, defender does not get a free attack)')
                self.special.add('Can leap from standstill')
                self.tacticsBucket.add('ambush_predator')
            #leopard head --> grants bite attack that grapples on very sucessful hits, ambush predator tactics
            elif prototyping == self.prototypingList[7]:
                attk=self.baseAttk()+1
                self.attacks.append('1 bite, +'+str(attk)+', '+str(self.level)+'d2')
                self.special.add('Grapples target if bite attack beats their defence by 5 or more.\n           If target is smaller, they are picked up in mouth.')
                self.tacticsBucket.add('ambush_predator')
            #vine leaves -->
            elif prototyping == self.prototypingList[8]:
                self.special.add('Can heal '+self.basicDamage()+'+'+str(self.level)+' health as a standard action if standing or swimming in water.')
            #vine tendrils -->
            elif prototyping == self.prototypingList[9]:
                self.special.add('Attackers that miss by five or more get their weapon tangled in vines and overgrown. \n           They can pull it out next turn with a str check, then it is lost until the underling is defeated.')
            #onryou long stringy hair --> reappears in front of you if you try to flee, undead tactics
            elif prototyping == self.prototypingList[10]:
                self.special.add('Reappears in front of you 1d4 rounds later if you try to flee from it')
                self.tacticsBucket.add('undead')
            #onryou burial kimono --> causes misfortune and damage to all around it
            elif prototyping == self.prototypingList[11]:
                aura=self.auraSize()
                damage=self.basicDamage()
                if self.level>8:
                    extra=', and must roll all dice twice and take the worse'
                else:
                    extra=''
                self.special.add('All within '+str(aura)+' meters, friend and foe alike, take '+damage+' damage on this Underling\'s turn'+extra+'.\n           The Fears of LOFAC and other underlings with an onryou prototyping are unaffected.')
                self.tacticsBucket.add('undead')
            #arashi matsuri doll four red eyes --> shapeshifting
            elif prototyping == self.prototypingList[12]:
                self.special.add('Can shapeshift at will to appear as other underlings/creatures.\n           Size and shape changes, but stats do not (including hp and ability to grapple).')
            #arashi matsuri doll clothes and flaxen braid --> smart tactics
            elif prototyping == self.prototypingList[13]:
                self.tacticsBucket.add('smart')

    def callPrototyping(self,prototyping=''):
        #initialization calls placed in a function outside of __init__
        #so underlings that are prototyped abnormally can override this function instead of __init__

        #prototype with given prototyping, if any
        self.prototype(prototyping)
        self.prototype()
        
        #50% chance of third prototyping, 25% chance of fourth, etc.
        prototypingLoopGovernor=random.randint(0,1)
        #keep exploding prototyping loop from running indefinitely
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
#       GRIST METHODS
#
#

    #EDIT THIS
    #
    def getGrist(self, grist):            
        #find what type of grist gristType is and apply proper modifiers

        #plush
        if grist == self.gristList[0]:
            #bonus protection, but thrown around by attacks
            self.protection+=1
            self.special.add('Flies back 1m whenever hit')

        #dust
        elif grist == self.gristList[1]:
            #speedy
            self.speed+=2

        #cobalt
        elif grist == self.gristList[2]:
            #gives bonus HP
            self.hp+=(+1)*2

        #mahogany
        elif grist == self.gristList[3]:
            #bonus def, but flees in the face of flame
            self.defence+=1
            self.special.add('Flees if it has a candle brandished at it or if it is damaged by fire')

        #amber
        elif grist == self.gristList[4]:
            a,b=self.basicDamage(False)
            self.special.add('If it moved last turn, deals '+str(a)+'d'+str(b//2)+' damage to the first thing to hit it with a conductive weapon')
        
        #bismuth
        elif grist == self.gristList[5]:
            self.special.add('Is pushed 1m away from any electric attack or discharge within 3m, before attack resolves')

        #cotton
        elif grist == self.gristList[6]:
            print('fix')
            
        #loam
        elif grist == self.gristList[7]:
            self.special.add('Can teleport in water')

        #indigo
        elif grist == self.gristList[8]:
            self.special.add('Stain everything they touch blue. Other indigo underlings will follow their tracks.')

        #ebony
        elif grist == self.gristList[9]:
            self.special.add('Creates darkness within '+ str(self.auraSize())+ ' meters.')

        #copper
        elif grist == self.gristList[10]:
            self.special.add('Takes double damage from electricity and fire, deals '+str(self.basicDamage())+' damage to everything adjacent')

        #phosphorous
        elif grist == self.gristList[11]:
            self.special.add('Explodes violently when killed, dealing '+ str(self.basicDamage())+ 'damage to all within ' + str(self.auraSize())+ ' meters.')

        #wool
        elif grist == self.gristList[12]:
            self.special.add('Resist 5 to fire, water, cold.')

        #sandstone
        elif grist == self.gristList[13]:
            #more resilient
            self.protection+=1
            self.defence+=1

        #woad
        elif grist == self.gristList[14]:
            a,b=self.basicDamage(False)
            self.special.add('Can swim, but loses the ability permanently when it emerges from water')
            self.special.add('The first time it emerges from water, it turns from yellow to blue and regains'+str(2*a)+'d'+str(b)+' health.')

        #ash
        elif grist == self.gristList[15]:
            self.special.add('Healed by fire. Will attempt to ignite self and others.')

        #glass
        elif grist == self.gristList[16]:
            self.special.add('Leave a pile of glass shards where they die. Deals 1d4 damage per m to anything walking over it.')

        #rust
        elif grist == self.gristList[17]:
            self.special.add('Leaves a trail of rust as it walks. Attacks do '+str(self.basicDamage())+' ongoing damage (spindown, take # rolled in damage each time)')

##        #brass
##        elif grist == self.gristList[18]:
##            self.special.add('Rings loudly when struck. This has a 1 in 6 chance of calling more underlings.')

        #polyester
        elif grist == self.gristList[18]:
            print('fix')

        #clay
        elif grist == self.gristList[19]:
            self.special.add('Can squeeze to fit through spaces as small as half their size.')

        #azurite
        elif grist == self.gristList[20]:
            print('fix')

        #wax
        elif grist == self.gristList[21]:
            self.special.add('Ignites if damaged by fire.\n           Takes 1d6 damage a round, all attacks deal fire damage, and casts light within '+ str(self.auraSize())+ ' meters.')

        #magnetite
        elif grist == self.gristList[22]:
            self.special.add('If there are metal objects around, has a 1 in 6 chance per turn of attracting one to itself as armor.\n           Each peice of armor gained this way gives it 1 additional protection. If a sharp object is attracted, it also takes 1d6 damage.')

        #aluminum
        elif grist == self.gristList[23]:
            self.defence+=1
            self.special.add('If it can swim, it can swim through clouds as if they were water.')

        #linen
        elif grist == self.gristList[24]:
            print('Glide speed equal to speed, must descend.')

        #cobble
        elif grist == self.gristList[25]:
            self.special.add('Deals 1 extra damage on all attacks.')
            self.loot.append('healing gel for '+str(self.basicDamage()))

        #lamp-black
        elif grist == self.gristList[26]:
            print('fix')

        #rosewood
        elif grist == self.gristList[27]:
            print('fix')

        #vinyl
        elif grist == self.gristList[28]:
            print('fix')

        #ink
        elif grist == self.gristList[29]:
            print('fix')

        #velvet
        elif grist == self.gristList[30]:
            self.special.add('Quiets sound within '+str(auraSiza())+'m. Makes it difficult to hear and nullifies magic song.')

        #humus
        elif grist == self.gristList[31]:
            print('fix')

        #turquoise
        elif grist == self.gristList[32]:
            print('fix')

        #redwood
        elif grist == self.gristList[33]:
            print('fix')

        #quartz
        elif grist == self.gristList[34]:
            print('fix')

        #silver
        elif grist == self.gristList[35]:
            print('fix')

        #silk
        elif grist == self.gristList[36]:
            print('fix')

        #opal
        elif grist == self.gristList[37]:
            print('fix')

        #ultramarine
        elif grist == self.gristList[38]:
            print('fix')

        #fiddleback
        elif grist == self.gristList[39]:
            print('fix')

        #ferrofluid
        elif grist == self.gristList[40]:
            print('fix')

        #fulgurite
        elif grist == self.gristList[41]:
            print('fix')


    def dropGrist(self, gristType, otherGrists):
        nativeGrists=['build',gristType]
        if otherGrists:
            try:
               nativeGrists=nativeGrists+otherGrists
            except TypeError:
                if type(otherGrists)is str:
                    otherGrists=[otherGrists]
                else:
                    otherGrists=list(otherGrists)
                nativeGrists=nativeGrists+otherGrists

        print (nativeGrists)
    
        scaleFactor=round(self.dropWorth/10)
        drops=0
        #randomly vary exact size of dropWorth
        if random.randint(0,1):
            drops=self.dropWorth+random.randint(0,5)*scaleFactor
        else:
            drops=self.dropWorth-random.randint(0,5)*scaleFactor
        while drops:
            print(drops)
            dropThis=random.randint(2, round(self.dropWorth*.6))
            drops-=dropThis
            #prevent overflow
            if drops<0:
                dropThis+=drops
                drops=0
            #randomly determines potential quality of drops
            governor=random.randint(0,30)
            if self.level>6 and governor < 2 and dropThis>50:
                self.dropExotic(dropThis)
            elif self.level>10 and governor < 4 and dropThis>50:
                self.dropExotic(dropThis)
            elif self.level>6 and dropThis>30 and governor<4:
                self.dropGreat(dropThis)
            elif self.level>6 and governor <8:
                self.dropGood(dropThis)
            elif self.level>1 and governor<10:
                self.dropRelated(nativeGrists,dropThis)
            elif drops>20 and governor<15:
                self.dropHeal(dropThis)
            elif self.level>4 and governor<15:
                self.dropRandom(dropThis)
            else:
                self.dropNative(nativeGrists, dropThis)

    def dropIt(self, grist, amount):
        if grist=='build':
            amount*=2
        elif grist in self.associatedGrist:
            pass
        elif grist in self.commonGrist:
            pass
        elif grist in self.goodGrist:
            amount-=10
            if amount<2:
                amount=2

        elif grist in self.greatGrist:
            amount=amount//2
            if not amount:
                amount=2

        elif grist in self.capstoneGrist:
            amount=amount//10
            if not amount:
                amount=2

        elif grist in self.exoticGrist:
            amount= amount//100+1


        self.loot.append(str(amount)+' '+grist+' grist')
        
    def dropNative(self, nativeGrists, amount):
        choose=random.randint(0,len(nativeGrists)-1)
        self.dropIt(nativeGrists[choose],amount)

    def dropHeal(self, amount):
        if amount<50:
            self.loot.append('healing gel for 1d6')
        elif amount<100:
            self.loot.append('healing gel for 2d6')
        else:
            self.loot.append('healing gel for 4d4')

    def dropRelated(self, grists, amount):
        refGrist=grists[random.randint(1,len(grists)-1)]
        reference = self.gristList.index(refGrist)
        if random.randint(0,1):
            newIndex=reference-6*random.randint(1,2)
            if newIndex<0:
                newIndex=reference-6
                if newIndex<0:
                    newIndex=reference
        else:
            newIndex=reference+6*random.randint(1,2)
            if newIndex>41:
                newIndex=reference+6
                if newIndex>41:
                    newIndex=reference
        newGrist=self.gristList[newIndex]
        self.dropIt(newGrist, amount)

    def dropRandom(self, amount):
        grist=self.gristList[random.randint(0,41)]
        self.dropIt(grist,amount)

    def dropGood(self, amount):
        grist=self.goodGrist[random.randint(0,11)]
        self.dropIt(grist,amount)

    def dropGreat(self, amount):
        if not random.randint(0,5):
            grist=self.capstoneGrist[random.randint(0,5)]
        else:
            grist=self.greatGrist[random.randint(0,5)]
        self.dropIt(grist,amount)

    def dropExotic(self,amount):
        grist=self.exoticGrist[random.randint(0,5)]
        self.dropIt(grist,amount)


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
        if 'mindless' in self.tacticsBucket:
            self.tactics='Performs same action or simple if/then conditional, regardless of circumstances.'
        else:
            #if not mindless, smarter tactics take precedence over less smart
            if 'smart' in self.tacticsBucket:
                self.tactics='Uses surroundings intelligently, sets traps and ambushes, deduces PC strategy and defenses from how they respond to attacks.'
            elif 'hit_and_run' in self.tacticsBucket:
                self.tactics='Attempts to avoid damage by fleeing as far as possible between attacks, then rushing back in to attack and flee.\n           Flees if damaged or threatened.'
                
            elif 'pack' in self.tacticsBucket:
                self.tactics='Coordinates with similar enemies to seperate the weakest looking target from the group and try to bring it down.\n           Flees if damaged or threatened.'
                
            elif 'ambush_predator' in self.tacticsBucket:
                self.tactics='Follows or waits to ambush. Attacks the weakest looking target. Tries to grapple and bring them down while avoiding damage.\n           Flees if damaged or threatened.'
            else:
                #default Underling tactics
                self.tactics='Attack closest enemies or enemies that most recently attacked them. Like to bunch up and try to avoid entering chokepoints.\n           Will not pursue fleeing enemies unless very confident.\n           Do not ambush; generally mill around, destroy surroundings or wander aimlessly if not engaged.'
            #undead tactics modify tactics other than mindless, rather than overriding them
            if 'undead' in self.tacticsBucket:
                self.tactics+='\n         - Never retreats unless magically compelled and always seeks to damage, with no regard to its survival.'

            
    def printout(self,file):
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
        self.tacticsBucket=set()
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
        gristType=gristType.lower().strip()
        while(gristType not in self.gristList[:42]):
              #if grist is invalid, prompt for replacement
              print('Invalid grist type. Enter grist type or enter 'r' for random. /n')
              #get and format input
              gristType = input('> ').lower().strip()
              if gristType == 'r':
                  #pick a random grist type from gristList
                  gristType = self.gristList[random.randint(0,41)]
        self.getGrist(gristType)
        self.dropGrist(gristType, alsoDrops)
        self.sortTactics()
##        #move this call to main once troubleshooting is done
##        self.printout(sys.stdout)
