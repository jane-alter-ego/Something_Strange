# Д6-левая ветка от начала концерта (конец разговора с Юлей), если говорили с Мику, то разговор с ВЦ, затем с ОД и ДВ
#
# Используется флаг Разговора с Мику про Лену alt_uvao_D6_left_MI_talk
#
#
label alt_day6_uvao_left_concert_time:
    # сцена не задаётся, переходит из предыдущего фрагмента
# пока что задаём сцену на время отладки
    play ambience ambience_camp_entrance_day fadein 3
    scene bg ext_stage_big_day:
        xalign .48 yalign .48 zoom 0.75
    show bush_frame at truecenter
    with fade 
# /пока что задаём сцену на время отладки
    $ volume(0.3, 'music')
    play music May_There_Always_Be_Sunshine #минусовка "Солнечный круг, небо вокруг"
    "Тут со стороны сцены внезапно грянула музыка, разом заглушив шум, производимый десятками пионеров всех возрастов, и несколько детских голосов, вступив невпопад, затянули про \"небо вокруг\"."
    hide uv with easeoutright
    "Юля подпрыгнула и, задрав хвост, бросилась к крайнему ряду кустов, пытаясь между ветками рассмотреть происходящее на сцене."
    if not alt_uvao_D6_left_MI_talk:
        me "Юля, подожди, ты так и не сказала…"
        uv "Не мешай!"
        me "Но мне очень надо у тебя узнать…"
        show uv rage with easeinright
        uv "Семён, не мешай! Будешь мешать, я под сцену спрячусь, так и знай!"
        hide uv with easeoutright
        "Поняв, что от Юли я сейчас больше ничего уже не добьюсь, я решил не терять времени и поговорить наконец с самой Леной."
        dreamgirl "Давно пора! А то строишь из себя какого-то великого сыщика, умора одна."
        "Осторожно раздвинув перед собой ветки кустов и оглядев со спины слушателей, я убедился, что Лены среди них не было."
        "По большому счёту, из всего первого отряда там только и были Мику - ну с ней-то понятно, она концерт ведёт - да сгорбившийся в заднем ряду Эл, всей спиной выражающий уныние."
        th "Не понял, а где все? Ну Шурик, допустим, в клубе затаился, но где Алиса, где Славя?"
        th "Где, наконец, наша обожаемая вожатая?"
        dreamgirl "Ну вот тебе и ответ - вожатая отвлеклась, пионеры разбежались. Совсем как ты, кстати."
        th "Так я-то по делу разбежался. {w}Впрочем, плевать, куда остальные делись. Где мне Лену-то искать?"
        th "Если рассуждать логически, то куда она могла пойти, если тоже смылась с концерта?"
        th "Может быть, в библиотеку? Сдаётся мне, она там должна быть частым гостем. {w}Опять же, место тихое, народу мало…"
        dreamgirl "…когда жужелица спит и ты по полу не ползаешь…"
        th "Короче говоря, для начала я иду в библиотеку. Ты как, со мной, или концерт пока посмотришь?"
        dreamgirl "Один - один!"
        "Обернувшись к Юле, я осторожно спросил у обращённой ко мне части её тела:"
        me "Ну… я пойду тогда?"
        "Юля не соизволила ответить на мой вопрос, лишь нетерпеливо дёрнув хвостом."
        "Я счёл это за знак окончания аудиенции и скромно удалился."
        stop music fadeout 5
        jump alt_day6_uvao_left_UN_search
    th "Так, суду всё ясно."
    th "Вот уж действительно, \"что-то пошло не так\". {w}Хотела прогнать девочку, а вместо этого мало того, что её в меня влюбила, так та теперь ещё и рисует виды из окна моей квартиры!"
    dreamgirl "И что ты теперь будешь делать?"
    th "Как бы всё это бедой не закончилось. Кажется, самое время прекращать самодеятельность и обо всём сообщить начальству."
    dreamgirl "О! Ты уже и начальством успел обзавестись! Шустрый, нечего сказать."
    "Поколебавшись, я осторожно спросил у обращённой ко мне части Юлиного тела:"
    me "Ну… я пойду тогда?"
    "Юля не соизволила ответить на мой вопрос, лишь нетерпеливо дёрнув хвостом."
    "Я счёл это за знак окончания аудиенции и, рассудив, что всё население лагеря собралось сейчас перед сценой, подался туда."
    $ renpy.music.set_volume(1.0, delay=2, channel='music')
    # сцена - сцена днём :) 125% без кустов
    scene bg ext_stage_big_day:
        xalign .5 yalign .6 zoom 1.25
    with fade
    "Тихонько выбравшись из кустов за спинами слушателей, я остановился, высматривая Виолетту или Ольгу и стараясь не морщиться от доносящихся из колонок жизнерадостных воплей певцов."
    # show cs normal3 far at fleft with dissolve
    "Вожатой нигде не было видно, зато белый халат медсестры обнаружился совсем недалеко от меня - Виола в гордом одиночестве восседала на скамейке в последнем ряду."
    show cs normal3 close at left with dissolve
    "Перебравшись через скамейку, я устроился рядом. Как ни странно, Виола никак не отреагировала на моё появление."
    "Даже после того, как я пару раз негромко окликнул её по имени, она не шелохнулась, всё так же пристально глядя куда-то поверх сцены."
    "Мне пришлось помахать у неё перед лицом ладонью - только тогда она вздрогнула и обернулась ко мне."
    show cs doubt3 close with dspr
    me "Виолетта, извините, что отвлекаю, но похоже, у нас возникла проблема…"
    "Тут я заметил, что сидящих перед нами пионеров мой разговор с Виолой явно интересует больше происходящего на сцене, и вспомнил о конспирации:"
    me "Понимаете… Мне неловко говорить… Дело в том, что у меня…"
    show cs normal3 close with dspr
    "Я наклонился к уху медсетры и торопливым шепётом принялся излагать свои подозрения насчёт Лены."
    "Рассказ получился на удивление коротким и скомканным. Хуже того, произнесённая вслух, вся эта история начала казаться мне самому на редкость нелепой - мало ли кто в кого влюбляется по вполне естественным причинам?"
    "Одним словом, чем ближе я был к концу истории, тем глупее себя чувствовал."
    "Однако Виола слушала меня очень внимательно, ни разу не перебив. Даже когда я упомянул о разговоре с Юлей, она нахмурилась, но промолчала."
    "Выслушав меня, она неподвижно сидела несколько секунд."
    cs "Так."
    "Ни слова больше не говоря, Виола встала и, не обращая внимания на любопытные взгляды, направилась к дорожке, ведущей к центру лагеря, жестом велев следовать за собой."
    hide cs with dissolve
    extend "Слегка озадаченный, я поплёлся за ней."
    $ renpy.music.set_volume(0.5, delay=2, channel='music')
    #сцена - сцена днём 100% _снизу_ прикрытая кустами
    scene bg ext_stage_big_day
    show bush_left_bottom
    show bush_bottom_central
    show bush_right_bottom
    with fade
    show cs normal3 close with dissolve
    "Лишь пройдя по дорожке пару десятков шагов, так что нас уже не могли видеть сидящие перед сценой, она повернулась ко мне и спокойно сообщила:"
    cs "Вообще-то, я опасалась чего-нибудь в этом роде."
    me "Что?! Но…"
    cs "Ну а чего ещё можно ожидать, если в последние две недели дельта-фактор…"
    "Тут она запнулась и досадливо махнула рукой:"
    cs "Ох, да о чём это я! Сейчас всё это неважно. "
    show cs important close with dissolve
    extend "Вот что: надо чтобы ты как можно скорее нашёл мне Ольгу."
    "Вспомнив, что вожатой среди слушателей концерта заметно не было, я открыл было рот:"
    me "А где…"
    show cs normal3 close with dissolve
    cs "Я думаю, что искать её надо где-нибудь в направлении спортплощадки. Во всяком случае, пять минут назад в ту сторону со скандалом убежала Двачевская, а Ольга побежала её догонять."
    cs "Пусть всё бросает и бежит ко мне, в медпункт."
    me "А…"
    cs "Да, и непременно разыщи и приведи Лену! Среди зрителей я её не видела."
    me "Но как…"
    cs "Да, и потом ещё… Впрочем нет, этим я сама займусь."
    me "Но…"
    show cs doubt3 close with dspr
    cs "Семён, ну чего ты стоишь?! Мне что, самой бежать? В конце концов, кому из нас семнадцать лет, мне или тебе?"
    stop music fadeout 5
    "Уловив намёк, я проглотил все свои незаданные вопросы. Прикинул, в какой стороне находится спортплощадка, и опрометью бросился туда, преследуемый доносящимися со сцены финальными аккордами песни."
    hide cs with dissolve
    play music music_list["that_s_our_madhouse"] fadein 1
    $ volume(1.0, 'music')
    scene bg ext_library_day with dissolve:
        linear 0.1 pos (5,3)
        linear 0.1 pos (5,0)
        linear 0.1 pos (-5,5)
        linear 0.1 pos (-5,0)
        repeat
    "На полной скорости я пронёсся мимо библиотеки и с ходу вломился в растущий позади неё кустарник."
    # хорошо бы сценой поставить какие-нибудь сплошные ветки, если есть. Тряска
    play sound_loop sfx_run_forest fadein 1
    scene bg ext_path_day with dissolve:
        linear 0.1 pos (5,3)
        linear 0.1 pos (5,0)
        linear 0.1 pos (-5,5)
        linear 0.1 pos (-5,0)
        repeat
    "Здесь дружно встретившие меня тонкие, но очень цепкие ветки заставили немедленно сбавить темп, да и в лёгких как-то очень быстро начало колоть. {w}Впрочем, учитывая, сколько я уже сегодня пробежал, пока искал Юлю…"
    th "Всё-таки, хилое какое-то тело мне здесь подсунули, мог бы ещё вчера это понять."
    dreamgirl "Ой, можно подумать, {i}там{/i} ты в последние годы был мастером спорта по лёгкой атлетике! Скажи спасибо, что хоть руки-ноги на месте и пальцев полный комплект!"
    me "Спасибо!"
    "Мрачно пропыхтел я вслух, прикрывая лицо от хлещущих ветвей и пытаясь понять, зачем вообще я, как лось, ломлюсь через эти проклятые кусты вместо того, чтобы сделать небольшой крюк и добраться до спортплощадки по дорожке?"
    "К счастью, прежде чем я успел всерьёз задуматься о том, что меня снова запрягли на общественно-полезные работы, кусты внезапно кончились, и я вывалился из них на задворки волейбольной площадки."
    stop sound_loop fadeout 1
    scene bg ext_playground_day with dissolve
    stop music fadeout 3
    play sound_loop breath fadein 1
    "Остановившись и утирая пот с лица, я окинул взглядом спортплощадку."
    "Очень хотелось надеяться, что мои усилия были не напрасны, и Ольга действительно где-нибудь здесь, а не свернула на полдороги к клубам, например."
    "Мне повезло - на дальнем конце футбольного поля я заметил две яростно жестикулирующие фигуры."
    "Я облегчённо перевёл дух и затрусил к ним."
    show mt angry panama pioneer far at cleft
    show dv angry pioneer2 far at cright
    with dissolve
    "Это действительно были Ольга и Алиса. Похоже, светская беседа была у них в самом разгаре, но, заметив моё приближение, они обе разом замолчали и уставились на меня."
    stop sound_loop fadeout 7
    # убираем дыхание fadeout 7
    show mt sad panama pioneer at cleft
    show dv sad pioneer2 at cright
    with dissolve
    me "Ольга… Дмитриевна!"
    "Выдавил я, остановившись перед ними и безуспешно пытаясь восстановить дыхание."
    me "Вас Виолетта срочно… просила придти к ней в медпункт."
    show mt surprise panama pioneer
    # show dv surprise pioneer2
    with dissolve
    "Видя, что вожатая не слишком торопится куда-то бежать, я добавил:"
    me "Кажется, ещё один случай, вроде вчерашнего."
    show mt feared panama pioneer with dissolve
    "При Алисе большего говорить явно не стоило, но этого и не потребовалось - Ольга разве что не подпрыгнула."
    mt "Чтооо?! Кто… С кем?.."
    me "Давайте я Вам по дороге всё расскажу."
    "Алиса тем временем развернулась и, вздёрнув голову, пошла прочь."
    hide dv with easeoutright
    "Ольга дёрнулась было за ней, но тут же остановилась."
    show mt sad panama pioneer with dissolve
    mt "Ладно. Пойдём, Семён."
    "И тут меня осенило."
    me "Ольга Дмитриевна, я догоню Вас буквально через пару секунд - если вы не возражаете, разумеется!"
    "Вожатая растерянно посмотрела на меня, открыла было рот, чтобы что-то спросить, но потом махнула рукой:"
    mt "Только быстро."
    hide mt with easeoutleft
    "Развернувшись, она зашагала к центру лагеря, а я бросился вдогонку за Алисой."
#    "Догнав Двачевскую в три прыжка, я схватил её за плечо. Та волчком крутанулась на месте и закричала в полный голос:"
    "Догнав Двачевскую в три прыжка, я схватил её за плечо. Та волчком крутанулась на месте и внезапно я оказался с ней лицом к лицу."
    # ЦГ с Алисой, хватающей ГГ за галстук.
    scene cg d6_uv_angry_dv with flash
    with vpunch
    "Схватив меня за галстук и притянув вплотную, она закричала мне в лицо:"
    dv "Да не пойду я на ваш дурацкий концерт, понял?!!{w=1} Отвали, придурок!!!"
    "Она отпустила меня, но сжатые кулаки, тяжёлое дыхание и налившееся кровью лицо не оставляли сомнений, что одно моё неверное слово или движение - и она ударит."
    scene bg ext_playground_day
    show dv rage pioneer2
    with fade
    "Слегка опешив, я отступил на шаг назад."
    me "Эй, полегче! Ты чего бесишься? Да плевать мне на все концерты вместе взятые!"
    me "Ты должна как можно скорее найти Лену."
    dv "Да иди ты! Никому я ничего не должна!{w} Тоже мне, нашёл девочку на побегушках! Тебе надо - ты сам и ищи!"
    "Она резко повернулась, явно намереваясь уйти, но отступать так просто я не собирался."
    "Пытаться ещё раз её удержать на месте я не рискнул, а вместо этого бросился за ней."
    me "Алиса, послушай пожалуйста! Это очень важно!"
    "Мне удалось опередить девушку, и ей пришлось остановиться, чтобы не налететь на меня."
    "Стараясь не обращать внимания на её сжатые кулаки, я выпалил:"
    me "Это очень важно для Лены, честное слово!"
    show dv angry pioneer2 with dissolve
    "Алиса стояла передо мной, по-прежнему тяжело дыша, но угроза физической расправы для меня, похоже, миновала."
    "Глядя исподлобья, она бросила сквозь зубы:"
    dv "И зачем тебе вдруг понадобилась наша распрекрасная Елена?"
    "Ощущая себя рыбаком, который чувствует по движению поплавка, что рыба осторожно пробует наживку на вкус, я сказал как можно спокойнее:"
    me "Понимаешь, я думаю… да нет, я уверен, что Лена влипла в крупные неприятности."
    me "Рассказать я всё не могу - тем более, что это длинная история - а врать тебе тоже не хочу."
    me "Просто поверь мне на слово - для Лены лучше всего будет как можно скорее оказаться в медпункте."
    "Двачевская посмотрела на меня с подозрением:"
    dv "Ты сам-то понимаешь, что несёшь? В медпункт-то ей зачем?{w}"
    show dv surprise pioneer2 with dissolve
    dv "Или это ты сейчас с Олькой про неё говорил?"
    me "Послушай, Двачевская, ты твёрдо уверена, что мне следует тебе лапши на уши навешать, или всё-таки обойдёмся без этого?"
    show dv angry pioneer2 with dissolve
    me "Тем более, ты потом сможешь всё у самой Лены узнать."
    dreamgirl "Ну вот, а говорил, что врать не будешь!"
    th "Тихо ты! Ничего я не вру - захочет, так расспросит.{w} Если сумеет."
    show dv sad pioneer2 with dissolve
    "По лицу Алисы было видно, что она ещё колеблется, но уже готова сдаться."
    dv "Ну хорошо, допустим я тебе поверю, но почему именно я должна за Ленкой бегать?"
#    dreamgirl "Подсекай!"
    "Я широко улыбнулся."
    me "Так кому же ещё, как не тебе? Сама подумай, если я начну Лену искать, то когда я её найду? К Новому году?"
    me "А ты мало того, что лагерь лучше всех знаешь, так наверняка ещё и в курсе, где Лена может быть. Вместо того, чтобы носиться туда-сюда, просто пойдёшь и приведёшь её."
    "По губам Алисы скользнула самодовольная улыбка."
    show dv normal pioneer2 with dissolve
    dv "Вообще-то, я и в самом деле догадываюсь, где её искать. Здесь рядом…"
    "Она оборвала себя на полуслове."
    dv "Неважно. У тебя свои секреты, у меня свои."
    dv "В общем, найти-то я её найду, но с чего ты взял, что она сразу всё бросит и прибежит?"
    dv "Лена каждый год в последний день смены прячется до самой ночи, с чего бы ей в этот раз поступать по-другому?"
    "На это у меня был готов железный ответ:"
    me "А вот это как раз самое простое, тебе даже выдумывать ничего не придётся.{w} Скажи ей, что это {i}я{/i} её ищу.{w} Чистая правда, между прочим."
    "Алиса скептически покачала головой, но спорить больше не стала."
    dv "Ладно, так и быть. Найду я Ленку и передам, что ты просил. Послушает она тебя, или нет - не моя забота…"
    "…её взгляд разом стал холодным…"
    dv "…но за тобой всё равно должок будет, {i}новичок{/i}!"
    "Я театральным жестом прижал руки к груди:"
    me "Моя признательность не будет знать границ в пределах разумного!"
    "Двачевская хмыкнула и направилась к обступившим футбольное поле деревьям."
    hide dv with dissolve
    dreamgirl "А ты не так прост. Кажется, это называется делегированием обязанностей? Далеко пойдёшь."
    "Я устало вздохнул и бросился догонять вожатую."
    scene bg ext_dining_hall_away_sunset with fade
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    show mt normal panama pioneer at cleft with dissolve
    "Нагнал я её возле столовой. Услышав мой топот, она остановилась и, дождавшись пока я подбегу, с подозрением спросила:"
    mt "И о чём ты с Двачевской говорил?"
    "Держась за бок, в котором от всей этой беготни нещадно кололо, я тем не менее не смог удержаться, чтобы не похвастаться:"
    me "Надо было поскорее Лену найти, вот я Алису и подрядил на это."
    show mt surprise panama pioneer with dissolve
    mt "Подожди, а при чём здесь Лена?"
    show mt feared panama pioneer with dissolve
    mt "Или… Так это она, что ли, под воздействие попала?"
#
    jump alt_day6_uvao_left_aidpost