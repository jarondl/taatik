taatik - translitertion of filenames from Herbrew letters to Latin letters.
===========================================================================

Latinize Hebrew filenames, for use in unicode-incompatible devices
such as old music players or car cd players. Supports two transliterations 
tables:

*   EKTB as suggested by [Amnon Katz in 1987][AK]. 
    Characters are identified by the early Hebrew letters from which they developed.

        converts   אבגדהוזחטיכלמנסעפצקרשתךםןףץ
        to         ABCDEFGHVIKLMNXOPZQRSTKMNPZ
        for example : הרחפת שלי מלאה בצלופחים ->  ERHPT SLI MLAE BZLFPHIM

    |א|ב|ג|ד|ה|ו|ז|ח|ט|י|כ|ל|מ|נ|ס|ע|פ|צ|ק|ר|ש|ת|ך|ם|ן|ף|ץ|
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    |A|B|C|D|E|F|G|H|V|I|K|L|M|N|X|O|P|Z|Q|R|S|T|K|M|N|P|Z|

*   PHONETIC 
    based on similar sounding letters, except ט->U ש->W which are based on figure.
    
        converts   אבגדהוזחטיכלמנסעפצקרשתךםןףץ
        to         ABGDHVZXUYKLMNSOPCQRWTKMNPC
        for example : הרחפת שלי מלאה בצלופחים ->  HRXPT WLY MLAH BCLVPXYM

    |א|ב|ג|ד|ה|ו|ז|ח|ט|י|כ|ל|מ|נ|ס|ע|פ|צ|ק|ר|ש|ת|ך|ם|ן|ף|ץ|
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    |A|B|G|D|H|V|Z|X|U|Y|K|L|M|N|S|O|P|C|Q|R|W|T|K|M|N|P|C|

Note that both schemes do not treat the five final letters differently.



[AK]:  dx.doi.org/10.1093/applin/9.3.306  "Article by Amnon Katz"


Usage
--------

    usage: taatik [-h] [-r] [-q] [-t {EKTB,PHONETIC}] FILENAME [FILENAME ...]

positional arguments:
    
    FILENAME              the filenames to rename

optional arguments:
    
    -h, --help            show this help message and exit
    -r, --really-rename   really rename the files. if not specified, the program
                          will only show what would have happend
    -q, --quiet           do not print anything
    -t {EKTB,PHONETIC}, --table {EKTB,PHONETIC}
                          use the specified translation table (default: EKTB)
