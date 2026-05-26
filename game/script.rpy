define a = Character("Alvi")
define au = Character("Aulia")
define hr = Character("Haruka")

image bg classroom = "images/bg/classroom.jpg"
image bg teacher_room = "images/bg/teacher_room.jpg"
image bg school_gate = "images/bg/school_gate.jpg"
image bg school_gate_rain = "images/bg/school_gate_rain.jpg"
image bg warehouse = "images/bg/warehouse.jpg"

image aulia normal = "images/characters/aulia_normal.png"
image aulia smile = "images/characters/aulia_smile.png"
image aulia laugh = "images/characters/aulia_laugh.png"
image aulia embarrassed = "images/characters/aulia_embarrassed.png"
image aulia surprised = "images/characters/aulia_surprised.png"
image aulia pout = "images/characters/aulia_pout.png"
image aulia blush = "images/characters/aulia_blush.png"

transform bgfit:
    size (1920, 1080)

transform charleft:
    xalign 0.15
    yalign 1.0
    zoom 0.45

transform charright:
    xalign 0.85
    yalign 1.0
    zoom 0.45

transform charcenter:
    xalign 0.5
    yalign 1.0
    zoom 0.45

init python:
    renpy.music.register_channel(
        "ambience",
        mixer="ambience",
        loop=True
    )

label start:

    scene bg classroom at bgfit with fade

    play music "audio/backsound.mp3" fadein 2.0

    "Sekolah di hari kamis ini selesai dengan lebih awal karena akan diadakan rapat."
    "Tapi aku sepertinya tidak bisa pulang seawal siswa lain."
    "Karena aku masih ada tanggungan tugas dari guru matematika."

    hr "Alvi, kerjakan dari halaman 34 sampai halaman 36 ya!"
    a "Huft...."
    hr "Kalo gitu ibu tinggal dulu."

    "Bu Haruka meninggalkan ruangan kelas, meninggalkanku bersama tugas matematika yang bikin pusing."

    a "Andai saja hari itu aku nggak sakit demam..."
    a "Mungkin sekarang aku udah nyantai di rumah menikmati enaknya pulang lebih cepat."

    scene bg classroom at bgfit with dissolve

    "Beberapa menit berlalu."
    "Aku mengerjakan tugas itu sepenuh hati di ruang kelas sendirian."

    a "Anjay akhirnya kelar......"
    a "Kumpulin ah, aku mau cepat-cepat pulang nih."

    scene bg teacher_room at bgfit with fade

    a "Bu Haruka ini tugasnya udah selesai."

    "Aku menaruh kertas tugas di meja Bu Haruka."

    hr "Oh Alvi, bagus sekali."
    a "Kalo gitu permisi bu."
    hr "Ya, hati-hati pulangnya."

    scene bg school_gate at bgfit with fade

    "Aku pun berjalan menuju gerbang sekolah."
    "Tapi saat sudah dekat dengan gerbang sekolah..."

    scene bg school_gate_rain at bgfit
    play sound "audio/thunder.mp3"
    with vpunch
    pause 1.0
    "Tiba-tiba hujan yang sangat deras mulai turun."
    stop sound
    a "Aduh..."
    play ambience "audio/rain.mp3" fadein 2.0
    a "Ini kalo kena hujan nanti aku sakit lagi."

    "Aku pun mencari tempat teduh."
    "Dan tempat terdekat dari situ adalah gudang olahraga."

    scene bg warehouse at bgfit with fade

    "Aku langsung lari menuju ke sana."
    "Untungnya bajuku cuma basah sedikit."

    "Saat membuka pintu gudang olahraga..."
    "Ternyata di sana sudah ada seseorang yang sedang berteduh."

    show aulia normal at charcenter with dissolve

    au "?!"
    au "Alvi?"

    a "Aulia?"

    show aulia smile with dissolve

    au "Hahaha..."
    au "Kamu kehujanan juga pasti."

    a "Ugh...."
    a "Padahal dah kelar nugas terus tinggal pulang."
    a "Kamu sendiri ngapain masih di sekolah?"

    au "Hari ini aku ada kegiatan ekstrakurikuler lari."
    au "Niat hati aku mau ambil cone buat di lapangan..."
    au "Eh malah hujan."

    a "Aku ngikut neduh boleh ya?"

    au "Sini."

    hide aulia
    show aulia normal at charleft with move

    "Aku pun berteduh bersama Aulia di gudang olahraga."

    "Suasana canggung mulai terasa detik demi detik."

    a "Kamu emang suka olahraga ya?"

    au "Ah itu mungkin sejak kecil."
    au "Aku sering diajak jogging sama kakakku muterin kota."

    a "Wah..."
    a "Pantesan kamu kuat lari terus pas olahraga."

    au "Hah?"
    au "Emang aku keliatan seaktif itu?"

    a "Lumayan."

    show aulia smile with dissolve

    "Aulia terkekeh pelan."

    "Suara hujan di luar gudang semakin deras, memenuhi jeda percakapan kami."

    "Aku duduk di dekat rak bola basket sambil memandangi hujan yang turun seperti tirai putih."

    au "Kalau kamu sendiri?"

    a "Selain mengeluh hidup."

    show aulia laugh with dissolve

    au "Buset..."
    au "Aku segitu keliatannya?"

    a "Sedikit."

    au "Sedikit apanya itu jelas banget nyindir."

    au "Hahaha..."

    "Aku diam beberapa detik."

    "Entah kenapa..."
    "Suasana yang awalnya canggung mulai terasa nyaman."

    a "Aku sebenarnya nggak punya hobi yang spesifik sih."
    a "Paling main game..."
    a "Terus kadang ngulas materi pelajaran."

    au "Woah... rajinnya."

    a "Yah belum seberapa."
    a "Intinya semester ini aku harus ranking satu."

    au "Hahaha..."
    au "Ketua kelas kita emang susah dikalahin sih."

    show aulia smile with dissolve

    "Aulia tersenyum kecil."

    play sound "audio/thunder.mp3"
    with hpunch

    "BRRAKKK!!"
    stop sound
    show aulia surprised with dissolve
    play ambience "audio/rain.mp3" fadein 2.0
    au "?!"

    show aulia blush with dissolve

    "Aulia sedikit terkejut sampai refleks memegang lenganku."

    pause 1.0

    "... "
    "... "

    show aulia embarrassed with dissolve

    au "Eh— maaf refleks."

    a "G-gapapa kok..."

    "Aku berusaha terdengar santai walaupun jantungku barusan hampir lompat keluar."

    "Suasana mendadak jadi aneh."

    "Hujan masih turun deras."
    "Tapi sekarang rasanya wajahku lebih panas daripada udara di gudang olahraga."

    a "Kayaknya hujannya masih lama reda."

    au "Iya..."

    a "Mana lapar lagi."

    show aulia normal with dissolve

    "Aulia langsung menoleh."

    au "Kamu belum makan?"

    a "Tadi buru-buru berangkat jadi belum sempet sarapan."

    au "Hm..."

    "Aulia tampak berpikir sebentar sebelum akhirnya membuka tasnya."

    show aulia smile with dissolve

    au "Aku ada biskuit sih..."

    a "Serius?"

    au "Tapi tinggal sedikit."

    a "Sedikit juga gapapa daripada mati kelaparan."

    show aulia laugh with dissolve

    au "Heh lebay."

    "Aulia memberikan bungkus biskuit kecil itu."

    "Tangan kami sempat bersentuhan sedikit."

    pause 0.7

    "Dan entah kenapa..."
    "Kami sama-sama langsung mengalihkan pandangan."

    a "...Makasih."

    au "Iya."

    pause 1.0

    "Hening lagi."

    "Aku menggigit biskuit sambil melihat hujan."

    a "Kalau hujannya nggak reda gimana?"

    show aulia normal with dissolve

    au "Hm..."

    "Aulia ikut melihat keluar gudang."

    au "Paling nunggu sampai sore."

    a "Wah..."
    a "Bisa lumutan kita di sini."

    show aulia laugh with dissolve

    au "Hahaha...."

    pause 1.0

    "Suasana kembali hening beberapa saat."

    "Namun kali ini tidak secanggung sebelumnya."

    "Aulia duduk di sebelah rak net voli sambil memainkan bungkus biskuit kosong di tangannya."

    show aulia normal with dissolve

    au "Ngomong-ngomong..."

    a "Hm?"

    au "UAS udah deket ya."

    a "Iya..."

    "Aku menghela napas panjang."

    a "Belum lagi tugas numpuk."

    show aulia smile with dissolve

    au "Makanya aku heran kamu masih sempet santai."

    a "Hah?"
    a "Aku keliatan santai?"

    au "Lumayan."

    a "Padahal dalem hati aku udah pengen tidur seminggu."

    show aulia laugh with dissolve

    au "Hahaha..."

    pause 1.0

    "Aulia tertawa kecil lagi."

    "Lalu setelah jeda beberapa detik..."
    "Suaranya berubah sedikit lebih pelan."

    show aulia normal with dissolve

    au "Alvi..."

    a "Hm?"

    show aulia embarrassed with dissolve

    au "...Ajarin aku belajar dong."

    "Aku langsung menoleh."

    a "Hah?"

    au "Ya... buat UAS."

    "Aulia menggaruk pipinya pelan."

    au "Nilai aku agak bahaya deh kali ini..."
    au "Terutama matematika."

    a "Oalah..."

    show aulia pout with dissolve

    au "Jangan 'oalah' gitu dong."

    a "Enggak maksudku..."
    a "Kirain kenapa."

    show aulia normal with dissolve

    "Aku tersenyum kecil."

    a "Ya boleh sih."

    show aulia surprised with dissolve

    au "Beneran?"

    a "Iya."
    a "Toh aku juga lagi fokus belajar."

    show aulia smile with dissolve

    "Wajah Aulia langsung sedikit lebih cerah."

    au "Yess..."

    a "Tapi belajar di mana?"

    show aulia normal with dissolve

    au "Nah itu."

    pause 1.0

    "... "
    "... "

    a "Rumahku sih kosong kalau sore."

    show aulia surprised with dissolve

    au "?!"

    a "Eh— maksudku bukan ngajak yang aneh ya."

    show aulia embarrassed with dissolve

    au "AKU JUGA NGGAK MIKIR GITU."

    a "Kenapa jadi teriak..."

    au "A-ah enggak..."

    "Wajah Aulia mulai memerah."

    "Aku yang sadar ucapanku barusan terdengar salah juga mulai salah tingkah sendiri."

    show aulia normal with dissolve

    au "Kalau... kalau rumahku kadang rame sih."

    au "Jadi mungkin susah fokus."

    a "Iya juga..."

    pause 1.0

    "Hening lagi."

    "Suara hujan mulai mengecil perlahan."

    pause 1.0

    show aulia surprised with dissolve

    au "Eh..."

    a "Hm?"

    show aulia smile with dissolve

    au "Kalau... di cafe aja?"

    a "...Cafe?"

    au "Iya."
    au "Kan sekarang banyak cafe yang buat belajar juga."

    au "WiFi ada..."
    au "Terus bisa sambil nugas."

    show aulia embarrassed with dissolve

    au "Eh tapi bukan ngajak date ya!"

    a "HAH?!"

    au "Eh maksudku— belajar!"
    au "Fokus belajar!"

    a "I-iya aku juga mikirnya belajar kali!"

    pause 0.7

    show aulia smile with dissolve

    au "Syukur deh..."

    a "Memangnya aku keliatan kayak orang yang mikir aneh-aneh?"

    show aulia laugh with dissolve

    au "...Sedikit."

    a "Buset."

    "Aulia menahan tawanya."

    pause 1.0

    show aulia normal with dissolve

    au "Jadi..."

    au "Gimana?"

    "Aku menarik napas kecil."

    a "...Boleh."

    show aulia smile with dissolve

    au "Hm?"

    a "Kita belajar di cafe."

    "Senyum kecil langsung muncul di wajah Aulia."

    au "Oke."

    pause 1.0

    "Dan entah kenapa..."

    "Melihat senyum itu membuatku mulai berharap hujannya turun sedikit lebih lama lagi."

    scene black with fade
    stop ambience fadeout 2.0

    centered "--- END ---"
    centered "--- Thank For Playing ---"

    return