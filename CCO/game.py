from direct.actor.Actor import Actor
from pandac.PandaModules import *
from direct.task import Task
import math
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from pandac.PandaModules import *
from direct.task import Task
import math
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.interval.IntervalGlobal import Sequence
from pandac.PandaModules import Point3
from pandac.PandaModules import *
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import TransparencyAttrib


from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from direct.actor.Actor import Actor

if __debug__:
    loadPrcFile("config/config.prc")



class GameTest(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        base.disableMouse()

        self.makeAcog = loader.loadModel("phase_5/models/cogdominium/tt_m_ara_cbr_barrelRoom.bam")
        self.makeAcog.reparentTo(render)
        self.stomper1 = (self.makeAcog.find('**/stomper_GRP_01'))
        self.stomper2 = (self.makeAcog.find('**/stomper_GRP_02'))
        self.stomper3 = (self.makeAcog.find('**/stomper_GRP_03'))
        self.stomper4 = (self.makeAcog.find('**/stomper_GRP_04'))
        self.stomper5 = (self.makeAcog.find('**/stomper_GRP_05'))
        self.stomper6 = (self.makeAcog.find('**/stomper_GRP_06'))
        self.stomper7 = (self.makeAcog.find('**/stomper_GRP_07'))
        self.stomper8 = (self.makeAcog.find('**/stomper_GRP_08'))
        self.stomper9 = (self.makeAcog.find('**/stomper_GRP_09'))
        self.stomper10 = (self.makeAcog.find('**/stomper_GRP_10'))
        self.stomper11 = (self.makeAcog.find('**/stomper_GRP_11'))
        self.stomper12 = (self.makeAcog.find('**/stomper_GRP_12'))
        self.stomper3.setPos(0, 0, 18.00)
        self.stomper5.setPos(0, 0, 10.00)
        self.stomper4.setPos(0, 0, 22.00)
        self.stomper2.setPos(0, 0, 7.00)
        self.stomper7.setPos(0, 0, 0)
        self.stomper8.setPos(0, 0, 5.00)
        self.stomper9.setPos(0, 0, 13.00)
        self.stomper10.setPos(0, 0, 10.00)
        self.stomper11.setPos(0, 0, 22.00)
        self.stomper12.setPos(0, 0, 7.00)


        self.music = loader.loadMusic("phase_3/audio/bgm/cco_make_a_cog.wav")
        self.music.play()
        self.music.setLoop(True)

        self.elevator = loader.loadModel("phase_5/models/cogdominium/cogdominiumElevator.bam")
        self.elevator.reparentTo(self.render)
        self.elevator.setY(25.37)
        self.elevator.find('**/floor_light_buttons').removeNode()
        self.rightDoor = (self.elevator.find('**/right_door'))
        self.leftDoor = (self.elevator.find('**/left_door'))
        self.leftDoor.setX(3.50)
        self.rightDoor.setX(-3.50)




        self.Lawbot = Actor('phase_3.5/models/char/suitC-mod.bam', {'neutral': 'phase_3.5/models/char/suitC-neutral.bam',
                                                                    'victory': 'phase_4/models/char/suitC-victory.bam',
                                                                    'walk': 'phase_3.5/models/char/suitC-walk.bam'})
        self.Lawbot.reparentTo(render)
        self.Lawbot.loop('neutral')
        self.TorsoTex = loader.loadTexture('phase_3.5/maps/l_blazer.jpg')
        self.Lawbot.find('**/torso').setTexture(self.TorsoTex, 1)
        self.ArmTex = loader.loadTexture('phase_3.5/maps/l_sleeve.jpg')
        self.Lawbot.find('**/arms').setTexture(self.ArmTex, 1)
        self.LegTex = loader.loadTexture('phase_3.5/maps/l_leg.jpg')
        self.Lawbot.find('**/legs').setTexture(self.LegTex, 1)
        self.Head = loader.loadModel('phase_3.5/models/char/suitC-heads.bam').find('**/flunky')
        self.headTexture = loader.loadTexture("phase_3.5/maps/bottom-feeder.jpg")
        self.Head.reparentTo(self.Lawbot.find('**/joint_head'))
        self.Lawbot.findAllMatches('**/joint_head').setTexture(self.headTexture, 1)
        self.icon = loader.loadModel('phase_3/models/gui/cog_icons.bam')
        self.icon.reparentTo(render)
        self.icon.reparentTo(self.Lawbot.find('**/joint_attachMeter'))
        self.icon.find('**/MoneyIcon').removeNode()
        self.icon.find('**/cog').removeNode()
        self.icon.find('**/SalesIcon').removeNode()
        self.icon.find('**/CorpIcon').removeNode()
        self.icon.setH(180)
        self.icon.setScale(0.70)
        self.Lawbot.setH(180.00)
        self.Lawbot.hide()


        self.Cashbot = Actor('phase_3.5/models/char/suitC-mod.bam', {'neutral': 'phase_3.5/models/char/suitC-neutral.bam',
                                                                    'victory': 'phase_4/models/char/suitC-victory.bam',
                                                                    'walk': 'phase_3.5/models/char/suitC-walk.bam'})
        self.Cashbot.reparentTo(render)
        self.Cashbot.loop('neutral')
        self.TorsoTex = loader.loadTexture('phase_3.5/maps/m_blazer.jpg')
        self.Cashbot.find('**/torso').setTexture(self.TorsoTex, 1)
        self.ArmTex = loader.loadTexture('phase_3.5/maps/m_sleeve.jpg')
        self.Cashbot.find('**/arms').setTexture(self.ArmTex, 1)
        self.LegTex = loader.loadTexture('phase_3.5/maps/m_leg.jpg')
        self.Cashbot.find('**/legs').setTexture(self.LegTex, 1)
        self.Head = loader.loadModel('phase_3.5/models/char/suitC-heads.bam').find('**/coldcaller')
        self.Head.reparentTo(self.Cashbot.find('**/joint_head'))
        self.icon = loader.loadModel('phase_3/models/gui/cog_icons.bam')
        self.icon.reparentTo(render)
        self.icon.reparentTo(self.Cashbot.find('**/joint_attachMeter'))
        self.icon.find('**/SalesIcon').removeNode()
        self.icon.find('**/cog').removeNode()
        self.icon.find('**/LegalIcon').removeNode()
        self.icon.find('**/CorpIcon').removeNode()
        self.icon.setH(180)
        self.icon.setScale(0.70)
        self.Cashbot.setH(180.00)
        self.Cashbot.hide()

        self.Sellbot = Actor('phase_3.5/models/char/suitC-mod.bam', {'neutral': 'phase_3.5/models/char/suitC-neutral.bam',
                                                                    'victory': 'phase_4/models/char/suitC-victory.bam',
                                                                    'walk': 'phase_3.5/models/char/suitC-walk.bam'})
        self.Sellbot.reparentTo(render)
        self.Sellbot.loop('neutral')
        self.TorsoTex = loader.loadTexture('phase_3.5/maps/s_blazer.jpg')
        self.Sellbot.find('**/torso').setTexture(self.TorsoTex, 1)
        self.ArmTex = loader.loadTexture('phase_3.5/maps/s_sleeve.jpg')
        self.Sellbot.find('**/arms').setTexture(self.ArmTex, 1)
        self.LegTex = loader.loadTexture('phase_3.5/maps/s_leg.jpg')
        self.Sellbot.find('**/legs').setTexture(self.LegTex, 1)
        self.Head = loader.loadModel('phase_3.5/models/char/suitC-heads.bam').find('**/coldcaller')
        self.Head.reparentTo(self.Sellbot.find('**/joint_head'))
        self.Head.reparentTo(self.Sellbot.find('**/joint_head'))
        self.icon = loader.loadModel('phase_3/models/gui/cog_icons.bam')
        self.icon.reparentTo(render)
        self.icon.reparentTo(self.Sellbot.find('**/joint_attachMeter'))
        self.icon.find('**/MoneyIcon').removeNode()
        self.icon.find('**/cog').removeNode()
        self.icon.find('**/LegalIcon').removeNode()
        self.icon.find('**/CorpIcon').removeNode()
        self.icon.setH(180)
        self.icon.setScale(0.70)
        self.Sellbot.setH(180.00)
        self.Sellbot.hide()

        self.Bossbot = Actor('phase_3.5/models/char/suitC-mod.bam',
                             {'neutral': 'phase_3.5/models/char/suitC-neutral.bam',
                              'victory': 'phase_4/models/char/suitC-victory.bam',
                              'walk': 'phase_3.5/models/char/suitC-walk.bam'})
        self.Bossbot.reparentTo(render)
        self.Bossbot.loop('neutral')
        self.TorsoTex = loader.loadTexture('phase_3.5/maps/c_blazer.jpg')
        self.Bossbot.find('**/torso').setTexture(self.TorsoTex, 1)
        self.ArmTex = loader.loadTexture('phase_3.5/maps/c_sleeve.jpg')
        self.Bossbot.find('**/arms').setTexture(self.ArmTex, 1)
        self.LegTex = loader.loadTexture('phase_3.5/maps/c_leg.jpg')
        self.Bossbot.find('**/legs').setTexture(self.LegTex, 1)
        self.Head = loader.loadModel('phase_3.5/models/char/suitC-heads.bam')
        self.Head.find('**/coldcaller').hide()
        self.Head.find('**/gladhander').hide()
        self.Head.find('**/micromanager').hide()
        self.Head.find('**/moneybags').hide()
        self.Head.find('**/tightwad').hide()
        self.Head.reparentTo(self.Bossbot.find('**/joint_head'))
        self.icon = loader.loadModel('phase_3/models/gui/cog_icons.bam')
        self.icon.reparentTo(render)
        self.icon.reparentTo(self.Bossbot.find('**/joint_attachMeter'))
        self.icon.find('**/MoneyIcon').removeNode()
        self.icon.find('**/cog').removeNode()
        self.icon.find('**/LegalIcon').removeNode()
        self.icon.find('**/SalesIcon').removeNode()
        self.icon.setH(180)
        self.icon.setScale(0.70)
        self.Bossbot.setH(180.00)
        self.Bossbot.hide()


        self.Sourcebot = Actor('phase_3.5/models/char/suitC-mod.bam',
                             {'neutral': 'phase_3.5/models/char/suitC-neutral.bam',
                              'victory': 'phase_4/models/char/suitC-victory.bam',
                              'walk': 'phase_3.5/models/char/suitC-walk.bam'})

        self.Sourcebot.reparentTo(render)
        self.Sourcebot.loop('neutral')
        self.TorsoTex = loader.loadTexture('phase_3.5/maps/t_blazer.jpg')
        self.Sourcebot.find('**/torso').setTexture(self.TorsoTex, 1)
        self.ArmTex = loader.loadTexture('phase_3.5/maps/t_sleeve.jpg')
        self.Sourcebot.find('**/arms').setTexture(self.ArmTex, 1)
        self.LegTex = loader.loadTexture('phase_3.5/maps/t_leg.jpg')
        self.Sourcebot.find('**/legs').setTexture(self.LegTex, 1)
        self.Head = loader.loadModel('phase_3.5/models/char/FlairDirector.egg')
        self.headTexture = loader.loadTexture("phase_3.5/maps/flair-director.jpg")
        self.Head.reparentTo(self.Sourcebot.find('**/joint_head'))
        self.Sourcebot.findAllMatches('**/joint_head').setTexture(self.headTexture, 1)
        self.Sourcebot.setH(180.00)
        self.Sourcebot.hide()

        self.Techbot = Actor('phase_3.5/models/char/suitC-mod.bam',
                               {'neutral': 'phase_3.5/models/char/suitC-neutral.bam',
                                'victory': 'phase_4/models/char/suitC-victory.bam',
                                'walk': 'phase_3.5/models/char/suitC-walk.bam'})

        self.Techbot.reparentTo(render)
        self.Techbot.loop('neutral')
        self.TorsoTex = loader.loadTexture('phase_3.5/maps/t_blazer.jpg')
        self.Techbot.find('**/torso').setTexture(self.TorsoTex, 1)
        self.ArmTex = loader.loadTexture('phase_3.5/maps/t_sleeve.jpg')
        self.Techbot.find('**/arms').setTexture(self.ArmTex, 1)
        self.LegTex = loader.loadTexture('phase_3.5/maps/t_leg.jpg')
        self.Techbot.find('**/legs').setTexture(self.LegTex, 1)
        self.Head = loader.loadModel('phase_3.5/models/char/PayrollConvertor.egg')
        self.headTexture = loader.loadTexture("phase_3.5/maps/PayrollConvertor.png")
        self.Head.reparentTo(self.Techbot.find('**/joint_head'))
        self.Head.setPos(0, 0, -0.15)
        self.Head.setScale(0.93)
        self.Techbot.findAllMatches('**/joint_head').setTexture(self.headTexture, 1)
        self.Techbot.setH(180.00)
        self.Techbot.hide()

        self.Pilotbots = Actor('phase_3.5/models/char/suitC-mod.bam',
                             {'neutral': 'phase_3.5/models/char/suitC-neutral.bam',
                              'victory': 'phase_4/models/char/suitC-victory.bam',
                              'walk': 'phase_3.5/models/char/suitC-walk.bam'})

        self.Pilotbots.reparentTo(render)
        self.Pilotbots.loop('neutral')
        self.TorsoTex = loader.loadTexture('phase_3.5/maps/t_blazer.jpg')
        self.Pilotbots.find('**/torso').setTexture(self.TorsoTex, 1)
        self.ArmTex = loader.loadTexture('phase_3.5/maps/t_sleeve.jpg')
        self.Pilotbots.find('**/arms').setTexture(self.ArmTex, 1)
        self.LegTex = loader.loadTexture('phase_3.5/maps/t_leg.jpg')
        self.Pilotbots.find('**/legs').setTexture(self.LegTex, 1)
        self.Head = loader.loadModel('phase_3.5/models/char/ConstructionBot.egg')
        self.headTexture = loader.loadTexture("phase_3.5/maps/Buildbot.png")
        self.Head.reparentTo(self.Pilotbots.find('**/joint_head'))
        self.Head.setPos(0, 0, -0.15)
        self.icon.setH(180)
        self.Pilotbots.findAllMatches('**/joint_head').setTexture(self.headTexture, 1)
        self.Pilotbots.setH(180.00)
        self.Pilotbots.hide()



        #-----Sequences------#

        Walk1 = self.stomper1.posInterval(9.50, Point3(0, 0, 18.00))
        Walk2 = self.stomper1.posInterval(9.50, Point3(0, 0, 0))
        self.stomperPound1 = Sequence(Walk1, Walk2)
        self.stomperPound1.loop()

        Walk1 = self.stomper6.posInterval(9.50, Point3(0, 0, 18.00))
        Walk2 = self.stomper6.posInterval(9.50, Point3(0, 0, 0))
        self.stomperPound2 = Sequence(Walk1, Walk2)
        self.stomperPound2.loop()



        Walk1 = self.stomper3.posInterval(9.50, Point3(0, 0, 0))
        Walk2 = self.stomper3.posInterval(9.50, Point3(0, 0, 18.00))
        self.stomperPound3 = Sequence(Walk1, Walk2)
        self.stomperPound3.loop()

        Walk1 = self.stomper5.posInterval(5.50, Point3(0, 0, 0))
        Walk2 = self.stomper5.posInterval(5.50, Point3(0, 0, 10.00))
        self.stomperPound4 = Sequence(Walk1, Walk2)
        self.stomperPound4.loop()

        Walk1 = self.stomper4.posInterval(5.50, Point3(0, 0, 0))
        Walk2 = self.stomper4.posInterval(5.50, Point3(0, 0, 22.00))
        self.stomperPound5 = Sequence(Walk1, Walk2)
        self.stomperPound5.loop()

        Walk1 = self.stomper2.posInterval(3.50, Point3(0, 0, 0))
        Walk2 = self.stomper2.posInterval(3.50, Point3(0, 0, 7.00))
        self.stomperPound6 = Sequence(Walk1, Walk2)
        self.stomperPound6.loop()

        Walk1 = self.stomper7.posInterval(9.50, Point3(0, 0, 18.00))
        Walk2 = self.stomper7.posInterval(9.50, Point3(0, 0, 0))
        self.stomperPound7 = Sequence(Walk1, Walk2)
        self.stomperPound7.loop()

        Walk1 = self.stomper8.posInterval(5.50, Point3(0, 0, 5.00))
        Walk2 = self.stomper8.posInterval(9.50, Point3(0, 0, 0))
        self.stomperPound8 = Sequence(Walk1, Walk2)
        self.stomperPound8.loop()

        Walk1 = self.stomper9.posInterval(6.50, Point3(0, 0, 0))
        Walk2 = self.stomper9.posInterval(6.50, Point3(0, 0, 13.00))
        self.stomperPound9 = Sequence(Walk1, Walk2)
        self.stomperPound9.loop()

        Walk1 = self.stomper10.posInterval(5.50, Point3(0, 0, 0))
        Walk2 = self.stomper10.posInterval(5.50, Point3(0, 0, 10.00))
        self.stomperPound10 = Sequence(Walk1, Walk2)
        self.stomperPound10.loop()

        Walk1 = self.stomper11.posInterval(5.50, Point3(0, 0, 0))
        Walk2 = self.stomper11.posInterval(5.50, Point3(0, 0, 22.00))
        self.stomperPound11 = Sequence(Walk1, Walk2)
        self.stomperPound11.loop()

        Walk1 = self.stomper12.posInterval(3.50, Point3(0, 0, 0))
        Walk2 = self.stomper12.posInterval(3.50, Point3(0, 0, 7.00))
        self.stomperPound12 = Sequence(Walk1, Walk2)
        self.stomperPound12.loop()



        Walk1 = self.camera.posInterval(2.50, Point3(-20.98, -14.61, 9.74))
        Spin1 = self.camera.hprInterval(1.00, Vec3(321.34, 348.11, 0))
        cogSpin = self.Sellbot.hprInterval(1.50, Vec3(0, 0, 0))
        Walk2 = self.camera.posInterval(5.0, Point3(-20.98, -14.61, 9.74))
        Walk3 = self.camera.posInterval(1.50, Point3(-20.98, 1.40, 7.97))
        Spin2 = self.camera.hprInterval(1.00, Vec3(281.31, 348.11, 0))
        Walk4 = self.camera.posInterval(8.50, Point3(-20.98, 1.40, 7.97))
        Walk5 = self.camera.posInterval(2.50, Point3(0, -19.61, 2.61))
        Spin3 = self.camera.hprInterval(1.00, Vec3(0, 0, 0))
        self.cameraMove = Sequence(Walk1, Spin1, cogSpin, Walk2, Walk3, Spin2, Walk4, Walk5, Spin3)

        Walk1 = self.camera.posInterval(2.50, Point3(0, -77.48, 3.42))
        Spin1 = self.camera.hprInterval(1.00, Vec3(0, 0, 0))
        Walk2 = self.camera.posInterval(2.50, Point3(0, -77.48, 3.42))
        Walk3 = self.camera.posInterval(3.00, Point3(0, -22.48, 3.42))
        self.cameraStart = Sequence(Walk1, Spin1, Walk2, Walk3)

        Walk1 = self.camera.posInterval(15.50, Point3(6.31, -45.31, 9.27))
        Spin1 = self.camera.hprInterval(0.00, Vec3(337.52, 0, 0))
        Walk2 = self.camera.posInterval(0.00, Point3(6.08, -100.53, 9.27))
        Walk3 = self.camera.posInterval(12.00, Point3(14.07, -77.33, 9.27))
        Walk4 = self.camera.posInterval(0.00, Point3(18.93, -82.36, 25.51))
        Spin2 = self.camera.hprInterval(0.00, Vec3(30.26, 347.91, 0))
        Walk5 = self.camera.posInterval(15.00, Point3(0.44, -51.38, 21.411))
        Spin3 = self.camera.hprInterval(0.00, Vec3(337.52, 0, 0))
        self.cameraIntro = Sequence(Walk1, Spin1, Walk2, Walk3, Walk4, Spin2, Walk5, Spin3)
        self.cameraIntro.start()



        #----camera---#


        self.camera.setPos(6.31, -82.36, 9.27)
        self.camera.setHpr(35.71, 0, 0)

        #--------Start-up-Menu--------#

        #-----buttons-------#

        #-----texts-------#
        self.logoLeft = OnscreenImage(image='phase_3/maps/cogcitycodeaffix-logo-hor-left[OLD].png', pos=(-0.46, 0, 0.2), scale=(0.7))
        self.logoLeft.setTransparency(TransparencyAttrib.MAlpha)

        self.logoRight = OnscreenImage(image='phase_3/maps/cogcitycodeaffix-logo-hor-right[OLD].png', pos=(0.56, 0, 0.18), scale=(0.7))
        self.logoRight.setTransparency(TransparencyAttrib.MAlpha)

        font = self.loader.loadFont("phase_3/models/fonts/vtRemingtonPortable.ttf")


        text = TextNode("play")
        text.setText("Press F1 to play")
        text.setFont(font)

        self.textNodePath = aspect2d.attachNewNode(text)
        self.textNodePath.setScale(0.09)
        self.textNodePath.setPos(-0.5, 0, -0.7)

        #-----optionText-----------#

        fps = ""
        textObject = OnscreenText(text=fps, pos=(-1.4, -0.97),
        scale=0.09, fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter, mayChange=1)
        textObject.setFont(font)

        fullscreen = ""
        textObject2 = OnscreenText(text=fullscreen, pos=(-1.34, -0.88),
                                  scale=0.09, fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter, mayChange=1)
        textObject2.setFont(font)

        audio = ""
        textObject3 = OnscreenText(text=audio, pos=(-1.48, -0.78),
                                   scale=0.09, fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter, mayChange=1)
        textObject3.setFont(font)


        #------doneButton--------#

        #font = self.loader.loadFont("phase_3/models/fonts/vtRemingtonPortable.ttf")

        #bk_text = ""
        #textObject = OnscreenText(text=bk_text, pos=(0.00, 0.73),
                                  #scale=0.16, fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter, mayChange=1)
        #textObject.setFont(font)
        #textObject.setColor(0.3, 0.3, 0.35, 1.0)

        #def setText(status):
            #if (status):
                #bk_text = "Do you want to continue?"
            #else:
                #bk_text = ""
            #textObject.setText(bk_text)


        #b = DirectCheckButton(text="Continue", scale=0.12, pos=(0, 0, -0.80), command=setText)

        #----------key/click-events-------#

        self.acceptOnce("f1", self.play)
        #self.accept("f", self.frameRate)

    def moveCamera(self):
        if self.camera:
           self.cameraMove.start()
        else:
            self.cameraMove.stop()

    def play(self):
        if self.logoRight:
           self.logoRight.destroy()
           self.logoLeft.destroy()
           self.textNodePath.hide()
           self.cameraIntro.finish()
           self.cameraStart.start()
        else:
           self.cameraStart.stop()

load = GameTest()
load.run()