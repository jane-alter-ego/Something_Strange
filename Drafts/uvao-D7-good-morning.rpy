# План-набросок на утро Д7 гуд (тру и фальш)
#
# Используется флаг тру-ветки alt_uvao_D6_CS_vetrov (совсем тру)
# Используется флаг alt_uvao_D6_left_MI_talk (true=медпункт / false=всё остальное)
# Используется флаг Зажигалки Алисы alt_uvao_D6_Zippo (1 - видели после обеда с Алисой(тру), 2 - зажигалка изъята ОД на глазах у ГГ(фальш))
#
#   На входе имеем диспозицию:
#   Славя: гарантированно в медпункте
#   Лена:
#       alt_uvao_D6_left_MI_talk - левый вечерний медпункт - в медпункте
#       not alt_uvao_D6_left_MI_talk - через карьер - в медпункте
#       через врезку:
#           alt_uvao_D6_CS_vetrov - Лена свободна, но ненавязчива (тру-ГГ не дал облить на шезлонгах и уболтал)
#           not alt_uvao_D6_CS_vetrov - Лена свободна и навязчива (облита на шезлонгах)
#       через где-то ещё - уехала на Саныче в ночь
#
label label alt_day7_uvao_getting_up:

    #эффект ряби, за ней - что-то похожее на звёздное небо
    "Я лежал в шезлонге и смотрел на звёздное небо."
    "Звёзды тихонько перешёптывались между собой о чём-то, ласково мне подмигивая и иногда улыбаясь."
    "Одно только было плохо - они никак не хотели складываться в знакомый с детства рисунок созвездий."
    "В какой-то момент я заприметил было Полярную звезду, но Ольга возразила мне:"
    #проявляется через dissolve по центру увеличенный и размытый голый спрайт ОД. Грудь по большей части или скрывается за нижним краем экрана, или вовсе уж размыта или затемнена. 
    mt "Какая же это Полярная звезда, Семён, ты что! Её только из Северного полушария видно!"
    mt "Вот, смотри - Южный крест. Правда, красиво?"
    #появляется небольшой анимированный Южный крест у неё над грудью
    "И в самом деле, на шее у Ольги на тонкой цепочке таинственно переливался россыпью звёзд Южный крест."
    "Она вдруг наклонилась ко мне."
    #blink-unblink
    #сцена - домик ОД изнутри утром.
    #with hpunch
    show mt pioneer panama surprised close
    mt "Семён, какой Южный крест, ты о чём вообще?"
    "Я попытался сесть в кровати, но запутался в одеяле."
    mt "С добрым утром, фантазёр!"
    show mt pioneer panama smile
    "Улыбнулась мне Ольга, выпрямляясь."
    me "Фачему фафтазёр?"
    "Кое-как промямлил я деревянным со сна языком."
    "Чувствовал я себя отвратительно невыспавшимся."
    mt "Потому что непременно надо быть фантазёром, чтобы видеть сны!"
    "Рассмеялась вожатая."
    show mt pioneer panama normal
    mt "Вставай, Семён. Полседьмого уже!"
    "Я отчаянно зевнул, чуть не вывихнув челюсть, и тут до меня дошло наконец."
    me "Как полседьмого?"
    "Я сел на краю кровати, кутаясь в одеяло."
    me "Что-то случилось?"
#    show mt pioneer panama normal
    "Ольга отрицательно покачала головой."
    mt "Да нет, ничего не случилось, не волнуйся так. {w}Во всяком случае, ничего нового."
    mt "Одевайся и выходи скорее, я тебя снаружи жду."
    "Торопливо распутывая брошенную вчера как попало одежду и отчаянно борясь с раздирающей рот зевотой, я мучительно пытался понять, чего ради Ольга подняла меня в такую рань."
    "Опыт предыдущих дней не давал мне никаких поводов для оптимизма."
    th "Не иначе, Юля кого-то ещё ошарашила. Или в медпункте что-то не так. Или…"
    "На глаза вдруг попался лежащий на столе металлический брусочек зажигалки."
    if (alt_uvao_D6_Zippo = 1): <видели зажигалку после обеда, Алиса выронила (тру? или фльш тоже может?)>:
        th "Что, Ольга ещё и курит, в довершение всего?!"
        "Впрочем, зажигалка показалась знакомой - ну да, точно такую же я видел вчера в руках у Алисы возле столовой."
        "Хотя, что значит \"такую же\"? Вряд ли здесь две таких одинаковых найдётся."
    elseif (alt_uvao_D6_Zippo = 2):
        #Видели после изъятия зажигалки, как Ольга курила.
        "Впрочем, зажигалка показалась знакомой - ну да, точно такую же Ольга вчера отобрала у Алисы."
        "Хотя, что значит \"такую же\"? Вряд ли здесь две таких одинаковых найдётся."
    else: 
        pass
    "Машинально я откинул крышку и, с третьей попытки уговорив изношенный механизм, пробудил к жизни язычок пламени."
    "Пару секунд я тупо пялился на него. {w}Потом закрыл зажигалку и бросил обратно на стол - все эти нюансы меня сейчас мало занимали."
    th "Что, всё-таки, случилось? Не просто же так меня Ольга разбудила!"
    "Одним словом, от силы через пару минут я уже выскочил из домика, на ходу застёгивая рубашку и ёжась от утренней прохлады."
    #сцена - домик ОД снаружи утром
    show mt pioneer panama normal
    "А ты быстро сегодня."
    "Вымученно улыбнулась мне Ольга."
    "Только сейчас я заметил, что она выглядит помятой и какой-то взъерошенной, а судя по мешкам под глазами, спала она сегодня куда меньше моего."
    me "Не томите, Ольга Дмитриевна. Что случилось-то?"
    "Ольга вновь покачала головой."
    mt "Говорю же тебе, ничего не случилось."
    mt "Просто сегодня последний день смены. Надо успеть сделать целую кучу дел, а я осталась без помощницы."
    mt "Так что если ты мне не поможешь, то не знаю, что и делать тогда."
    show mt pioneer panama sad
    "Наверное, взгляд мой был более, чем красноречив, потому что она виновато потупила глаза и как-то беспомощно развела руками."
    mt "Дел и вправду невпроворот, а рассчитывать мне в отряде больше не на кого."
    mt "Вернее… Я хочу сказать, остальным можно попытаться поручить что-то несложное, но надо будет стоять рядом и контролировать непрерывно, а у меня совсем нет на это времени. {w}Мне нужен человек с головой на плечах, самостоя…."
    "Тут Ольга отчаянно зевнула, не сдержавшись, и помотала головой."
    show mt pioneer panama normal
    mt "У Виолы растворимый кофе есть… {w=1.0}Бразильский…"
    "Мечтательно пробормотала она."
    mt "Жаль только, сейчас в медпункт…"
    "Вожатая запнулась и посмотрела на меня чуть ли не умоляюще."
    mt "Ну так как, поможешь мне?"
    #ЛБ: наверное, здесь или текст на весь экран (но текста маловато), или затенить картинку
    th "Помочь Ленивовне закрыть смену? Вот это номер!"
    th "Что же, отличная возможность отыграться за все её придирки да насмешки!"
    th "Тоже мне, нашла дурака, помогать я ей стану. Пусть сама вертится, как хочет - на то она и вожатая, а я пойду досыпать!"
    #конец полного экрана/визуального эффекта
    "Вздохнув, я спросил:"
    me "Что делать-то надо? Умыться хоть успею?"
    #визуальный переход - blink или ещё как
    #далее после каждой фразы беспорядочно меняем бэки, пока не доберёмся до столовой.
    "Оказалось, что делать надо много чего. Оставалось лишь гадать, как это они раньше без меня умудрялись заканчивать смену."
    "Я даже чувствовал по этому поводу нечто вроде гордости. {w}Первые пятнадцать минут."
    "Потом гордость уступила место раздражению - опять на халяву запрягли идиота."
    "Потом мне стало уже всё равно."
    "К началу завтрака я уже успел раз десять обежать по кругу лагерь с разными Важными Поручениями и хорошенько пропотеть."
    #сцена - столовая утром изнутри
    if alt_uvao_D6_left_MI_talk: #были в левом медпункте в Д6
        "Стоя с подносом в очереди, я вдруг вспомнил про вчерашний разговор с поварихой и строгий наказ вернуть посуду из медпункта до завтрака."
        "К счастью, от необходимости объясняться ней меня избавила зашедшая в столовую Виола."
   else:
        "От созерцания затылка стоящего передо мной в очереди к раздаче незнакомого пионера меня отвлекла Виола."
    "Торопливо подойдя к раздаче, она о чём-то коротко переговорила с поварихой и, кивнув мне на ходу, покинула помещение."
    "В голову разом полезли вчерашние мысли о том, как-то оно ещё у меня сложится - с утра как-то не до них было."
    "Впрочем, долго терзаться сомнениями мне не дали."
    "Стоило мне сесть за свободный столик, как на горизонте нарисовалась Лена, причём с явным намерением подсесть ко мне."
    "Все прежние переживания разом вылетели из головы от мысли о предстоящем продолжении вчерашнего разговора."
    th "Ну не готов я к этому, не готов!"
    th "Пожалуйста, пожалуйста, только не сейчас! Обещаю, я буду хорошо себя вести…"
    "Через мгновение за мой столик уселась выскочившая откуда-то со своим подносом Мику, незамедлительно принявшаяся щебетать нечто жизнерадостное." #ЛБ: мне самому интересно, намёк ли это; наверное, нет.
#   if <через врезку> and alt_uvao_D6_CS_vetrov:
        "Лена растерянно потопталась на месте, но потом, смущённо улыбнувшись мне, пошла искать себе другое место."
#   else:
        "Лена растерянно замерла на несколько секунд, закусив губу, потом поднос в её руках опасно накренился…"
    #звон бьющегося чего-нибудь. хоть та же тарелка сойдёт.
        "…и столовую огласил звон грохнувшегося об пол стакана с какао."
        "Швырнув поднос с остатками завтрака на чей-то столик, Лена опрометью бросилась вон из столовой."
    "Остаток завтрака прошёл в полном молчании {w}- если не считать непрерывно тараторящей что-то японки."
    "Впрочем, мне даже поддакивать ей не приходилось, да и от ненужных мыслей эта своеобразная звуковая завеса защищала неплохо."
    "На выход я решился двинуться, лишь убедившись, что Ольга не смотрит в мою сторону."
    "У меня было совершенно отчётливое желание спрятаться где-нибудь на часок-другой и наверстать упущенное время сна."
    if (alt_uvao_D6_Zippo = 1): #видели зажигалку в Д6 после обеда с Алисой. тру (ГГ-герой).
        "Увы, с самого начала всё пошло не так - едва проскользнув в дверь столовой, я наткнулся на понуро сидящую на крыльце Алису."
        "Хмуро глянув на меня, она вернулась к прежнему занятию - разглядыванию собственных коленей."
        "Я сделал было шаг к ступеням крыльца, но тут в памяти всплыло совсем свежее воспоминание - меньше суток ведь прошло."
        "Здравый смысл подсказывал ловить момент и, пока хищник дремлет, поскорее проскочить мимо {w}- но кому он нужен в здешнем бедламе, этот здравый смысл!"
        me "Скучаешь?"
        "Бросил я небрежно, облокачиваясь на перила."
        dv "…"
        "Неразброчиво процедила Алиса сквозь зубы."
        "Здравый смысл буквально кричал, что надо уйти, пока не поздно. Что же, тем больше поводов поступить ему наперекор."
        me "Слушай, Алиса, ты не знаешь, Ольга давно курит?"
        "Решил я зайти издали."
        me "Я у неё зажигалку видел."
        "Алиса вздрогнула."
        "Помолчав немного и бросив на меня быстрый взгляд, она начала вкрадчиво:"
        #ЛБ: ToDo - подобрать спрайты в диалоге
        #хитрая dv
        if alt_uvao_D6_left_MI_talk: #через левый медпункт
            dv "Новичок, а ты в курсе, что долг платежом красен?"
            me "В курсе. Похоже, у меня есть шанс этот долг отдать, да?"
            dv "Вот именно."
            "Без промедления подтвердила девушка."
            dv "Думаю, тебе будет нетрудно… Хотя, мне всё равно, как ты это сделаешь."
            dv "Это моя зажигалка, и я хочу её вернуть до отъезда из лагеря."
            "Поколебавшись немного, я всё-таки не смог сдержать любопытство:"
            me "А почему…"
            #смущённо-надутая dv
            dv "Это не твоё дело."
            me "Что?…"
            dv "Это не твоё дело, зачем мне эта зажигалка."
            "Упрямо повторила Алиса."
            dv "Она мне нужна до отъезда, и всё тут."
            dv "Или обязательно надо {i}тебе{/i} на уши лапши навешать?"
            "Возразить на это было нечего."
            th "В конце концов, я сам установил вчера правила этой игры… И это действительно не моё дело."
            me "Ладно, идёт. Отдаю тебе зажигалку, и мы квиты."
        else: #через карьер
            dv "Новичок, а ты в курсе, что все люди братья, все должны помогать друг другу?"
            me "Конечно. {w}Братья. {w}А ещё - сёстры."
            me "Дай угадаю - тебе нужна эта зажигалка?"
            #смущённо-надутая (guilty?) dv
            dv "Да."
            "Поколебавшись, неохотно подтвердила Алиса."
            dv "Она моя."
            me "Ладно, допустим. {w}Допустим, я достану для тебя эту зажигалку."
            me "Осталось лишь понять, зачем {i}мне{/i} это нужно. Что взамен?"
            #какая-то смена эмоции dv
            "Алиса растерянно заморгала, словно не ожидала такого поворота разговора."
            "Я молчал, наблюдая за ней с долей ехидства."
            "Наконец она выдавила из себя:"
            dv "Если ты достанешь мне зажигалку до отъезда…"
            #смущённая dv
            "Девушка запнулась и покраснела, потом начала заново:"
            dv "Если ты достанешь мне зажигалку до отъезда, то я… то… то я тебя…"
            th "Всё ясно."
            "Приятно было хоть отчасти поквитаться с рыжей за все унижения, но и перегибать палку мне не хотелось."
            me "Расслабься, я пошутил. Будем считать это актом доброй воли с моей стороны."
            "Поколебавшись мгновение, я всё-таки не смог сдержать любопытство:"
            me "Но только скажи мне, зачем…"
            dv "Это не твоё дело."
            me "Прости?…"
            dv "Это не твоё дело, зачем мне эта зажигалка."
            "Упрямо повторила Алиса."
            dv "Она мне нужна до отъезда, и всё тут. Я не могу тебе сказать."
            dv "Так ты… Ты поможешь мне?"
            me "Ладно, пусть так."
            me "Посмотрю, что можно сделать."
        me "Но только одно маленькое условие - потрудись наконец запомнить моё имя."
        me "Меня зовут Семён."
        #хитрая dv
        "Алиса хмыкнула, и, больше ничего не сказав, удалилась."
        th "Вот ведь…"
    elseif (alt_uvao_D6_Zippo = 2): #видели зажигалку в Д6 после озера. (фальш-ГГ).
        "Увы, с самого начала всё пошло не так - едва я проскользнул в дверь столовой, как меня окликнула Алиса."
        "Увидев меня, она резво поднялась на ноги."
        dv "Слушай, новичок, ты в курсе, что долги надо отдавать?"
        "Я опешил."
        me "Не понял, когда это я тебе успел задолжать?"
        #ЛБ: ToDo текст
    else:
        pass
    #
    # проворачиваем афёру с зажигалкой.
    # Тру-ГГ сам проявляет инициативу, спрашивает ОД, уговаривает отдать ему зажигалку для передачи Алисе - та ему очень помогла вчера и т.п. Отдаёт Алисе - "не люблю быть должным, да и вообще…". Оставляет девушку в некоторой растерянности.
    # Фальш-ГГ отловлен Алисой, которая одновременно и наезжает про вернуть должок с наглым видом, и готова чуть ли не расплакаться, хотя и скрывает. ГГ тырит зажигалку и отдаёт Алисе - "Теперь мы квиты. Только смотри, ни полслова никому!". Позже ОД спрашивает Фальш-ГГ про зажигалку, тот не признаётся "Зажигалка? Металлическая? "Зиппо"? Нет, не видел."

#Если Лена свободна и навязчива (облита на шезлонгах), то фальш-ГГ вынужден уворачиваться всё утро. В какой-то момент Лена его загонит-таки в угол для Окончательного Выяснения Вопросов, но нечаянно набижит ОД и спасёт ГГ:
               # un "Семён! Мы должны поговорить!"
               # me "…"
               # выскакивает ОД
               # mt "Вот вы где! Лена, подожди, со мной пойдёшь, а ты, Семён, беги скорее…"
               # "Не дожидаясь продолжения, я повернулся и побежал что есть духу."
               # "Ольга что-то кричала мне вслед, но я не стал возвращаться, и выяснять, что именно."
               # минут через пятнадцать ГГ снова пересекается с ОД. Та отправляет его куда-то ещё Делать Полезное, но не выдерживает и ржёт: "Да не бойся ты, наказание моё, нет там Лены!"

# Возможно, в какой-то момент его отлавливает Юля. Опять же, возможно, она вручает ему наивный подарок (стеклянный шарик, кулёчек с сахаром, банка консервов) - от сердца оторвала!
# Ближе к полудню наконец-то всё заканчивается, детям выдают сухой паёк и грузят в автобус.

# Чтобы не забыть, возможные занятия по хозяйству (наверное, не всё, а выбрать что-то. Иначе Сэм до конца следующей смены провозится):
# - проконтролировать сдачу постельного белья, помочь младшим.
# - заставить сдать тех, кто не сдал.
# - проконтролировать по всем домикам укладку свёртков с матрасами и одеялами.
# - там же проконтролировать поломанную мебель и т.п.
# - разобрать на бельевом складе какой-то тюк с постиранной одеждой пионеров и раздать по вожатым отрядов согласно меткам. Часть меток отсутствует или расплылась ("додумались же, авторучкой метку подписать!"). Морока, одним словом. Палевный ГГ уже видел этот тэк вчера, на хозработах - Славя так его и не разобрала…
# - получить в столовой на всех пионеров сухпайки и воду в дорогу и всё это дотащить до стоянки, потом ещё и вожатым раздать сообразно количеству детей в отрядах.
# - напоследок пробежаться по домикам в поисках забытых вещей ("ну как такую здоровую дуру можно забыть? Как???") и найти владельцев.
# - помочь/организовать помощь детям из младших отрядов в переноске вещей к стоянке.
