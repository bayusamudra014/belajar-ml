import os
import csv
from google_play_scraper import reviews, Sort


def create_required_directories():
    os.makedirs('data', exist_ok=True)
    os.makedirs('models', exist_ok=True)


def get_reviews(app_id, count=100):
    result = []

    for i in range(1, 6):
        tmp, _ = reviews(
            app_id,
            lang='id',
            country='id',
            sort=Sort.NEWEST,
            count=count,
        )
        result += tmp

    return result


apps = [
    'brain.guess.word.quiz.puzzle',
    'brain.word.train.puzzle.guess.game',
    'com.BlackGames.MathRiddles',
    'com.Bow3.TheClaw',
    'com.CarXTech.highWay',
    'com.DL.war.planes.inc.torpedo.bomber.fighter.aircraft.ww2',
    'com.GhostInteractive.BusSimulatorBangladesh',
    'com.HomeNetGames.Warplanes',
    'com.HyperBeardGames.MyDearFarm',
    'com.ParsisGames.AirCombatEn',
    'com.StudioFurukawa.PixelCarRacer',
    'com.albiononline',
    'com.amanotes.gs.g06',
    'com.and.games505.TerrariaPaid',
    'com.arcadesindo.dimensilainserena',
    'com.as.modern.highway.bus.driving.games.simulator.offline.bus.games',
    'com.bethsoft.falloutshelter',
    'com.bgg.jump',
    'com.bigbluebubble.singingmonsters.full',
    'com.biglime.cookingmadness',
    'com.brainbow.peak.app',
    'com.bubadu.bubbu',
    'com.budgestudios.googleplay.BudgeRacing',
    'com.budgestudios.googleplay.HotWheelsUnlimited',
    'com.carxtech.carxdr2',
    'com.carxtech.rally',
    'com.carxtech.sr',
    'com.digidust.elokence.akinator.freemium',
    'com.dts.freefiremax',
    'com.dts.freefireth',
    'com.dynamicgames.worldbusdrivingsimulator',
    'com.ea.game.nfs14_row',
    'com.ea.game.pvzfree_row',
    'com.ea.game.simcitymobile_row',
    'com.ea.games.r3_row',
    'com.ea.games.simsfreeplay_row',
    'com.ea.gp.fifamobile',
    'com.ea.gp.simsmobile',
    'com.easybrain.brain.test.easy.game',
    'com.easygames.race',
    'com.elektron.mindpal',
    'com.esproject.ebs',
    'com.eyewind.case.master',
    'com.fds.infiniteflight',
    'com.fgol.HungrySharkEvolution',
    'com.find.out.hidden.objects',
    'com.fingersoft.hcr2',
    'com.fingersoft.hillclimb',
    'com.firstcenturythinking.braintraining',
    'com.flaregames.zgs',
    'com.fugo.wow',
    'com.gamedevltd.modernstrike',
    'com.gamedevltd.wwh',
    'com.gameinsight.airport',
    'com.gameloft.android.ANMP.GloftA8HM',
    'com.gameloft.android.ANMP.GloftA9HM',
    'com.gameloft.android.ANMP.GloftAGHM',
    'com.gameloft.android.ANMP.GloftDMHM',
    'com.gameloft.android.ANMP.GloftDOHM',
    'com.gameloft.android.ANMP.GloftM5HM',
    'com.gameloft.anmp.disney.speedstorm',
    'com.garena.game.fctw',
    'com.garena.game.kgid',
    'com.google.android.play.games',
    'com.gtooist.bussimulator.busdriving.real.bus',
    'com.haegin.playtogether',
    'com.haugland.woa',
    'com.hospital.craze.clinic.happy.doctor.ASMR',
    'com.hutchgames.formularacing',
    'com.hyperbeard.adorablehome',
    'com.hyperbeard.kumosushibar',
    'com.hyperbeard.pocketlove',
    'com.idbs.simulator.bus.malaysia',
    'com.idle.foodgame.catcookingbar',
    'com.ig.delete.one.part',
    'com.imaginalis.HouseFlipperMobile',
    'com.imangi.templerun2',
    'com.imayi.monstertruckgofree',
    'com.infinitygames.eureka',
    'com.innersloth.spacemafia',
    'com.kiloo.subwaysurf',
    'com.king.candycrushsaga',
    'com.kitkagames.fallbuddies',
    'com.levelinfinite.sgameGlobal',
    'com.levelupgarage.spotracers',
    'com.lockwoodpublishing.avakinlife',
    'com.logicapp',
    'com.ludo.king',
    'com.lumoslabs.lumosity',
    'com.matteljv.uno',
    'com.melemoe.dreamcat',
    'com.melemoe.lovelycat',
    'com.meluapp.tekatekisilangpintar',
    'com.memorado.brain.games',
    'com.miHoYo.GenshinImpact',
    'com.mind.quiz.brain.out',
    'com.miniclip.eightballpool',
    'com.mkarpenko.worldbox',
    'com.mobile.legends',
    'com.mojang.minecraftpe',
    'com.monclarity.brainwell',
    'com.movile.playkids.pkxd',
    'com.naturalmotion.customstreetracer2',
    'com.nekki.shadowfight3',
    'com.neptune.domino',
    'com.netease.partyglobal',
    'com.netease.racerna',
    'com.nexon.kart',
    'com.nianticlabs.pokemongo',
    'com.nintendo.zaka',
    'com.nordcurrent.flyingfever',
    'com.nuomondo.millionaire.quiz',
    'com.orbital.brainiton',
    'com.os.airforce',
    'com.osg.takeoff',
    'com.outfit7.mytalkingangela2',
    'com.outfit7.mytalkingangelafree',
    'com.outfit7.mytalkinghank',
    'com.outfit7.mytalkingtom2',
    'com.outfit7.mytalkingtomfree',
    'com.outfit7.mytalkingtomfriends',
    'com.pazugames.avatarworld',
    'com.pizzagames.constructcar',
    'com.playrix.fishdomdd.gplay',
    'com.playrix.gardenscapes',
    'com.playrix.township',
    'com.playstrom.dop2',
    'com.playstrom.dop4',
    'com.pocketchamps.game',
    'com.ripcyber.gym.fighting.newgame',
    'com.roblox.client',
    'com.rovio.baba',
    'com.scopely.monopolygo',
    'com.sparklingsociety.cityisland5',
    'com.supercell.clashofclans',
    'com.supercell.clashroyale',
    'com.supercell.hayday',
    'com.surfgames.playwithmaffin',
    'com.tapblaze.pizzabusiness',
    'com.teatime.LovelyDoll',
    'com.tebakgambar',
    'com.tellmewow.focus',
    'com.tensquaregames.letsfish2',
    'com.tfgco.games.sports.free.tennis.clash',
    'com.timbojimbo.ssr',
    'com.tocaboca.tocalifeworld',
    'com.tree.idle.catsnackbar',
    'com.truckid.bus.lintas.jawa',
    'com.turborilla.MadSkillsMotocross2',
    'com.tutotoons.app.fluvsies.free',
    'com.tutotoons.app.smolsies2',
    'com.tutotoons.app.smolsiesmycutepethouse.free',
    'com.ubisoft.hungrysharkworld',
    'com.unicostudio.braintest',
    'com.unicostudio.braintest2new',
    'com.unicostudio.braintest4',
    'com.vectorunit.cobalt.googleplay',
    'com.weplay.motogp',
    'com.whoyaho.tanghulu',
    'com.wildlifestudios.jet.airplane.games.sky.warriors',
    'com.wonder',
    'com.zeptolab.ctr2.f2p.google',
    'es.socialpoint.DragonCity',
    'info.flowersoft.theotown.theotown',
    'it.rortos.extremelandings',
    'jp.pokemon.pokemonunite',
    'math.puzzle.games.crossmath.number.puzzles.free',
    'me.pou.app',
    'shooter.online.warplanes',
    'com.gamegos.mobile.cafeland',
    'com.ea.gp.fifaultimate',
    'com.jetstartgames.chess',
    'com.llx.chess',
    'com.chess',
    'com.gamovation.chessclubpilot',
    'com.miniclip.chess',
    'com.kingsofgames.chessuniverse',
    'pl.lukok.chess',
    'chessfriends.online.chess',
    'org.lichess.mobileapp',
    'com.vng.autochess',
    'com.rockstargames.gtasa',
    'com.scottgames.fivenightsatfreddys',
    'com.scottgames.fnaf2',
    'com.manuelgenaro.fnam',
    'com.scottgames.sisterlocation',
    'com.scottgames.fnaf3',
    'com.Ravenstone.CNaF2',
    'com.scottgames.fnaf4',
]

create_required_directories()

result = []
i = 0
for app_id in apps:
    print(
        f'[{i}/{len(apps)} apps] Scraping {app_id}: {len(result)} reviews scraped')
    results_raw = get_reviews(app_id, count=100)

    for res in results_raw:
        data = dict()
        data['content'] = res['content']
        data['score'] = res['score']

        result.append(data)

    i += 1

csv_writter = csv.DictWriter(open('data/reviews.csv', 'w', newline=''),
                             fieldnames=['content', 'score'])

csv_writter.writeheader()
csv_writter.writerows(result)
