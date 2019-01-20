# Д6 левая ветка, хозработы со Славей.
# План-набросок
#
# Используется флаг alt_day3_duty дежурства по столовой в Д3
# Используется флаг alt_day3_dancing партнёрши по танцам в Д3 (ЛБ: сейчас не работает - при сычевании второго танца (выход на ЮВАО) всегда выставляется alt_day3_dancing = 5, и мы ничего не знаем про первый танец. Печаль-беда, перед релизом надо будет договариваться с Автором
# Используется индикатор степени настойчивости Слави alt_uvao_D6_sl_assert
#
# Устанавливает флаг Левых хозработ alt_uvao_D6_left_duty в True
#
label alt_day6_uvao_left_dutywork:
    scene bg ext_warehouse_day with fade
    "Целью недолгой пробежки оказался бельевой склад."
    sl "Надо грязное постельное бельё отвезти в прачечную."
    "Объяснила нисколько не запыхавшаяся Славя."
    sl "Там сушилка была сломана, только вчера починили, вот и накопилось, а завтра конец смены, это ещё бельё со всего лагеря. {w}Пока всё постирают, а в пересменок с ним возиться особо некому будет…"
    "Я лишь покорно кивал, восстанавливая дыхание. Возиться с грязным бельём мне вовсе не хотелось, но обратный ход давать было уже поздно."
    th "Не будь это Славя, я бы решил, что она волнуется из-за чего-то. Или стесняется кого-то, то есть - меня."
    th "А здесь - заразилась от Мику за завтраком, не иначе."
    "Славя отперла наконец дверь и мы зашли на склад."
    window hide
    play sound sfx_open_door_clubs fadein 0
    scene bg int_shed_day 
    show sl normal pioneer
    with dissolve
    window show
    show sl normal pioneer
    sl "Давай их наружу вынесем, я там тележку уже приготовила."
    "Славя показала на два объёмистых тюка."
    "Я примерно представлял себе, сколько может весить такой объём белья, и слегка приуныл, но тюк на удивление оказался не слишком тяжёлым."
    play sound sfx_open_door_clubs fadein 0
    window hide
    scene bg ext_warehouse_day 
    show sl normal pioneer
    with dissolve
    window show
    "Сгрузив ношу на стоявшую здесь же тележку, мы готовы были уже тронуться в путь, как Славя вдруг всплеснула руками."
    sl "Ох, я совсем забыла! Подожди секунду."
    hide sl with dissolve
    "Девушка скрылась на складе и тут же вернулась с каким-то тряпичным свёртком."
    show sl normal pioneer with dissolve
    sl "Вот, я и своё постирать хотела заодно… Ой!"
    "Она неловко перехватила свой свёрток так, что тот раскрылся, выворачивая содержимое наружу."
    "Рефлексы мои оказались на высоте - я нырнул вперёд{w}… и в руках у меня оказался симпатичный и довольно объёмистый лифчик."
    "Кажется, на меня напал какой-то ступор - я стоял полусогнувшись и тупо разглядывал незатейливые кружева, которыми были отделаны чашечки."
    "Славя, проворно подбирающая прочие, надо полагать, не менее деликатные предметы белья, смущённо усмехнулась:"
    show sl laugh pioneer with dspr 
    #Коллекционер: Добавил от себя красно-смеющуюся Славю 
    sl "Извини, но мне кажется, это не твой фасон."
    "Выпрямившись, она протянула руку, слегка порозовев от смущения."
    sl "Ну что ты, как маленький. Бюстгальтера никогда не видел?"
    "Забрав у меня лифчик, она вновь упаковала его вместе с остальными своими пожитками."
    "Сообщать Славе, что бюстгальтеров в своей жизни я повидал несколько больше, чем она могла бы подумать, явно не стоило."
    "Запоздало покраснев, я неловко пожал плечами."
    me "Да не то, чтобы совсем не видел, просто как-то неожиданно вышло. {w}Ты, когда в следующий раз решишь шоу устроить - предупреждай заранее, минут за пять, я приготовлюсь."
    show sl tender pioneer with dspr
    "Моя неловкая попытка отшутиться почему-то произвела на Славю самое неожиданное действие - девушка разом изменилась в лице, и в глазах её мелькнул испуг."
    show sl smile pioneer with dissolve
    "Впрочем, через секунду она снова весело мне улыбалась."
    sl "Ну что, взялись?"
    window hide
    scene bg ext_dining_hall_near_day
    show sl normal pioneer 
    with dissolve
    window show
    "Толкать тележку вдвоём оказалось занятием вовсе не трудным."
    "Да что вдвоём - здесь и одному-то делать было особенно нечего - знай только, не давай тележке съехать с мощёной дорожки в сторону."
    "Я помалкивал, всё ещё слегка смущаясь после недавнего конфуза. Славя тоже не спешила заводить разговор, лишь то и дело поглядывая на меня искоса."
#ЛБ: здесь ГГ начинает терзаться мыслями о Юле и воспоминаниями об утреннем разговоре с ВЦ и терзается вплоть до внезапной реплики Шизы.
    dreamgirl "Не думаю, что он у неё был единственный."
    th "О, а я уже чуть было не заскучал без тебя. {w}Кстати, ты о чём?"
    dreamgirl "О лифчике. Ты уже минут пять пялишься на её грудь. {w}Так вот, под рубашкой на ней наверняка надёто всё, что положено."
    "Я смущённо отвёл взгляд в сторону."
    "Возможно, мне послышалось, но Славя, будто подслушав мой внутренний диалог, едва слышно хихикнула."
    #здесь должен быть какой-то бэк "возле прачечной" - это где-то возле администрации. Пока неясно, что с ним делать. Посмотреть, что там у Автора в Славя-руте насчёт здания администрации.
    #Коллекционер: поставил администрацию
    window hide
    scene bg ext_admins_day
    show sl normal pioneer
    with dissolve
    window show
    show sl normal pioneer
    "Наконец мы остановились у невзрачной пристройки на задворках здания администрации."
    sl "Подожди, я сейчас."
    "Бросила мне Славя и, без особого труда подхватив оба тюка разом, скрылась с ними внутри прачечной."
    "Я присел было на тележку, вяло размышляя, кому могло придти в голову разместить бельевой склад и прачечную в разных концах лагеря, но Славя уже вышла наружу."
    "Я поспешно вскочил на ноги, а на моё место плюхнулись два новых тюка, поменьше."
    sl "Это постиранное, надо на склад отвезти."
    "Пока я щёлкал клювом, прикидывая, не следует ли проявить себя джентльменом и предложить даме посильную помощь, Славя сбегала за ещё одной парой тюков, и мы отправились в обратный путь."
    window hide
    scene bg ext_square_day
    show sl normal pioneer
    with dissolve
    window show
    
    "Разглядывая забранные из прачечной видавшие виды мешки, сшитые из полосатой когда-то материи, я невольно задумался о судьбе Славиного свёртка."
    th "Если его содержимое постирают так же, как мои несчастные джинсы, то на выходе даже тряпочек не останется."
    if alt_day3_duty:
        "Недавнее знакомство с чудом современной кухонной техники - местной картофелечисткой - оптимизма тоже не добавляло."
    th "Я-то думал, подобные вещи в те времена вручную стирали. {w}Вернее, стирают в {i}наше время{/i}, так что ли у меня теперь получается?"
    dreamgirl "Что же ты, надо было предложить девушке услуги по ручной стирке. Произвёл бы незабываемое впечатление - хозяйственные мужики во все времена нарасхват."
    "За всеми этими размышлениями о способах стирки и временных парадоксах на болтновню меня по-прежнему не тянуло."
    "Славя, беззаботно напевающая что-то себе под нос, с разговорами тоже не лезла."
    "Обратная дорога к складу никаких затруднений не вызвала - пусть груз и стал вдвое больше, зато теперь мы двигались преимущественно под уклон."
    window hide
    scene bg ext_warehouse_day
    show sl normal pioneer
    with fade
    window show
    "Добравшись до склада, мы приткнули тележку возле двери и занесли мешки внутрь."
    window hide
    play sound sfx_open_door_clubs fadein 0
    scene bg int_shed_day
    show sl shy pioneer
    with dissolve
    "Освободившись от своей ноши, Славя посмотрела на меня непривычно робко."
    sl "Семён, а Семён? Можно я тебя ещё поэксплуатирую?"
    show sl sad pioneer with dspr
    sl "Или тебе надо бежать, выполнять то поручение?"
    th "Минутку, какое ещё поручение?"
    dreamgirl "Ну ты же сам ей возле столовой лапшу на уши вешал про {i}срочное поручение{/i}. А она запомнила, смотри-ка!"
    "Я решительно махнул рукой."
    me "Никуда не убежит это поручение."
    me "А если и убежит - само найдётся. {w=1.5}Командуй!"
    hide sl with fade2
    "Через несколько минут я сидел верхом на одном из тюков, доставая из другого сложенное вперемешку чуть влажноватое после прачечной бельё и раскладывая его по стопкам."
    th "Пододеяльник, наволочка, наволочка, простыня, наволочка, просты… нет, пододеяльник, ещё пододеяльник, простыня, наволочка…"
    #ЛБ: кстати, из этого можно сделать идиотскую миниигру "собери комплект" с падающими сверху предметами постельного белья, которые надо сортировать. Не знаю только, кому это может понадобиться.
    "Славя набирала из стопок комплекты и проворно раскладывала их по складским полкам."
    "Не самое интересно занятие, конечно, но с другой строны - работа была не бей лежачего."
    "Минут через пятнадцать, распотрошив до половины третий тюк, я не выдержал."
    me "Послушай, Славя, а зачем ты меня помочь-то просила?"
    show sl surprise pioneer with dspr
    "Я отмахнулся от собиравшейся что-то возразить девушки и продолжил:"
    me "Работа не тяжёлая, да и сделала ты её почти всю сама, помощи от меня особой не было."
    me "Что есть я, что нет - никакой разницы."
    show sl serious pioneer with dspr
    "Помолчав несколько секунд, Славя отложила в сторону стопку белья и присела напротив меня на последний неразвязанный тюк."
    show sl serious pioneer close with dissolve
    #вообще, дальше активно поиграться с эмоциями
    sl "Ты не думаешь, что мне не так уж весело быть всё время одной?"
    "Вздохнула она и посмотрела мне прямо в глаза."
    sl "Я понимаю, это странно звучит, ведь вокруг меня всегда полно народу, я всё время что-то организую, помогаю кому-то, что-то улаживаю."
    sl "На самом деле, мне это и вправду нравится. {w}Нравится быть всё время занятой, быть нужной и полезной моим товарищам."
#ЛБ: TODO возможно, здесь надо больше букв про приятность полезности. Подсмотреть у Автора.
 
    sl "Но ты знаешь, Семён…"
    "Девушка нервно стиснула руки, переплетя пальцы."
    show sl tender pioneer
    sl "Иногда и мне хочется почувствовать себя не Славей-активисткой, а простой девушкой."
    sl "Хочется, чтобы кто-то позаботился и обо мне, помог не по обязанности… да просто побыл рядом!"
    sl "Кто-то хороший, Семён. Такой, как ты…"
    "Последние слова Славя произнесла еле слышно, глядя в пол."
    "Я, слушавший это неожиданное признание с открытым ртом, растерянно заморгал, но девушка тут же выпрямилась, махнув рукой."
    show sl smile2 pioneer
    sl "Ох, извини Семён. Что-то я разболталась."
    sl "У тебя, небось, своих дел полно, а тут я тебя мало того, что с тряпками возиться заставила, так ещё и всякими глупостями голову тебе забиваю, нашла время."
    "Она хотела было встать, но я, неожиданно для себя самого, удержал её за руку."
    "От прикосновения невольно вздрогнули оба. Славя медленно опустилась назад, вновь, как и за пару минут до того, пристально глядя мне прямо в глаза."
    me "Да нет, Славя, мне вовсе не трудно было тебе помочь."
    "Запинаясь, выдавил я из себя, отпуская руку девушки и стараясь сделать это по возможности деликатнее."
    me "И просто составить тебе компанию - я тоже рад. {w}Тем более, раз ты сама не против моего общества…"
    "Я неловко замолчал, чувствуя, что вступаю на тонкий лёд, но Славя, к счастью, не стала настаивать на продолжении."
    sl "Ну вот и хорошо! {w}Тогда давай заканчивать, да?"
    show sl normal pioneer
    "Я кивнул, и мы вернулись к работе, некстати прерванной моим вопросом."
    #текст на весь экран
    
    "Простые искренние слова девушки невольно тронули меня."
    "Продолжая машинально ковыряться в простынях, я сидел и думал, что мне давно не встречались такие хорошие, открытые люди, как Славя."
    "Думал, что за все эти дни не видел от неё ничего, кроме хорошего."
    "Тут я вспомнил нашу первую встречу возле автобуса и смущённо покосился на девушку."
    th "Знала бы она, что я тогда про неё думал… {w}Хорошо всё-таки, что телепатии не существует - иначе сраму бы не обобрался."
    "В последнем тюке оказались выстиранные личные вещи отыхающих - всякие там штаны-рубашки."
    "Славя легкомысленно махнула рукой."
    sl "Семён, оставь, пусть лежат пока."
    sl "Я потом разберу по отрядам, там везде метки нашиты, без них в стирку не принимают, а дальше вожатые раздадут."
    window hide
    play sound sfx_open_door_clubs fadein 0
    scene bg ext_warehouse_day 
    show sl normal pioneer
    with dissolve
    window show
    "Мы вышли из прохладного полумрака склада под изрядно припекающее уже солнце, и Славя, немного повозившись с замком, заперла дверь."
    sl "Семён, спасибо тебе большое!"
    show sl shy pioneer
    sl "Знаешь, я, наверное, совсем обнаглела, но… {w}Ты как, не против ещё немного мне помочь?"
    sl "Если я тебе не слишком надоела, конечно."
    me "Конечно же нет, не против!"
    "Невольно вырвалось у меня прежде, чем я успел прикусить язык."
    th "А хотя, что здесь такого? Поработаю ещё немного на пользу общества в приятной компании. Социализация, опять же…"
    th "В любом случае, дольше, чем отсюда и до обеда, работать не придётся."
    show sl smile pioneer
    sl "Вот и славно!"
    "Не заставила уговаривать себя девушка."
    sl "Пойдём скорее!"
    "Не успел я опомниться, как меня уже вновь тащили за руку - и вновь в неизвестном направлении."
#ЛБ: далее правленная копипаста варианта Сычёва
#ЛБ: нужна проверка спрайтов, сцен и проч.
    # сцена - дорожка между домиками днём, затем площадь. Тряска от бега.
    me "Славя, а теперь-то куда?"
    "Пропыхтел я на бегу."
    th "Что за жизнь такая, неужели нельзя хотя бы иногда не бежать, а идти нормально?"
    sl "А я разве не сказала? Мы с тобой в клуб идём. Серёжа нас уже, наверное, заждался."
    me "Сыроежкин?"
    sl "Ну да. Я ему сказала, чтобы через полчаса после завтрака был как штык возле музыкального клуба. А он очень ответственный, волноваться будет."
    hide sl with dissolve
    window hide
    scene bg ext_musclub_day
    show sl normal pioneer
    with dissolve
    window show
    "Но возле клуба Электроника не было."
    th "Где же наш невероятно пунктуальный кибернетик?"
    el "Ребята! Вот вы где!"
    "Раздался сзади запыхавшийся голос Сыроежкина."
    show sl normal pioneer at right
    show el normal pioneer at left
    with dissolve
    el "Слушайте, где вы ходите? Я вас по всему лагерю ищу, бегаю… Работа же стоит."
    me "Работа стоит, а срок идёт. Не забывай: у тебя зарплата в рублях, а у меня в сутках."
    "В тон ему ответил я."
    show el laugh pioneer at left
    with dissolve
    "Эл пару секунд хлопал глазами, но потом рассмеялся - видимо, дошло."
    show sl smile pioneer at right
    with dissolve
    "Улыбка Слави вышла немного неуверенной, но и она деликатно хихикнула пару раз."
    show sl normal pioneer at right
    show el normal pioneer at left
    with dissolve
    sl "Ладно, заходим, а то и правда не успеем ничего."
    window hide
    play ambience ambience_music_club_day fadein 4
    #ЛБ: хорошо бы поставить какую-нибудь мелодию на фортепьяно, раз Мику репетирует. Например, memories_piano. Потом мелодия обрывается по короткому fadeout после реплики Мику
    play music lastlight_piano fadein 2
    play ambience ambience_music_club_day fadein 4
    scene bg int_musclub_day with dissolve
    window show
    "В этот раз Мику сидела не под роялем, а за ним, наигрывая какую-то незнакомую мелодию."
    th "Наверное, репертуар на вечер подбирает."
    show mi normal pioneer at right behind sl
    show sl normal pioneer
    show el normal pioneer at left
    with dissolve
    stop music fadeout 1
    mi "Привет, ребята! Как хорошо, что вы зашли."
    "Защебетала болтушка и махнула головой, отчего длиннющие ультрамариновые хвосты её волос прыгнули вверх-вниз, застаив меня невольно залюбоваться."
    show mi happy pioneer at right with dspr
    mi "Я столько всего приготовила к концерту! Буду петь, и танцевать, и вести… А вы что-нибудь приготовили?"
    if alt_day2_club_join_musc:
        "Я отрицательно помотал головой и Мику укоризненно посмотрела на меня."
        mi "Сёма, ты ведь записывался в музкружок, а не участвуешь ни в одном номере. И даже ни разу не зашёл ни на одну репетицию. Не стыдно тебе?"
        "Я пожал плечами."
        me "Да не особенно…"
        "Мику изо всех сил старалась напустить на себя строгий вид, но глаза её смеялись."
        mi "Ладно, мы ещё сделаем из тебя настоящего музыканта. Ты ещё будешь выступать…"
    sl "Подожди, Мику."
    show mi normal pioneer at right with dspr
    "Остановила девочку-оркестр Славя."
    sl "Ты утром говорила мне про инструменты и аппаратуру."
    mi "Конечно-конечно, берите. Вот гитары, вот барабанная установка, вот усилитель, а вот здесь колонки."
    "Говорила она, размахивая руками."
    mi "А вот шнуры ещё. И стойки для микрофонов."
    "Я почесал затылок, оглядывая всё это музыкальное добро. Много. За один раз-то и не унести. Но уж взялся за гуж…"
    "И вот уже второй раз мы с Электроником стали товарищами по несчастью в переноске всяких тяжёлых и бесполезных грузов."
    window hide
    play ambience ambience_camp_center_day fadein 4
    scene bg ext_stage_normal_day
    show sl normal pioneer
    with dissolve
    window show
    "Проклятый усилитель оттянул мне все руки, а несколько сотен метров от клуба до сцены показались марафонской дистанцией."
    th "Ну вот почему здесь так распространён ручной труд, а?"
    th "А Славя тоже хороша - знала ведь, что аппаратуру таскать придётся, могли захватить хотя бы ту тележку, на которой бельё возили."
    "Мы занесли неуклюжий ящик по ступенькам, по пути чуть не уронив, и с облегчением поставили на дощатый пол сцены."
    "Впрочем, вспомнив про колонки, я снова приуныл - возьни с ними будет ненамного меньше, чем с усилком. А ещё ведь остальное барахло тащить… {w}И дёрнула же меня нелёгкая согласиться помогать."
    "Провозились мы в итоге целую вечность, пока наконец не перенесли всё. Хорошо хоть, обе девочки помогали - Мику тоже не смогла усидеть в клубе, и под предлогом «мне тут одной всё равно скучно», вместе со Славей носила то, что полегче."
    play music eat_horn fadein 3
    "Водрузив на сцену последнюю пару микрофонных стоек, я уселся на край сцены, чтобы немного передохнуть."
    "Не успел я перевести дух, как ко мне подсела Славя."
    "Я с завистью покосился на девушку - вот уж кому работа не была в тягость."
    "Слегка покачивая ногой, она улыбнулась мне немного смущённо."
    sl "Семён, я просто не знаю, как тебя благодарить."
    me "Пустое…"
    "Устало буркнул я. Очень хотелось пить, а ещё - сорвать наконец эту чёртову красную удавку с шеи и зашвырнуть куда подальше."
    sl "Ну что ты, Семён! Как же \"пустое\", если ты на меня полдня потратил. Я тебе очень, очень благодарна, правда!"
    show sl shy pioneer with dspr
    sl "И знаешь, я тебя хотела спросить…"
    "Славя неловко замялась и я, уже наученный горьким опытом, не смог сдержать стон."
    th "Шо, опять?!!"
    "Взглянув на меня, девушка рассмеялась."
    show sl laugh pioneer with dspr
    sl "Ох, извини, но у тебя такое лицо сделалось!"
    show sl smile pioneer dspr
    sl "Не бойся, носить больше ничего не нужно."
    sl "Я просто хотела спросить тебя… {w=2} Ты пойдёшь сегодня вечером на танцы?"
    "До меня не сразу дошло, о чём она говорит."
    th "Ах да, сегодня же последний день, а значит - дискотека вечером."
    dreamgirl "А потом - королевская ночь, если ты вдруг забыл."
    "Я пожал плечами."
    me "Да я как-то не думал, честно говоря."
    show sl normal pioneer dspr
    sl "А вот возьми и подумай."
    sl "Тем более в лагере есть одна девушка, которая очень-очень будет тебя там ждать."
    show sl shy pioneer with dspr
#ЛБ: Следующая вилка сейчас не работает - при сычевании второго танца (выход на ЮВАО) всегда выставляется alt_day3_dancing = 5, и мы ничего не знаем про первый танец. В противном же случае это было бы исключительно "2" - остальные варианты ("20" и "21") невозможны, т.к. подразумевают второй танец со Славей вместо сычевания
#    if (alt_day3_dancing == 2 or alt_day3_dancing == 20 or alt_day3_dancing == 21):
#        sl "И эта девушка совсем не прочь вновь с тобой потанцевать."
#    else:
#        sl "И эта девушка совсем не прочь с тобой потанцевать, пусть уж в прошлый раз и не удалось."
    sl "И эта девушка совсем не прочь с тобой потанцевать."
    #горн
    "Славя легко спрыгнула со сцены."
    show sl smile pioneer with dissolve
    if alt_uvao_D6_sl_assert = 3:
        sl "А ведь после дискотеки ещё и вечер будет. {w}Долгий-долгий…"
    "Лукаво улыбнувшись мне напоследок, она заспешила в сторону столовой."
    hide sl with easeoutleft
    if alt_uvao_D6_sl_assert = 3:
        th "Вот это что сейчас было про \"долгий-долгий вечер\", а? {w}Или я что-то пропустил?"
        dreamgirl "А что тебе непонятно? {w}Вполне прозрачный намёк - кто девушку танцует, тот её и… того-этого."
        th "Что ты плетёшь, какое ещё тебе \"того-этого\"?"
        dreamgirl "Ну в данном случае - всё-таки целоваться, наверное. {w}Хотя, кто знает, кто знает…"
    "Проводив Славю взглядом, я сполз со сцены и поплёлся следом за ней."
    $ alt_uvao_D6_left_duty = True
    stop music fadeout 5
    #jump alt_day6_uvao_lunch
