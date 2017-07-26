import csv
import random as r

emotions = ["Angry", "Happy", "Sad", "Neutral", "Frustrated",
           "Excited", "Fearful", "Disgusted", "Other", "Undefined"]

phonemes = ["AA", "AE", "AH", "AO", "AW",
            "AX", "AXR", "AY", "B", "CH",
            "D", "DD", "DX", "DH", "EH",
            "ER", "EY", "F", "G", "HH",
            "IH", "IX", "IY", "JH", "K",
            "KD", "L", "M", "N", "NG",
            "OW", "OY", "P", "R", "S",
            "SH", "T", "TD", "TH", "TS",
            "UH", "UW", "V", "W", "Y",
            "Z", "ZH", "SIL", "+LAUGHTER+", "+LIPSMACK+",
            "+GARBAGE+", "+BREATHING+"]


dat = open('./test.dat', 'w')
dwriter = csv.writer(dat)
emo = open('./test.emo', 'w')
ewriter = csv.writer(emo)
pho = open('./test.pho', 'w')
pwriter = csv.writer(pho)


pho_to_pick = phonemes[r.randint(0, len(phonemes)-1)]
for i in xrange(10000):
    ewriter.writerow([emotions[r.randint(0, len(emotions)-1)]])
    first_entry = phonemes[r.randint(0, len(phonemes)-1)]
    pwriter.writerow([first_entry, phonemes[r.randint(0, len(phonemes)-1)], phonemes[r.randint(0, len(phonemes)-1)], phonemes[r.randint(0, len(phonemes)-1)]])

    if(first_entry == pho_to_pick):
        dlist = [1] * 57
    else:
        dlist = [0] * 57
    dwriter.writerow(dlist)

dat.close()
emo.close()
pho.close()
