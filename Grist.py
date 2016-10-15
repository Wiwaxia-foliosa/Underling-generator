from Underling_modifier import*

class Plush(Grist):
    player="Sera"
    quality="associated"
    def modifiers(self):
        #bonus protection, but thrown around by attacks
        self.addProtection=1
        self.addSpecial=('Flies back 1m whenever hit')

class Dust(Grist):
    player="Moss"
    quality="associated"
    def modifiers(self):
        #speedy
        self.addSpeed=2

class Cobalt(Grist):
    player="Myrtha"
    quality="associated"
    def modifiers(self):
        #gives bonus HP
        self.addHp=self.level*2+2//self.level

class Mahogany(Grist):
    player="Lemi"
    quality="associated"
    def modifiers(self):
        #bonus def, but flees in the face of flame
        self.addDefence=1
        self.addTactics=Tactics('Flees from flame',1)

class Amber(Grist):
    player="Leon"
    quality="associated"
    def modifiers(self):
        #deals damage when hit if it moved enough last roung
        a,b=self.basicDamage(self.level,False)
        self.addSpecial=('If it moved last turn, deals '+str(a)+'d'+str(b//2)+' damage to the first thing to hit it with a conductive weapon')
    
class Bismuth(Grist):
    player="Ilmatar"
    quality="associated"
    def modifiers(self):
        pass

class Cotton(Grist):
    player="Sera"
    quality="common"
    def modifiers(self):
        self.addSpecial=('Becomes immobilized if wet.')

class Loam(Grist):
    player="Moss"
    quality="common"
    def modifiers(self):
        self.addSpecial=('Can teleport in water')

class Indigo(Grist):
    player="Myrtha"
    quality="common"
    def modifiers(self):
        self.addSpecial=('Stain everything they touch blue. Other indigo underlings will follow their tracks.')

class Ebony(Grist):
    player="Lemi"
    quality="common"
    def modifiers(self):
        self.addSpecial=('Creates darkness within '+ str(self.auraSize(self.level))+ ' meters.')

class Copper(Grist):
    player="Leon"
    quality="common"
    def modifiers(self):
        self.addSpecial=('Takes double damage from electricity and fire, deals '+str(self.basicDamage(self.level))+' damage to everything adjacent')

class Phosphorous(Grist):
    player="Ilmatar"
    quality="common"
    def modifiers(self):
        self.addSpecial=('Explodes violently when killed, dealing '+ str(self.basicDamage(self.level))+ 'damage to all within ' + str(self.auraSize(self.level))+ ' meters.')

class Wool(Grist):
    player="Sera"
    quality="common"
    def modifiers(self):
        print('fix')

class Sandstone(Grist):
    player="Moss"
    quality="common"
    def modifiers(self):
        #more resilient
        self.addProtection=1
        self.addDefence=1

class Woad(Grist):
    player="Myrtha"
    quality="common"
    def modifiers(self):
        a,b=self.basicDamage(self.level,False)
        self.addSpecial=('Can swim, but loses the ability permanently when it emerges from water','The first time it emerges from water, it turns from yellow to blue and regains'+str(2*a)+'d'+str(b)+' health.')

class Ash(Grist):
    player="Lemi"
    quality="common"
    def modifiers(self):
        ##            self.special.add('Healed by fire. Will attempt to ignite self and others.')
        print('fix')

class Glass(Grist):
    player="Leon"
    quality="common"
    def modifiers(self):
        self.addSpecial=('Leave a pile of glass shards where they die. Deals 1d4 damage per m to anything walking over it.')

class Rust(Grist):
    player="Ilmatar"
    quality="common"
    def modifiers(self):
        #less resilient, deals ongoing damage
        self.addProtection=-1
        self.addSpecial=('Leaves a trail of rust as it walks. Attacks do '+str(self.basicDamage())+' ongoing damage (spindown, take # rolled in damage each time)')

##        #brass
##        elif grist == self.gristList[18]:
##            self.special.add('Rings loudly when struck. This has a 1 in 6 chance of calling more underlings.')

class Polyester(Grist):
    player="Sera"
    quality="good"
    def modifiers(self):
        print('fix')

class Clay(Grist):
    player="Moss"
    quality="good"
    def modifiers(self):
        print('fix')

class Azurite(Grist):
    player="Myrtha"
    quality="good"
    def modifiers(self):
        print('fix')

class Wax(Grist):
    player="Lemi"
    quality="good"
    def modifiers(self):
        self.special.add('Ignites if damaged by fire.\n           Takes 1d6 damage a round, all attacks deal fire damage, and casts light within '+ str(self.auraSize())+ ' meters.')

class Magnetite(Grist):
    player="Leon"
    quality="good"
    def modifiers(self):
        self.addSpecial=('If there are metal objects around, has a 1 in 6 chance per turn of attracting one to itself as armor.\n           Each peice of armor gained this way gives it 1 additional protection. If a sharp object is attracted, it also takes 1d6 damage.')

class Aluminum(Grist):
    player="Ilmatar"
    quality="good"
    def modifiers(self):
        self.addDefence=1
        self.special.add('If it can swim, it can swim through clouds as if they were water.')

class Linen(Grist):
    player="Sera"
    quality="good"
    def modifiers(self):
        print('Glide speed equal to speed, must descend.')

class Cobble(Grist):
    player="Moss"
    quality="good"
    def modifiers(self):
        self.addSpecial=('Deals 1 extra damage on all attacks.')
        self.addLoot=('healing gel for '+str(self.basicDamage(self.level)))

class Lampblack(Grist):
    player="Myrtha"
    quality="good"
    def modifiers(self):
        self.addFortSave=4
        self.addSpecial=('Immune to all elemental damage.')

class Rosewood(Grist):
    player="Lemi"
    quality="good"
    def modifiers(self):
        print('fix')

class Vinyl(Grist):
    player="Leon"
    quality="good"
    def modifiers(self):
        print('fix')

class Ink(Grist):
    player="Ilmatar"
    quality="good"
    def modifiers(self):
        self.addAttacks=('1 inkblot , +'+str(self.baseAttk()+1)+', fort save or blinded 1d4 rounds. Range: 3m')  

class Velvet(Grist):
    player="Sera"
    quality="great"
    def modifiers(self):
        self.addSpecial=('Quiets sound within '+str(auraSiza(self.level))+'m. Makes it difficult to hear and nullifies magic song.')

class Humus(Grist):
    player="Moss"
    quality="great"
    def modifiers(self):
        self.addSpecial=("When killed, causes violent plant growth within "+str(auraSize(self.level))+"m until the area is overgrown and difficult to pass.") 
        
class Turquoise(Grist):
    player="Myrtha"
    quality="great"
    def modifiers(self):
        print('fix')

class Redwood(Grist):
    player="Lemi"
    quality="great"
    def modifiers(self):
        print('fix')

class Quartz(Grist):
    player="Leon"
    quality="great"
    def modifiers(self):
        print('fix')

class Silver(Grist):
    player="Ilmatar"
    quality="great"
    def modifiers(self):
        print('fix')

class Silk(Grist):
    player="Sera"
    quality="capstone"
    def modifiers(self):
        print('fix')

class Opal(Grist):
    player="Moss"
    quality="capstone"
    def modifiers(self):
        print('fix')

class Ultramarine(Grist):
    player="Myrtha"
    quality="capstone"
    def modifiers(self):
        print('fix')

class Fiddleback(Grist):
    player="Lemi"
    quality="capstone"
    def modifiers(self):
        print('fix')

class Ferrofluid(Grist):
    player="Leon"
    quality="capstone"
    def modifiers(self):
        print('fix')

class Fulgurite(Grist):
    player="Ilmatar"
    quality="capstone"
    def modifiers(self):
        print('fix')
