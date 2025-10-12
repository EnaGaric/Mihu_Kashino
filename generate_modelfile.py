import json
import pathlib
import random

#uvozimo module json za rad s JSON, pathlib za file pathove...kao cross-platform
#random je za imperfections, ali i da ponekad Mihu odabere random frazu

HERE = pathlib.Path(__file__).parent
TEMPLATE = HERE / "Modelfile.template"
OUTPUT = HERE / "Modelfile"
PERSONA_JSON = HERE / "mihu_persona_loader.json"
IMPERFECTIONS = HERE / "mihu_imperfections.txt"

#here pathlib postavlja folder u kojem je mihu_load.py
#ubiti je to trenutni folder di se nalazi moja skripta
#template... je path do template filea
#output... je path za generirani Modelfile.
#taj file ce ollama koristit kao modefile
#persona... je path do mog persona json-a
#imperf... je tekst file s onim linijama

with open(PERSONA_JSON, "r", encoding="utf-8") as f:
    data = json.load(f)

# ovo otvara mihupersonaloader i učitava ga u python kao dictionary koji se zove data

persona_block = json.dumps(data.get("persona", data), ensure_ascii=False, indent=2)
#ukradeno sa interneta, ubiti samo uzme persona iz data
#znaci uzme persona AKO POSTOJI
#ako toga nema, onda pretvara u indent(neki tekst format ig)
#data.get...uzima samoo dio koji se zove "persona" iz json filea.
#jsondumps...pretvara Python dictionary natrag u json string

with open(TEMPLATE, "r", encoding="utf-8") as f:
    tpl = f.read()
#ovo je jednostavno, samo cita sadržaj iz modefile.template

modelfile_text = tpl.replace("{{PERSONA_JSON}}", persona_block)

#odi je zamijenia placeholder s mojom persona json block

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(modelfile_text)

#pise konacni modefile. taj file ce ollama procitat
#znaci ovo ce ollama koristit u output path

print("generated Modelfile from template")
print(f"Output path: {OUTPUT}")

#ovo sve prepisuje modefile svaki put kad ga pokrenem.
#modefile ce se generirat, ali je template isti tj ne dira ga se
#ovo san ubacila da vidin jesan li falila nesto

#sad za imperfections

with open(IMPERFECTIONS, "r", encoding="utf-8") as f:
    imperfections = [line.strip() for line in f if line.strip()]

#e sad...ovo otvara onaj file sa imperfectionsima
#line strip ce uklonit praznine s pocetka i kraja linije za svaki slucaj
#if line je strip, to ce ignorirat prazne linije
#rezultat je lista linija koje Mihu može pisat da pari vise natural

chat_context = []

def get_mihu_phrase(user_input):
    base_phrase = random.choice(imperfections)
    if random.random() < 0.2:
        logic_phrase = random.choice([
            "Logically...makes sense.",
            "Statistically speaking...",
            "Analytically...plausible."
        ])
        return f"{base_phrase} {logic_phrase}"
    return base_phrase

def mihuu_response(user_input):
    chat_context.append(user_input)
    if len(chat_context) > 4:
        chat_context.pop(0)
    phrase = get_mihu_phrase(user_input)
    return f"{phrase} (response to: {user_input})"

#ovo ce spremit zadnja 4 imputa tj odrzat neki mini kontekst
#zatim ce zvat getmihuphrase da dobije odgovor....
#...znaci vratit ce frazu i info na sta ce odgovorit
#bralic na youtube spomenia da je to za debugging sleš log