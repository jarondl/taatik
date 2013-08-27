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

*   PHONETIC 
    based on similar sounding letters, except ט->U ש->W which are based on figure.
    
        converts   אבגדהוזחטיכלמנסעפצקרשתךםןףץ
        to         ABGDHVZXUYKLMNSOPCQRWTKMNPC
        for example : הרחפת שלי מלאה בצלופחים ->  HRXPT WLY MLAH BCLVPXYM

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
