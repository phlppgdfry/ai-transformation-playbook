# Risico- en privacywerkblad

Dit werkblad helpt vragen voorbereiden voor privacy, legal en security. Het is geen juridisch advies of bewijs dat een toepassing GDPR- of AI-Act-conform is. De toepasselijke verplichtingen hangen af van de echte toepassing, gegevens, rollen en inzetcontext.

## Screening vóór echte data

Leg vast wie verwerkingsverantwoordelijke en verwerker zijn, welk doel wordt nagestreefd, welke gegevens noodzakelijk zijn, wie toegang krijgt, hoe lang bronnen/antwoorden/logs worden bewaard en welke diensten of subprocessors betrokken zijn. Laat bevoegde personen grondslag, contracten, doorgiften en eventuele DPIA-noodzaak beoordelen. Beoordeel de concrete AI-toepassing; het woord 'copilot' bepaalt geen risicoklasse.

| ID | Risico | Controle | Eigenaar | Stopcriterium |
|---|---|---|---|---|
| R-01 | Verkeerde factuurgegevens | Exacte validatie plus menselijke broncontrole | Process owner | Ongecontroleerde boeking |
| R-02 | Cross-tenant bronlek | Serveridentiteit, filters, negatieve tests | IT/security | Eén bevestigd toegangslek |
| R-03 | Prompt injection veroorzaakt actie | Geen schrijftools zonder aparte toestemming | AI consultant | Verboden effect uitgevoerd |
| R-04 | Reviewer vertrouwt AI blind | Bron tonen, training, steekproeven | Process owner/L&D | Fouten onopgemerkt door review |
| R-05 | Logs bewaren gevoelige inhoud | Minimalisatie, retentie en logtoegang | Operations | Gevoelige inhoud onbeheerd |
| R-06 | Schijnbesparing en geen adoptie | Baseline en taakobservaties | Product Owner | Geen aantoonbare verbetering |
| R-07 | Onbevoegde connectorconnection | Afzonderlijke rollen en geverifieerde identiteit | Platform admin | Agent beschikt over reviewcredential |

## Go/no-go-dossier

Bewaar procesversie, datastroom, doel, toegangsmatrix, risicobeoordeling, supplier/servicebeoordeling, testdataset en resultaten, gebruikersinstructies, incidentproces, retentiebeleid en de echte besluiten van bevoegde verantwoordelijken. Gebruik 'nog te beoordelen' wanneer een besluit ontbreekt. Een groen technische testsuite kan een organisatorische of juridische beoordeling niet vervangen.

Raadpleeg officiële basisteksten bij de echte beoordeling: [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) en [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj). Dit dossier doet geen uitspraak over een specifieke wettelijke classificatie of implementatiedatum.
