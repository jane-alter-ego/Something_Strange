label alt_day6_uvao_prufung_sl:
    "Славя наверняка сейчас организует концерт - декорации, аппаратура, генеральная репетиция… Вот там её и застанем. Врасплох."
    "Я быстрым шагом направился к сцене."

    scene bg ext_stage_big_day
    "Подготовка была в самом разгаре."
    # нужен новый персонаж - пионеры
    pis "Славя, где провода?!"
    pis "Славя, тут занавес заедает!"
    pis "Славя, а музыку уже принесли? А где она?"
    pis "Славя, а где нам переодеваться?"
    pis "Славя!{w} … Славя!{w} … Славя! …" 
    $renpy.pause (2.0, hard=True)
    me "… Славя?"
    show sl angry pioneer with dspr
    sl "НУ ЧТО ЕЩЁ?!" with vpunch
    show sl scared pioneer with dspr
    sl "Ой! Семён, извини, пожалуйста, я думала… Что это опять… Извини!"
    show sl normal pioneer with dspr
    sl "А что ты хотел?"
    me "Да ничего, просто поговорить. Но раз ты занята…"
    show sl smile pioneer with dspr
    sl "Ни капельки! Вообще-то они и без меня разберутся."
    me "Да?"
    "Было немного странно, что наша активистка так просто бросает всё на самотёк…{w} Впрочем, тем лучше."
    me "Тогда, может, отойдём? Чтобы не мешали."
    sl "Давай!"
    
    #кусты 
    "Мы отыскали достаточно густые кусты поодаль. Здесь нас, надеюсь, не прервут."
    show sl smile pioneer with dspr
    sl "Так о чём ты хочешь поговорить?"
    "Кхм. Как бы это получше сформулировать…"
    me "Что происходит, Славя?"
    show sl surprise pioneer with dspr
    sl "Что? О чём ты?"
    me "О тебе. И обо мне."
    "Ясности в её глазах это не прибавило, поэтому я поспешил объяснить."
    me "Просто сегодня с самого утра ты мне кажешься… странной. Особенно в столовой."
    # музыку для романтического настроения 
    show sl smile pioneer with dspr
    sl "А что такого?"
    "Она вновь смущённо улыбалась."
    sl "Ты прав, полагается, чтоб мужчина делал первый шаг."
    sl "Но… У нас ведь сегодня последний день. Последняя ночь! А завтра уже все разъедемся, и, возможно, никогда больше не увидимся."
    sl "Так что… Я просто захотела слегка поторопить события. Потому что не хочу с тобой расставаться!"
    sl "Настолько не хочу, что готова поехать не домой"
    #сделать бы сюда саркастическое выражение, а дальше через extend
    extend "а к тебе!{w} Просто, понимаешь, очутиться с тобой, у тебя дома!"
    me "А как же… Родители, семья, друзья?"
    "Она лишь отмахнулась."
    show sl tender pioneer with dspr
    sl "Это всё ерунда."
    sl "Главное - быть с тобой! Только это важно."
    #здесь для драматического эффекта обрубаем музыку. 
    $renpy.pause (2.0, hard=True)
    me "Не верю."
    show sl scared pioneer with dspr
    sl "Ч-Что… ? Почему?"
    me "Потому что. Ты не похожа на влюбленную дурочку, которая забыла всё на свете, уж это-то я способен заметить!"
    me "Мало того, ты и на себя не похожа."
    me "Что происходит, Славя? Что ты задумала? Зачем ты пытаешься меня одурачить?"
    sl "Семён…"
    "Я распалялся всё сильнее. "
    me "Это всё-таки какое-то задание от Виолы? Или от Ольги?"
    me "Зацепить покрепче пришельца из другого мира, чтобы он остался?!"
    sl "О чём ты говоришь? Ты же не можешь здесь оставаться!"
    show sl cry pioneer with dspr
    sl "И я - я тоже не могу, не хочу, не хочу снова становиться декорацией!"
    sl "Пожалуйста, Семён, забери меня отсюда! В реальный мир!"
    $renpy.pause (1.0, hard=True)
    me "Какой ещё реальный мир?! "
    sl "Твой!"
    sl "Ты ведь придумал всё это, для собственного развлечения. Лагерь, меня, остальных, может быть даже весь мир, не знаю!"
    th "ЧЕГО-О-О-О?!?!" 
    "Столь дикое утверждение разом выбило почву у меня из-под ног. Я собирался выяснить, что ей от меня нужно, а оказалось…"
    "На какую-то секунду я даже засомневался - а вдруг она права, раз говорит это с такой непоколебимой уверенностью?"
    "Или, по крайней мере, все остальные здесь считают так же, только помалкивают?"
    "Что мне теперь, бегать и расспрашивать всех - вы, часом, не считаете меня творцом всего сущего?!"
    me "Славя, что ты несёшь… "
    "Она не слушала."
    sl "Наверное, у тебя были причины сделать всё именно так, именно таким, чтобы всё казалось совсем настоящим, наверное, ты старался, чтобы мы были похожи на живых… "
    me "Сла…"
    sl "Но что потом, когда ты наиграешься? Ты вернёшься к себе, а что станет с нами? Со мной?"
    sl "Я не хочу! Ты должен меня забрать отсюда! Пожалуйста! Я ведь уже не безвольная кукла, я - живая!!!" 

    "Она, кажется была в двух шагах от истерики - готова либо пасть мне в ноги, либо вцепиться в горло, всё, лишь бы заставить меня выполнить её просьбу."
    "Вот только проблема в том, что я, чёрт возьми, нихрена не знаю, как это осуществить!"

    dreamgirl "Ну, по крайней мере, ты знаешь, как отсюда убраться самостоятельно. Может быть, если повезёт, сможешь захватить с собой и её?" 
    th "Убраться? Как?" 
    dreamgirl "Ты чем слушал? Тебе же ясно сказали - если попаданец не приживается в новом мире, его выкидывает обратно."
    th "Предположительно. Отсюда-то он исчезает, а вот появляется ли у себя?"
    dreamgirl "Ну… Значит, придётся рискнуть."
    th "И что мне нужно делать? Чтобы не прижиться."
    dreamgirl "Да ничего особенного. Почувствовать, что тебе здесь места нет. Накрутить себя посильнее, возненавидеть весь этот мир и лагерь в частности - ну, ты умеешь."
    dreamgirl "И тогда тебя, наверное, выкинет обратно. Возможно, вместе с ней."
    dreamgirl "А может быть и нет."
    $renpy.pause (1.0, hard=True)
    dreamgirl "Ну так как? "

    menu:
        "Поехали":
            th "Да."
            "Просто вернуть всё обратно."
            "Просто как следует захотеть, как советуют разные эзотерики."
            "Как я мог этому противиться? Материализовать собственные желания? Попробовать стать демиургом для одной девушки? Чертовски соблазнительная перспектива."
            $renpy.pause (1.0, hard=True)
            "Ладно."

            me "Ладно."
            "Повторил я вслух, для Слави."
            me "Я попробую."
            sl "П-правда?"
            me "Правда."
            me "Вот только результат не обещаю. Я, на самом деле, понятия не имею, что произойдёт."
            "Она шмыгнула носом, торопливо утёрла глаза."
            sl "Ничего. Я готова! Что нужно делать?"
            th "Да чтоб я знал!" 
            me "Ну… Наверное, держись за меня крепко. И закрой глаза."
            "Она с готовностью ухватила меня за руку, прижалась, уткнулась лбом в плечо."
            th "Пора приступать. Значит, так…" 

            "Я крепко, до вспышек, зажмурился и попытался… освободиться, наверное. Нащупать кнопку \"Quit\" - я уверен, она должна быть где-то здесь!"
            th "Я должен выйти. Здесь, в этом мире картонных персонажей, мне нет места." 
            th "Как бы ни было больно признавать, но это всё - иллюзия."
            th "Славя права, увы. И лучше оборвать это сейчас, чем дожидаться трели будильника - конец всё равно один и тот же, разница только в обманутых надеждах."
            # добавить ещё самонакручивания? 
            "Итак."
            "Верните меня домой!"
            "…"
            "…" 
            "…" 
            th "Что-то не… "
            jump alt_uvao_ending_neutrals 

        "Нет":
            pass
    th "Что-то не хочется."
    "Убегать обратно в нору было… неправильно. Глупо, если пожелаете."
    "Фильм на этом моменте я б выключил и никогда бы не вернулся к этому придурку."
    "Похоже, я незаметно для себя уже начал ассимилироваться. И когда это, интересно?"
    "Этот мир пророс в меня, а я - в него. Взаимная диффузия, так, кажется, называется."
    th "Но что тогда делать со Славей?" 
    dreamgirl "Ну, у меня есть парочка идей…" 
    th "Поручик…" 
    dreamgirl "Нет, помимо этого."
    th "Да? Тогда делись. Теми, которые помимо." 
    dreamgirl "Во-первых, даже не вздумай наотрез ей отказывать. Она и сейчас-то не вполне адекватная, а так, боюсь, совсем с катушек слетит. Уклончиво надо."
    "Возражений не было. Психически неустойчивых людей лучше не раздражать…"
    "Но, чёрт возьми, с чего?! Славя же всегда была просто несокрушимо… нормальная! Морально устойчивая, просто живая иллюстрация человека из светлого будущего! "

    th "А вторая идея какая?"
    dreamgirl "Не пытаться решить проблему в одиночку. По крайней мере, для начала посоветоваться с умным и опытным человеком." 
    th "Виола?" 
    dreamgirl "Ага." 
    if alt_uvao_D6_CS_vetrov: #тру-ветка
        "Сложно было не согласиться." 
        "Виолетта свет Церновна - самый информированный человек в лагере, причём по обоим направлениям - и в медицине, и во всей этой каше с параллельными вселенными."

        menu:
            "В медпункт":
                "Да, надо рассказать Виоле. Я, в конце концов, не психиатр, даже рядом не стоял! А у неё наверняка есть какие-нибудь волшебные таблеточки… Вернее, анти-волшебные."

            "Сам буду разбираться!":
                jump расследование 

    else: # фальш-ветка
        "Да, наверное, стоит спихнуть эту проблему в руки официальных лиц. Они-то должны знать, что полагается делать в такой ситуации!"
        "Виола… Или Ольга.{w} Ольга даже лучше!"
        dreamgirl "Чем это?" 
        th "Она так яростно меня убеждала, что мне всё почудилось… Вот и посмотрим, кто оказался прав!" 
        dreamgirl "Злорадство? Это хорошо, это правильно." 

    sl "Семён… ну… ну пожалуйста!"
    "Эти небесно голубые глаза, наполовину наполненные слезами, и на другую половину - надеждой… Почему от простого взгляда становится так больно?"
    dreamgirl "Может быть, потому что ты собираешься её обмануть?"
    th "Это для её же блага."
    dreamgirl "Ну да, ну да." 
    me "Я… постараюсь что-нибудь сделать."
    sl "Правда?! Семён… спасибо!"
    me "Но только не сейчас! Мне ещё надо кое-что сделать."
    sl "А когда? И где?"
    "Я задумался. Пока найду, пока объясню…"
    me "Давай после концерта? Встретимся у тебя в домике. Я к тебе зайду."
    "Она поморщилась."
    show sl sad pioneer with dspr
    sl "Ох. Концерт этот ещё!"
    me "А тебе, кстати, совсем не обязательно на нём быть. Скажись больной или ещё как, и жди меня."
    sl "Да, наверное…"
    "Она с сомнением покачала головой."
    me "Точно тебе говорю. Лучше вещи собери, одежду там, всё необходимое…"
    show sl smile pioneer with dspr
    "Она встряхнула головой и улыбнулась."
    sl "Договорились! Буду тебя очень ждать. И вещи собирать, в дорогу."
    me "Ага."
    "Разговаривать больше было не о чем."
    me "Тогда до встречи. Я побежал!"
    sl "До встречи…"
    hide sl with dspr
    "Провожаемый чарующей улыбкой, я поспешил отступить. И так-то на душе хреново… "

    if alt_uvao_D6_CS_vetrov: #Тру-ветка 
        scene bg ext_square_day
        "Ладно, чего зря тянуть резину."
        dreamgirl "К психиатррру! К психиатррру!" 

        scene bg ext_aidpost_day
        #тук-тук
        cs "Войдите!"
        dreamgirl "Вот как это у неё получается звучать настолько похабно? Даже через дверь!" 
        #скрип двери 
        scene bg int_aidpost_day
        "Доктор Виола была, как всегда, на своём месте - за столом, вполоборота, чтобы любой вошедший мог с первого взгляда оценить как глубокое декольте, так и высокий разрез на бедре."
        show cs smile glasses_thr with dspr
        cs "Проходи, пионер, садись, раздевайся."
        th "Да сколько можно уже! Каждый раз одно и то же…" 
        "Стараясь не показывать никаких эмоций, я послушно сел на кушетку и принялся развязывать галстук. Виола внимательно наблюдала поверх очков."
        "Закончив с галстуком, я занялся пуговицами, выпростал рубашку из-за пояса, снял и, аккуратно сложив, повесил на спинку стула. Всё это с каменным лицом, под бурное одобрение внутреннего комментатора."
        me "Достаточно?"
        cs "Да, спасибо. Можешь одеваться."
        dreamgirl "Один-один, кажется." 
        cs "С чем пришёл?"
        me "С проблемой."
        cs "Понятно. Не волнуйся, такое бывает,если перенервничать. Главное, успокоиться, и всё получится, не в этот раз, так в следующий. А если девушка понимающая - то практически сразу."
        dreamgirl "Один-два." 
        "Я лишь вздохнул."
        me "Спасибо за совет, но он мне мало поможет. Я по поводу Слави."
        В: - Так, и что же с ней? 
        th "Вот даже не знаю, как сформулировать." 
        me "Скажите, она ведь тоже ваш сотрудник?"
        cs "Скорее, стажёр. Будущий сотрудник. А пока просто присматриваемся."
        me "Но она в курсе про меня? Что я - не отсюда?"
        cs "На самом деле нет. Мы её ни в какие секреты не посвящали."
        me "Да? А чем же тогда она занимается?"
        show cs normal glasses_thr with dspr
        "Виола нахмурилась."
        cs "Семён, хватит ходить вокруг да около. Славя помогает нам, например, отслеживать странности в поведении детей. Чтобы не было таких эксцессов, как с Александром."
        me "Что-то не очень помогло…"
        cs "Ошибки всегда возможны, увы. Это всё, что ты хотел узнать?"
        me "Не совсем. Только что у меня был с ней весьма интересный разговор…"
        cs "Да? И о чём же?"
        me "Если вкратце, она требовала, чтобы я забрал её отсюда к себе. В свой мир."
        "Виола сняла очки и некоторое время пристально смотрела мне в глаза."
        show cs normal glasses with dspr
        cs "Вот, значит, как. А зачем ей это, не объяснила?"
        me "Если только это можно назвать объяснением. Больше всего это было похоже на какой-то бред!"
        me "Она… Она почему-то считает меня творцом всего этого!"
        me "Что я каким-то образом всё вот это придумал и создал. Лагерь, людей, мир…"
        me "А она хочет вырваться из этой песочницы, потому что только мой мир реален!"
        #спрайт Виолы с фейспалмом
        cs "Да уж. Любопытная теория."
        cs "И, я так понимаю, ты не захотел возвращаться с ней обратно? Раз уж ты здесь."
        me "А что, я мог?!"
        cs "Вряд ли. По крайней мере, о таких случаях мне неизвестно. До сих пор такого не случалось."
        cs "Но ты мог бы попробовать вернуться обратно, сам. Тогда отсюда ты бы просто исчез."
        me "И что бы тогда стало со Славей?"
        cs "Неизвестно. Аномалия - чертовски непредсказуемая штука, особенно по воздействию на посторонних людей."
        cs "Так что хорошо, что ты не стал экспериментировать."
        cs "И до чего вы в итоге договорились?"
        me "Да ни до чего. Уговорились встретиться после концерта, у неё - я предложил, чтоб время потянуть. Других идей не было."
        cs "Не самая плохая идея."
        show cs normal glasses_thr far with dspr
        "Она взглянула на часы, и поднялась из-за стола."
        cs "В общем, так. Я сейчас уйду, и пока не вернусь - ты сидишь здесь, и никуда не уходишь. Остаёшься за дежурного фельдшера. Ясно?"
        me "Ясно…"
        cs "Как вернусь - отправимся к Славяне."
        me "А… Что с ней-то будет?"
        cs "Надеюсь, всё будет хорошо. Дам ей успокоительных, отоспится в изоляторе, а завтра - на автобус и домой."
        me "А там - уже не ваша забота?"
        "вырвалось у меня против воли."
        show cs normal glasses_over far with dspr
        "Она сверкнула на меня холодным взором."
        cs "А там - никакого влияния аномалии, большие шансы на нормализацию."
        cs "А за такие намёки прописать бы тебе парочку {i}процедур{/i}, да какой смысл зря инструментарий портить."
        me "Извините…"
        cs "Пока прощён. Сиди, жди тут."
        "Она кинула на стол связку ключей и вышла."
        hide cs with dspr
        $renpy.pause (2.0, hard=True)
        dreamgirl "Может, пока никого нет… Всё-таки глянем, что там у доктора в компе?" 
        dreamgirl "Вдруг там и впрямь секретный правительственный интернет?" 
        dreamgirl "Ну или гамесов каких-нибудь найдём. Будет чем время скоротать." 
        "Нет уж. Я и так половину жизни за этим адским агрегатом провёл, не хватало ещё и здесь…"
        th "Да и что ты там надеешься такого интересного найти? Крестики-нолики? Арканоид?"
        dreamgirl "А вдруг альтернативные советские программисты уже написали тут какой-нибудь шедевр?" 
        th "Ага. Советский фоллаут. Или древних свитков…" 
        dreamgirl "Ну, один каджит у нас уже есть. И двемерские руины, с непонятными механизмами - тоже."

        "Да ну. Любая, даже самая шедевральная игра - это всегда ограничения, рамки, в которые тебя утрамбовывает сценарист."
        "Любой шаг вправо-влево уже заранее предусмотрен сюжетом, либо просто невозможен."
        "Эрзац, идеально подходящий для самообмана, для тех достижений, что недоступны в реальности. Неинтересно."

        "Поэтому я просто ждал. Никто не спешил в медпункт с ссадинами и синяками, никому срочно не требовались таблетки от живота. Пресловутые резиновые изделия тоже лежали без дела."
        "Да и кому они могут быть нужны, здесь, в детском лагере-то?!"
        dreamgirl "Мелкой рыжей." 
        th "Сдурел?!" 
        dreamgirl "Ты знаешь, сколько воды можно в один презерватив влить? Ведро! Представь, какая капитошка получится." 
        th "А, ну да. Только кто ж ей выдаст?" 
        dreamgirl "Например, ты? Возьми штук пять, осчастливь мелкую." 
        # и впрямь взять? Опять же, будет чем Лену мочить. 

        $renpy.pause (1.0, hard=True)
        #скрип двери 
        "На пороге появилась Виола."
        cs "Готов, пионер?"
        "Я вздохнул."
        me "Всегда готов…"
        cs "Тогда пошли."

        scene bg ext_aidpost_day
        "Снаружи нас ждали Ольга и хмурящийся от непонимания физрук."

    else: #фальш-ветка

        scene bg ext_house_of_mt_day #дом. Затереть кресло! 
        "Дома Ольги, как ни странно, не было. Дверь была заперта."
        th "Ну и где её искать теперь? Тоже мне, вожатая, которая всё время чёрт-те где, а не со своим отрядом!"
        dreamgirl "У грамотного руководителя всё работает само, без вмешательства начальства."
        th "Вот я и вижу, как оно работает! То Шурик, то вот Славя…" 
        $renpy.pause (0.5, hard=True)
        "Ладно, это всё лирика, а у меня тут насущная проблема."
        th "Так, возле сцены её не было. Что странно, как-никак, отчётное мероприятие!"
        th "Может, у директора? Или у Виолы, строят очередные коварные планы по мою душу."
        dreamgirl "Обязательно! Прямо ночей не спят, куска в рот не берут, всё планы строят, один другого коварнее!" 
        dreamgirl "Скорее, стоит спортзал проверить. Вдруг она там, опять с физруком любезничает?"
        "Я вздохнул. Никак не успокоится!"
        "В очередной раз обвел взглядом дом, кусты сирени, пожарный щит… И вдруг понял, что было не так."
        "Шезлонг! Кресло-шезлонг куда-то делось с его обычного места."
        dreamgirl "Браво, Шерлок. Значит, Вожатовна опять изволят принимать солнечные ванны. Предлагаю поспешить и устроить ей пренеприятное пробуждение." 
    
        scene bg ext_square_day with moveout_right
        $renpy.pause (1.5, hard=True)
        scene bg ext_boathouse_day with moveout_right
        $renpy.pause (1.5, hard=True)
        scene bg ext_beach_day with moveout_right
        "Так и есть. На безлюдном, залитом ярким солнцем пляже стоял одинокий шезлонг, лицом к воде, так, что со спины было видно только поля панамы."
        dreamgirl "Поздравляю вас, коллега, с успешным подтверждением нашей гипотезы." 

        #если сможем - цг
        "Ольга Дмитриевна дремала, надвинув панаму на глаза. На песке валялись полотенце и какая-то книга. Не хватало только хрустального бокала с тропическим коктейлем. "
        me "Ольга-а-а… Дмитриевна-а-а…"
        "Негромко позвал я. Безрезультатно. Она даже не пошевелилась."
        dreamgirl "Дрыхнет. Зачерпни вон воды из реки, сразу вскочит!" 
        $renpy.pause (0.5, hard=True)
        dreamgirl "Хотя погоди. Ты зацени, какая фигура!" 
        "Этот комментарий внутреннего пошляка заставил взглянуть на вожатую с иным настроением."
        "И впрямь, было на что посмотреть! Крупные груди, слегка прикрытые смелым купальником, изящная талия, крутые бёдра, длинные стройные ноги… Не девочка, но молодая женщина, в самом расцвете!"
        dreamgirl "Почему это чуть что - я пошляк?! Что плохого в том, чтобы любоваться красивым женским телом, а? Это ты себя самостоятельно загнобил так, что даже помыслить смущаешься, вот мне и приходится компенсировать!" 
        dreamgirl "Эх, надо было в первый же день разглядеть! Как там было - комсомолка, спортсменка… Да ещё - прошу заметить! - с отдельным жильём. Ну просто все козыри в руки. Это тебе не вздохи на скамейке под ручку, тут уже совершенно другие охи и ахи! Вместо того, чтобы за кошками бегать… "
        dreamgirl "Короче, раз уж ты планируешь тут зацепиться, обрати внимание на сей вариант."
        th "А физрук?"
        dreamgirl "Не стенка, можно и подвинуть. Ну, ты её будишь?"
        dreamgirl "Или ждём, пока спящая красавица сама очнётся?"
        "После всех этих мыслей не получалось просто схватить её за плечо и встряхнуть. Такое простое прикосновение почему-то приобретало странный подтекст… "
        dreamgilr "Совсем одичал. Ну сходи и вправду набери воды. Заодно и себе голову намочи."
        "Я всё-таки собрался с духом и слегка потряс её за плечо."
        me "Оль… Кхм-Кхм!"
        "Прочистив некстати сорвавшийся голос, я попробовал ещё раз."
        me "Ольга Дмитриевна! Проснитесь!"
        show mt surprise swim with dspr
        mt "Семён? Что, уже концерт начался?"
        "Она глянула на наручные часы и принялась торопливо собираться."
        show mt normal swim with dspr
        me "Не знаю, может быть."
        "Сложенный шезлонг был вручён мне, сама же она обернулась полотенцем на манер юбки и в таком виде поспешила домой. Я двинулся следом." 
        mt "Как это - не знаешь? Только не говори, что ты опять хочешь где-то отсидеться."
        mt "Пионер должен принимать участие в жизни лагеря!"
        mt "Демонстрировать свои достижения, в самодеятельности, в спорте, в культурных мероприятиях…"

        scene bg ext_boathouse_day
        show mt normal swim with dspr
        th "Вот только лекции мне сейчас не хватает." 
        me "Ольга Дмитриевна-а-а! Отвяжитесь."
        show mt surprise swim with dspr
        "Она запнулась на полуслове, и я постарался воспользоваться этой паузой."
        me "Сейчас не до концерта, у нас проблемы посерьёзнее."
        mt "Что? Что-то случилось?"
        me "Да. Славя."
        me "Ты опять? Мы ведь уже это обсудили…"
        me "И сошлись на том, что мне всё почудилось. Так вот что я вам скажу, Ольга Дмитриевна - верить надо своим пионерам!"
        scene bg ext_square_day
        show mt angry swim with dspr
        "Я готовился торжествующе выложить свои козыри, пожать лавры и насладиться триумфом, но Ольга сбила меня на взлёте."
        mt "Так, Семён! Говори немедленно, что произошло. И без этих своих хаханек!"
        "Ну ладно. Тем более, что повод и в самом деле невесёлый."

        me "Я вызвал Славю на разговор, хотел выяснить, в чём дело. Она тоже сначала напирала на внезапную влюблённость, но потом…"
        $renpy.pause (0.5, hard=True)
        mt "Ну, что потом?"
        me "Ну… Она потребовала забрать её в мой мир, так, будто это вопрос жизни и смерти."
        show mt surprise swim with dspr
        mt "Что? Зачем?!"
        me "Потому что, оказывается, я - творец и создатель…{w} Выдумал и сотворил лагерь и всё его население." 
        me "И её это положение дел не устраивает, она хочет в настоящий мир…"
        me "Всех, видите ли, устраивает, а её одну - нет! Вас вот, Ольга Дмитриевна, устраивает? Если нет, вы мне скажите, я попробую что-нибудь исправить!"
        show mt angry swim with dspr
        mt "Семён! Прекрати паясничать! Что со Славей?"
        me "Я отболтался, что сейчас не могу, и пообещал, что приду к ней попозже. Она сейчас, наверное, в домике, собирается в дорогу."
        show mt surprise swim with dspr
        mt "Погоди! А концерт?!"
        me "Какой ещё концерт, Ольга Дмитриевна? Выдуманных пионеров для выдуманных зрителей?"
        me "Чихать она на него хотела, и на все прочие заботы тоже. Ей сейчас главное - уйти со мной!"
        scene bg ext_house_of_mt_day #дом. Затереть кресло!  
        show mt normal swim with dspr
        "Она с усилием потёрла виски, принимая какое-то решение."
        mt "Так…{w} Так…{w} Значит, так."
        mt "Семён. Сходи, пожалуйста, в спортзал, и приведи Бориса. К медпункту."
        me "Зачем?"
        mt "Чтобы потом пойти к Славе. Понял меня? Вот и поспеши."
        hide mt with dspr
        "Она скрылась внутри. Вздохнув, я вернул кресло на законное место и отправился выполнять поручение."
        scene bg ext_square_day with moveout_right
        $renpy.pause (1.5, hard=True)
        scene bg ext_dining_hall_away_day with moveout_right
        $renpy.pause (1.5, hard=True)
        scene bg ext_playground_day  with moveout_right
        "На открытых площадках Саныча не обнаружилось. Должно быть, снова дрыхнет на матах в крытом зале. Где это он, интересно, так устаёт, что постоянно спит?"
        dreamgirl "У меня есть предположение, но ты опять назовёшь меня пошляком." 
        th "Твоя правда." 

        scene bg int_sporthall_day
        "В зале было пусто, что удивительно. Зато откуда-то раздавались частые глухие удары - из-за двери в дальней стене, кажется. На стук никто не ответил, и я, поколебавшись, решил войти."
        
        "Борис Саныч сосредоточенно лупцевал подвешенную к потолку грушу. От каждого удара она содрогалась, казалось, вместе со всей каморкой. Я застыл на пороге, не решаясь отвлечь его от этого занятия. "
        th "А ты говоришь - подвинуть…" 
        dreamgilr "Значит, надо сделать так, чтобы Ольга его сама подвинула."
        dreamgilr "А что, ты всё-таки решил воспользоваться этим вариантом?" 
        th "Нет." 
        "Физрук завершил очередную серию - кажется, нокаутом - и обернулся ко мне."
        show ba normal uniform with dspr
        ba "Ну? Чего надо?"
        me "Ээ… Там Ольга Дмитриевна просила подойти. К медпункту."
        ba "Что там ещё случилось?"
        "Рассказывать всё произошедшее ещё раз не хотелось. Да и кто знает, в курсе он про подноготную этого лагеря или нет… "
        me "Да я не знаю, странная какая-то история. Пусть лучше Ольга расскажет."

        "Он пожал плечами, вытер пот полотенцем. Под давлением его взгляда я вышел наружу, он запер дверь, и мы двинулись к точке рандеву."
        scene bg ext_aidpost_day
        "Ольга и Виола уже ждали нас на крыльце."
        
    show mt pioneer normal at center with dspr
    show ba normal uniform at cleft with dspr
    show cs normal at cright with dspr
        
    cs "Ну вот, все в сборе, можно идти."
    ba "Погодите-ка."
    ba "Мне кто-нибудь объяснит, в чём дело? И что от меня нужно?"
    cs "От тебя, Борис, требуется всего лишь присутствовать, для внушительности. Проблема у нас в том, что одна из наших подопечных…"
    cs "Скажем так, она накрутила себя чуть ли не до нервного срыва и бреда. И от нас требуется обеспечить ей необходимую медицинскую помощь. Даже несмотря на её возможное сопротивление."
    ba "Короче, я нужен в роли санитара, так?"
    cs "Если потребуется."
    "Саныч хмыкнул, пожал плечами."
    ba "Что-то слишком много у нас тут ненормальных развелось. Ну ладно. Пошли, что ли?"

    scene bg ext_square_day with moveout_right
    $renpy.pause (1.5, hard=True)
    scene bg ext_houses_day with moveout_right
    "В молчании мы пересекли площадь и вышли к дому. Саныч всю дорогу косился на меня, наверное, пытаясь угадать, зачем я потребовался, но вопросов больше не задавал."
    show cs normal at cright with dspr
    cs "Иди, Семён."
    "Я вздохнул и направился к двери, оставив {i}особую тройку{/i} поодаль."
    scene bg ext_house_of_sl_day
    #тук-тук
    sl "Кто там?"
    dreamgirl "Сто грамм." 
    me "Это я!"
    "Какой-то шум, и дверь распахнулась."
    #Славя радостная
    show sl laugh pioneer close at cright with dspr
    sl "Семён! Ты всё-таки пришёл, а я уже боялась…"
    "Через плечо у неё висела спортивная сумка, с эмблемой Олимпиады."
    sl "Я готова! Куда…"

    show cs normal at left with dspr
    show sl angry pioneer with dspr

    cs "Славяна. Нам нужно с тобой поговорить."
    "Увидев Виолу, и Ольгу с Санычем за ней, Славя осеклась. Прожгла меня презрительным взглядом."
    sl "Предатель!"
    me "Славя… Прости, я… Так будет лучше, поверь."
    "Она меня не слушала, даже не смотрела. Казалось, лишь воспитание не позволяет ей плюнуть в мою сторону."
    cs "Заглянешь ненадолго ко мне? "
    "Молча спустилась, так же молча отдала сумку Борису. Я сделал пару неуверенных шагов вслед, но наткнулся на взгляд Виолы, и застыл."
    hide sl with dspr
    hide cs with dspr
    dreamgirl "Пойдёмте отсюда, товарищ Иуда. Целовать нас, похоже, сегодня не будут." 
    th "Стихами заговорил?" 
    dreamgirl "Виноват, само вырвалось, больше не повторится!" 
    "Процессия скрылась из виду - впереди Славя с гордо поднятой головой, остальные следом. Я повернулся и пошёл, не важно куда, лишь бы прочь отсюда и от них."

#и здесь нужен релаксирующий эвент 
