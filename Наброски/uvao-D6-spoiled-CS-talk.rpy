# Д6 средяння левая ветка, разговор с Виолой.
# План-набросок-черновик
#
# Используется флаг alt_uvao_D4_viola_morning
#
label alt_day6_uvao_spoiled_CS_talk
#ЛБ: далее до отметки - правленный мной текст Сычёва. Ожидаются новые итерации.
    window hide
    scene bg ext_aidpost_sunset with dissolve
    play ambience ambience_camp_center_day fadein 4
    $ persistent.sprite_time = "day"
    $ day_time()
    window show
    "Страшилки вожатой по-прежнему казались мне не слишком убедительными, но прояснившаяся было после умывания голова снова беспокоила меня всё больше и больше, а звон в ушах всё усиливался."
    "Что ж, видно и вправду придётся навестить доктора Виолу. Столовая подождёт – голова важнее."
    # сцена - дорожка между домиками утром
    "Дорога до медпункта, по идее недолгая, заняла у меня раза в три больше времени, чем должна была. Я шел медленно, стараясь не растрясти больную голову и заодно пытаясь собрать мысли в кучу."
    "Вроде бы и неубедительные, слова Ольги всё время приходили мне на ум."
    th "Эй, ты здесь?"
    "Без особой надежды позвал я, решив провести консультацию со своим внутренним голосом."
    dreamgirl "Здесь конечно. Я всегда здесь. Чего изволите-с?"
    th "Можно хоть иногда без твоих шуточек обойтись?"
    dreamgirl "В принципе можно, конечно… Но нужен ли тебе будет такой скучный внутренний собеседник?"
    dreamgirl "Кажется, тебе собственного занудства должно быть достаточно!"
    "Голос захихикал, довольный собственной шуткой, но тут же резко оборвал сам себя."
    dreamgirl "Ладно, чего хотел-то?"
    th "Мне по Юле консультация нужна. Ты же, вроде как, за интуицию считаешься? Вот и выскажись."
    dreamgirl "Ну если судить по словам и поведению вожатой, которая, похоже, боится данного явления до… гхм… в общем, сильно боится, то опасаться стоит и тебе."
    dreamgirl "Вопрос в том, чего именно тебе следует опасаться? Думаю, тебе стоит сначала переговорить с нашей милейшей докторицей."
    th "Как-то на голос интуиции это мало похоже. Хотя и говорят, что одна голова хорошо, а две…? Одна у меня, а другая… тоже у меня. {w}И с головой этой явно надо уже что-то делать."
    # сцена - медпункт снаружи утром
    play sound sfx_knock_door7_polite
    "Вот и медпункт. Глубоко вздохнув, я постучался."
    cs "Заходи, пионер, заходи."
    th "Интересно, как она узнала, что это я? Ах, да! Она же ко всем так обращается."
    "Моя паранойя, помноженная на шизофрению, иногда позволяла делать парадоксальные выводы."
    window hide
    scene bg int_aidpost_day
    show cs normal glasses far
    with dissolve
    play music music_list["eternal_longing"] fadein 4
    play sound sfx_open_door_1
    play ambience ambience_int_cabin_day fadein 4
    window show
    "Виолетта Церновна сидела за столом и заполняла какие-то бланки."
    cs "А, Семён. Присядь пока."
    "И она приглашающим жестом показала на кушетку."
    show cs normal glasses with dissolve
    "Присев, я от нечего делать стал рассматривать кабинет. Раньше как-то возможности не было. Весы, шкаф с лекарствами, пара кушеток, ничего необычного. На стене плакат с бодрой надписью, призывающей разводить овощи. Зачем он здесь?"
    "Вспомнив, что Ольга говорила про Шурика, я покосился на дверь в изолятор, но та была закрыта."
    "Есть ли кто-то в изоляторе, нет ли - было совершенно непонятно."
    "Впрочем, прежде чем я успел заскучать, Виолетта закончила писать и повернулась ко мне."
    cs "Я тебя внимательно слушаю, Семён."
    me "Голова меня беспокоит."
    if alt_uvao_D4_viola_morning:
        cs "Ну с очень похожей жалобой ты уже приходил ко мне пару дней назад."
        cs "На что сегодня жалуемся?"
    else:
        cs "В каком смысле?"
    me "Шум, гул, звон в ушах…"
    "Виола кивнула."
    cs "Что ж, давай проведём осмотр."
    show cs smile glasses with dspr
    cs "Да не бойся ты!"
    "Рассмеялась она, заметив как я сжался."
    cs "Сегодня просто обычный осмотр."
    "Оказывается она может и нормально разговаривать."
    cs "Можешь даже рубашку не снимать… пионер."
    show cs normal glasses with dspr
    "Виола поочерёдно посветила мне фонариком в глаза, послушала пульс, смерила давление и задумалась."
    cs "Ну что я могу сказать. По первичным результатам обследования, все медицинские показатели у тебя в норме."
    cs "Хорошо бы ещё, конечно, томограмму головного мозга сделать."
    "Виолетта обвела помещение задумчивым взглядом, явно прикидывая, не завалялся ли где-нибудь под шкафом томограф."
    cs "...Но сегодня не получится, наверное."
    cs "Я думаю, ты просто переутомился. Возможно, перегрелся на солнце."
    cs "А пока – вот тебе таблетка болеутоляющего."
    "Она достала таблетку анальгина и налила стакан воды." #ЛБ: может, лучше цитрамона?
# Далее - текст ЛБ
    "Под её внимательным взглядом я запил таблетку и вернул стакан назад."
    me "Ну... Я пойду, наверное? Завтрак уже скоро."
    "Засобирался было я, но Виола удивлённо подняла брови."
    cs "Как же так, я-то надеялась, что ты не только за таблеткой зашёл, пионер."
    cs "Думала, поговорим по душам, содержательно."
    th "Так, начинается. Кажется, снова будут воспитывать."
    cs "Я, правда, надеялась, что ты это сделаешь немного раньше. "
    if alt_uvao_D4_viola_morning:
        extend "Скажем, на пару дней раньше, я бы сказала."
    cs "Впрочем, лучше поздно, чем никогда."
    cs "Нам совершенно точно есть о чём поговорить с тобой, уверяю тебя."
    cs "К сожалению, как ты справделиво заметил, скоро уже завтрак, а мне сегодня надо в столовую успеть пораньше, снять пробу."
    "Виола поморщилась."
    cs "Обычно это пустая формальность, между нами говоря, но вчера чуть ли не весь четвёртый отряд слёг с расстройством желудка - якобы наелись зелёных ягод."
    cs "Во всяком случае, такова официальная версия, хотя сейчас я уже точно знаю, чьи именно родители решили побаловать своё чадо скоропортящимся лакомством, идиоты..."
    dreamgirl "Какая трогательная история! Но тебе-то она зачем всё это рассказывает?"
    cs "...так или иначе, но сегодня целая толпа детей завтракает четвёртым столом, а на мне - снятие пробы с соблюдением всех положенных формальностей. {w}Не хочу, чтобы возможные проверяющие дёргали меня потом из-за этой ерунды."
    th "Может, ей поделиться не с кем, вот она и разоткровенничалась?"
    dreamgirl "А может, она к тебе в друзья набивается?"
    cs "Так что, проводишь меня до столовой, пионер?"
    "Не дожидаясь моего ответа, Виолетта направилась к выходу, на ходу одёргивая халат."
    "Мне ничего не оставалось, как последовать за ней. {w}Ещё чего доброго запрёт меня здесь - с неё станется."
#последовательно сменяют друг друга сцены утренних медпункта снаружи, площади, столовой издали.
    "Мы вышли на крыльцо. Медсестра аккуратно заперла дверь на ключ, опустила его в карман и повернулась ко мне."
    cs "Вот что, Семён..."
    "Начала она негромко."
    th "Ну что, меня ждёт очередная сексистская шуточка?"
    cs "...давай поговорим как взрослые люди."
    cs "Мы ведь с тобой {i}оба{/i} взрослые люди, правда?"
    "Ни тон, которым это было сказано, ни взгляд, которым меня одарила Виола, не оставляли сомнений - паспорт мой не сгинул вместе с курткой и таинственным автобусом, а попал {i}куда следует{/i}."
    "По спине отчего-то пробежал холодок, но Виолетта продолжала сверлить меня настойчивым взглядом разноцветных глаз, и я нехотя кивнул, признавая её правоту."
    cs "Ну вот и славно!"
    cs "Не то, чтобы я собиралась делать объявление по лагерю о некоторых фактах твоей {i}прошлой{/i} биографии, просто так мы сможем временно отказаться от своих ролей и поговорить на равных."
    "Дружелюбно улыбнулась в ответ Виола и не спеша двинулась по дорожке к площади, жестом приглашая меня идти рядом с ней."
    "Помедлив секунду, я догнал медсестру и пошёл по левую руку от неё. {w}В конце концов, начало разговора уже было интересным... а сбежать я всегда успею, если что."
    cs "Так вот, Семён, у меня к тебе есть весьма заманчивое предложение."
    "Продолжала Виола."
    cs "Нет-нет, не из тех, что принято подписывать кровью, не делай такое серьёзное лицо."
    cs "Уверяю тебя, про разноцветные глаза - это всё суеверия."
    "Усмехнулась она, искоса поглядывая на меня."
    cs "И да, прежде всего, просто чтобы не оставлять недосказанностей - это не твой родной мир. {w}Я знаю, что ты это знаешь, но хотела расставить все точки над i."
    cs "Самопроизвольный перенос людей из вашего мира не то, чтобы явление совсем уж обыденное, но случается... время от времени. {w}Подробности позже, если позволишь - это долгий разговор."
    "Виолетта помолчала несколько секунд, но я твёрдо решил не открывать рта до победного - пусть уж первая раскрывает карты."
    # сцена - площадь
    cs "Так вот, возвращаясь к моему предложению. От тебя не потребуется ничего невыполнимого."
    cs "Я всего-то и хочу, чтобы ты контролировал Юлю, если она вдруг появится, и обеспечивал таким образом безопасность лагеря до конца смены."
    me "А..."
    "Посмотрев на меня, и убедившись, что продолжения не будет, Виола утвердительно кивнула головой."
    cs "Да-да, безопасность не только отдельных личностей - возьми хоть Трофимова, у него провалы в памяти, как следствие контакта - но и всего лагеря."
    "Виола остановилась и кивнула на стайку детей, с жизнерадостным гиканьем несущихся куда-то через площадь."
    cs "Я понимаю, ты наверняка склонен недооценивать опасность для окружающих этого существа, Юли, но это по неведению."
    cs "Уверяю тебя, при других обстоятельствах я сама была бы двумя руками за продолжение наблюдений, но были, как я вчера уже упоминала, очень неприятные инциденты в прошлом. {w}{b}Чрезвычайно{/b} неприятные."
    cs "Одним словом, не надо ей пока что ни с кем больше контактировать, может плохо кончиться."
    "На мой взгляд, всё сказанное Виолой по-прежнему выглядело не слишком убедительно."
    th "В конце концов, что я достоверно знаю об этом месте? Нет, даже об этом мире? Только то, что он очень похож на привычный мне... И что {i}там{/i}, у меня, не встречаются девочки с ушами и хвостом - разве что на косплей-вечеринках."
    th "А вот кстати, насчёт ушей... Ладно, чёрт с ней, с моей конспирацией - всё равно у Виолы все карты на руках."
    me "Скажите, Виолетта, я правильно понимаю, что подобные, скажем так, существа, здесь, {i}в этом мире{/i}, явление вполне обыденное?"
    # show cs удивлённая
    cs "Да нет, я бы не сказала. Скорее уж наоборот - в отличие от переноса сюда людей из вашего мира, появление подобных существ - событие, мягко говоря аномальное."
    cs "Больше того скажу, до сих пор таких случаев было зафиксировано всего несколько{w}... И все закончились в той или иной степени трагично - или для самого контактёра, или для окружающих."
    "Между нами повисло тяжёлое молчание."
    "Виола возобновила неспешное шествие в сторону столовой, я поплёлся следом."
    me "Скажите, Виола... А почему Вы так уверены, что и меня не постигнет та же учать? Нет, поймите меня правильно..."
    "Слова медсестры - хотя какая она, к чёрту, медсестра! - по-прежнему вызывали у меня большие сомнения. Не вязалось у меня это милое, немного легкомысленное существо с образом опасного монстра."
    "Но если хотя бы половина услышанного мной - правда... Становиться героем мне совсем не хотелось."
    cs "Ну что ты, здесь нечего стесняться. Разумная предострожность никогда не повредит, я понимаю твоё беспокойство."
    cs "Для тебя Юля не опасна, если будешь думать {i}головой{/i}. {w}Я... настоятельно рекомендую избегать слишким близких контактов с ней, хотя она и вызывает у тебя сильную симпатию."
    cs "Я ведь права, вызывает?"
    me "Ну да, мне она представляется очень милым и вполне безобидным существом."
    "Честно признался я."
    if alt_uvao_D5_hentai:
        me "И симпатия эта носит вполне взаимный характер."
    else:
        me "И мне кажется, симпатия носит вполне взаимный характер."
    "Твёрдо заявил я. {w}Виола качнула головой."
    cs "В этом я как раз не сомневаюсь. Но позволь мне нескромный вопрос - как далеко вы успели продвинуться в реализации этой вашей взаимной симпатии."
    "От такого вопроса, что называется, \"в лоб\" я слегка опешил, но Виола быстро выставила вперёд ладонь."
    cs "Пойми, я не из любопытства спрашиваю. Если бы речь шла о ком-то другом - о ком угодно из {i}людей{/i}, то поверь мне, я и сама не стала бы проявлять любопытства, и у других отбила бы охоту совать нос в твои дела."
    cs "Здесь же я вынуждена задать этот вопрос, и рассчитываю на твою откровенность, уж извини."
    if alt_uvao_D5_hentai:
        th "Вряд ли она меня хочет потроллить. {w}Да и чего мне стесняться-то? Что я, в самом деле маленький?"
        me "Ну, раз это так важно... Откровенно говоря, мы довольно далеко продвинулись. Пожалуй, дальше некуда."
        "Признался я, пожав плечами."
        th "Надеюсь, аморальные действия подобного рода с представителями другой расы - не повод для исключения из пионеров?"
        "Виола снисходительно кивнула, едва заметно вздохнув."
        cs "Что же, этого можно было ожидать."
        cs "Сочетание опыта взрослого мужчины с гормональным фоном подростка... Скорее уж можно удивляться, что ты в лагере никого поближе за это время не присмотрел. {w}Ну или не попытался хотя бы."
        "Подобная прямота Виолы меня несколько покоробила, но возразить было нечего - я и в самом деле думал вчера не только и даже не столько головой."
        cs "Впрочем, насколько я могу судить по твоим реакциям, по тому, как ты разговариваешь - процесс если и начался, то не успел зайти далеко."
        cs "Но уж будь любезен, в дальнейшем воздержись при общении с Юлей от чрезмерно активных проявлений взаимной симпатии. {w}Держи дистанцию, проще говоря, и всё будет хорошо."
        me "Простите, Виола, а о каком \"процессе\" Вы говорите?"
        cs "О весьма нежелательном для тебя, уж поверь мне на слово. Подробности позже - это длинная история."
    else:
        me "Ну, раз это так важно... Откровенно говоря, Юля проявляла весьма недвусмысленный интерес к... гхм... максимальному сближению, но почему-то мне эта идея не очень понравилась."
        "Виола заинтересованно приподняла бровь."
        cs "Ну надо же, кто бы мог подумать."
        cs "Сочетание опыта взрослого мужчины с гормональным фоном подростка... А ты не так прост, раз смог себя контролировать."
        cs "Что же, по крайней мере понятно, почему ты в лагере никого поближе за это время не присмотрел. {w}Ну или не попытался хотя бы."
        "Подобная прямота Виолы меня несколько покоробила, но возразить было нечего - кажется, меня только что похвалили, пусть и на весьма своеобразный манер? Или нет?"
        cs "Что же, если ты и в дальнейшем при общении с Юлей будешь держать дистанцию, то всё будет хорошо."
    cs "Так вот, ещё раз. От тебя требуется помочь мне спокойно закрыть смену. Всего-то сутки с небольшим и осталось-то."
    if alt_uvao_D5_evening_sl:
        cs "Кстати, ты хоть в курсе, что завтра последний день?"
        me "Да, вот только вчера вечером узнал."
        "Смущённо признался я."
        th "А если бы не вчерашняя встреча со Славей на пляже - и сейчас бы не знал. Повезло в кои-то веки хоть в чём-то."
#        dreamgirl "Слушай, не гневи рандом. Тебе не кажется, что события последних нескольких дней - вообще сплошное везение, начиная с самого факта твоего прибытия сюда?"
        "Виолетта довольно кивнула."
        cs "Что же, значит, у тебя было время свыкнуться с этой мыслью."
    else:
        me "Что? Как завтра? Всегда же смены по три недели были?"
        cs "Смена и вправду три недели, но ты-то не к началу {i}прибыл{/i}."
        "Видимо, моё лицо слишком явно отразило всё, что творилось сейчас у меня в голове, потому что Виола успокивающе покачала головой."
        cs "Семён, не расстраивайся так. Ничто не может продолжатсья бесконечно, и пребывание в этом лагере - не исключение."
        cs "Конечно, в этом маленьком мирке намного проще найти своё место, но и там, {i}снаружи{/i}, это не так уж сложно, правду говоря."
    cs "Так что завтра на автобус и вперёд - в город."
    cs "Кстати, о городе. Кажется, самое время озвучить мою часть нашей маленькой сделки - если ты ещё не забыл о ней."
    "Разумеется, за пёстрым ворохом свалившейся на меня информации я забыл вообще обо всём на свете, но признаваться в этом не стал."
    cs "Так вот, по приезду в город с меня - помощь с устройством после лагеря, а если захочешь - то и помощь в получении образования с перспективой весьма интересной работы в дальнейшем. Скучно не будет, обещаю."
    cs "Разумеется, даже если ты откажешься от моего предложения, то голодным и холодным тебя не бросят, но... с моим содействием тебе будет намного проще."
    cs "Те же документы о {i}полном{/i} среднем образовании, например... Полагаю, ты однажды подтвердил уже свои познания в школьной программе, и предпочёл бы не делать это повторно. Если понимаешь, о чём я."
    "У меня-то как раз не было уверенности, что я понимаю, о чём говорит Виолетта. Ну подумаешь, аттестат, программа."
    dreamgirl "...Экзамены... Ты что, всерьёз думаешь, что сможешь хоть завтра, хоть через неделю пойти и сдать экзамен... Ну, скажем, по тригонометрии?"
    th "Ну а что такого... {w}Хотя, если подумать... {w}Ох, чёрт!"
    dreamgirl "Вот именно."
    "Виола, молча наблюдавшая за эволюциями выражения моего лица, усмехнулась."
    cs "Ну и информации обо всём происходящем в лагере ты получишь намного больше, чем сейчас, обещаю. {w}Тебе же интересно, я угадала?"
    cs "Так что ты посиди пока что, подумай, а я сейчас вернусь."
    # Сцена - крыльцо столовой вблизи
    "С некоторым удивлением я осознал, что мы, оказывается, довольно давно уже топчемся на месте возле крыльца столовой."
    "Немногочисленные пока ещё пионеры, ожидающие завтрака, пялились на нас с явным любопытством, но близко не подходили - надо полагать, побаиваясь моей спутницы."
    "Виола вдруг плотоядно улыбнулась мне, томно подмигнула и, легко взбежав по ступенькам, скрылась за дверью столовой."
    th "Ясно. Снова вошла в роль."
    "Пробурчал я, усаживаясь на одну из стоящих на крыльце скамеек."
    
# Сидим, думаем. Как в замедленной съёмке наблюдаем слоняющихся пионеров, обращаем внимание, какое всё яркое и хорошее вокруг. Шиза накручивает - "не слишком ли яркое, чтобы быть настоящим?", "Всё на свете из пластмассы/И вокруг пластмассовая жизнь."
#
    menu:
        "Пусть даже так.":
            th "Я не хочу назад. Даже если всё это ненастоящее - пусть! Если эту сказку расскажут мне до самого конца, и на этом - всё, финал... то я согласен на это."
            dreamgirl "И ты согласен всю жизнь прожить в неведении, настоящий ли этот мир?"
            th "Что значит это слово - \"настоящий\?"
            th "Если я не смогу различить, где сон, а где явь - не всё ли равно? В чём тогда разница между ними?"
            dreamgirl "Что же, это было честно сказано."
            dreamgirl "Я тебе тоже кое-что скажу."
            dreamgirl "Это не мир вокруг ненатурально яркий. Он совершенно обычный. Он был точно таким во времена твоего детства, вспомни, ну же, давай!"
            dreamgirl "Просто со временем ты разучился на него смотреть, ты попросту забыл, как это делать. А сейчас - вспомнил, только-то и всего."
            pass
        "Мне не нужны подделки.":
    th "Я не хочу сидеть здесь и всю жизнь сомневаться - настоящий этот мир, или нет. {w}Мне нужна определённость."
    dreamgirl "Что же, вольному воля."
    # пускаем эффект noir
    dreamgirl "А вот так реалистичнее выглядит?"
    th "Теперь да, как обычно... Подожди, я не понял, что случилось?"
    #немедленная катапульта. Добро пожаловать в милую нераскрашенную "реальность". Автобус и река прилагаются.
# Из столовой выходит ВЦ.
    cs "Ну как, надумал что-нибудь... пионер?"
    me "По-моему, это называется покупать кота в мешке... но я не вижу ни одной причины, чтобы отказаться."
    cs "Что же, я нисколько не сомневалась... Почти."
    cs "Ладно, иди завтракай. Кстати, если вдруг доведётся разговориться с Трофимовым - порасспрашивай его... аккуратно. Может, вспомнит что-то интересно, ну ты понимаешь."
    th "Кажется, мне садятся на шею! Но снявши голову по волосам не плачут!"
# jump идём завтракать с Шуриком.
    

    
#ЛБ: дальше всё удалить. Никаких схождений с ума!
#
#ЛБ: ВЦ, раз уж Сэм соблаговолил зайти, чутка делится информацией. Поясняет без подробностей, что Юля опасна не столько для Семёна, сколько для окружающих. "Катастрофические последствия! Угроза безопасности всех этих детей!". Взывает к ответственности.
#ЛБ: Вообще, до завтрака времени всего ничего было, и его потратили на осмотр, так что дальнейший разговор стоит перенести на "по дороге к столовой"
    "Слова Виолы почти успокоили меня, но я не дал себе расслабиться."
    me "Виолетта Церновна."
    cs "Что-нибудь ещё?"
    me "Да. На самом деле, у меня есть подозрения, что моё ухудшившееся состояние связано с… с Юлей."
    "Виола снова вздрогнула, хоть и мгновенно взяла себя в руки. Как и в прошлый раз, когда я упомянул это имя."
    # ЛБ: "Виола снова вздрогнула" - кажется, Виола пока что не вздрагивала до этого...
    cs "Да, это очень вероятно."
    "Спокойно кивнула головой она."
    cs "А я всё ждала, когда ты сам придёшь с этим вопросом."
    cs "Ты ведь помнишь, что случилось с Трофимовым? Боюсь, что подобный кризис может повториться. И он будет повторяться всё чаще и чаще, пока психика данного субъекта не будет полностью разрушена."
    # ЛБ: Разве тема про Трофимова уже где-то обсуждалась ранее подробно?
    me "Что!?"
    "Я вскочил с кровати."
    me "Шурик полностью сойдёт с ума?"
    cs "Это один из вариантов развития событий."
    "Всё с тем же убийственным спокойствием ответила Виола."
    cs "Как только он будет попадать в зону воздействия этой… аномалии, его психика будет страдать."
    cs "И с каждым разом всё сильнее."
    me "Что же делать?"
    cs "Единственный известный мне способ, который позволит избежать воздействия, это полностью исключить контакт с аномалией."
    me "Значит надежда всё-таки есть."
    "С облегчением сказал я, снова усаживаясь."
    cs "Я пока не настроена столь оптимистично."
    cs "Подобное предупреждение и тебя касается тоже, Семён."
    "Тут она посмотрела прямо мне в глаза своим разноцветными глазищами."
    cs "Я не хочу тебя пугать… но твоя кошкодевочка опасна.{w} Очень опасна."
    cs "То, что у тебя воздействие проявляется в другой форме, нежели у Трофимова, возможно ещё хуже."
    cs "Ты, как более спокойный человек, в конечном итоге, окончишь свои дни полностью в вегетативном состоянии."
    play sound eat_horn fadein 2
    cs "Подумай о моих словах, а сейчас иди завтракать."
    hide cs
    "И в самом деле, по лагерю разносился сигнал горна."
    window hide
    stop sound fadeout 3
    scene bg ext_aidpost_sunset with dissolve
    play ambience ambience_camp_center_day fadein 4
    play sound sfx_open_door_1
    window show
    "Я вышел из медпункта полностью опустошённым. Одна новость хлеще другой."
    "Что же мне делать? Поверить Ольге? Поверить Виоле? Но не могли же они сговориться? Или могли? Да и зачем всё это? Разыграть такой спектакль ради меня одного. Вопросов как всегда больше, чем ответов…"
    "Меня обгоняли беззаботные пионеры, спеша занять лучшие места в столовой. Что же у меня за пионерлагерь такой получается? Все дети, как дети – отдыхают, веселятся. А у меня сплошные думы и непонятки."
    dreamgirl "А что ты, собственно удивляешься, дружок? Ты сам-то, что – обычный пионер? Или ты из соседнего города приехал на летний отдых? {w}Вот и я о том же."
    dreamgirl "Необычному пионеру – и отдых необычный."
    menu:
        "Поверить словам Виолы":
            th "Дыма без огня не бывает, как говорится. Наверное, мне действительно стоит прислушаться к её словам."
            "И я не спеша отправился к столовой."
            jump alt_day6_uvao_breakfast_with_sh
        "Да это же какой-то бред":
            #TODO Текст
            "Если я правильно понимаю, тут должна быть катапульта. Нейтрал."
