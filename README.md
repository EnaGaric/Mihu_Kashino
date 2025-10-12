-----------------------
How to install:
-----------------------

1) First and foremost, download the latest version of Ollama!!!

#quick guide to LLM
-on prima niz tokena(tekst) i predviđa sljedeće tokene -> tako se generiraju rečenice
-"Zašto mi je potreban?" jer ti je on glavni "mozak" koji formulira i piše odgovore
- skraćenica je za Large Language Model

#Ollama
- ako te baš zanima dubinski kako se radi LLM, pogledaj vector embeding, tokenizing...
- ukratko, uči se model da su pas i mačka slični, ali ananas i sunce nisu...to je jako dug proces i zahtjeva puno para
- Ollama je library LLM modela koje su ljudi napravili: nadohvat ti je ruke! Samo odabereš model, instaliraš ga i good to go, totalno free!!
- Ollama sada ima i aplikaciju, tako da ti je lakše "priačti s AI-em"
- svaki model radi druge stvari (model za prepoznavanje i generiranje slika, necenzurirani, za različite procesore...)

https://ollama.com/download
instalirati će se installation exe file od 1gb, pokreneš ga, instalira u direktorij (najčešće u users...AppData/Local)

2) Install lokalni LLM
- uđi u terminal (cmd)
. napiši ollama pull llama3:8b (to ti je baza, base model, zamisli kao glavni mozak)
- preporuka, instaliraj na SSD ili na USB stick
- unutar aplikacije možeš postavit di će ti se instalirat LLM modeli, jer će ZAUZIMAT PROSTORA
- također, idi u:
tražilica-> advanced system settings->ući ćeš u system properties-> klikni env variables
a) new...variable name = OLLAMA_MODELS (baš prepiši ovo), te u values dodaj di želiš da ti se sejva (meni je u D:\ollama\models)
b) nađi Ollama path i dodaj u value (npr meni je u C:\Users\Ena Garic\AppData\Local\Programs\Ollama), ime: "OllamaPath"
- stisni svugdje save te ok

3) možeš testirati u terminalu, ili u Ollama aplikaciji (pokreni .exe, moja preporuka) te probaj nešto napisati, npr who are you itd.

#meni je trebalo par minuta da mi da odgovor jer nemam jaki laptop, specs su mi sljedeći:
Device name	Ena
Processor	AMD Ryzen 7 5700U with Radeon Graphics            1.80 GHz
Installed RAM	16.0 GB (13.8 GB usable)
Device ID	466013F8-5190-4375-875A-CDF5DBA2D438
Product ID	00330-81623-69706-AA582
System type	64-bit operating system, x64-based processor
Pen and touch	No pen or touch input is available for this display
#važno ti je da imaš minimalno 12 RAM-a te dobar procesor, ali većina novijih laptopa ima već odličan

4) povuci fajlove sa mog githuba

git clone https://github.com/EnaGaric/My-own-AI.git

(možeš i preuzet zip file, ali topla preporuka je da copy paste udreš, da se navikneš na git...osjećat ćeš se kao programer, trust me)
ako imaš github, pretpostavljam da imaš skinut i git. Ako nemaš, instaliraj ga!
moja preporuka: instaliraj visual studio code te instaliraj sve extensions koje imaju "git" u sebi. ili možeš direktno: https://git-scm.com/downloads/win
*) ako ćeš zip file:
a) extract, otvori terminal u folderu

5) moraš znati gdje ti se nalazi models. idi na git terminal (git bash) i upiši cd My-own-AI

-----otvori folder. Unutra bi trebao vidjeti file koji se zove Modelfile (npr My-own-AI/MihuAI/Modelfile)
to je "blueprint" koji ollama koristi da bi kreirao Mihu AI, tj costum AI model

možeš ga i otvoriti (vidit ćeš tu FROM, PARAMETER, SYSTEM...)

6) NAPRAVI KORAK 5!!!!!!!!!! u terminal cd My-own-AI da uđeš u taj folder
-unutar tog foldera, runaj: ollama create mihu -f Modelfile
(to ubiti govori Ollami ka ej napravi mi ovaj ai koristeći upute u tom Modelfile)
- pazi da su ti svi fajlovi u istom folderu gdje je i Modelfile (ersona.json, mihu_persona_loader.json, ...)

7) gotov si
možeš u terminalu ollama run mihu
---> preporuka, uđi u Ollama app, donji desni kut pored strelice za poslat poruku stisni botun te nađi "mihu", stisni
BUM! Mihu je skinuta. Šalji joj poruke (u početku će tribat vrimena za slat poruke...kasnije će se malo ubrzat) te radi šta god oćeš
- feel free to add anything to additional branches, pogotovo ako želiš radit sa mnom da je učinimo najboljim Ai-em ikad


:)
