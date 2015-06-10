# Отдыхаем у домика МТ, встречаем Юлю.
label alt_day6_uvao_mt_house:
    window hide
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 4
    play music music_list["dance_of_fireflies"] fadein 4
    window show
    "Чем занять себя благородному дону до вечера? Пойти мячик попинать с Ульянкой? Или на речку потихоньку свалить? А, ничего мне на самом деле не охота, пойду-ка я лучше отдохну. Буквально только глаза прикрою. Буду решать архиважную проблему - на каком боку удобнее провести следующие пару часов."
    dreamgirl "Ну и ленив же ты, братец. Что, сил для игр и роста требуется ой, как много?"
    th "Конечно много. Мне ещё вечером Славю разговаривать. Кто знает, что она от меня хочет."
    "В самом деле: Очень Важный Разговор – это вам не просто разговор."
    th "Да, этот разговор стоит обдумать. О чём бы он ни был. И отношение Слави ко мне тоже. Она, видимо, с самого начала оказывала мне какие-то знаки внимания, а я, увлечённый поиском ответов, похоже ничего вокруг не замечал. Но ничего, мы ещё наверстаем упущенное."
    window hide
    scene bg ext_square_day with dissolve
    window show
    th "Блин, и о чём я только думаю? Я, «человек в футляре», человек, больше всего на свете ценящий собственную независимость, интроверт, боящийся, как огня, общества людей, человек избравший своим жизненным кредо девиз \"Просто оставьте меня в покое\" -  и обдумываю какие-то планы на, подумать только, отношения с девочкой. Возможно длительные и далеко идущие."
    th "Я боюсь признаться в этом самому себе, но кажется лагерь изменил меня. И изменения мне нравятся. Да, ассимиляция произошла не сразу, но сейчас я уже не то безвольное, рефлексующее существо, шагнувшее в ворота лагеря неделю назад."
    th "Поэтому надо вести себя соответственно  - плечи расправлены, голова прямо, походка твёрдая, уверенная. Характер нордический, стойкий… Да, над характером ещё надо поработать, конечно."
    window hide
    scene bg ext_house_of_mt_day with dissolve
    window show
    "За этими размышлениями я не заметил, как подошёл к нашему с вожатой домику. "
    play sound sfx_bush_leaves
    extend "В кустах зашуршало и Юлин голос, сдавленный от сдерживаемого смеха, позвал."
    uv "Семён, иди сюда."
    "Меня как будто ледяной водой из ведра окатили. По спине побежали весёлые стайки мурашек, походка тут же утратила всю свою твёрдость, а плечи снова втянулись на положенное им место."
    me "Кто, я?"
    "Спросил я у кустов. Неожиданно севшим голосом."
    uv "Ты конечно. Смешной. Здесь же кроме тебя никого нет."
    #"В ушах зазвучали предупреждения Виолетты Церновны. А внутренний голос вкрадчиво поинтересовался:" 
    #dreamgirl "Да, Семён, может быть, правда {i}здесь кроме тебя никого нет?{/i}" #Альт. вариант от Ленофага
    "У меня в ушах снова зазвучали все предостережения Виолетты Церновны: "
    #Может и не нужны эти пунчи, уберите если надо -R
    extend "\"…аномалия опасна…\", " with hpunch
    extend "\"…страдает психика…\", " with vpunch
    extend "\"…вегетативное состояние…\", " with hpunch
    extend "\"…держаться подальше…\"." with vpunch
    "Думай, Семён, думай. Причём на раздумья у тебя не более двух секунд."
    "Итак, что же мне делать? Ведь я для себя решил не иметь больше с… Юлей никаких контактов. Даже после всех предупреждений и предостережений, у меня язык не поворачивался назвать её аномалией."
    "Ну не была она похожа на аномалию! Вот в \"Ждалкере\" аномалии. \"Жарка\" там, или \"Трамплин\". Но здесь не \"Зона\", а Юля не \"Исполнитель Желаний\". Хотя кто знает…"
    "Да и зачем обижать её отказом? Она мне ничего плохого не сделала. Ну разве что голова разболелась, но это необязательно из за неё. Голова может болеть по множеству причин. От недосыпа например, чем я регулярно грешил в той своей жизни."
    "Ладно, будем держать дистанцию. И чтобы всё в рамках приличия."
    uv "Семён, ну где ты там? Уснул что-ли?"
    "Вновь напомнила о себе Юля."
    "Помедлив мгновенье, я шагнул в кусты."
    play sound sfx_bush_leaves
    $ renpy.pause(1, hard=True)
    show uv surprise close at center with dissolve
    "И сразу заметил, что Юля здорово взбудоражена. Зрачки расширены, уши торчком, хвост нервно мечется из стороны в сторону."
    me "Э-э-э… Юля, что с тобой?"
    "Поинтересовался я, на всякий случай отодвинувшись подальше."
    uv "Что? А что со мной не так?"
    "И она оглядела себя со всех сторон, даже попытавшись заглянуть за спину. Там понятное дело ничего подозрительного не было."
    me "Да я про то, что ты нервничаешь, похоже. Случилось что-то?"
    uv "Нет, ничего не случилось. Ваши по лагерю бегают. Много. Раньше не было такого. Мне интересно."
    me "А, это. Это они к концерту вечернему готовятся."
    show uv normal close at center with dspr
    uv "А что это такое?"
    "Придётся видимо потратить некоторое время на объяснения."
    me "Ну это когда одни люди поют или танцуют на сцене. А другие люди смотрят и получают удовольствие…"
    uv "А, помню."
    show uv smile close at center with dspr
    "Перебила меня Юля."
    uv "Ты, когда только приехал, тоже на сцене выступал. Это он и был, этот твой концерт?"
    "Я закрыл лицо рукой. Мне даже показалось, что над головой у меня загорелся здоровенный смайлик с фейспалмом."
    "В этом лагере вообще остался человек, который не видел бы моих кривляний на сцене? Похоже, что нет."
    me "Ну это как бы не совсем концерт был."
    "Почему-то попытался оправдаться я."
    me "Репетиция."
    show uv surprise close at center with dspr
    uv "Ре-те-петиция…? А это что?"
    me "Ну каждый музыкант перед настоящим выступлением репетирует свой номер. Чтобы всё гладко прошло." 
    uv "Я слышала, как поёт девочка с длинными аквамариновыми волосами."
    show uv normal close at center with dspr
    uv "Я в окно подсмотрела: она сидела за какой-то большой  штукой и нажимала на белые и чёрные полоски и получался очень красивый звук."
    me "Музыкальный клуб. Мику играла на рояле."
    "Понимающе кивнул я."
    me "Да, у неё очень красивый голос."
    me "Ну и вот, перед любым выступлением, музыканты настраивают инструменты: гитарист гитару, пианист фортепиано, а певец голос тренирует. На музыкальных инструментах играют, а в микрофон поют, понимаешь?"
    "Мой рассказ о преимуществах струнного инструмента перед клавишным несколько раз прерывался, из за того что в домик вожатой по очереди приходили Лена, Славя и почему-то Саныч."
    "Потоптавшись на крыльце и убедившись, что в домике  никого нет, они уходили восвояси. Интересно, где же это наша вожатая околачивается, что её никто нигде найти не может?"
    "Юля, похоже, понимала меня с пятого на десятое и постоянно порывалась вылезти из кустов, в которых мы так удачно спрятались. Видимо её будоражили звуки репетиции со сцены."
    show uv smile close at center with dspr
    uv "Я тоже приду на концерт."
    "Вдруг безапелляционно заявила она."
    "Я почему-то совершено не удивился."
    me "И как ты себе это представляешь?"
    "Усмехнулся я."
    me "Оденем тебя в пионерскую форму? Уши под панамку спрячем, а хвост куда денешь?"
    show uv guilty close at center with dspr
    uv "Не знаю."
    "С явным неудовольствием ответила Юля."
    "Похоже желание посмотреть концерт было настолько велико, что она даже готова была пойти на риск быть кем-то замеченной."
    uv "Никакую форму я одевать не буду."
    uv "Подберусь поближе незаметно, как всегда, вот и всё."
    "По насупившемуся лицу Юли видно было, что от своего она не отступится. Почему-то в этот момент она очень напоминала Ульянку. Разве что у Ульянки ушей нет."
    dreamgirl "И хвоста!"
    me "Юль, да я и не собираюсь тебя отговаривать."
    me "Просто не надо близко подходить. Заметят ведь. Там сегодня весь лагерь будет. А это ого-го как много людей. Кто-нибудь непременно заметит."
    uv "Я буду осторожна."
    "Пообещала Юля."
    "Спасибо и на этом. Не хотелось бы панику создавать. Реакцию толпы пионеров, заметивших кошко-девочку, предсказать невозможно."
    "Тем временем из репродукторов по лагерю разносился голос Мику, открывающей концерт. Ого! Время-то незаметно прошло. Надо бежать, а то вожатая меня скормит кому-нибудь. Не пираньям конечно. Но тому же Санычу вполне, вполне…"
    me "Ладно, Юль, мне бежать пора уже, а то ругаться будут."
    show uv smile close at center with dspr
    uv "За уши оттреплют?"
    "Улыбнулась кошечка."
    me "Ну не оттреплют конечно, но надают по ним точно."
    "Ответил шуткой на шутку и я."
    "Ну что же, пора приобщаться к местной самодеятельности. Пусть грянут мне что-нибудь этакое."
    stop music fadeout 4
    stop ambience
    jump alt_day6_uvao_concert
