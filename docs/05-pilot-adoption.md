# Pilot, opleiding en duurzaam gebruik

## Vier fasen

| Fase | Concrete activiteit | Exitcriterium |
|---|---|---|
| Voorbereiding | Owner, data, rollen, baseline, tests, herstelplan | Bevoegde betrokkenen accepteren scope |
| Shadow mode | AI doet voorstellen naast normaal werk; geen externe effecten | Fouten verklaard en beoordelaars afgestemd |
| Beperkte pilot | Kleine getrainde groep, broncontrole, dagelijkse triage | Vooraf bepaalde kwaliteits- en procescriteria gehaald |
| Opschalen | Support, release-eigenaar, observability en training geborgd | Elke uitbreiding opnieuw beoordeeld |

De portfolio-demo's tonen de technische mechanismen. Deze fasen zijn nog niet met echte medewerkers doorlopen.

## Opleidingssessie van 45 minuten

Start met één herkenbare taak. Toon een correct voorstel, een fout voorstel en een geval waarin het systeem geen antwoord moet geven. Laat medewerkers in tweetallen een factuur reviewen, een ontbrekende bron herkennen en een onveilig verzoek weigeren. Laat daarna een eigen oefening uitvoeren: zonder hulp besluiten, bron aanwijzen, fout melden. Sluit af met een korte uitleg over toegestane data en het supportpad.

Een presentielijst is geen bewijs van vaardigheid. Registreer hoeveel deelnemers zelfstandig de drie taken volbrengen en welke fouten terugkomen. L&D past de volgende sessie daarop aan.

## KPI-werkblad

| KPI | Definitie | Meetbron | Waarde in dit portfolio |
|---|---|---|---|
| Behandeltijd | Actieve minuten per vergelijkbare taak | Observatie vóór/na | Nog niet gemeten |
| Doorlooptijd | Tijd vanaf intake tot besluit | Procestimestamps | Alleen demo-events |
| Correct voorstel | Door reviewers geaccepteerde juiste velden | Gelabelde steekproef | Live kwaliteit niet gemeten |
| Ernstige fouten | Verkeerde acties/lekken per taak | Incidenten en evals | Negatieve fixtures als controle |
| Adoptie | Bevoegde actieve gebruikers / doelgroep | Gebruik met passende privacywaarborgen | Nog niet gemeten |
| Herwerk | Correctietijd na voorstel | Taakregistratie | Alleen scenario-input |
| Kosten | Model, platform, beheer, support | Facturatie en tijden | Geen live cloudkosten |

Definieer vóór de pilot minimumkwaliteit en stopregels met de procesowner. Voorbeeld van een harde regel: geen uitvoering zonder onafhankelijk akkoord; één toegangslek stopt de pilot. Een gekozen doelpercentage voor correctheid moet passen bij de ernst van fouten en de representativiteit van je dataset.

## Support en rollback

Een melding bevat scenario, request-ID, tijd, verwachte/werkelijke uitkomst en foutcode; geen credentials of onnodige klantinhoud. AI consultant triageert, operations bewaakt beschikbaarheid, process owner beslist over procesimpact. Stop nieuwe acties bij een incident, behoud audit, onderzoek bestaande effecten en herstel alleen met bevoegde goedkeuring. Een software-rollback draait reeds aangemaakte taken of boekingen niet automatisch terug.
