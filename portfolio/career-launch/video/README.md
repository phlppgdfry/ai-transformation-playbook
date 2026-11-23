# Nederlandstalige portfolio-rondleiding — 2:20

[Bekijk de video op de publieke showcase](https://phlppgdfry.github.io/ai-transformation-playbook/#tour) · [download de MP4](../../../site/media/portfolio-tour-nl.mp4) · [volledig transcript](../../../site/media/TRANSCRIPT-NL.md).

Deze stille video toont echte opnamen van de zes publieke showcases. De Nederlandse captions staan in een aparte balk onder het ongewijzigde applicatiebeeld. Geen stem, muziek, fictieve klant, gegenereerde appbeelden of opgevoerde auteursgetuigenis is toegevoegd.

## Wat de opname bewijst

- De businesscase reageert op adoptie nul.
- De factuurdemo wijst een cent verschil af en markeert een onbekende leverancier.
- De kennisdemo laat het verschil tussen finance- en HR-toegang zien.
- Bestaande evaluatierapporten tonen een geslaagde en een onveilige controle.
- Workflow en Microsoft tonen **replays** van eerder uitgevoerde runs; deze film doet geen nieuwe model- of Microsoft-cloudcall.

Het is een rondleiding door het publieke portfolio, niet de volledige lokale API-integratiescenario-opname uit het [oorspronkelijke demoscript](../DEMO-SCRIPT.md). De browsercontrole schrijft geen factuur naar een backend. Die grenzen worden zichtbaar benoemd. Geen echte e-mails, ERP-acties of klantgegevens worden gebruikt.

## Reproduceren

De opname gebruikt de bestaande Playwright-installatie uit `integration`, een geïnstalleerde Chrome-browser, FFmpeg met H.264, Python met Pillow en een lokaal Inter-font. Geen extra runtime-afhankelijkheid van de toepassingen en geen betaalde dienst is toegevoegd.

Vanaf de repositoryroot:

```bash
node portfolio/career-launch/video/record.cjs /tmp/portfolio-tour-capture
python3 portfolio/career-launch/video/render.py /tmp/portfolio-tour-capture site/media --font /path/to/Inter-Regular.ttf
ffprobe -v error -show_entries format=duration,size:stream=codec_name,width,height,r_frame_rate -of json site/media/portfolio-tour-nl.mp4
node portfolio/career-launch/video/verify.cjs https://phlppgdfry.github.io/ai-transformation-playbook /tmp/portfolio-tour-browser.json
```

`record.cjs` stopt bij een ontbrekende verwachte toestand of browserfout. Als een publieke demo verandert, onderzoek dat eerst; vervang een mislukte actie niet door een verzonnen opname. De renderer weigert een onvolledige capture. Ruwe opnamen blijven buiten Git; scripts, captions, provenance en de uiteindelijke video worden meegeleverd. Upload geen sessies, tokens of privévensters.

## Bestanden en rechten

- `record.cjs`: echte browseracties en controle op uitkomsten.
- `render.py`: trims, concatenatie en de losse captionbalk; wijzigt geen applicatieresultaat.
- `verify.cjs`: echte videoweergave, metadata, transcript en layout op vier schermbreedtes.
- `site/media/portfolio-tour-nl.mp4`: 1280×720 H.264, 24 fps, zonder audiotrack.
- `site/media/poster.jpg`: frame uit de uiteindelijke video.
- `site/media/TRANSCRIPT-NL.md`: toegankelijk leesalternatief en hoofdstukken.
- `site/media/provenance.json`: datum, bronnen, scenevolgorde en montagescope.

Bronbeelden zijn eigen, publiek gepubliceerde MIT-portfolio-interfaces met synthetische gegevens. Inter wordt alleen gebruikt voor gerasterde captions (SIL Open Font License); er wordt geen fontbinary herverdeeld. Er is geen stockmateriaal, stemkloon of derdepartijmuziek gebruikt. Spreek niet over een persoonlijke opname door de auteur: dit is een geautomatiseerde demonstratie die de auteur zelf nog kan oefenen en toelichten.

## Begeleidende tekst om zelf te gebruiken

> Zes onderdelen, één fictieve accountingcase: van businesscase tot factuurcontrole, kennisrechten, agentvoorstellen, evaluatie en menselijke goedkeuring. Deze korte rondleiding toont de publieke demo's en benoemt expliciet waar het om een replay of mock gaat. Onafhankelijk project met uitgebreide AI-ondersteuning; geen klantresultaten of bewezen cloudimplementatie.

Publicatie naar LinkedIn, berichten aan recruiters en sollicitaties worden niet automatisch uitgevoerd. Een eigen gesproken opname kan later helpen jouw begrip te tonen, maar is geen technische releasevoorwaarde.
