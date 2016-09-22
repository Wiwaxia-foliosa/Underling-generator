# If you want to add new Underling types/subclasses:
#    - assign name and level-appropriate stat values
#    - override rollHd with the correct size of die/dice to roll for hp per level
#    - override fillStats to assign the default values for your new Underling type to the fields created in __init__
#    - if your new Underling type is prototyped abnormally, override callPrototyping
#    - ensure that any new tactics labels are added to tacticsBucket by prototype or getGrist, are checked for by sortTactics
#         in approptiate order of priotity and have an appropriate description inserted into tactics by sortTactics
#    - DO NOT override __init__


#    *UNDERLING SUBCLASS TEMPLATE*
#
#
##class ### (Underling):
##    name= ###
##    # have   HD
##    level=
##    # have  HP per HD by mass
##    hd= 
##    def rollHd(self):
##        return random.randint(1, 
##    def fillStats(self):
##        self.rollHp(self.level)
##        self.defence= 
##        self.protection= 
##        self.fortSave= 
##        self.refSave= 
##        self.willSave= 
##        self.speed= 
##        self.size= 
##        self.dropWorth= 
##        self.attacks.append(
##        self.tactics=
##        self.incidental(#weight in pounds/1000)
##        self.special.add(
##        self.spells.append(


from Underling import *
import random

class Imp(Underling):
    name='Imp'
    #Imps have 1 HD
    level=1
    #Imps have 1d4 HP per HD by mass
    hd='1d4'
    def rollHd(self):
        return random.randint(1,4)
    def fillStats(self):
        self.rollHp(self.level)
        self.defence=10
        self.protection=0
        self.fortSave=5
        self.refSave=5
        self.willSave=5
        self.speed=4
        self.size='1m'
        self.dropWorth=10
        self.attacks.append('1 jab, +0, 1d4')
        self.tactics='mill around engaging in mischeif/petty vandalalism, only attack if approached, only work together accidentally, flee immmediately from anything that looks strong'
        #imps have no default spells or special abilities

class Ogre(Underling):
    name='Ogre'
    #Ogres have 2 HD
    level=2
    #Ogres have 1d10 HP per HD by mass
    hd='1d10'
    def rollHd(self):
        return random.randint(1,10)
    def fillStats(self):
        self.rollHp(self.level)
        self.defence=9
        self.protection=1
        self.fortSave=13
        self.refSave=5
        self.willSave=5
        self.speed=4
        self.size='3m diameter round'
        self.dropWorth=500
        self.attacks.append('1 hit, -1, 1d12')
        self.incidental(1)
        self.tactics='seek the high ground or important places and stay there, attack anything that approaches or is in the way, don\'t pursue'

class Basilisk_lesser(Underling):
    name='Basilisk'
    #basilisks have 3 HD
    level=3
    #lesser basilisks have 1d6+1d4 HP per HD by mass
    hd='1d6+1d4'
    def rollHd(self):
        return random.randint(1,6)+random.randint(1,4)
    def fillStats(self):
        self.rollHp(self.level)
        self.defence=12
        self.protection=0
        self.fortSave=10
        self.refSave=10
        self.willSave=10
        self.speed=6
        self.size='3m line'
        self.dropWorth=750
        self.attacks.append('1 bite, +1, 1d8')
        self.incidental(1)
        self.special.add('Grapples target if bite attack beats their defence by 5 or more.\n           If target is smaller, they are picked up in mouth.')
        self.spells.append('Fire breath: cone 3d6 damage, -1 die per meter, ref save to jump 1m back.\n           Recharges on a 6 on d6.')
        self.tactics='lie around or wander aimlessly, attack anything they stumble across, try to spread attacks and fire around, pursue but don\'t enter choke points'


class Basilisk_greater(Underling):
    name='Basilisk'
    #basilisks have 3 HD
    level=3
    #greater basilisks have 2d6 HP per HD by mass
    hd='2d6'
    def rollHd(self):
        return random.randint(1,6)+random.randint(1,6)
    def fillStats(self):
        self.rollHp(self.level)
        self.defence=11
        self.protection=1
        self.fortSave=12
        self.refSave=9
        self.willSave=10
        self.speed=6
        self.size='5m line'
        self.dropWorth=1000
        self.attacks.append('1 bite, +1, 1d8')
        self.incidental(2)
        self.special.add('Grapples target if bite attack beats their defence by 5 or more.\n           If target is smaller, they are picked up in mouth.')
        self.spells.append('Fire breath: cone 3d6 damage, -1 die per meter, ref save to jump 1m back.\n           Recharges on a 6 on d6.')
        self.tactics='lie around or wander aimlessly, attack anything they stumble across, try to spread attacks and fire around, pursue but don\'t enter choke points'


class Gristmoss(Underling):
    name='Gristmoss'
    #actual number of HD is determined randomly in fillStats
    #for the purposes of assembling underling types by level, the default level is 3
    level=3
    #gristmoss has 1d4 HP per HD by mass
    hd='1d4'
    def rollHd(self):
        return random.randint(1,4)
    #gristmoss does not benefit from the effects of prototyping
    def callPrototyping(self,prototyping=''):
        pass
    def fillStats(self):
        #gristmoss has variable HD, depending on the area it covers
        self.level=random.randint(1,6)
        self.rollHp(self.level)
        self.defence=0
        self.protection=5
        self.fortSave=10
        self.refSave=0
        self.willSave=20
        self.speed=0
        self.size=str(self.level)+'m area'
        self.dropWorth=80*self.level
        self.attacks.append('none')
        self.special.add('All adjacent enemies take 1d4 damage per level every turn, ignoring defence and protection.')
        self.special.add('Disguised as ordinary grist')
        self.tactics='mindless'

class Lich(Underling):
    name='Lich'
    #liches have 4 HD
    level=4
    #liches have 1d6 HP per HD by mass
    hd='1d6'
    def rollHd(self):
        return random.randint(1,6)
    def fillStats(self):
        self.rollHp(self.level)
        self.defence=13
        self.protection=0
        self.fortSave=9
        self.refSave=12
        self.willSave=14
        self.speed=5
        self.size='1m'
        self.dropWorth=750
        self.prototypingSpells=True
        self.attacks.append('1 touch, +1, fort save or paralyzed 1d4 rounds')
        self.spells.append('Magic Missile: range 10m, hits automatically, deals 1d4 damage.\n           Recharges on a 4+ on d6.')
        self.loot.append('skull')
        self.special.add('Ressurects from skull in 1d6 turns unless skull is smashed.')
        self.tactics='wait to attack until enemies are already weakened or engaged, attack from a distance, paralyze ranged attakers or anyone getting close'

class Harpy(Underling):
    name='Harpy'
    #harpies have 4 HD
    level=4
    #harpies have 1d2 HP per HD by mass
    hd='1d2'
    def rollHd(self):
        return random.randint(1,2)
    def fillStats(self):
        self.rollHp(self.level)
        self.defence=15
        self.protection=0
        self.fortSave=5
        self.refSave=15
        self.willSave=7
        self.speed=10
        self.size='1m'
        self.dropWorth=400
        self.attacks.append('1 flyby (move action), +1, 1d6')
        self.attacks.append('2 claws/1 bite/2 wings, +2/+1(+1 per claw hit)/+5, 1d6/1d6/1d4')
        self.spells.append('Scream: 1/6 chance of attracting more Underlings (as per encounter table).\n            Recharges on 6 on d6.')
        self.tactics='avoid damage, hit and run then circle back to follow at a safe distance, don\'t attack and just scream for help when wounded'

class Giclops(Underling):
    name='Giclops'
    #giclopses have 5 HD
    level=5
    #giclopses have 2d10 HP per HD by mass
    hd = '2d10'
    def rollHd (self):
        return random.randint(1,10)+random.randint(1,10)
    def fillStats (self):
        self.rollHp(self.level)
        self.defence=8
        self.protection=3
        self.fortSave=15
        self.refSave=2
        self.willSave=8
        self.speed=3
        self.size='5m diameter round'
        self.dropWorth=5000
        self.attacks.append('1 hit, +0, 2d8')
        self.attacks.append('1/2 crush (takes 2 rounds), -2, 2d20')
        self.incidental(16)
        self.special.add('Vulnerable [0] back, [-10] eye (def 17 from range)')
    
class Barghest(Underling):
    name= 'Barghest'
    # have 5 HD
    level= 5
    # have 1d6 HP per HD by mass
    hd= '1d6'
    def rollHd(self):
        return random.randint(1,6)
    numberOccuring=2
    def fillStats(self):
        self.rollHp(self.level)
        self.defence= 13
        self.protection= 0 
        self.fortSave= 9
        self.refSave= 14
        self.willSave= 9
        self.speed= 9
        self.size= '1m'
        self.dropWorth= 750
        self.attacks.append('(1 bite, +3, 2d4 crits on natural 18+)')
        self.attacks.append('(1 nip, +6, 1d2 and halt movement)')
        self.special.add('Gets 1 free attack per round against opponents moving past or alongside it')
        self.tactics='work together to seperate out and take down the weakest, flee if wounded or if unsuccessful'

class Semilich(Underling):
    pass
##    name= Semilich
##    # have 6 HD
##    level= 6
##    # have  HP per HD by mass
##    hd= 
##    def rollHd(self):
##        return random.randint(1, 
##    def fillStats(self):
##        self.rollHp(self.level)
##        self.defence= 
##        self.protection= 
##        self.fortSave= 
##        self.refSave= 
##        self.willSave= 
##        self.speed= 
##        self.size= 
##        self.dropWorth= 
##        self.attacks.append(
##        self.incidental(#weight in pounds/1000)
##        self.special.add(
##        self.spells.append(
##    #grist 1000

class Hydra(Underling):
    pass
    #grist 3000

class Bruticorn(Underling):
    pass
    #grist 5500

class Archlich(Underling):
    pass
    #grist 8000

class Formoriarm(Underling):
    pass
    #grist 10k

class Horrorse(Underling):
    pass

class Spawntinel(Underling):
    pass
    #grist 

class Spectaterror(Underling):
    pass
    #grist 

class Roc(Underling):
    pass

class Gigalisk(Underling):
    pass
    #grist 

class Beast(Underling):
    pass

class Minotyrant(Underling):
    pass

class Kraken(Underling):
    pass

class Acheron(Underling):
    pass
    #grist 100k

class Colossus(Underling):
    pass

class Titachnid(Underling):
    pass

class Linnorm(Underling):
    pass
    #grist 250k
                            
class Leviathan(Underling):
    pass

class Behemoth(Underling):
    pass

class Lich_queen(Underling):
    level=13
##    #gristworth 1mil
