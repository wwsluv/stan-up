import pandas as pd
import streamlit as st

# 函數：生成 CSV 檔案
def generate_csv_files():
    # 偶像資料
    idol_data = {
        "group": ["bts", "bts", "bts", "bts", "bts", "bts", "bts", "svt", "svt", "svt", "svt", "svt", "svt", "svt", "svt", "svt", "svt", "svt", "svt", "svt", "zb1", "zb1", "zb1", "zb1", "zb1", "zb1", "zb1", "zb1", "zb1", "aespa", "aespa", "aespa", "aespa", "nmixx", "nmixx", "nmixx", "nmixx", "nmixx", "nmixx", "TWS", "TWS", "TWS", "TWS", "TWS", "TWS", "skz", "skz", "skz", "skz", "skz", "skz", "skz", "skz", "viviz", "viviz", "viviz", "enhypen", "enhypen", "enhypen", "enhypen", "enhypen", "enhypen", "enhypen", "boynextdoor", "boynextdoor", "boynextdoor", "boynextdoor", "boynextdoor", "boynextdoor", "illit", "illit", "illit", "illit", "illit", "babymonster", "babymonster", "babymonster", "babymonster", "babymonster", "babymonster", "babymonster", "izna", "izna", "izna", "izna", "izna", "izna", "izna"],
        "member": ["Jungkook", "RM", "JIN", "SUGA", "jhope", "jimin", "V", "S.COUPS", "JEONGHAN", "JOSHUA", "JUN", "HOSHI", "WONWOO", "WOOZI", "DK", "MINGYU", "THE 8", "SEUNGKWAN", "VERNON", "DINO", "金地雄", "章昊", "成韓彬", "seok matthew", "金泰來", "ricky", "金奎彬", "朴乾旭", "韓維辰", "karina", "winter", "ningning", "giselle", "lily", "haewon", "sullyoon", "bae", "jiwoo", "kyujin", "申惟", "金道勳", "英宰", "韓振", "志薰", "炅潣", "方燦", "Lee Know", "彰彬", "鉉辰", "HAN", "Felix", "昇玟", "I.N", "銀河", "信飛", "嚴智", "HEESEUNG", "JAY", "JAKE", "SUNGHOON", "SUNOO", "JUNGWON", "NI-KI", "SUNGHO", "RIWOO", "JAEHYUN", "TAESAN", "LEEHAN", "WOONHAK", "Yunah", "Minju", "Moka", "Wonhee", "Iroha", "Ruka", "Pharita", "Asa", "Ahyeon", "Rami", "Rora", "Chiquita", "MAI", "BANG JEEMIN", "YOON JIYOON", "KOKO", "RYU SARANG", "CHOI JUNGEUN", "JEONG SAEBI"],
        "生日": ["1997/09/01", "1994/09/12", "1992/12/04", "1993/03/09", "1994/02/18", "1995/10/13", "1995/12/30", "1995/08/08", "1995/10/04", "1995/12/30", "1996/06/10", "1996/06/15", "1996/07/17", "1996/11/22", "1997/02/18", "1997/04/06", "1997/11/07", "1998/01/16", "1998/02/18", "1999/02/11", "1998/12/14", "2000/07/25", "2001/06/13", "2002/05/28", "2002/07/14", "2004/05/20", "2004/08/30", "2005/01/10", "2007/03/20", "2000/04/11", "2001/01/01", "2002/10/23", "2000/10/30", "2002/10/17", "2003/02/25", "2004/01/26", "2004/12/28", "2005/04/13", "2006/05/26", "2003/11/07", "2005/01/30", "2005/05/31", "2006/01/05", "2006/03/28", "2007/10/02", "1997/10/03", "1998/1025", "1999/08/11", "2000/03/20", "2000/09/14", "2000/09/15", "2000/09/22", "2001/02/08", "1997/05/30", "1998/06/03", "1998/08/19", "2001/10/15", "2002/04/20", "2002/11/15", "2002/1208", "2003/06/24", "2004/02/09", "2005/12/09", "2003/09/04", "2003/10/22", "2003/12/04", "2004/08/10", "2004/10/20", "2006/11/29", "2004/01/15", "2004/05/11", "2004/10/08", "2007/06/26", "2008/02/04", "2002/03/20", "2005/08/26", "2006/04/17", "2007/04/11", "2007/10/17", "2008/08/14", "2009/02/17", "2004/10/28", "2005/05/08", "2005/07/14", "2006/11/14", "2007/04/18", "2007/08/04", "20080122"],
        "代表物": ["兔子", "無尾熊", "羊駝", "貓", "松鼠", "雞", "老虎", "櫻桃", "天使", "鹿", "貓", "老虎", "貓或狐狸", "米飯", "兔子 馬", "狗", "撞球8 青蛙", "橘子 熊", "白熊", "水獺", "蝴蝶 熊", "浣熊", "倉鼠", "狐狸", "鴨子", "貓", "狗", "獅子 豬", "兔子", "藍色愛心", "星星", "蝴蝶", "月亮", "無尾熊", "白熊", "兔子", "雞", "狗", "貓", "長頸鹿", "狼", "狗", "兔子", "水母", "狐獴", "狼", "兔子", "豬兔", "雪貂", "短尾矮袋鼠", "小雞", "小狗", "沙漠狐狸", "兔子", "貓", "倉鼠", "小鹿、倉鼠", "憤怒鳥", "沈小狗", "冰雪王子", "떠누", "梁真圓", "小麥可傑克森", "肩膀；南瓜", "woli riwoo", "天才小狗", "韓泰山", "王子", "泰迪熊", "盧秀宗", "憨柱、朴包子", "金Moka、金棉花", "布魯尼", "傑尼龜", "露露", "ta 妹", "Kim Asa", "雅嫻", "神厦藍", "李茶仁", "Canny", "無", "無", "無", "無", "無", "無", "無"],
        "暱稱": ["果果；黃金忙內", "破壞王；拉蒙", "大哥；太平洋肩膀", "閔咻嘎；閔swag；糖糖", "厚比", "糯米糕", "泰泰；四方嘴", "酷酷", "漢尼", "刷", "俊尼", "老虎", "圓又圓", "VOBO", "道兼米", "珉古", "小八", "小橘子", "啵噥", "燦尼", "熊尼", "章估哩；小熊貓", "彬彬；倉鼠貓", "友鉉歐巴", "時尚恐怖份子", "沈貓貓", "金咕嚕彬", "帕果奴", "桃子", "柚子；知珉", "金冬甜；冬冬", "寧王", "季節", "莉莉", "五百元", "薛將軍", "貝", "啾", "Q金", "申申惟", "Ddo-ee、Do-don-i、伊卡洛斯", "永春", "珍珍、大振哥", "小雞", "福星忙內", "Chris", "李糯、李知道", "大佬、彬尼", "黃選、塞口哥", "闊卡、韓尼", "菲菲、貓貓", "奶玟", "尹恩、小羊", "西瓜妹妹", "妃爺", "無", "鹿", "老鷹", "狗", "企鵝", "沙漠狐狸", "貓咪", "豹", "貓", "博美犬", "小浣熊", "黑貓", "蝦子", "熊", "獵豹", "兔子", "倉鼠", "小狗", "烏龜", "蝸牛", "麋鹿", "兔子", "熊；蝴蝶", "海豚；海豹", "熊貓", "黑貓", "狐狸", "貓", "白熊", "黑貓", "老虎", "獵豹", "兔子"],
        "入坑必看舞台直拍": [
            "https://youtu.be/w5XxXWJrARU?list=PLYCIUF7gsLsMtixdr10RDFdF0BPwAuU7e",
            "https://youtu.be/JeWcBiK7l6A?list=PLViit8r-YdDVxFJ3aKBsE4IjYzLLYmG9H",
            "https://youtu.be/ILHozj9ncG0?list=PLYPHcpcES1o5-KzaIflWgVB-sxVDcggSF",
            "https://youtu.be/BZ7N161noT8",
            "https://youtu.be/VEAl4KjrQDA",
            "https://youtu.be/GfX62fI1NyA",
            "https://youtu.be/bXqElV07pO0?list=PLAIthTXqwhyweIqb4_aRhaRLERpZoXUjt",
            "https://youtu.be/Gx0qhFLw2-8?list=PLWyKN3M4adL2-6dPrxsPmyS96Ty7lxrbG",
            "https://youtu.be/l6WM8qyfOC0",
            "https://youtu.be/e6Vk7idSZ18",
            "https://youtu.be/skuu60G-6Fs",
            "https://youtu.be/GEI-MRNJRbw",
            "https://youtu.be/5ZWFtpM2whI",
            "https://youtu.be/kyDpO7Y1wy4",
            "https://youtu.be/4XOzTeIP3NI",
            "https://youtu.be/b1T3ooOtvOQ",
            "https://youtu.be/iW98v8PRoJc",
            "https://youtu.be/y245KIyw8rI?list=PLPXccaIsptSFUX5RSfJPe_7VAypvXdNAX",
            "https://youtu.be/yJ92IOcLMOM?list=PLkKAHz93oMBp1N0mNR6knYq0JpL7G-5Hk",
            "https://youtu.be/xJffijTpBb0?list=PLPXccaIsptSEDkclz7RpHgSJYcH0L9HPg",
            "https://youtu.be/B4lbrjNBEcw?list=PLnJGkdkTCu5rMYIi3ER3ekB7cDSPGqI31",
            "https://youtu.be/njavuTCaTzk?list=PLnJGkdkTCu5pdVlTs8s7JTCSFi8tH6iXB",
            "https://youtu.be/QzllsuAhTZ4",
            "https://youtu.be/VwdWY47SkEY?list=PLnJGkdkTCu5qKBQxl9CnOmG9Hs1Rcq0Wk",
            "https://youtu.be/-lvGl1VdbLU?list=PLVTxGOtz9-DljZwSSqPaa5IwITV0FH8X4",
            "https://youtu.be/Om6scxCTW3c?list=PLqUNWZS6cTAhG_-GHtWdk8DxPOU_6HkOU",
            "https://youtu.be/3FOhaLaOvNo?list=PLM9YNb5ahCdO7rZgDjfnCs0UXzsgJGkXg",
            "https://youtu.be/a3XV_rq4AvM?list=PLG6P1BsAhfO4hxCuHBQ_IHknsELiJiZWH",
            "https://youtu.be/tL7h38TKsUw?list=PLVTxGOtz9-Dncri5XBcjtEgpEr-wZ_iiV",
            "https://youtu.be/tbg3QAu-GnI",
            "https://youtu.be/qe0gepQh8N0?list=PLehPR0Z83CK5yU7y8x-vmQJAuM_gN-ki6",
            "https://youtu.be/Dvt7ZPL15xU",
            "https://youtu.be/XtO1XPSc67k?list=PLbCQnac5F70BN-4qd-n20C5Tz1bjz-O-s",
            "https://youtu.be/KFDRy9979Cs?list=PLJlIE1K_SquKK1sD9l6ZxrSLeS4xOUx5g",
            "https://youtu.be/ufwsqBS2VEo?list=PLe9b_otc9xsc7-ZPOC1GHphlHr5QjCLe4",
            "https://youtu.be/N4fPJNr0Qsk",
            "https://youtu.be/TbU3_uhlNZo?list=PLJlIE1K_SquLWcQoFAE5orJut21LA4vK9",
            "https://youtu.be/MnmQYLxQzcg?list=PLJlIE1K_SquLoJ4hjaM-gYSYdopZWpASL",
            "https://youtu.be/B0Lw_nkd7Ak?list=PLJlIE1K_SquKsvtBrfXv8YrhQdPWVYj78",
            "https://www.youtube.com/watch?v=VxmqjkFGyE0",
            "https://youtu.be/vDoPRKZc5Gs",
            "https://www.youtube.com/watch?v=MjPswsM0vcQ&list=PLwxKqzHQy4gVgHy0v5CKdt0orAAu1Gfpq&index=16",
            "https://www.youtube.com/watch?v=WxDm3oin7lk",
            "https://www.youtube.com/watch?v=7IG40w3Y-I0",
            "https://youtu.be/K3Nyu2AZM8c?list=PLnJGkdkTCu5pVXnMoUe04ClWTPXYlDjvp",
            "https://youtu.be/Bhrsgg28pVs",
            "https://youtu.be/HSY-Zlcy9PI",
            "https://youtu.be/0KutQ-2awW4",
            "https://youtu.be/wy_tMUsuHsE",
            "https://youtu.be/RzUtFk6ifLw",
            "https://youtu.be/K7T4_1vPm04",
            "https://youtu.be/Se9mxq3H4uA",
            "https://youtu.be/XJhXiEp5_nI",
            "https://www.youtube.com/watch?v=Gn8eN1OEh74",
            "https://youtu.be/mY_0AIdZmqc",
            "https://youtu.be/g8ngHI8699Q?list=PLPXccaIsptSFlXge0FpQJa2iehqhkxSus",
            "https://youtu.be/TkBkqtxsbNI",
            "https://youtu.be/bf-YPL2inBc",
            "https://youtu.be/0t5TOxtw5wQ",
            "https://youtu.be/wqw9A88tliE?list=PLpnX1H63BQ3PcI52BpSaeZd2YI2xiPekR",
            "https://youtu.be/yBtzvEKGrGw",
            "https://youtu.be/YClZaajazvM",
            "https://youtu.be/IuUVp3rn9pw",
            "https://youtu.be/UZNPMOPDaes",
            "https://youtu.be/7Ed2wC4VUfQ",
            "https://youtu.be/PX05ht8so7s",
            "https://youtu.be/Oae_jWpjdOU",
            "https://youtu.be/aQ5oaNHh7ts?list=PLBXiEUh8vqRoZ8PYxH6p9kjTBNPVz5toQ",
            "https://youtu.be/PYfH2NLzlJE",
            "https://youtu.be/CAqRGetyj6E?list=PLW5wOVk-AKkFBcq70Hk0xEA0LGfv7DAwu",
            "https://youtu.be/stnXEC9Q3B4",
            "https://youtu.be/zTihNUfbVEI",
            "https://youtu.be/sAlm8jlMFuQ?list=PLnJGkdkTCu5oCGwrmtqz5brsc-dMIv1TS",
            "https://youtu.be/r3YL0uAWBkk",
            "https://youtu.be/eP7wxVATQNY",
            "https://youtu.be/OC9FgU-o8D8",
            "https://youtu.be/B0z9ewmntkQ",
            "https://youtu.be/ciXIQK6G230",
            "https://youtu.be/9a60VuhDJag?list=PLxGZmhYgTIMleVy9kzKXSTy4FoTaLFHOu",
            "https://youtu.be/T-r0nuDjXsg",
            "https://youtu.be/Tn3bGHiBWkg",
            "https://youtu.be/ngcoNtBUR78?list=PLq7Sw1pjVmicN6QyYtLpTCMA_vxT6xef6",
            "https://youtu.be/uSIhULcHihE?list=PLW5wOVk-AKkF3fvObLqtO96xLRMHKLBbE",
            "https://youtu.be/nquPBfaaHOE?list=PLbb9vRmJcNZRTTj9lEvvqeOttRzzLzadK",
            "https://youtu.be/g2aPm-j_VZ4?list=PLq7Sw1pjVmic3FS4N1LdKSwNTEP5kAY5a",
            "https://youtu.be/afgIq0XOVDY",
            "https://youtu.be/aNL47e6dc30",
            "https://youtu.be/fcNVTssWyio"
        ],
        "image_path": [
            "https://i.pinimg.com/736x/a7/1c/72/a71c7240d10a3365c6598e60a908d890.jpg", "https://i.pinimg.com/736x/a6/c0/3a/a6c03a059b65e78e1ec413532d8d2f1d.jpg", "https://i.pinimg.com/736x/97/76/4c/97764ce7760f1d9fe598b62098578e2e.jpg", "https://i.pinimg.com/736x/ef/35/9f/ef359f9215fa227cbaea8fdbd555ea67.jpg",
            "https://i.pinimg.com/736x/fb/b9/1a/fbb91a4a810680754edeba0033334267.jpg", "https://i.pinimg.com/736x/19/30/9c/19309c3069b544311d3f1096c368b585.jpg", "https://i.pinimg.com/736x/da/ca/d2/dacad279c23c29f220b3109c781f3913.jpg", "https://i.pinimg.com/736x/c4/1c/bd/c41cbdbaec23a33ad69f602201736c1b.jpg",
            "https://i.pinimg.com/736x/63/86/51/63865181cc88d99fd14941249be6d3c9.jpg", "https://i.pinimg.com/736x/28/83/da/2883da8bb4b9298a11c72581a9137705.jpg", "https://i.pinimg.com/736x/b9/ca/76/b9ca766578acf8a5f0f57e81416bd68b.jpg", "https://i.pinimg.com/736x/b1/49/61/b14961f0f836d4e8cafad48299c9eb6d.jpg",
            "https://i.pinimg.com/736x/5a/8d/d0/5a8dd0629d60494efc92135f52694cbe.jpg", "https://i.pinimg.com/736x/88/ed/1d/88ed1d284a9ddc70ee898ff688f9f15d.jpg", "https://i.pinimg.com/736x/38/8f/0e/388f0e133b9a1d05300f4819d5116205.jpg", "https://i.pinimg.com/736x/59/2d/21/592d21c744ef822ecc5f0bdaf211af1b.jpg",
            "https://i.pinimg.com/736x/96/8b/08/968b0863cd68f0fb61813ae836c3b28b.jpg", "https://i.pinimg.com/736x/3b/c1/6d/3bc16df21e61f196e7dc3707e8cb94b0.jpg", "https://i.pinimg.com/736x/95/51/19/9551193fefa483974f34be74c58f9997.jpg", "https://i.pinimg.com/736x/09/2e/40/092e40120a353ba7b3107a1256238389.jpg",
            "https://i.pinimg.com/736x/3d/2a/aa/3d2aaad6bd801ebcee006ca3715a9812.jpg", "https://i.pinimg.com/736x/43/7f/dc/437fdc11b17dedf0306a41d278a37e51.jpg", "https://i.pinimg.com/736x/96/8c/13/968c1307ad37cc1fc8971b68b3f2550d.jpg", "https://i.pinimg.com/736x/20/06/f9/2006f9c18764c28b94eb10c552d192e1.jpg",
            "https://i.pinimg.com/1200x/46/4e/28/464e283bb445dc010d89621251b7e31c.jpg", "https://i.pinimg.com/736x/0b/53/da/0b53da3abae5e59be8627baa809ec6b7.jpg", "https://i.pinimg.com/736x/ff/94/f0/ff94f044764b7f9e9e7841c6cd30e51b.jpg", "https://i.pinimg.com/736x/02/b1/a1/02b1a1f747d3eeab842f6900a0ed883a.jpg",
            "https://i.pinimg.com/736x/78/ee/c2/78eec2f28b6bd473cf3decc956815394.jpg", "https://i.pinimg.com/736x/64/0d/91/640d91cead9994b18a9cc06073a036e3.jpg", "https://i.pinimg.com/736x/28/b7/56/28b7563c58fb6831a5b5f2441ecd2795.jpg", "https://i.pinimg.com/736x/1f/c9/b0/1fc9b03b6a5941fe20a2b7c5297c6e1b.jpg",
            "https://i.pinimg.com/736x/6f/f0/57/6ff057718a56c991794d0ce68a6d1c0f.jpg", "https://i.pinimg.com/736x/8b/16/1c/8b161c524198c1e6ef70e55179bca684.jpg", "https://i.pinimg.com/736x/33/41/78/334178681ff319daf4ba8fc9b2f9e319.jpg", "https://i.pinimg.com/736x/6e/46/68/6e4668fa31d274f3175778953be46542.jpg",
            "https://i.pinimg.com/736x/02/0e/eb/020eebbf7da9c5ded02b5b66e71c0741.jpg", "https://i.pinimg.com/736x/a9/5a/98/a95a98f7c6028170bae5aa1198cac7a7.jpg", "https://i.pinimg.com/736x/6c/51/5f/6c515f04471a4af6a436593a5537fc73.jpg", "https://i.pinimg.com/736x/10/74/a9/1074a94bd30ebf576bdb188696fc339a.jpg",
            "https://i.pinimg.com/736x/77/21/16/772116bae78d28bfacdae39bf1413eac.jpg", "https://i.pinimg.com/736x/b5/63/2c/b5632cba08b52b6f0838809e35a00b69.jpg", "https://i.pinimg.com/736x/de/dd/be/deddbe9deef319a33a233ae7e23a595e.jpg", "https://i.pinimg.com/736x/fa/8f/7d/fa8f7d49636bc624a648c65e80b7212b.jpg",
            "https://i.pinimg.com/736x/33/a9/95/33a9950bdfebf45f9bcae3b1b7dc834c.jpg", "https://i.pinimg.com/736x/3a/b7/0d/3ab70d4b7d27573452712ac0e981674e.jpg", "https://i.pinimg.com/736x/5e/c8/58/5ec858187258c759a307f33526011467.jpg", "https://i.pinimg.com/736x/65/f7/56/65f756af58ef58e0699db1553d4e2eb2.jpg",
            "https://i.pinimg.com/736x/22/c5/e9/22c5e929bb927ce3091d26a676205934.jpg", "https://i.pinimg.com/736x/05/7a/f4/057af4b73c807f6d41ae01b3f86cd322.jpg", "https://i.pinimg.com/736x/23/4e/f5/234ef589d06b5484747821fc608a6ae5.jpg", "https://i.pinimg.com/736x/47/42/04/47420495e7aca2451e4940c1bd936c48.jpg",
            "https://i.pinimg.com/736x/25/ff/49/25ff490a54e388c2bd5a48efdeb0494e.jpg", "https://i.pinimg.com/736x/f1/7a/7a/f17a7aded94fbf5c4400da6bd427d760.jpg", "https://i.pinimg.com/736x/7a/9d/87/7a9d87189a781028d6a2a39643fa080c.jpg", "https://i.pinimg.com/736x/9d/73/68/9d736850d4ff32df3041d52ccbb6c19e.jpg",
            "https://i.pinimg.com/736x/94/90/6b/94906bba383f10406086deab16c1743a.jpg", "https://i.pinimg.com/736x/f7/68/f4/f768f47ace543252d4d3ce12cb594d24.jpg", "https://i.pinimg.com/736x/47/63/a7/4763a7796b2ee79bbe64538654b435c3.jpg", "https://i.pinimg.com/736x/95/ea/59/95ea593409958c3b5ea017154da5df2e.jpg",
            "https://i.pinimg.com/736x/ee/68/83/ee68832c7f9fffd4f8fe8516e5331ed6.jpg", "https://i.pinimg.com/736x/d2/7b/12/d27b121684b562b2fb21c9f208834448.jpg", "https://i.pinimg.com/736x/77/21/2b/77212b3a7766cd05dd7e4b6efa504785.jpg", "https://i.pinimg.com/736x/2d/6a/a9/2d6aa9af941ba0de8eeb6b65ecceb5e2.jpg",
            "https://i.pinimg.com/736x/29/b9/ea/29b9ea6189d37bd7518a1b54a6bf30e1.jpg", "https://i.pinimg.com/736x/48/08/47/480847cd80d99839d4c1f7183e50dd02.jpg", "https://i.pinimg.com/736x/f6/ce/f5/f6cef5daafb827eaf4b6d30e0958c9bb.jpg", "https://i.pinimg.com/736x/06/dd/34/06dd3458a802b3c3a405cdad5f1ac466.jpg",
            "https://i.pinimg.com/736x/29/8b/8c/298b8c1e63ec008f0db304dc52c8f49a.jpg", "https://i.pinimg.com/736x/32/b8/ea/32b8eaa25d8a946677a6644698bf37ed.jpg", "https://i.pinimg.com/736x/84/43/94/8443942203cd32089f33315c9af23834.jpg", "https://i.pinimg.com/736x/43/ea/49/43ea499a6db4af6643a5a0a84b8be103.jpg",
            "https://i.pinimg.com/736x/32/30/c0/3230c0e3e87a1936cc0ae93918e47d6d.jpg", "https://i.pinimg.com/736x/b7/79/cb/b779cb5f5f57159b88b7fb87dc7d115f.jpg", "https://i.pinimg.com/736x/8d/84/aa/8d84aa786fe6cc5fc04cb45d41f63370.jpg", "https://i.pinimg.com/736x/06/65/1e/06651e9c29c1d612dada921f300ea24d.jpg",
            "https://i.pinimg.com/736x/1b/5f/10/1b5f107099bd3624c60ba314332c9ff1.jpg", "https://i.pinimg.com/736x/ac/95/a6/ac95a6e7f0df0198f1bd2793c4435d20.jpg", "https://i.pinimg.com/736x/7d/76/7e/7d767edd3431ea47c73b8bd9dc76609b.jpg", "https://i.pinimg.com/736x/fc/1e/bc/fc1ebc0b6b0b8264835906ffcd307854.jpg",
            "https://i.pinimg.com/736x/8b/2c/8e/8b2c8e58c18e745cbe09762347d88957.jpg", "https://i.pinimg.com/736x/8a/ce/cd/8acecdb6545e2e91773ec7cee2f52c28.jpg", "https://i.pinimg.com/736x/c5/fe/20/c5fe208507cdfe958df201d3420b7e85.jpg", "https://i.pinimg.com/736x/b2/87/32/b287324e11f32d283505e7f4c2e75efe.jpg",
            "https://i.pinimg.com/736x/e6/1d/fa/e61dfa2e3f918d64650fa71b42d7a6f2.jpg", "https://i.pinimg.com/736x/1c/1b/6a/1c1b6a7596c9258866a272de6a76c020.jpg", "https://i.pinimg.com/736x/ab/e7/a8/abe7a8b1db6069a52ee46710ab8d65dc.jpg", "https://i.pinimg.com/736x/07/ce/68/07ce68fe42025da561e0c4cb3d81803c.jpg"
        ]
    }

    # 團體資料
    group_data = {
        "group": ["bts", "svt", "zb1", "nmixx", "aespa", "TWS", "stray kids", "viviz", "enhypen", "boynextdoor", "illit", "babymonster", "izna"],
        "出道日期": ["20130613", "20150526", "20230420", "20220222", "20201117", "20240122", "20180325", "20220209", "20201130", "20230530", "20240325", "20231127", "20241125"],
        "出道曲": [
            "https://www.youtube.com/watch?v=gdZLi9oWNZg&list=PL1s89zMwwA_0KHFlD_PL5qVDptDaaC9Yh&index=8",
            "https://youtu.be/zEkg4GBQumc?si=K86G-awX2_8R2IH0",
            "https://www.youtube.com/watch?v=trzeUClQIIg",
            "https://www.youtube.com/watch?v=3GWscde8rM8",
            "https://www.youtube.com/watch?v=ZeerrnuLi5E",
            "https://www.youtube.com/watch?v=YPg1sA0qNpo&pp=ygUNJ09oIE15bXkgOiA3cw%3D%3D",
            "https://youtu.be/u6unJQownW4",
            "https://youtu.be/cM963tI7Q_k",
            "https://youtu.be/nQ6wLuYvGd4",
            "https://youtu.be/jizAb-SLvtM",
            "https://youtu.be/Vk5-c_v4gMU",
            "https://youtu.be/olDWm2veCrM",
            "https://youtu.be/d3mqW9wqqx0"
        ],
        "點閱率最高的mv": [
            "https://www.youtube.com/watch?v=gdZLi9oWNZg",
            "https://youtu.be/zEkg4GBQumc?si=K86G-awX2_8R2IH0",
            "https://www.youtube.com/watch?v=V5ACuj_jOnc",
            "https://www.youtube.com/watch?v=3GWscde8rM8",
            "https://www.youtube.com/watch?v=4TWR90KJl84",
            "https://youtu.be/hVAc1Vf2ITU",
            "https://youtu.be/TQTlCHxyuu8",
            "https://youtu.be/9JFi7MmjtGA",
            "https://www.youtube.com/watch?v=wXFLzODIdUI&pp=ygUHQml0ZSBNZdIHCQmGCQGHKiGM7w%3D%3D",
            "https://youtu.be/jizAb-SLvtM",
            "https://youtu.be/Vk5-c_v4gMU",
            "https://youtu.be/olDWm2veCrM",
            "https://youtu.be/d3mqW9wqqx0"
        ],
        "最新資訊": [
            "全員6月退伍",
            "於20250526發行13人完整體的全新專輯",
            "即將展開2025巡演",
            "NMIXX 最近推出了 EP《Fe3O4: Forward》",
            "目前在歐洲進行巡演",
            "TWS將於2025年6月20日至22日,在首爾蠶室室內體育場舉行首次巡迴演唱會",
            "近期還在進行第三次世界巡演《Dominate World Tour》,於2025年7月30日結束",
            "因2025 MIXPOP Concert,她們將於 5 月 18 日在台北國際會議中心登台演出",
            "將於 2025 年 6 月 5 日發行第六張迷你專輯《DESIRE: UNLEASH》",
            "將於 5 月 13 日發行迷你四輯《No Genre》",
            "將於 2025 年 6 月 7 日至 8 日,在首爾奧林匹克公園奧林匹克大廳舉辦首場粉絲演唱會「2025 ILLIT GLITTER DAY IN SEOUL」",
            "將於 6 月 28 日與 29 日在台北林口體育館巡迴演出",
            "將於2025年7月展開亞洲巡演"
        ],
        "舞台合輯": [
            "https://www.youtube.com/watch?v=P131csq4P6Q&list=PLhzD1T0axOh72DKAVP-J7b4-2IlArhRym",
            "https://youtu.be/tQh9Byy_7zE?si=vuxdOkrIvtY5Wu0l",
            "https://www.youtube.com/watch?v=zCRSWzC1-6c&list=PLo8xA-0HtW7vA5HkdLG4KlUGJk__IQmak",
            "https://www.youtube.com/watch?v=a-ZGTUrkYlg&list=PLvPEt8BOGuPRGr1SH60s0lpKc1j8HCiIO",
            "https://www.youtube.com/watch?v=uZD-9ikcZC0&list=PLvPEt8BOGuPQyFf00w5OeGgJEZ-SqezyQ",
            "https://youtube.com/playlist?list=PLmd3-ToAK_wW41VyCRbKQ5AGkQ_kJYzL5&si=FzNzZ6v70GVra8ls",
            "https://www.youtube.com/watch?v=oDhUiQBI_xw&list=PLTQIoxF1vIPnc8WvL3Qaz8P8f5YQJtU1X",
            "https://youtube.com/playlist?list=PLmNPDBrP4zfCF_aZgWZ2HKcKZtdNHygdi&si=vnn4DSz5AVpzbP6L",
            "https://www.youtube.com/watch?v=nfTsxYXUWXU&list=PL8XTuWdY68hMAzdVAFzh52FnrnxzmCDww",
            "https://youtube.com/playlist?list=PLnJGkdkTCu5psKRGhn5q5FIL8O9l_cUAx&si=O-yrD0FhZ0N1Tyre",
            "https://www.youtube.com/watch?v=DDzxfRX1FFE&list=PLRpwZXhGAATcEO72QLUTa4L-o1DMzZSlm",
            "https://www.youtube.com/watch?v=mpOkycQwepk&list=PLnJGkdkTCu5pY27Ae8XILbqY8x45biDiO",
            "https://www.youtube.com/watch?v=k2_u6byRSg8&list=PLRpwZXhGAATeRfRz6n9R64kVV_eK_3NZ5"
        ],
        "推薦主打歌": [
            "https://www.youtube.com/watch?v=9DwzBICPhdM",
            "https://www.youtube.com/watch?v=zSQ48zyWZrY",
            "https://www.youtube.com/watch?v=2hwiRN8t8Ok",
            "https://www.youtube.com/watch?v=EDnwWcFpObo",
            "https://www.youtube.com/watch?v=phuiiNCxRMg",
            "https://youtu.be/NRgZuuwD2WY",
            "https://youtu.be/X-uJtV8ScYk",
            "https://youtu.be/_ow5Yp9RWhM",
            "https://open.spotify.com/track/44hqFxUWsADWewEJELnncj?si=484e4aa9a43349bd",
            "https://open.spotify.com/track/0Tq7v8YAmwdnAYBwyR1pZ4?si=63a2a2f9dbd543e3",
            "https://open.spotify.com/track/2MoUuJhpSO4a0czxvsrSC6?si=81ade64a6d1c401e",
            "https://open.spotify.com/track/3VBj0lzjmhTzVFPEDOjNCG?si=5de6b50a9a6641e7",
            "https://youtu.be/88GkYKvnvvI"
        ],
        "推薦寶藏歌": [
            "https://www.youtube.com/watch?v=Fw7C6IsDYgI",
            "https://www.youtube.com/watch?v=smBgtaImlx8",
            "https://www.youtube.com/watch?v=mLy2ZS6ASXs",
            "https://www.youtube.com/watch?v=4q3JKyLc4xA",
            "https://www.youtube.com/watch?v=i0RCcSBPjuU",
            "https://youtu.be/iILHUtvJ7vc",
            "https://youtu.be/N6WYvY5DMlw",
            "https://youtu.be/p2RtRDwlwGs",
            "https://youtu.be/qeA0U6qjvmk",
            "https://youtu.be/Nsm56FuORYc",
            "https://youtu.be/NChlBP5DSc4?list=PLd2IB9MqCSpHybAVjESGQ9dZ5nzw3qyln",
            "https://youtu.be/XShaIZs7J7M",
            "https://www.youtube.com/watch?v=kvgVKhqGwAE"
        ],
        "音樂合輯": [
            "https://www.bilibili.com/video/BV1oy4y1G7mn/?spm_id_from=333.337.search-card.all.click&vd_source=cae1867025219e7048c627d0d78738d6",
            "https://www.bilibili.com/video/BV1aUjSzDEZZ/?spm_id_from=333.337.search-card.all.click&vd_source=cae1867025219e7048c627d0d78738d6",
            "https://www.bilibili.com/video/BV1bqZmYKEGC/?spm_id_from=333.337.search-card.all.click&vd_source=cae1867025219e7048c627d0d78738d6",
            "https://www.youtube.com/watch?v=gZrd_qNEghU&list=PLZnInaEvZIDYEi2HEf9gN5fN1SKLv0VKW",
            "https://www.bilibili.com/video/BV1wGzpYrEfg/?spm_id_from=333.337.search-card.all.click&vd_source=cae1867025219e7048c627d0d78738d6",
            "https://youtube.com/playlist?list=PL_bz3Z6iH2Pa2oc3oWHcXtFIiKwS0lZAi&si=jIodLqUxx3g3hzqH",
            "https://youtube.com/playlist?list=PL2HLJ87twWI3H5CwvG_xTOiHJ-muq8vrq&si=aiXfzlCRIBSoL8Fa",
            "https://youtube.com/playlist?list=PLmYEc5xCbgfnNPPnml-9cT2aVqWPNcNhb&si=n3pLvcmCrXV2YHdQ",
            "https://open.spotify.com/playlist/6Z05FMYGnZxTzxU9AZRsWA",
            "https://open.spotify.com/playlist/5ZFz5w4CDSWTwYOGZPVQBC",
            "https://open.spotify.com/playlist/4Ee25btXMewwC4RBTvIFwU?si=yajtRw_KR1ie6t1o59GRaw",
            "https://open.spotify.com/playlist/1AzzoErwnmCPhT2fA6AqjJ",
            "https://www.youtube.com/watch?v=XeFlHMxOhQo&list=PLw19uoIvQsKkNBm32UKETcqmUyuj4j44A"
        ],
        "團綜": [
            "https://www.bilibili.com/video/BV1Qi4y1b7KU/?share_source=copy_web&vd_source=9e320472205994318bd230792ec41c84",
            "https://www.bilibili.com/video/BV1Ci4y1C7sc/?spm_id_from=333.337.search-card.all.click",
            "https://search.bilibili.com/all?keyword=zbtv%E5%90%88%E9%9B%86&from_source=webtop_search&spm_id_from=333.788&search_source=5",
            "https://www.dcard.tw/search?query=%E5%9C%98%E7%B6%9C&forum=nmixx",
            "https://search.bilibili.com/all?keyword=aespa%E5%9B%A2%E7%BB%BC&from_source=webtop_search&spm_id_from=333.788&search_source=2",
            "https://search.bilibili.com/all?keyword=tws%E5%9B%A2%E7%BB%BC&from_source=webtop_search&spm_id_from=333.1007&search_source=2",
            "https://www.bilibili.com/video/BV1i7411N7HU/?spm_id_from=333.337.search-card.all.click",
            "https://search.bilibili.com/all?keyword=viviz%E5%9B%A2%E7%BB%BC&from_source=webtop_search&spm_id_from=333.1007&search_source=2",
            "https://www.bilibili.com/video/BV1uy4y1u7ng/?spm_id_from=333.337.search-card.all.click",
            "https://search.bilibili.com/all?keyword=boynextdoor%E5%9B%A2%E7%BB%BC&from_source=webtop_search&spm_id_from=333.1007&search_source=2",
            "https://search.bilibili.com/all?keyword=illti%E5%9B%A2%E7%BB%BC&from_source=webtop_search&spm_id_from=333.1007&search_source=2",
            "https://search.bilibili.com/all?keyword=babymonstar%E5%9B%A2%E7%BB%BC&from_source=webtop_search&spm_id_from=333.1007&search_source=2",
            "https://search.bilibili.com/all?keyword=izna%E5%9B%A2%E7%BB%BC&from_source=webtop_search&spm_id_from=333.1007&search_source=2"
        ],
        "入坑必看團綜": [
            "https://www.bilibili.com/video/BV17x411X7yK/?p=35&share_source=copy_web&vd_source=9e320472205994318bd230792ec41c84",
            "https://www.bilibili.com/video/BV1x24y1T7c3?spm_id_from=333.788.videopod.episodes&vd_source=cae1867025219e7048c627d0d78738d6",
            "https://www.bilibili.com/video/BV1eeRYYcEYS/?spm_id_from=333.337.search-card.all.click",
            "https://www.bilibili.com/video/BV1YN4y1K7Dg/?spm_id_from=333.337.search-card.all.click&vd_source=cae1867025219e7048c627d0d78738d6",
            "https://www.bilibili.com/video/BV1od4y157Gb/?spm_id_from=333.337.search-card.all.click&vd_source=cae1867025219e7048c627d0d78738d6",
            "https://www.bilibili.com/video/BV17f42127hW/?share_source=copy_web&vd_source=9e320472205994318bd230792ec41c84",
            "https://www.bilibili.com/video/BV1cM411m7Yy/?spm_id_from=333.337.search-card.all.click",
            "https://www.bilibili.com/video/BV1pM411t77J/?spm_id_from=333.337.search-card.all.click",
            "https://www.bilibili.com/video/BV1i5zAYBEVP/?spm_id_from=333.337.search-card.all.click",
            "https://www.bilibili.com/video/BV1x2S8YoEKF/?spm_id_from=333.337.search-card.all.click",
            "https://www.bilibili.com/video/BV1sw4m167nJ/?spm_id_from=333.337.search-card.all.click",
            "https://www.bilibili.com/video/BV1Bb421J7ZR/?spm_id_from=333.337.search-card.all.click",
            "https://www.bilibili.com/video/BV1gji2YLEYg/?spm_id_from=333.337.search-card.all.click"
        ],
        "必看神級舞台": [
            "https://www.youtube.com/watch?v=9n-aYhf7ygk",
            "https://www.youtube.com/watch?v=38dIHkJMtHw",
            "https://www.youtube.com/watch?v=IqC_amTIgc4",
            "https://www.youtube.com/watch?v=KevsI_IPFNc",
            "https://www.youtube.com/watch?v=7dOPvVV1Ui4",
            "https://youtu.be/BhQ-Fx3Np84",
            "https://youtu.be/KLBelKB5oeg?list=PLXhZWRwsnrxhdY0wPovLgJk4JB5jqrD9y",
            "https://youtu.be/674Q7UTA5hQ",
            "https://youtu.be/Pcz4Cz3k6RU",
            "https://youtu.be/ed5zAD0UKIg",
            "https://www.youtube.com/watch?v=fUtT_Fja0YM",
            "https://www.youtube.com/watch?v=n_2oVnjL1y4",
            "https://youtu.be/rTj06CFlDTU"
        ],
        "image_path": [
            "https://i.pinimg.com/736x/5d/ee/e4/5deee43e0c43b4b93b12846627fe1e05.jpg", "https://i.pinimg.com/736x/f9/04/0e/f9040ea0134ec7bbf87d028f69fd6ffa.jpg", "https://i.pinimg.com/736x/46/7a/a9/467aa9208ad10f9c0ff64e4883b96db6.jpg", "https://i.pinimg.com/736x/d7/87/cf/d787cf236dcfef5ae0f12179a018383a.jpg",
            "https://i.pinimg.com/736x/43/d5/09/43d509558f64e1a26e6bb9fb68fada78.jpg", "https://i.pinimg.com/736x/eb/38/eb/eb38eb540440358c622f8a05263597c2.jpg", "https://i.pinimg.com/736x/d6/16/22/d6162213ad0c79aaa8c921928197182a.jpg", "https://i.pinimg.com/736x/d1/45/58/d145584154be45019136c25d7bf13ff9.jpg",
            "https://i.pinimg.com/736x/60/0b/ea/600beacd0556bd2284f4a2f296f022d9.jpg", "https://i.pinimg.com/736x/03/03/65/030365b7dbe0b880fb1da34dfc959cfb.jpg", "https://i.pinimg.com/736x/f7/4d/e1/f74de1a31c49c5f230ba2c93267b93fe.jpg",
            "https://i.pinimg.com/736x/87/f5/2a/87f52a29c124b885ebbbea0da75c8c09.jpg", "https://i.pinimg.com/736x/d0/e3/ed/d0e3edfaf60c419d4b6856096730ee34.jpg"
        ]
    }

    # 建立並匯出 CSV
    pd.DataFrame(idol_data).to_csv('idol_data.csv', encoding='utf-8-sig', index=False)
    pd.DataFrame(group_data).to_csv('group_data.csv', encoding='utf-8-sig', index=False)

# 函數：將值轉為可點擊超連結
def make_clickable(val, text="點擊連結"):
    if pd.isna(val) or val == "無" or not val.strip():
        return val
    if val.startswith("http"):
        return f'<a href="{val}" target="_blank">{text}</a>'
    return val

# 函數：將圖片路徑轉為 HTML 圖片標籤
def make_image(val, width=200):
    if pd.isna(val) or not val.strip():
        return "無圖片"
    return f'<img src="{val}" width="{width}" style="border-radius: 8px; object-fit: cover;">'

# Streamlit 應用程式
def main():
    # 設置頁面標題
    st.title("Stan-Up")

    # 添加 CSS 樣式美化卡片
    st.markdown("""
        <style>
        .card {
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            background-color: #fff;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
        .card-content {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .card-image {
            text-align: center;
        }
        .card-text {
            font-size: 16px;
            line-height: 1.5;
        }
        .card-text strong {
            color: #333;
        }
        a {
            color: #1e90ff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        </style>
    """, unsafe_allow_html=True)

    # 生成 CSV 檔案
    generate_csv_files()

    # 讀取 CSV 檔案
    try:
        idol_df = pd.read_csv('idol_data.csv', encoding='utf-8-sig')
        group_df = pd.read_csv('group_data.csv', encoding='utf-8-sig')
    except FileNotFoundError:
        st.error("找不到 CSV 檔案，請確認 idol_data.csv 和 group_data.csv 已生成！")
        return
    except UnicodeDecodeError:
        st.error("讀取 CSV 檔案失敗，請確認檔案編碼！")
        idol_df = pd.read_csv('idol_data.csv', encoding='gbk')
        group_df = pd.read_csv('group_data.csv', encoding='gbk')

    # 搜尋功能
    st.header("搜尋成員或團體")
    search_query = st.text_input("輸入成員名稱（如 jk、karina）或團體名稱（如 bts、aespa）：", "")

    # 僅在有搜尋輸入時顯示結果
    if search_query:
        # 搜尋偶像資料
        idol_results = idol_df[
            idol_df['member'].str.contains(search_query, case=False, na=False) |
            idol_df['group'].str.contains(search_query, case=False, na=False)
        ]

        # 搜尋團體資料
        group_results = group_df[
            group_df['group'].str.contains(search_query, case=False, na=False)
        ]

        # 顯示搜尋結果
        if not idol_results.empty or not group_results.empty:
            st.success(f"找到與 '{search_query}' 相關的資料！")

            # 顯示偶像資料結果
            if not idol_results.empty:
                st.subheader("匹配的偶像資料")
                for _, row in idol_results.iterrows():
                    image_html = make_image(row['image_path'], width=200)
                    stage_link = make_clickable(row['入坑必看舞台直拍'], "觀看直拍")
                    card_html = f"""
                        <div class="card">
                            <div class="card-content">
                                <div class="card-image">{image_html}</div>
                                <div class="card-text">
                                    <p><strong>團體</strong>: {row['group']}</p>
                                    <p><strong>成員</strong>: {row['member']}</p>
                                    <p><strong>生日</strong>: {row['生日']}</p>
                                    <p><strong>代表物</strong>: {row['代表物']}</p>
                                    <p><strong>暱稱</strong>: {row['暱稱']}</p>
                                    <p><strong>入坑必看舞台直拍</strong>: {stage_link}</p>
                                </div>
                            </div>
                        </div>
                    """
                    st.markdown(card_html, unsafe_allow_html=True)

            # 顯示團體資料結果
            if not group_results.empty:
                st.subheader("匹配的團體資料")
                url_columns = [
                    "出道曲", "點閱率最高的mv", "舞台合輯", "推薦主打歌", "推薦寶藏歌",
                    "音樂合輯", "團綜", "入坑必看團綜", "必看神級舞台"
                ]
                link_text = {
                    "出道曲": "觀看出道曲",
                    "點閱率最高的mv": "觀看MV",
                    "舞台合輯": "觀看合輯",
                    "推薦主打歌": "聽主打歌",
                    "推薦寶藏歌": "聽寶藏歌",
                    "音樂合輯": "聽合輯",
                    "團綜": "觀看團綜",
                    "入坑必看團綜": "觀看團綜",
                    "必看神級舞台": "觀看舞台",
                }
                for _, row in group_results.iterrows():
                    image_html = make_image(row['image_path'], width=200)
                    card_html = f"""
                        <div class="card">
                            <div class="card-content">
                                <div class="card-image">{image_html}</div>
                                <div class="card-text">
                                    <p><strong>團體</strong>: {row['group']}</p>
                                    <p><strong>出道日期</strong>: {row['出道日期']}</p>
                                    <p><strong>最新資訊</strong>: {row['最新資訊']}</p>
                    """
                    for col in url_columns:
                        link = make_clickable(row[col], link_text.get(col, "點擊連結"))
                        card_html += f"<p><strong>{col}</strong>: {link}</p>"
                    card_html += """
                            </div>
                        </div>
                    """
                    st.markdown(card_html, unsafe_allow_html=True)
        else:
            st.warning(f"未找到與 '{search_query}' 相關的資料，請檢查輸入！")

if __name__ == "__main__":
    main()
