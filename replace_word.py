import fileinput
import os, psutil
import time

start = time.time()

replace_texts ={'abide' : 'respecter',
'about' : 'sur',
'above' : 'au dessus',
'abroad' : 'Ã  l Ã©tranger',
'absence' : 'absence',
'abuse' : 'abuser de',
'according' : 'selon',
'account' : 'Compte',
'accuse' : 'accuser',
'acquainted' : 'connaissance',
'action' : 'action',
'advantage' : 'avantage',
'advice' : 'Conseil',
'affairs' : 'affaires',
'affection' : 'affection',
'affections' : 'affections',
'afraid' : 'peur',
'after' : 'aprÃ¨s',
'afterwards' : 'ensuite',
'again' : 'encore',
'alive' : 'vivant',
'almost' : 'presque',
'alone' : 'seul',
'along' : 'le long de',
'already' : 'dÃ©jÃ ',
'although' : 'bien que',
'always' : 'toujours',
'ambition' : 'ambition',
'ancient' : 'ancien',
'angel' : 'ange',
'anger' : 'colÃ¨re',
'another' : 'un autre',
'answer' : 'rÃ©pondre',
'anything' : 'n importe quoi',
'apparel' : 'vÃªtements',
'appear' : 'apparaÃ®tre',
'appears' : 'apparaÃ®t',
'approach' : 'approche',
'argument' : 'argument',
'ariel' : 'Ariel',
'armour' : 'armure',
'aside' : 'de cÃ´tÃ©',
'asleep' : 'endormi',
'assure' : 'assurer',
'athens' : 'AthÃ¨nes',
'attend' : 'assister',
'attended' : 'assistÃ©',
'authority' : 'autoritÃ©',
'avoid' : 'Ã©viter',
'awake' : 'Ã©veillÃ©',
'awhile' : 'quelque temps',
'banish' : 'bannir',
'barren' : 'DÃ©nudÃ©',
'bassianus' : 'bassianus',
'bastard' : 'Connard',
'battle' : 'bataille',
'beard' : 'barbe',
'bearing' : 'palier',
'bears' : 'ours',
'beast' : 'la bÃªte',
'beaten' : 'battu',
'beauty' : 'beautÃ©',
'because' : 'car',
'become' : 'devenir',
'bedford' : 'Bedford',
'before' : 'avant',
'beggar' : 'mendiant',
'begin' : 'commencer',
'behalf' : 'nom',
'behind' : 'derriÃ¨re',
'behold' : 'voir',
'being' : 'Ã©tant',
'believe' : 'croyez',
'belike' : 'Ãªtre comme',
'below' : 'au dessous de',
'benefit' : 'avantage',
'besides' : 'outre',
'betray' : 'trahir',
'better' : 'mieux',
'between' : 'entre',
'beyond' : 'au-delÃ ',
'birth' : 'naissance',
'bishop' : 'Ã©vÃªque',
'bitter' : 'amer',
'black' : 'noir',
'blame' : 'faire des reproches',
'bless' : 'bÃ©nir',
'blessing' : 'bÃ©nÃ©diction',
'blest' : 'heureux',
'blind' : 'aveugle',
'blood' : 'du sang',
'blows' : 'coups',
'blunt' : 'cru',
'blush' : 'rougir',
'bodies' : 'corps',
'bones' : 'des os',
'borne' : 'supportÃ©',
'bottom' : 'bas',
'bought' : 'achetÃ©',
'bound' : 'liÃ©',
'bounty' : 'prime',
'brain' : 'cerveau',
'brains' : 'cerveaux',
'brave' : 'courageux',
'breast' : 'Sein',
'breath' : 'souffle',
'breed' : 'race',
'brief' : 'bref',
'bright' : 'brillant',
'bring' : 'apporter',
'broke' : 'cassÃ©',
'brook' : 'ruisseau',
'brother' : 'frÃ¨re',
'brought' : 'apportÃ©',
'brows' : 'sourcils',
'burden' : 'fardeau',
'buried' : 'enterrÃ©',
'burning' : 'brÃ»lant',
'business' : 'Entreprise',
'cannot' : 'ne peux pas',
'capitol' : 'Capitole',
'captain' : 'capitaine',
'cardinal' : 'cardinal',
'cares' : 'se soucie',
'carry' : 'porter',
'castle' : 'ChÃ¢teau',
'catch' : 'capture',
'cause' : 'cause',
'cease' : 'cesser',
'certain' : 'certain',
'chain' : 'chaÃ®ne',
'chair' : 'chaise',
'challenge' : 'dÃ©fi',
'chamber' : 'chambre',
'chance' : 'chance',
'change' : 'changement',
'charge' : 'charge',
'charity' : 'charitÃ©',
'chaste' : 'chaste',
'cheek' : 'joue',
'cheer' : 'acclamation',
'chide' : 'gronder',
'chief' : 'chef',
'child' : 'enfant',
'choice' : 'choix',
'church' : 'Ã©glise',
'cinna' : 'cinna',
'citizen' : 'citoyenne',
'civil' : 'civil',
'claim' : 'prÃ©tendre',
'clarence' : 'clartÃ©',
'claud' : 'claud',
'claudio' : 'Claudio',
'clear' : 'clair',
'clifford' : 'Clifford',
'close' : 'proche',
'cloten' : 'cailloter',
'clothes' : 'vÃªtements',
'clouds' : 'des nuages',
'clown' : 'pitre',
'college' : 'UniversitÃ©',
'colour' : 'Couleur',
'comes' : 'vient',
'comfort' : 'confort',
'coming' : 'venir',
'cominius' : 'cominius',
'command' : 'commander',
'commanded' : 'commandÃ©',
'commend' : 'saluer',
'commercial' : 'commercial',
'commission' : 'commission',
'commit' : 'commettre',
'common' : 'commun',
'companion' : 'un compagnon',
'company' : 'entreprise',
'complete' : 'AchevÃ©e',
'complexion' : 'complexion',
'condition' : 'Ã©tat',
'conduct' : 'conduite',
'confess' : 'avouer',
'conscience' : 'conscience',
'consent' : 'consentement',
'consider' : 'considÃ©rer',
'constable' : 'gendarme',
'constant' : 'constant',
'contempt' : 'mÃ©pris',
'content' : 'contenu',
'contrary' : 'contraire',
'copies' : 'copies',
'copyright' : 'droits d auteur',
'could' : 'pourrait',
'council' : 'conseil',
'counsel' : 'Conseil',
'count' : 'compter',
'counterfeit' : 'contrefaire',
'countess' : 'comtesse',
'country' : 'pays',
'courage' : 'courage',
'course' : 'cours',
'court' : 'tribunal',
'courtesy' : 'courtoisie',
'cousin' : 'cousin',
'coward' : 'lÃ¢che',
'crave' : 'demander',
'creature' : 'crÃ©ature',
'credit' : 'crÃ©dit',
'cromwell' : 'Cromwell',
'cross' : 'traverser',
'crown' : 'couronne',
'cruel' : 'cruel',
'cunning' : 'ruse',
'cupid' : 'Cupidon',
'curse' : 'malÃ©diction',
'custom' : 'Douane',
'dagger' : 'dague',
'damned' : 'damnÃ©',
'dance' : 'Danse',
'danger' : 'danger',
'darkness' : 'obscuritÃ©',
'daughter' : 'fille',
'deadly' : 'mortel',
'dearest' : 'trÃ¨s cher',
'dearly' : 'chÃ¨rement',
'death' : 'dÃ©cÃ¨s',
'deeds' : 'actes',
'defend' : 'dÃ©fendre',
'degree' : 'diplÃ´me',
'delight' : 'dÃ©lice',
'deliver' : 'livrer',
'demand' : 'demande',
'denied' : 'refusÃ©',
'depart' : 'partir',
'desert' : 'dÃ©sert',
'deserve' : 'mÃ©riter',
'desire' : 'le dÃ©sir',
'despair' : 'dÃ©sespoir',
'desperate' : 'dÃ©sespÃ©rÃ©',
'despite' : 'malgrÃ©',
'device' : 'dispositif',
'devil' : 'diable',
'devise' : 'concevoir',
'didst' : 'didst',
'dinner' : 'dÃ®ner',
'discourse' : 'discours',
'discover' : 'dÃ©couvrir',
'disgrace' : 'disgrÃ¢ce',
'dishonour' : 'dÃ©shonorer',
'dispatch' : 'envoi',
'displeasure' : 'mÃ©contentement',
'disposition' : 'disposition',
'distributed' : 'distribuÃ©',
'divine' : 'Divin',
'doctor' : 'docteur',
'doing' : 'Faire',
'dolabella' : 'Dolabella',
'doors' : 'des portes',
'double' : 'double',
'doubt' : 'doute',
'download' : 'TÃ©lÃ©charger',
'dramatis' : 'dramatis',
'drawn' : 'tirÃ©',
'dread' : 'crainte',
'dreadful' : 'horrible',
'dream' : 'rÃªver',
'dreams' : 'rÃªves',
'drink' : 'boisson',
'drops' : 'gouttes',
'drown' : 'noyer',
'drums' : 'tambours',
'drunk' : 'ivre',
'duncan' : 'Duncan',
'durst' : 'durst',
'dwell' : 'habiter',
'dying' : 'en train de mourir',
'early' : 'de bonne heure',
'earth' : 'Terre',
'edmund' : 'Edmund',
'effect' : 'effet',
'egypt' : 'Egypte',
'either' : 'Soit',
'elbow' : 'coude',
'elder' : 'aÃ®nÃ©',
'embrace' : 'embrasse',
'emilia' : 'Ã‰milie',
'emperor' : 'empereur',
'empty' : 'vide',
'encounter' : 'rencontre',
'endure' : 'supporter',
'enemies' : 'ennemis',
'enemy' : 'ennemi',
'enjoy' : 'prendre plaisir',
'enobarbus' : 'Ã©nobarbus',
'enough' : 'assez',
'enter' : 'entrer',
'entertain' : 'divertir',
'entertainment' : 'divertissement',
'entreat' : 'supplier',
'equal' : 'Ã©gal',
'estate' : 'biens',
'eternal' : 'Ã©ternel',
'every' : 'chaque',
'everything' : 'tout',
'excellent' : 'excellent',
'except' : 'sauf',
'excuse' : 'excuse',
'execution' : 'exÃ©cution',
'exeter' : 'Exeter',
'exeunt' : 'sortir',
'express' : 'Express',
'faces' : 'visages',
'faint' : 'perdre connaissance',
'fairy' : 'FÃ©e',
'faith' : 'Foi',
'falls' : 'des chutes',
'FALSE' : 'faux',
'familiar' : 'familier',
'fancy' : 'fantaisie',
'farewell' : 'adieu',
'farther' : 'plus loin',
'fashion' : 'mode',
'fatal' : 'fatal',
'father' : 'pÃ¨re',
'fault' : 'faute',
'favour' : 'favoriser',
'fearful' : 'craintif',
'fears' : 'peurs',
'feast' : 'le banquet',
'feeble' : 'faible',
'fellow' : 'compagnon',
'fenton' : 'Fenton',
'ferdinand' : 'Ferdinand',
'fetch' : 'chercher',
'field' : 'champ',
'fiend' : 'dÃ©mon',
'fierce' : 'fÃ©roce',
'fiery' : 'ardent',
'fight' : 'bats toi',
'figure' : 'figure',
'finds' : 'trouve',
'finger' : 'doigt',
'first' : 'premiÃ¨re',
'flatter' : 'flatter',
'flesh' : 'la chair',
'flies' : 'mouches',
'flight' : 'vol',
'flood' : 'inonder',
'flourish' : 'fleurir',
'flower' : 'fleur',
'flowers' : 'fleurs',
'follow' : 'suivre',
'folly' : 'folie',
'foolish' : 'insensÃ©',
'fools' : 'imbÃ©ciles',
'forbear' : 'ancÃªtre',
'forbid' : 'interdire',
'force' : 'Obliger',
'forces' : 'les forces',
'forest' : 'forÃªt',
'forget' : 'oublier',
'former' : 'ancien',
'forsooth' : 'en vÃ©ritÃ©',
'forth' : 'en avant',
'fortune' : 'fortune',
'forward' : 'vers l avant',
'fought' : 'combattu',
'found' : 'a trouvÃ©',
'fourth' : 'QuatriÃ¨me',
'frame' : 'Cadre',
'france' : 'France',
'freely' : 'librement',
'french' : 'franÃ§ais',
'fresh' : 'Frais',
'friend' : 'ami',
'frown' : 'froncer les sourcils',
'fruit' : 'fruit',
'further' : 'plus loin',
'gallant' : 'galant',
'garden' : 'jardin',
'gates' : 'portes',
'gaunt' : 'dÃ©charnÃ©',
'general' : 'gÃ©nÃ©ral',
'gentle' : 'doux',
'ghost' : 'fantÃ´me',
'given' : 'donnÃ©',
'giving' : 'donnant',
'glass' : 'verre',
'glorious' : 'glorieux',
'glory' : 'gloire',
'going' : 'Aller',
'golden' : 'd or',
'goodness' : 'la bontÃ©',
'gower' : 'gower',
'grace' : 'la grÃ¢ce',
'grant' : 'subvention',
'grave' : 'la tombe',
'great' : 'gÃ©nial',
'green' : 'vert',
'greet' : 'saluer',
'grief' : 'douleur',
'grieve' : 'pleurer',
'gross' : 'brut',
'ground' : 'sol',
'grown' : 'grandi',
'guard' : 'garde',
'guess' : 'devine',
'guilty' : 'coupable',
'habit' : 'habitude',
'hands' : 'mains',
'hanging' : 'pendaison',
'hangs' : 'bloque',
'happiness' : 'bonheur',
'happy' : 'heureux',
'haste' : 'hÃ¢te',
'hateful' : 'odieux',
'having' : 'ayant',
'hazard' : 'danger',
'heads' : 'tÃªtes',
'health' : 'santÃ©',
'heard' : 'entendu',
'heart' : 'cÅ“ur',
'heaven' : 'paradis',
'heavy' : 'lourd',
'hector' : 'Hector',
'heels' : 'talons',
'hence' : 'Par consÃ©quent',
'henceforth' : 'dÃ©sormais',
'hereafter' : 'ci-aprÃ¨s, par la suite',
'herself' : 'se',
'highness' : 'altesse',
'holds' : 'tient',
'hollow' : 'creux',
'honest' : 'honnÃªte',
'horse' : 'cheval',
'hostess' : 'hÃ´tesse',
'hours' : 'heures',
'house' : 'maison',
'hubert' : 'Hubert',
'humble' : 'humble',
'humour' : 'humour',
'hundred' : 'cent',
'husband' : 'mari',
'ignorant' : 'ignorant',
'image' : 'image',
'includes' : 'comprend',
'indeed' : 'En effet',
'infinite' : 'infini',
'innocent' : 'innocent',
'instant' : 'instant',
'intend' : 'avoir l intention',
'intent' : 'intention',
'issue' : 'problÃ¨me',
'itself' : 'lui-mÃªme',
'jealous' : 'jaloux',
'jewel' : 'bijou',
'judge' : 'juge',
'judgment' : 'jugement',
'julia' : 'Julia',
'justice' : 'Justice',
'keeps' : 'garde',
'kindness' : 'la gentillesse',
'kingdom' : 'Royaume',
'kings' : 'rois',
'knave' : 'fripon',
'kneel' : 's agenouiller',
'knees' : 'les genoux',
'knife' : 'couteau',
'knight' : 'Chevalier',
'knock' : 'frappe',
'knowing' : 'connaissance',
'knowledge' : 'connaissance',
'known' : 'connu',
'knows' : 'sait',
'labour' : 'la main d oeuvre',
'ladies' : 'Dames',
'ladyship' : 'Madame',
'lands' : 'terres',
'large' : 'grand',
'laugh' : 'rire',
'launce' : 'lancer',
'lawful' : 'lÃ©gitime',
'learn' : 'apprendre',
'learned' : 'appris',
'least' : 'moins',
'leave' : 'laisser',
'leisure' : 'loisir',
'leontes' : 'leontes',
'letter' : 'lettre',
'liberty' : 'libertÃ©',
'library' : 'bibliothÃ¨que',
'liege' : 'Liege',
'lieutenant' : 'lieutenant',
'light' : 'lumiÃ¨re',
'limbs' : 'membres',
'little' : 'peu',
'lives' : 'vies',
'living' : 'vivant',
'longer' : 'plus long',
'looks' : 'regards',
'loose' : 'ample',
'lords' : 'seigneurs',
'lordship' : 'seigneurie',
'lorenzo' : 'Lorenzo',
'lovely' : 'charmant',
'lovers' : 'les amoureux',
'loves' : 'aime',
'loving' : 'aimant',
'lucentio' : 'Lucentio',
'machine' : 'machine',
'madness' : 'la dÃ©mence',
'maiden' : 'jeune fille',
'maids' : 'servantes',
'maintain' : 'maintenir',
'majesty' : 'majestÃ©',
'makes' : 'fait du',
'making' : 'fabrication',
'malice' : 'malice',
'manner' : 'maniÃ¨re',
'march' : 'Mars',
'marcius' : 'Marcius',
'marcus' : 'Marcus',
'margaret' : 'margaret',
'maria' : 'maria',
'mariana' : 'Mariana',
'marriage' : 'mariage',
'marry' : 'marier',
'master' : 'MaÃ®tre',
'match' : 'rencontre',
'matter' : 'matiÃ¨re',
'meaning' : 'sens',
'means' : 'veux dire',
'meant' : 'signifiait',
'measure' : 'mesure',
'meeting' : 'rÃ©union',
'membership' : 'adhÃ©sion',
'memory' : 'MÃ©moire',
'merchant' : 'marchande',
'mercy' : 'pitiÃ©',
'merit' : 'mÃ©rite',
'merry' : 'joyeux',
'messenger' : 'Messager',
'midnight' : 'minuit',
'might' : 'pourrait',
'mighty' : 'puissant',
'milan' : 'Milan',
'minds' : 'esprits',
'minister' : 'ministre',
'miranda' : 'Miranda',
'mirth' : 'gaietÃ©',
'mischief' : 'sottises',
'misery' : 'misÃ¨re',
'mistake' : 'erreur',
'mistress' : 'maÃ®tresse',
'modest' : 'modeste',
'money' : 'argent',
'monster' : 'monstre',
'month' : 'mois',
'morning' : 'Matin',
'morrow' : 'demain',
'mortal' : 'mortel',
'mother' : 'mÃ¨re',
'motion' : 'mouvement',
'mouth' : 'bouche',
'mowbray' : 'mowbray',
'murder' : 'meurtre',
'murther' : 'aller plus loin',
'music' : 'la musique',
'myself' : 'moi mÃªme',
'naked' : 'nu',
'names' : 'des noms',
'native' : 'originaire de',
'natural' : 'Naturel',
'nature' : 'la nature',
'needs' : 'Besoins',
'neighbour' : 'voisine',
'neither' : 'ni',
'never' : 'jamais',
'niece' : 'niÃ¨ce',
'night' : 'nuit',
'noble' : 'noble',
'noise' : 'bruit',
'nothing' : 'rien',
'nought' : 'nÃ©ant',
'number' : 'nombre',
'nurse' : 'infirmiÃ¨re',
'oaths' : 'serments',
'obedience' : 'obÃ©issance',
'oberon' : 'Oberon',
'object' : 'objet',
'occasion' : 'occasion',
'offence' : 'infraction',
'offend' : 'offenser',
'offer' : 'offre',
'office' : 'Bureau',
'often' : 'souvent',
'oliver' : 'oliver',
'opinion' : 'opinion',
'order' : 'ordre',
'orlando' : 'orlando',
'other' : 'autre',
'others' : 'autres',
'ourselves' : 'nous-mÃªmes',
'outward' : 'vers l extÃ©rieur',
'oxford' : 'Oxford',
'padua' : 'Padoue',
'pains' : 'des douleurs',
'painted' : 'peint',
'painter' : 'peintre',
'palace' : 'palais',
'pandarus' : 'Pandarus',
'paper' : 'papier',
'pardon' : 'pardon',
'paris' : 'Paris',
'parolles' : 'parolles',
'parted' : 'sÃ©parÃ©',
'particular' : 'particulier',
'partly' : 'partiellement',
'parts' : 'les piÃ¨ces',
'party' : 'fÃªte',
'passage' : 'passage',
'passion' : 'la passion',
'patience' : 'la patience',
'patient' : 'patient',
'paulina' : 'paulina',
'peace' : 'paix',
'pedro' : 'pedro',
'people' : 'gens',
'perceive' : 'apercevoir',
'percy' : 'Percy',
'perfect' : 'parfait',
'perhaps' : 'peut-Ãªtre',
'peril' : 'pÃ©ril',
'permission' : 'autorisation',
'person' : 'la personne',
'personal' : 'personnel',
'phebe' : 'phebe',
'philip' : 'Philippe',
'picture' : 'image',
'piece' : 'piÃ¨ce',
'pistol' : 'pistolet',
'place' : 'endroit',
'plague' : 'peste',
'plain' : 'plaine',
'plead' : 'plaider',
'please' : 'S il vous plaÃ®t',
'pleasure' : 'plaisir',
'pluck' : 'cueillir',
'poins' : 'poins',
'point' : 'point',
'poison' : 'poison',
'policy' : 'politique',
'polixenes' : 'polixÃ¨nes',
'pompey' : 'pompey',
'porter' : 'porter',
'possible' : 'possible',
'posthumus' : 'posthume',
'pound' : 'livre',
'power' : 'Puissance',
'practice' : 'entraine toi',
'praise' : 'louange',
'prayers' : 'priÃ¨res',
'precious' : 'prÃ©cieux',
'prepare' : 'prÃ©parer',
'presence' : 'prÃ©sence',
'present' : 'prÃ©sent',
'pretty' : 'jolie',
'pride' : 'fiertÃ©',
'priest' : 'prÃªtre',
'prince' : 'prince',
'prison' : 'prison',
'private' : 'privÃ©',
'prize' : 'prix',
'proceed' : 'procÃ©der',
'proclaim' : 'proclamer',
'profit' : 'profit',
'prohibited' : 'interdit',
'project' : 'projet',
'prologue' : 'prologue',
'promise' : 'promettre',
'proof' : 'preuve',
'proper' : 'correct',
'protector' : 'protecteur',
'protest' : 'manifestation',
'proud' : 'fier',
'prove' : 'prouver',
'provided' : 'Ã  condition de',
'public' : 'Publique',
'purpose' : 'objectif',
'purse' : 'bourse',
'quality' : 'qualitÃ©',
'quarrel' : 'querelle',
'queen' : 'reine',
'question' : 'question',
'quick' : 'rapide',
'quiet' : 'silencieux',
'quite' : 'assez',
'quoth' : 'quoth',
'raise' : 'Ã©lever',
'ransom' : 'une ranÃ§on',
'rascal' : 'coquin',
'rather' : 'plutÃ´t',
'readable' : 'lisible',
'ready' : 'prÃªt',
'realm' : 'domaine',
'reason' : 'raison',
'receive' : 'recevoir',
'regard' : 'qui concerne',
'reign' : 'rÃ¨gne',
'reignier' : 'rÃ¨gne',
'remain' : 'rester',
'remedy' : 'remÃ¨de',
'remember' : 'rappelles toi',
'render' : 'rendre',
'repair' : 'rÃ©paration',
'repent' : 'se repentir',
'report' : 'rapport',
'reputation' : 'rÃ©putation',
'request' : 'demande',
'respect' : 'le respect',
'return' : 'revenir',
'revenge' : 'vengeance',
'reverence' : 'rÃ©vÃ©rence',
'revolt' : 'rÃ©volte',
'right' : 'droite',
'rivers' : 'riviÃ¨res',
'rogue' : 'coquin',
'rotten' : 'pourri',
'rough' : 'rugueux',
'round' : 'rond',
'royal' : 'Royal',
'sacred' : 'sacrÃ©',
'safety' : 'sÃ©curitÃ©',
'saint' : 'Saint',
'salerio' : 'salerio',
'satisfied' : 'satisfait',
'saying' : 'en disant',
'scarce' : 'rare',
'scene' : 'scÃ¨ne',
'scorn' : 'mÃ©pris',
'search' : 'chercher',
'season' : 'saison',
'second' : 'seconde',
'secret' : 'secret',
'seeing' : 'voyant',
'senate' : 'sÃ©nat',
'senator' : 'sÃ©nateur',
'sense' : 'sens',
'sentence' : 'phrase',
'servant' : 'serviteur',
'serve' : 'servir',
'service' : 'un service',
'seven' : 'Sept',
'several' : 'nombreuses',
'shadow' : 'ombre',
'shake' : 'secouer',
'shall' : 'doit',
'shame' : 'la honte',
'shape' : 'forme',
'sharp' : 'tranchant',
'shepherd' : 'berger',
'shine' : 'Ã©clat',
'shore' : 'rive',
'short' : 'court',
'shortly' : 'prochainement',
'should' : 'devrait',
'shows' : 'montre',
'sickness' : 'maladie',
'sight' : 'vue',
'silence' : 'silence',
'silver' : 'argent',
'simple' : 'Facile',
'since' : 'depuis',
'single' : 'CÃ©libataire',
'sirrah' : 'sirrah',
'sister' : 'sÅ“ur',
'skill' : 'compÃ©tence',
'slain' : 'tuÃ©',
'slander' : 'calomnie',
'slave' : 'esclave',
'sleep' : 'sommeil',
'slender' : 'mince',
'small' : 'petit',
'smell' : 'odeur',
'smile' : 'sourire',
'soldier' : 'soldat',
'solemn' : 'solennel',
'somerset' : 'somerset',
'something' : 'quelque chose',
'sometime' : 'parfois',
'sooner' : 'plus tÃ´t',
'soothsayer' : 'devin',
'sorrow' : 'chagrin',
'sorry' : 'Pardon',
'sought' : 'recherchÃ©',
'souls' : 'Ã¢mes',
'sound' : 'du son',
'sovereign' : 'souverain',
'spare' : 'de rechange',
'speak' : 'parler',
'speaks' : 'parle',
'special' : 'spÃ©cial',
'speech' : 'discours',
'speed' : 'la vitesse',
'spend' : 'dÃ©penser',
'spirit' : 'esprit',
'spite' : 'dÃ©pit',
'spoke' : 'parlait',
'sport' : 'sport',
'spring' : 'printemps',
'staff' : 'Personnel',
'stain' : 'tache',
'stand' : 'supporter',
'stars' : 'Ã©toiles',
'state' : 'Etat',
'steal' : 'voler',
'steel' : 'acier',
'steward' : 'intendant',
'still' : 'encore',
'stomach' : 'estomac',
'stone' : 'calcul',
'stood' : 'se tenait',
'store' : 'boutique',
'storm' : 'orage',
'story' : 'rÃ©cit',
'straight' : 'tout droit',
'strange' : 'Ã©trange',
'street' : 'rue',
'strength' : 'force',
'strike' : 'la grÃ¨ve',
'stroke' : 'accident vasculaire cÃ©rÃ©bral',
'strong' : 'fort',
'struck' : 'frappÃ©',
'study' : 'Ã©tude',
'stuff' : 'des trucs',
'subject' : 'matiÃ¨re',
'substance' : 'substance',
'success' : 'SuccÃ¨s',
'sudden' : 'soudain',
'suddenly' : 'tout Ã  coup',
'suffer' : 'souffrir',
'suffolk' : 'suffolk',
'summer' : 'Ã©tÃ©',
'supper' : 'souper',
'surely' : 'sÃ»rement',
'surrey' : 'Surrey',
'suspect' : 'suspect',
'swear' : 'jurer',
'sweat' : 'transpiration',
'sweet' : 'sucrÃ©',
'swift' : 'rapide',
'sword' : 'Ã©pÃ©e',
'swore' : 'jurÃ©',
'sworn' : 'jurÃ©',
'syracuse' : 'Syracuse',
'table' : 'table',
'tailor' : 'tailleur',
'taken' : 'pris',
'talbot' : 'talbot',
'tarry' : 'goudronneux',
'taste' : 'goÃ»t',
'taught' : 'enseignÃ©',
'teach' : 'enseigner',
'tears' : 'larmes',
'tedious' : 'fastidieux',
'teeth' : 'les dents',
'tells' : 'raconte',
'tempest' : 'tempÃªte',
'tender' : 'soumissionner',
'terms' : 'termes',
'thank' : 'remercier',
'their' : 'leur',
'themselves' : 'se',
'there' : 'LÃ ',
'therefore' : 'par consÃ©quent',
'therein' : 'la bride',
'these' : 'celles-ci',
'thief' : 'voleur',
'thing' : 'chose',
'think' : 'pense',
'third' : 'troisiÃ¨me',
'thomas' : 'Thomas',
'those' : 'ceux',
'though' : 'bien que',
'thought' : 'pensÃ©e',
'thrive' : 'prospÃ©rer',
'throat' : 'gorge',
'throne' : 'trÃ´ne',
'through' : 'par',
'throw' : 'jeter',
'thrust' : 'poussÃ©e',
'thunder' : 'tonnerre',
'times' : 'fois',
'title' : 'Titre',
'together' : 'ensemble',
'tongue' : 'langue',
'tonight' : 'ce soir',
'touch' : 'toucher',
'toward' : 'vers',
'tower' : 'la tour',
'train' : 'train',
'traitor' : 'traitre',
'tread' : 'bande de roulement',
'treason' : 'trahison',
'treasure' : 'TrÃ©sor',
'trial' : 'procÃ¨s',
'tribunes' : 'tribunes',
'trick' : 'tour',
'triumph' : 'triomphe',
'trouble' : 'difficultÃ©',
'truly' : 'vraiment',
'trumpet' : 'trompette',
'trust' : 'confiance',
'truth' : 'vÃ©ritÃ©',
'turns' : 'se tourne',
'twice' : 'deux fois',
'tyrant' : 'tyran',
'ulysses' : 'Ulysse',
'uncle' : 'oncle',
'under' : 'sous',
'understand' : 'comprendre',
'undertake' : 'entreprendre',
'undone' : 'dÃ©fait',
'unhappy' : 'malheureux',
'unknown' : 'inconnue',
'unless' : 'sauf si',
'until' : 'jusqu Ã ',
'unworthy' : 'indigne',
'utter' : 'prononcer',
'valentine' : 'Valentin',
'valiant' : 'vaillant',
'valour' : 'valeur',
'vantage' : 'avantage',
'vengeance' : 'vengeance',
'venice' : 'venise',
'version' : 'version',
'victory' : 'la victoire',
'villain' : 'scÃ©lÃ©rat',
'viola' : 'alto',
'violent' : 'violent',
'virtue' : 'vertu',
'visit' : 'visite',
'voice' : 'voix',
'walls' : 'des murs',
'warlike' : 'guerrier',
'warrant' : 'mandat',
'waste' : 'dÃ©chets',
'watch' : 'regarder',
'water' : 'eau',
'wealth' : 'richesse',
'weapons' : 'armes',
'weary' : 'se lasser',
'weeds' : 'mauvaises herbes',
'weeping' : 'larmes',
'weight' : 'poids',
'welcome' : 'Bienvenue',
'wench' : 'jeune fille',
'whence' : 'd oÃ¹',
'where' : 'oÃ¹',
'wherein' : 'oÃ¹',
'whether' : 'qu il s agisse',
'which' : 'lequel',
'while' : 'tandis que',
'whither' : 'oÃ¹',
'whole' : 'entier',
'whore' : 'putain',
'whose' : 'dont',
'widow' : 'veuve',
'willing' : 'prÃªt',
'window' : 'la fenÃªtre',
'wings' : 'ailes',
'winter' : 'hiver',
'wisdom' : 'sagesse',
'witch' : 'sorciÃ¨re',
'withal' : 'avec',
'within' : 'dans',
'without' : 'sans pour autant',
'witness' : 'tÃ©moin',
'wives' : 'Ã©pouses',
'wolsey' : 'Wolsey',
'woman' : 'femme',
'wonder' : 'merveille',
'works' : 'travaux',
'world' : 'monde',
'worse' : 'pire',
'worship' : 'culte',
'worth' : 'vaut',
'would' : 'aurait',
'wound' : 'blessure',
'wounded' : 'blessÃ©s',
'wrath' : 'colÃ¨re',
'wretch' : 'misÃ©rable',
'write' : 'Ã©crire',
'written' : 'Ã©crit',
'wrong' : 'faux',
'wrought' : 'forgÃ©',
'yield' : 'rendement',
'yonder' : 'lÃ -bas',
'young' : 'Jeune',
'yours' : 'le tiens',
'yourself' : 'toi mÃªme',
'youth' : 'jeunesse',
}
for line in fileinput.input('t8.shakespeare - dummy.txt', inplace=True):
	for search_text in replace_texts:
		replace_text = replace_texts[search_text]
		line = line.replace (search_text,replace_text)
	print (line, end=' ' )


end = time.time()
T_delta =end -start

print('Time to process[sec]:',T_delta)
print('Memory used :',psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2 ,"Mb")