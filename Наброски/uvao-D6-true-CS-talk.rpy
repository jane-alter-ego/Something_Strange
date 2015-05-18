# Д6-общение с Виолой в медпункте и допрос Шурика
#
# Устанавливает флаг Полной Информированности alt_uvao_D6_CS_vetrov
# используется флаг Большого Побега alt_day2_us_escape, и флаги обхода медпункта в д2
#
 # TODO: Спрайты, фоны, звуки!
label alt_day6_true_CS_talk:
    # Долгий разговор с Виолой под чай с печеньками
    $ alt_uvao_D6_CS_vetrov = True
    "Вволю наумывавшись ледяной водой, я направился к медпункту как был - прямо с полотенцем через плечо. Ничего, свои люди."
    "Впрочем, подойдя к двери, я всё-таки решил постучаться. Как-никак, медицинский кабинет, мало ли что…"
    cs "Открыто, открыто!"
    # входим
    me "Доброе утро, Виолетта!"
    "Увидев меня, Виолетта рассеянно помахала рукой:"
    cs "Да, доброе… Сядь куда-нибудь, я сейчас…"
    "И она снова забарабанила по клавиатуре передового достижения отечественного компьютеростроения."
    "К некоторому моему удивлению, Шурика в медпункте видно не было."
    "Я уселся на кушетку и приготовился ждать."
    th "Интересно, где Шурик? Наверное, его уже выпустили."
    dreamgirl "Или наоборот, у него опять сорвало крышу и он убежал в леса."
    "Я поёрзал на жестком гладком покрытии кушетки, безуспешно пытаясь устроиться поудобнее.{w} Если бы меня на ночь уложили спать на это прокрустово ложе, я бы тоже сбежал, пожалуй!"
    th "Главное, чтобы на этот раз {i}не меня{/i} отправили за ним бегать. Вчерашних впечатлений мне вполне достаточно."
    "Заскучав, я покосился на монитор. Кажется, такие назывались алфавитно-циферными?{w} Жаль, что я в подобных раритетах не разбираюсь."
    dreamgirl "Не \"циферный\", а алфавитно-цифровой."
    "Прозвучал в голосе надзидательный голос Шизы."
    dreamgirl "Забавно - память у нас общая на двоих, но почему-то пользоваться ей как следует умею только я."
    th "Это называется разделением обязанностей. Я занимаюсь сложными мыслительными процессами. Не барское это дело - отвлекаться на всякую рутину."
    "Препираться с собственным подсознанием было довольно странным занятием, но люди со скуки чего только не делают."
    "Кажется, Шизе тоже было скучновато, потому что довольно скоро голос в моей голове поинтересовался:"
    dreamgirl "Кстати, а зачем тебе разбираться в этом хламе, который здесь считают за компьютеры?"
#
    th "Ну… Смог бы больше узнать об уровне {i}их{/i} технологического развития.{w} Пока что всё, что я здесь видел, не даёт никаких стоящих привязок."
    th "Тот же \Икарус\", например - он может и на тридцать лет устареть, а его всё будут использовать, если только не развалится раньше."
    dreamgirl "Ну так и комп этот ни о чём не говорит. Может быть, он последней модели, а может - старьё убогое, которое попросту выбросить жалко."
    "Довод был веским, возразить было особенно нечего. Я мысленно вздохнул:"
    th "Ну, может, хоть покопался бы в документах на нём, приведись такой случай. А так непонятно даже, что и как там запускать…"
    th "Да, жаль не удасться пойти по техническому пути поиска ответов."
    if alt_day2_club_join_cyb:
        dreamgirl "Чего это ты вдруг так приуныл? Наведайся к кибернетикам, у них там похожий комп, помнится, был, авось помогут. А там дальше сам сообразишь, тыжпрограммист."
        th "Да не, бред какой-то несёшь."
        dreamgirl "Да."
        "Согласился внутренний голос."
        dreamgirl "И имею на то полное право."
    else:
        th "Впрочем, не больно-то и хотелось."
    "Голос Виолы прервал мою беседу с подсознанием."
    cs "Всё!"
    "Нанеся несколько особенно резких ударов по клавишам, Виола выключила компьютер."
    cs "Ох, если бы ты знал, пионер, насколько у меня из-за всего этого прибавилось бюрократической волокиты!"
    "Она откинулась на спинку стула и с удовольствием потянулась.{w} Я поспешно перевёл взгляд на таблицу для проверки зрения."
    cs "Мне и так хватает регулярной писанины, а после вчерашних подвигов Александра я теперь до осени буду отчёты писать."
    "Она села прямо и осуждающе посмотрела на меня:"
    cs "Вот скажи мне, Семён, неужели нельзя было обойтись без этой беготни?"
    "Впрочем, увидев моё возмущённое лицо, Виола поспешила сменить гнев на милость:"
    cs "Ладно, ладно, не обижайся!{w} Я знаю, что ты здесь не при чём, а наоборот, проявил себя героем, и всё такое.{w} Просто если что-то мне и не нравится в моей работе, так эта вот писанина."
    "Она недовольно поморщилась - похоже, это действительно было для неё больной темой.{w} Потом кивнула на монитор перед собой:"
    cs "Спасибо, хоть эту железяку выделили, писать всё это от руки было бы просто адской мукой."
    me "Ну, если у Вас {i}медицинский{/i} почерк…"
    "Почувствовав, что хватил несколько через край, я поспешно заткнулся, но Виолетта только рассмеялась:"
    cs "В точку, пионер, в точку! Здесь у нас с начальством действительно была вполне обоюдная заинтересованность."
    "Решительно отвернувшись от стола, она заявила:"
    cs "Вот что! Я уже часа два как на ногах, так что изрядно проголодалась.{w} Да и тебя на завтрак лучше не отпускать, а то убредёшь куда-нибудь…"
    "Отмахнувшись от моих возражений, она продолжила:"
    cs "…Поэтому предлагаю позавтракать прямо здесь и перейти наконец к {i}делу{/i}."
    "Сделав ударение на последнем слове, она искоса взглянула на меня, и, видимо, удовлетворившись достигнутым эффектом, продолжила как ни в чём не бывало:"
    cs "Уверена, у тебя накопилось достаточно вопросов.{w} На некоторые из них у меня даже найдутся ответы."
    cs "Но сначала - завтрак! Пошарь-ка под изголовьем кушетки, там должна быть плитка. Керамическая."
    "Изрядно озадаченный, я заглянул под кровать. Действительно, там обнаружилась солидных размеров облицовочная плитка, которую я и извлёк на свет божий."
    "Тем временем Виола встала и, покопавшись в одном из своих шкафчиков, достала оттуда приземистый аллюминиевый чайник и, почему-то, провод."
    dreamgirl "Ух ты, а вот это и вправду раритет!"
    "Наполнив чайник водой, Виола отобрала у меня плитку и положила её на стол. Водрузив чайник сверху, она кивнула на мой недоумённый взгляд:"
    cs "Противопожарная безопасность! Учись, студент!"
    "Сзади у чайника обнаружился керамический разъём. Подключив к нему один конец провода в матерчатой изоляции, Виолетта воткнула вилку на другом его конце в розетку и, удовлетворённо кивнув, подошла к холодильнику."
    "…"
    "Как оказалось, в холодильнике и в ящиках стола можно было найти не только лекарства, так что через десять минут мы уже пили крепкий чай с бутербродами с сыром и хрустели печеньем \"Юбилейное\""
    me "Виола, скажите, а как у Шурика дела?"
    "Поинтересовался я, не отрываясь от еды. Медсестра отмахнулась от меня кусочком печенья:"
    cs "Да нормально всё с вашим Трофимовым. Отоспался, и теперь бодрый как огурчик.{w} Психосоматика у него в порядке, разве что налицо спутанность воспоминаний о вчерашнем дне."
    cs "Я пока что его отправила отсюда, чтобы не мешался. Велела перед обедом заглянуть, попробую его разговорить - может и вспомнит что-нибудь."
# Возможно, нужно больше умных букв про состояние Шурика и причины оного. Всё-таки медик-научник.
    "Когда с едой было покончено, заметно подобревшая Виола благосклонно кивнула:"
    cs "Спрашивай."
    me "Э-э-э… Виолетта, а может быть, лучше Вы мне сначала расскажете что-нибудь? Обрисуете в общих чертах, так сказать?"
    cs "Что же, это неплохая мысль. Пожалуй, так даже лучше будет, времени не так много осталось - Сегодня ведь последний день смены, ты в курсе, кстати?"
    jump alt_day6_true_CS_talk_main
    
label alt_day6_true_CS_talk_short:
    $ alt_uvao_D6_CS_vetrov = False
    # Короткий разговор с Виолой
    # Про эф.Ветрова не узнаём
    #
    # Зато узнаём, что завтра - последний день смены (ВЦ сожалеет, что ГГ пришёл так поздно, времени, мол, и так мало осталось)
    "Когда я добрался наконец до медпункта, время уже явно приближалось к полудню."
    "Подойдя к двери, я решил постучаться. Как-никак, медицинский кабинет, мало ли что…"
    cs "Открыто!"
    # входим
    me "Добрый день, Виолетта!"
    "Увидев меня, Виолетта нахмурилась."
    cs "Я уже думала, ты вовсе не придёшь. Что, так сильно напугала тебя вчера на ужине, или у тебя утро начинается с полудня?"
    me "Да я…"
    cs "Ладно, садись. Чай будешь?"
    "Виола кивнула на стоящий на письменном столе странноватого вида металлический чайник, судя по проводу - электрический."
    me "Да спасибо, я только что поел…"
    "Промямлил я, усаживаясь на краешек кушетки. Виола слегка подняла одну бровь, но больше своё удивление по поводу столь позднего завтрака никак не показала."
    cs "Ну что же, тогда к делу. Времени не так много, скоро Трофимов должен придти, я его ещё с утра выпроводила позавтракать и подышать воздухом, чтобы не мешался здесь, велела перед обедом зайти."
    "Она вновь одарила меня недовольным взглядом, явно досадуя на моё опоздание, и я поспешил увести разговор несколько в сторону:"
    me "Ой, да, Шурик! Как у него дела, кстати? Не бузил больше?"
    cs "Да нормально всё с вашим Трофимовым. Отоспался, и теперь бодрый как огурчик.{w} Психосоматика у него в порядке, разве что налицо спутанность воспоминаний о вчерашнем дне."
    cs "Как придёт, попробую его разговорить - может и вспомнит что-нибудь."
    me "Так, может быть, я потом к Вам зайду, когда времени побольше будет?"
    cs "Потом времени не будет вовсе. Сегодня ведь последний день смены, ты что, не знал?"

label alt_day6_true_CS_talk_main
    # Общий блок по длинному и короткому разговорам
    if not alt_uvao_D5_evening_sl:
        "От неожиданности я подскочил на месте."
        me "Как последний? Меньше недели ведь прошло!"
        cs "Ну так ты и… гм… прибыл сюда не к началу смены. Сегодня прощальные ужин и дискотека, а завтра на автобус до райцентра - и по домам."
        "Я почувствовал, что в глазах темнеет."
    else:
        me "Вот только недавно узнал…"
        cs "И действительно, кому это придет в голову прислушиваться к словам вожатой на линейке…"
# Здесь нужна рефлексия о том, как мало успелось и хочется ли возвращаться назад.
    me "Виола, скажите…{w=1} А я что, тоже… домой?"
    "Последнее слово далось мне с неожиданным трудом. Я вдруг отчётливо понял, что язык не поворачивается назвать приютившее меня до этого место - домом."
    window hide
    $ set_mode_nvl()
    window show
    th "Да, именно приютившее. Место, где можно спать и хранить одежду, для которой сейчас не сезон, - и только. Место, куда приходишь потому, что больше идти некуда, а не потому, что хочешь туда придти.{w} Место, где меня никто не ждал и не будет ждать."
    "Голос Шизы в моём мозгу прозвучал спокойно и как-то даже буднично:"
    dreamgirl "Подумай-ка лучше вот о чём - весь {i}тот{/i} мир - можешь ли ты назвать его своим домом?{w} А главное - хочешь ли ты его так называть?"
    dreamgirl "Что связывает тебя с ним? Работа, которая тебе неинтересна и неприятна ровно настолько, чтобы её можно было терпеть? Те несколько человек, которые считаются твоими друзьями только потому, что ты всё ещё не удалил их номера из телефона?"
    dreamgirl "Аноны всех мастей, эти призраки по ту сторону экрана, которым нет никакого дела до тебя, а тебе - до них?{w} Подумай."
    th "Но ведь и здесь я чужой! Здесь меня тоже никто не ждёт и никому до меня нет дела!"
    dreamgirl "Ты прав.{w} Почти прав. Тебе и здесь совсем нетрудно будет отгородиться ото всех стеной безразличия, ты неплохо освоил это умение, и тебя рано или поздно оставят в покое."
    dreamgirl "Однако, если тебе удастся ухватиться за этот шанс, ты сможешь попробовать сделать что-то иначе."
    dreamgirl "Вспомни, всем ли людям, встреченным тобой за эти несколько дней, не было до тебя никакого дела?"
    dreamgirl "Да, с тобой никто не нянчился и на руках не носил. Да, над тобой подшутили пару раз не самым приятным образом - но именно подшутили, тебе не желали зла по-настоящему."
    dreamgirl "Зато когда ты из-за этих шуток остался голодным - тебя накормили. Помогли не по обязанности, а просто потому, что тебе была нужна помощь."
    dreamgirl "Кстати, когда тебе вчера чуть не устроили внеплановую проверку содержимого черепа - никто ведь не заставлял Лену тебя спасать. Просто она могла помочь - и сделала это."
    th "Если уж на то пошло, если бы меня вчера не припахали к этим поискам, то мне вообще ничего бы не угрожало!"
    dreamgirl "Это так, но что странного в том, что люди, готовые тебе помочь {i}просто так{/i}, ожидают того же самого и от тебя?{w} Не потому, что ты у них в долгу, а просто потому, что кому-то нужна помощь, а ты можешь помочь."
    th "Тебя послушать, так здесь просто идеальное общество какое-то! Царствие небесное на земле! Все люди братья, все помогают друг другу!"
    dreamgirl "Ну разумеется, нет. Заметь только, что и не каждый человек другому обязательно - волк. Подумай, хочешь ли ты быть кому-то нужным и готов ли к тому, что кто-то снова будет нужен тебе?"
    dreamgirl "Так что ещё раз повторю - ты можешь попытаться сделать что-то иначе."
    dreamgirl "Умный учится на чужих ошибках, дурак - на своих. А как называется тот, кто не учится ни на чьих?"
    window hide
    $ set_mode_adv()
    window show
    cs "Да, Семён, ты завтра тоже отправишься домой, это вне всякого сомнения."
    "Подала наконец голос молчавшая всё это время Виолетта."
    "Я внезапно почувствовал, что не могу вздохнуть, словно чьи-то крепкие бесжалостные руки сжали горло, начисто перекрыв кислород."
    th "Неужели эта нелепая фантазия о возможности остаться здесь, этот призрачный шанс, упомянутый Шизой, и вправду так уж нужны мне?"
    "Не сводящая с меня глаз Виола вдруг слегка улыбнулась."
    cs "Впрочем, я не возьмусь сказать наверняка, где именно окажется этот самый дом, куда ты отправишься - это будет зависеть только от тебя."
    "Вероятно, моё лицо в этот момент представляло собой то ещё зрелище, потому что она несколько секунд с явным интересом меня разглядывала, прежде чем пуститься в объяснения."
    cs "Видишь ли, то, что ты попал в этот лагерь, да и вообще в наш мир - не совсем случайно. Такое случается время от времени с людьми, которые там, {i}у вас{/i}, не имеют крепких социальных связей, привязанностей, постоянно чувствуют себя ненужными."
    cs "Разумеется, такое происходит далеко не со всеми, на наше счастье - иначе здесь уже не повернуться было бы от попаданцев."
    "Тут она улыбнулась немного виновато и развела руками."
    cs "Надеюсь, ты простишь мне профессиональный жаргон - \"попаданцы\". Не слишком-то благозвучно, но официальное \"лица, непроизвольно осуществившие переход через точку прокола\" даже руководство избегает употреблять." # официальный термин может быть и другим, но непременно громоздким и неуклюжим
    "Я робко кивнул, и Виола продолжила:"
    cs "Ну так вот, слабо привязанного к своему родному миру человека иногда может, скажем так, \"притянуть\" сюда. Причём это всегда происходит в местности с достаточно большим количеством благожелательно настроенных людей, готовых принять появление новичка за естественное событие."
    cs "Чаще всего это случается на курортах, в домах отдыха каких-нибудь. Ну или как здесь, например, - в пионерском лагере. Так или иначе, обязательно нужен мощный благоприятный эмоциональный фон - это обязательное условие для возникновения в этом месте точки прокола, как мы это называем."
    "Тут она посмотрела на меня с некоторым сомнением и осведомилась:"
    cs "Я не слишком заумно объясняю? Пока что всё понятно?"
    "Кажется, Виола вплотную подошла наконец к весьма важному для меня моменту, так что я лишь нетерпеливо отмахнулся:"
    me "Да понятно всё, понятно! Идею насчёт этих… попаданцев я уловил. Что дальше-то происходит с ними? Вернее, с нами…"
    "Виола усмехнулась моей нетерпеливости и продолжила:"
    cs "А дальше начинается процесс адаптации. Если он заканчивается успешной ассимиляцией, то в нашем мире становится на одного человека больше."
    cs "Если попаданцу не удалось здесь адаптироваться, то его, по-видимому, выбрасывает обратно в родной мир."
    me "И что же нужно для этой самой… успешной адаптации?"
    "Я затаил дыхание в ожидании ответа, но Виола лишь пожала плечами:"
    cs "Да ничего особенного, по большому-то счёту. Достаточно, чтобы человек действительно захотел остаться."
    cs "Попросту говоря, человек попадает сюда, только если он чужой {i}там{/i} и остаётся, если почувствует себя своим {i}здесь{/i}."
    me "А как понять, что адаптация прошла успешно?"
    "Виола мягко улыбнулась."
    dreamgirl "Вообще, она сегодня на редкость улыбчивая, ты не находишь?"
    cs "Я смотрю, тема адаптации тебя заинтересовала? Что же, ничего удивительного. Все хотят знать про своё будущее."
    cs "Видишь ли, в первое время попаданец сильно связан с местом перехода, удаляться от неё далеко он не может."
    cs "При попытке сделать это его либо отбросит назад, в район перехода, либо вообще выбросит обратно в родной мир - зависит от того, насколько он успел здесь закрепиться."
    if alt_day2_us_escape:
        cs "Кстати, подозреваю, что на второй день пребывания здесь ты уже испытал такой перенос в пространстве. Или я ошибаюсь?"
        "Я смущённо заёрзал на месте, вспомнив нашу совместную с Ульянкой авантюру."
        me "Ну, мы вроде бы как, действительно догнали проходящий состав и забрались в него, а потом проснулись снова на острове. Но я думал, всё это нам просто приснилось!"
        cs "Вот именно: {i}вам{/i}. Насколько мне удалось выяснить, Ульяна видела аналогичный сон, так что гипотеза о переносе представляется мне вполне вероятной."
        th "И всё-то она знает, даже то, что приснилось Ульянке…{w} Минуточку! Ульянка!"
        me "Виола, подождите, а Ульяна - она что, тоже из… Ну, нездешняя?"
        cs "Нет, она местная, это совершенно точно. А с чего ты это взял?"
        "Виолетта недоумённо посмотрела на меня поверх очков, и я смущённо потупился."
        me "Ну если это был не сон, то, получается, что её тоже перенесло вместе со мной…"
        cs "Ах вот ты о чём. Нет, здесь, вероятно, сыграло роль твоё присутсвие рядом. К сожалению, такие случаи вообще пока что плохо изучены.{w} Впрочем, всё это сейчас несущественно."
    cs "Важно то, что завтра лагерь опустеет, и привычный эмоциональный фон исчезнет. Поэтому при попытке уехать переноса в пространстве уже не произойдёт - тебя либо выбросит назад в твой родной мир, либо ты окончательно останешься в этом."
    cs "Так что через сутки с небольшим ты самостоятельно сможешь оценить, насколько успешно прошла твоя адаптация."
    "Виола замолчала, откинувшись на спинку стула. Молчал и я, переваривая услышанное."
# Чувствуем нарастающую панику - обратно тоскливо, здесь - ссыкотно
    me "Виола, скажите, а если я останусь здесь…"
    cs "Да не волнуйся ты так, Семён."
    cs "Не беспокойся раньше времени о том, чего ещё не случилось, да и выплывать совсем уж в одиночку тебе не придётся. С базовой социальной адаптацией тебе помогут, а дальше уже всё от тебя будет зависеть."
    "Она вдруг рассмеялась:"
    cs "Кстати, тебе сколько лет-то, {i}пионэр{/i}?"
    me "Э-э… Семнадцать?"
    cs "Ну да, правильно! Так всем и говори. Мало ли что там написано в каком-то странном паспорте несуществующей страны, пусть там даже и твоя фотография?"
    th "Так, похоже, что пальто моё нашлось…"
    cs "Просто не забывай, что по сравнению со среднестатистическим выпускником детского дома у тебя, можно сказать, есть фора в десять лет опыта взрослой жизни. Вернее будет, если сумеешь остаться."
# А и в самом деле, чего я паникую? прорвёмся!
# Чтобы отвлечься:
    me "Скажите, Виола, а зачем всё это? Я имею в виду, все эти переходы, точки… этих, как их… точки прокола… Вся эта возня с нами, попаданцами?"
    cs "Ну насчёт существования феномена проколов как такового - вопрос \"зачем\" ставить некорректно. Всё равно что спрашивать \"зачем светит солнце\". Проколы просто существуют, а мы их изучаем по мере возможности."
    cs "А что касается \"возни с попаданцами\", как ты выразился, то здесь же всё достаточно очевидно. Во-первых, люди прибывают, хотим мы этого или нет. Даже если отбросить элементарный гуманизм, всё равно гораздо практичнее сразу помочь им, чем получить впоследствии потенциально асоциальные личности."
    cs "Ну а во-вторых, большинство из попадающих сюда в итоге оказываются довольно полезны для общества. Люди способные, мыслящие, как-то больше склонны задумываться о тщетности всего сущего и заметно чаще оказываются чужими среди своих."
    dreamgirl "Кажется, тебе только что сделали комплимент, причислив к способным и мыслящим, ты не находишь?"
    th "Ну она же не сказала, что {i}все попаданцы{/i} обязательно такие…"
    "Словно подслушав наш разговор, Виола внезапно перешла, если так можно выразиться, на личности:"
    cs "Вот взять хотя бы тебя, например. Достаточно устойчив психически, чтобы сохранить адекватность поведения, попав абсолютно внезапно в непривычную обстановку…"
    "…Я вспомнил, как валялся в обмороке на полу домика вожатой в свой первый день здесь, и почувствовал, что краснею…"
    if semen_panique: # Паника возле автобуса
        "… А приступ паники и безумная беготня по дороге?"
        dreamgirl "Всё познается в сравнении. Возможно, другие вели себя еще хуже."
    cs "…и не лишён определённых артистических наклонностей, раз сумел не раскрыться ни перед кем из пионеров за это время."
    cs "Кроме того, демонстрируешь весьма похвальную любознательность, раз при встрече с визуализацией пошёл с ней на контакт, да и вообще, я смотрю, ты в это дело втянулся."
    "К этому моменту я от смущения уже готов был начать ковырять пальцем клеёнку на кушетке, так что ухватился за возможность сменить тему на несколько отвлечённую от моей персоны."
    me "Виола, вот, кстати…"
    "Я протянул ей смартфон."
    me "Вы просили Юлю сфотографировать."
    "Виола с любопытством разглядывала снимок."
    cs "Интересное проявление…{w} Порождает больше вопросов, чем ответов."
    me "Так кто она… что она такое?"
    cs "Видишь ли, пионер, проколы бывают двух видов. Обычный прокол открыт примерно неделю-другую, плюс-минус. О многих из них мы узнаем пост-фактум, когда попаданец возникает в нашем мире."
    cs "И изучать при этом особенно нечего - пока оборудование доставят, пока локализуют аномалию… Впрочем, подробности тебе вряд ли интересны."
    cs "Но иногда, по непонятным причинам, прокол получается аномальным - счет идет на годы, но переноса не происходит. И вот в них-то и заводятся подобные… э-э-э… существа. Мы считаем, что это одно из проявлений самого прокола."
    cs "Собственно, твоя фотография это подтверждает. Это ведь город из твоего мира, если я не ошибаюсь?"
    me "Да… Очень похоже на вид из моего окна.{w} Так это первая фотография аномалии, получается?"
    cs "Да. За последние семьдесят лет таких долговеременных прокола было всего четыре. И, как оказалось, обращаться с визуализациями следует с большой осторожностью."
    me "Почему вы тогда были так уверены, что со мной ничего не произойдёт?"
    cs "Общение с визу… с Юлей опасно для всех, кроме тебя. На тебя, как на субъекта переноса, у неё своего рода привязка, поэтому ты ничего не ощущаешь." 
    cs "Впрочем, от сумасшедствия попаданцы тоже не застрахованы."
    "Я буквально почувствовал, как спина похолодела от реплики внутреннего голоса:"
    dreamgirl "Не бойся, чувак, ты совершенно здоров."
    "На моё счастье, Виола не заметила, как я вздрогнул и всё это время продолжала:"
    cs "…роисходит с другими — ты видел вчера."
    "Мне стоило значительных усилий снова поймать нить разговора. Дабы показать, что слушаю, я, скорчив глубоко сочувствующее выражение лица, вставил:"
    me "Значит, это Юля Шурика так…"    
    if alt_uvao_D6_CS_vetrov: # длинный разговор за чаем
        "Виола сделала небольшую паузу, что я счёл за положительный ответ. Потом она продолжила:"
        cs "Я думаю, Юля выполняет роль… как бы лучше выразиться… проводника между реальностями."
        cs "Помимо этого есть мнение, что она бессознательно выполняет ещё и защитную функцию - не допускает провалов случайных людей между реальностями."
        cs "Вообще-то это уже из разряда домыслов… Как бы там ни было, всё приблизительно сходится. Вот, смотри."
        cs "Факт первый. Для перемещения между реальностями необходимо как-то с взаимодействовать с аномалией." 
        cs "Факт второй. Как правило, большинство попыток контакта с ней заканчивались либо потерей памяти, либо тяжёлыми психическими расстройствами."
        cs "Делаем вывод, что для успешного путешествия между реальностями нужно пройти некий барьер, не дающий возможности случайным людям как-либо контактировать с ней."
        cs "Говоря совсем простым языком - взаимодействия между Юлей и разумом, сознанием человека не произойдёт, если нечему будет взаимодействовать."
        me "Значит…?"
        cs "Да. И к сожалению, это иногда происходит дорогой ценой. Полагаю, вы вчера успели весьма и весьма вовремя."
        cs "Как жаль, что в семьдесят четвёртом мы ещё об этом не знали…"
        me "А что тогда было?"
        "Виола помрачнела, и я пожалел, что своим вопросом пробудил в ней какие-то неприятные воспоминания. Я уже было хотел дать заднюю, как Виола собралась с мыслями и ответила:"
        cs "Куратор мой погиб."
        +me "Оу..."
        "Только и сумел выдавить я."
        "В воздухе на некоторое время повисло тяжёлое молчание."
        cs "Решила Юлия Валерьевна в обход всех инструкций контакт с визуализацией наладить. Наладила… Спасибо, эффектом Ветрова лагерь не накрыло."
        Виола говорила с неким нарочитым безразличием, однако я ощущал, насколько ей эта тема неприятна. Поэтому, я решил помочь ей, направив разговор в нужное мне русло:"
        me "Эффект Ветрова? Что это?"
        cs "А, правильно, ты же не в курсе. Защитный эффект аномалии. Назвали, кстати, по фамилии попаданца из того прокола."
        cs "Когда он впервые проявился всё было примерно так же, как и у нас сейчас. Появился субъект переноса, началась адаптация."
        cs "А потом появилось что-то вроде того, что ты назвал Юлей. Кому-то из начальства наград захотелось, погнали взвод вояк на захват. Только они вошли, а местность возьми и закройся, туманный пузырь вокруг турбазы появился."
        cs "Пробовали войти — не получается, пара минут в тумане и выходишь с другой стороны. Ну, что делать… Оцепили, стали ждать. На четвёртый день двое из тумана этого вышли, всё, что от группы захвата осталось."
        cs "Один не помнил вообще ничего, а второй нёс какую-то чушь про карателей, девочек в эсэсовской форме, демонов каких-то… Так что единственное, что удалось вынести из той истории — фамилию субъекта переноса. Так и назвали - эффект Ветрова."
        "Мы помолчали."
        me "Хорошо, я понял. Те люди как-то взаимодействовали с аномалией и их \"накрыло\". Но что насчёт меня? Я не помню, чтобы я с ней как-то общался в своём мире."
        cs "А ты подумай. Человек не обязательно должен выступать инициатором взаимодействия. Иногда аномалия, а в нашем случае, Юля может перетянуть человека в свою реальность. Впрочем, ей обязательно нужно на то согласие."
        "Голос Виолы немного притих и она добавила:"
        cs "Как правило, легче соглашаются те, кого в своём мире мало что держит."
        "С грустью я осознал, насколько она права. Спроси меня всего пару месяцев назад, будь у меня возможность кардинально поменять мир вокруг себя без надежды на возвращение или же оставить всё как есть, я бы ответил не задумываясь."
        dreamgirl "Тебя и спросили."
        play music knock fadein 5
        window hide
        scene anim prolog_1
        window show
        "В голове вдруг встал нечёткий образ девочки из сна. Мы встречаемся в этом повторяющемся сне уже чуть больше года, но вот что странно: в моей памяти так и не отпечаталось как она выглядит."
        "Наутро я всегда помню сон в общих чертах, из памяти стирается только её внешность. Почему? Сколько я себя не спрашивал, мне никогда не удавалось найти ответа."
        "Девочка медленно идёт в мою сторону. Время словно замирает, а я просто стою и жду, пока она подойдёт ближе. Для меня становится очень важным рассмотреть её."
        "Отчаявшееся сознание предпринимает очередную бесплодную попытку. Какой в ней смысл, если я всё равно ничего не вспомню утром?"
        "Девочка между тем подходит достаточно близко, чтобы я смог разглядеть её одежду. На ней красное детское платьице. Красивое. А ещё почему-то совсем нет никакой обуви."
        "Вот она делает ещё пару шагов и я с удивлением замечаю, что платьице вовсе не новое - оно порвалось в нескольких местах и явно в разы старше его обладательницы. Мамино?"
        "Девочка медленно приближается ко мне. Я никак не могу разглядеть её лицо, сколько не пытаюсь всматриваться."
        "Память почему-то усердно твердит мне, что я её знаю, что я определённо знаком с ней."
        "Она делает ещё несколько шажков. Неожиданно моему взгляду открываются миленькие ушки на её голове. Может, накладные?" 
        "Она подходит всё ближе и ближе, а я вдруг обращаю внимание на то, что откуда-то из-за спины у неё выныривает длинный кошачий хвостик."
        "Вот нас разделяет всего несколько метров. Мне ясно открывается что она вовсе не человек, а ушки, казавшиеся издалека накладными, вовсе таковыми не являются."
        "Мне почему-то совсем не страшно."
        "Девочка подходит почти вплотную и поднимает на меня взгляд."
        "Мне наконец-то удаётся разглядеть её лицо. Она, не моргая, тоже смотрит на меня ореховыми глазами, полными любопытства и...надежды?"
        "Я застываю от её внимания и не могу отвести взгляда. Мы просто стоим и смотрим друг на друга."
        "Она первой нарушает тишину."
        uv "Ты пойдёшь со мной?"
        window hide
        stop music fadeout 5
        "Я не успеваю ответить. Её голос словно разрезает пространство между содержимым моей головы и реальностью."
        "Детальки паззла,кажется, понемногу сходились воедино."
        cs "…?"
        "Судя по всему она что-то спросила, но я ничего не разобрал. Голос Виолы был каким-то...ватным? Я потряс головой, пытаясь прийти в норму."
        me "А? Что?"
        cs "Всё понятно с тобой. Я уж подумала, ты из реальности выпал."
        "Кажется, Виола поняла, что сморозила редкостную глупость, глядя на то, как меняется моё выражение лица."
        cs "Кхм. Извини, неловко получилось."
        me "Это ничего. Кстати о выпадениях из реальности. Я ведь не первый попаданец, верно?"
        cs "Не первый."
        me "И кто же был первым? Вы знали его?"
        cs "Не вживую. Я тогда ещё и не родилась, вообще говоря."
        cs "Впрочем, думаю, ты с ним тоже в какой-то степени знаком."
        me "Да?"
        dreamgirl "Ага. А ещё он общается с тобой телепатически сквозь время благодаря высокоразвитым технологиям прямо сейчас."
        #play sound sfx_scary_sting
        th "Серьёзно?"
        $ renpy.pause(2.0)
        dreamgirl "Ха, повёлся."
        cs "Ну, даже догадатьтся не попробуешь кто?"
        dreamgirl "Да, интересно, это что за покемон?"
        "Мне почему-то казалось, что ответ лежит на поверхности, что он совсем очевиден. Однако, в голову ничего не лезло."
        "Виоле, похоже, надоело разглядывать мою озадаченную физиономию, так что она намекнула:"
        cs "Ему, кстати, памятник стоит."
        me "Генда? Игорь Генда - первый попаданец?"
        "Сказать что я не был готов к такому - ничего не сказать."
        cs "Ну, по крайней мере он первый из тех, о ком нам известно доподлинно."
        cs "Он же, кстати, и положил начало изучению попаданцев."
        dreamgirl "Ага, как в том анекдоте. Физики - кучка атомов, которые изучают сами себя."
        me "То есть он основал этот лагерь для изучения попаданцев? И памятник ему здесь именно поэтому, а не потому что он светило науки?"
        cs "Нет, аномалия здесь появилась уже после того, как лагерь был построен. А с памятником просто совпадение получилось."
        me "Ну хорошо… Но все равно ведь получается, что \"Совёнок\" - уникальное место, ведь так?"
        cs "Это уж точно. Аномалия здесь открылась… дай посчитать… 33 года назад."
        me "Сколько?! И что, все эти годы тут бегает Юля?"
        cs "Нет, она появилась не сразу - через несколько лет после открытия аномалии. С каждом годом проявлялась все чаще, вот Юлия Валерьевна и решила с ней пообщаться…"
        cs "Когда ее нашли повесившейся в кабинете, думали, что теперь прокол уже закроется. Самоубийство должно было напрочь перехерить весь эмоциональный фон - какие уж тут попаданцы!"
        cs "Меня, как ее подопечную, оставили приглядывать, исследовать процесс коллапса прокола. Построили новые корпуса, перенесли лагерь…"
        cs "Но никакого коллапса не произошло! Прокол оставался открытым, хотя Юля долгое время и не проявлялась."
        cs "А в  последние лет пять снова начались слухи про дикую девочку-кошку, которая ворует вещи и продукты. Как раз тогда и Ольгу сюда назначили."
        me "Погодите, но ведь если \"Совёнок\" такой уникальный - где исследователи? Вся аппаратура, ученые, лаборатории всякие - где всё это?{w} Бункер с парой осциллографов?"
        cs "А, ты и туда влез, пионер… Да, это наши приборы, хотя толку с них не очень-то много.{w} Все дело в том самом эмоциональном фоне."
        cs "Много раз пробовали - привозили тонны приборов, присылали исследователей - результат был один.{w} Прокол немедленно закрывался, а недоадаптированный попаданец растворялся в воздухе - иногда прямо в людных местах."
        cs "Даже если исследователей маскировали под обыкновенных отдыхающих - это не помогало. Где-то с пятого раза поняли, что это - не совпадение, а правило."
        cs "Курорт и замаскированный под курорт полигон исследований кардинально отличаются именно эмоциональным фоном."
        cs "А сильное ухудшение фона влечет за собой закрытие прокола. Всегда… за исключением \"Совёнка\"."
        me "Но почему?"
        cs "Никто не знает. У нас не так уж много знаний о природе аномалии. Фактически, мы здесь в положении алхимиков, пытающихся разобраться в работе ядерного реактора."
        # продолжение длинного разговора
        # Продложаем говорить про Юлю, обсуждаем воздействие визуализации на людей, а заодно и основы мирозданья ваапче
        
        # Вставить в умные тексты по поводу физической подоплёки проколов и прочего примерно следующее:
        # me "И что, вот так вот всё просто? Я имею в виду, Вы так легко об этом говорите - <проколы, переходы, умные_слова>…"
        # cs "Послушай, Семён, вот ты ходишь, разговариваешь, и вообще мыслишь. Это же не означает, что ты можешь в подробностях описать природу этих процессов, ну или хотя бы сообщить мне химический состав желудочного сока, с помощью которого сейчас переваривается съеденный тобой завтрак. Я, как врач, знаю об этом побольше твоего, но тоже до определённого предела."
        # cs "Во всякой области знаний есть узкие специалисты, но их мало, и понять их могут, в основном, такие же, как они сами, специалисты. Или вот, скажем, термоядерный синтез. Я в нём совершенно не разбираюсь и подозреваю, что ты тоже, но это ведь не мешает нам греться на солнышке."
        # me "Спасибо за разъяснения, товарищ {i}Коллайдер{/i}… Ой, извините, Виолетта {i}Церновна{/i}!"
        # cs смеётся "Ну наконец хоть кто-то оценил!"
        #
        #
        "Я хотел спросить что-то ещё, но наш разговор был прерван стуком в дверь."        
    else:
        # Продолжение короткого разговора, а скорее - заглушка или согласующий переход к alt_day6_true_SH_exam
        "Я собирался как следует расспросить Виолу обо всем, но тут в дверь постучали."

label alt_day6_true_SH_exam:
    play sound sfx_knock_door7_polite
    sh "Можно?"
    "В дверь нерешительно заглянул наш вчерашний \"ценный груз\"."
    cs "Да-да, входи, пионер. Позавтракал? Самочувствие не ухудшилось?"
    sh "Н-нет… все в порядке, я себя хорошо чувствую."
    th "И вправду, выглядит вполне нормально."
    cs "Все равно, лишний раз {i}осмотреть{/i} не помешает.{w} Проходи, раздевайтся."
    th "Виола снова в своем репертуаре… Хорошо, что на мне не практикуется. Наверное, потому что мы теперь \"коллеги\"?"
    dreamgirl "Просто ты ей нужен более-менее соображающий, а не пускающий слюни. А Шурик наверняка от нее с утра натерпелся, поэтому и зашуганный такой."
    me "Виолетта Церновна, я тогда пойду?"
    "Шурик с мольбой посмотрел на меня. Оставаться с Виолой лицом к лицу ему явно не хотелось."
    cs "Нет, Семен, останься. Вдруг мне потребуется помощь в {i}процедурах{/i}?"
    dreamgirl "Что ты там говорил, \"коллега\"?"
    if med_done: # Если в д2 заходили в медпункт
        if alt_day2_rendezvous in [1,2,3]:
            th "Теперь моя очередь стоять в уголке и хихикать!"
            dreamgirl "Тогда вместо Шурика надо пригласить "
            if alt_day2_rendezvous == 1:
                extend "Лену, "
            elif alt_day2_rendezvous == 2:
                extend "Славю, "
            elif alt_day2_rendezvous == 3:
                extend "Алису, "
            extend "чтоб сполна расплатиться."
        else:
            th "Хоть оценю со стороны, насколько жутко это выглядит."
    else:
        "Я отошел и оперся о край стола, чтобы не мешать {i}осмотру{/i}."
    "Несмотря на многозначительные намеки Виолы, медосмотр завершился довольно быстро."
    cs "Да, пионер, ты практически здоров. Физически."
    sh "А… психически?"
    cs "А голова - предмет тёмный… Впрочем, будет полезно, если ты расскажешь, чем ты вчера занимался и что с тобой произошло."
    "Шурик задумался."
    sh "Вчера? Я вчера хотел детали поискать… Радиодетали, для робота… Нам в клубе не хватает, и мы никак закончить не можем."
    "Виола поошрительно кивнула."
    cs "Хорошо, детали."
    sh "А я, когда на чердаке копался, нашел старую схему лагеря. На ней было бомбоубежище нарисовано, и я подумал… что там может быть старая аппаратура."
    th "Что-то я сомневаюсь, что он за аппаратурой туда попёрся…"
    cs "Понимаю. А дальше?"
    sh "Дальше… не помню.{w} Помню, что ходил по каким-то тоннелям, шахтам… а потом - очнулся от того, что меня Ольга Дмитриевна по лицу бьёт."
    sh "Что потом - вы знаете…{w} Может, я чем-то в шахтах надышался? Каким-нибудь газом?"
    cs "Не исключено…"
    "Она достала из шкафа растрёпанную картонную папку, подписанную \"Трофимов А.\", пролистала страницы, сплошь покрытые врачебными каракулями…"
    cs "Вот что, пионер. Все с тобой будет в порядке, но лучше тебе не переутомляться.{w} Отдыхай, гуляй, дыши свежим воздухом. Купайся."
    cs "И поменьше торчи в вашем клубе. У вас там от канифоли не продохнёшь, и здоровому-то поплохеет, а тебе сейчас это вообще противопоказано."
    "Шурик печально вздохнул."
    sh "Но мы тогда… Мы хотели робота доделать… А то не успеем до конца смены."
    cs "Здоровье важнее! {w} Все, кыш отсюда оба."
    "Шурик торопливо выскочил за дверь, завязывая галстук на ходу. Я не спеша последовал за ним."
    window hide
    scene bg ext_aidpost_day with dissolve
    window show
    th "Да уж. От такого объёма информации голова скоро взорвется."
    "Предписание Виолы, насчет отдыха и купания, показалось мне весьма заманчивым. Почему бы и нет?"

    #//Шурик проснулся утром и был выпущен умываться-завтракать
    # допрос Шурика
    #//Аккуратно расспрашивем с Виолой на предмет взаимодействия с аномалией
    # Шурик увлечённо врёт, что пошёл за радиодеталями, говорит, что не нашёл спуск в _бомбоубежище_.
    # Далее явно врёт, что пошёл было обратно в лагерь, а дальше - не помнит.
    # Задумываемся о том, где он шлялся всё время, пока за ним не пришли. Скрывает, собака!
    # ВЦ на Шурика не давит, добра и гуманна.
    # В итоге выгоняет ГГ и Шурика отдыхать и наслаждаться.
    #
    jump alt_day6_true_beach
