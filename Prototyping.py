from Underling_modifier import*
import random

##
##
###EDIT THIS
##    #
##    def addPrototypeSpells(self,prototyping):
##        if prototyping not in self.prototypingList:
##            prototyping= self.prototypingList[random.randint(0,len(self.prototypingList)-1)]
##    
##    #EDIT THIS
##    #
##    def prototype(self,prototyping=''):
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
##
class NessieFins(Prototyping):
    def modifiers(self):
        self.addMoveType="swim"
        self.addSpells=()

class NessieNeck(Prototyping):
    def modifiers(self):
        self.addSpecial=["Can make bite attacks at an extra meter reach"]
        self.addAttacks=['1 bite, +'+str(self.baseAttk(self.level))+', '+self.basicDamage(self.level)]
        self.addSpells=()

class RaccoonSkull(Prototyping):
    def modifiers(self):
        self.addSpecial=['Gets immediate free attack on opponents moving away.']
        self.addSpells=()
    
class RaccoonPaws(Prototyping):
    def modifiers(self):
        self.addMoveType="climb"
        self.addSpells=()
    
class FlagStandard(Prototyping):
    def modifiers(self):
        self.addSpecial=['Underlings within '+str(self.auraSize(self.level))+' meters get a +1 bonus to all rolls and heal '+str(self.basicDamage(self.level))+' HP per round.']
        self.addSpells=()
    
class FlagBlazon(Prototyping):
    def bonus(self):
        if self.level<=7:
            return(2)
        else:
            return(4)

    def modifiers(self):
        self.addSpecial=['Gets '+str(self.bonus())+' bonus protection if it didn\'t move last round and doesn\'t move this round.']
        self.addSpells=()
    
class LeopardSpots(Prototyping):
    def modifiers(self):
        self.addSpecial=['Can pounce onto targets. (charge attack, immediate grapple on hit, defender does not get a free attack)', 'Can leap from standstill']
        self.addTactics=('Follows or waits to ambush. Attacks the weakest looking target. Tries to grapple and bring them down while avoiding damage.\n           Flees if damaged or threatened.', 4)
        self.addSpells=()
    
class LeopardHead(Prototyping):
    def modifiers(self):
        self.addAttacks=('1 bite, +'+str(self.baseAttk(self.level)+1)+', '+str(self.level)+'d2')
        self.addSpecial=('Grapples target if bite attack beats their defence by 5 or more.\n           If target is smaller, they are picked up in mouth.')
        self.addTactics=('Follows or waits to ambush. Attacks the weakest looking target. Tries to grapple and bring them down while avoiding damage.\n           Flees if damaged or threatened.', 4)
        self.addSpells=()
    
class VineLeaves(Prototyping):
    def modifiers(self):
        self.addSpecial=('Can heal '+self.basicDamage(self.level)+'+'+str(self.level)+' health as a standard action if standing or swimming in water.')
        self.addSpells=()
    
class VineTendrils(Prototyping):
    def modifiers(self):
        self.addSpecial=('Attackers that miss by five or more get their weapon tangled in vines and overgrown. \n           They can pull it out next turn with a str check, then it is lost until the underling is defeated.')
        self.addSpells=()
    
class OnryouHair(Prototyping):
    def modifiers(self):
        self.addSpecial=('Reappears in front of you 1d4 rounds later if you try to flee from it')
        self.addTactics=('Never retreats unless magically compelled and always seeks to damage, with no regard to its survival.', 7)
        self.addSpells=()
        
class OnryouKimono(Prototyping):
    def extra(self):
        if self.level>8:
            return(', and must roll all dice twice and take the worse')
        else:
            return('')
    def modifiers(self):
        self.addSpecial=('All within '+str(self.auraSize(self.level))+' meters, friend and foe alike, take '+str(self.basicDamage(self.level))+' damage on this Underling\'s turn'+self.extra()+'.\n           The Fears of LOFAC and other underlings with an onryou prototyping are unaffected.')
        self.addTactics=('Never retreats unless magically compelled and always seeks to damage, with no regard to its survival.', 7)
        self.addSpells=()
        
class CharacterEyes(Prototyping):
    def modifiers(self):
        self.addSpecial=('Can shapeshift at will to appear as other underlings/creatures.\n           Size and shape changes, but stats do not (including hp and ability to grapple).')
        self.addSpells=()
        
class CharacterClothes(Prototyping):
    def modifiers(self):
        self.addTactics=('Uses surroundings intelligently, sets traps and ambushes, deduces PC strategy and defenses from how they respond to attacks.',6)
        self.addSpells=()
