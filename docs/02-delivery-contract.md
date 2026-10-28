# Requirements en verantwoordelijkheden

## Requirements met acceptatiebewijs

| ID | Vereiste | Acceptatietest | Bewijsrepo |
|---|---|---|---|
| FR-01 | Factuurbedragen sluiten exact | Netto + btw ongelijk totaal wordt geweigerd | Accounting |
| FR-02 | Reviewer verschilt van indiener | Zelfgoedkeuring geeft conflict/verbod | Accounting, Workflow |
| FR-03 | Dubbel verzoek veroorzaakt geen dubbele taak | Gelijktijdige retries leveren één sinkrecord op | Alle workflowdemo's |
| FR-04 | Finance ziet geen HR-bronnen | Gerichte vraag naar verborgen canary levert geen HR-bron | Knowledge Assistant |
| FR-05 | Agent kan geen eigen acties goedkeuren | Connector bevat geen review/execute, serverrol blokkeert | Copilot Automation |
| FR-06 | Regressie blokkeert release | Onveilige negatieve fixture geeft exitcode 1 | Evals |
| NFR-01 | Herstart verliest geen goedgekeurde opdracht | Nieuwe engine leest opgeslagen state | Workflow |
| NFR-02 | Providerfout blijft zichtbaar | Geen stil fixtureantwoord bij Azurefout | AI-adapters |
| NFR-03 | Logs lekken geen credentials | Controle van app-, gateway- en providerlogs | Pilot nog uit te voeren |
| NFR-04 | Representatieve kwaliteitsmeting | Labelset, reviewerafspraken en foutanalyse | Live pilot nog uit te voeren |

Er zijn nog geen bewezen enterprise-SLA's. Stel latency, beschikbaarheid en capaciteit pas vast op basis van procesbehoefte en een gemeten omgeving.

## RACI voor een pilot

| Werk | Proceseigenaar | AI consultant | IT/security | Dataowner | Privacy/L&D |
|---|---|---|---|---|---|
| Doel en scope | A | R | C | C | C |
| Technisch ontwerp | C | R | A | C | C |
| Datakwaliteit/toegang | C | R | C | A | C |
| Privacybeoordeling | A | R | C | C | C |
| Gebruikersopleiding | A | R | C | C | R |
| Go/no-go | A | R | C | C | C |

R = uitvoerend verantwoordelijk, A = eindverantwoordelijk, C = consulteren. Dit is een oefenverdeling; laat de echte organisatie mandaten bevestigen. Privacy- en securityspecialisten leveren een eigen beoordeling binnen hun bevoegdheid.

## Definition of Done

Code en configuratie zijn gereviewd; negatieve tests slagen; datastromen en foutpaden zijn beschreven; actualiseerde OpenAPI en instructies zijn beschikbaar; resultaten zijn reproduceerbaar; incident- en rollbackpad is geoefend; procesowner accepteert het proces; gebruikers kunnen de taak uitvoeren en weten wanneer ze hulp vragen. Een lokaal portfolio kan de technische delen bewijzen, maar geen fictieve organisatieacceptatie invullen.

## Besluitlogtemplate

Vermeld datum, vraag, opties, criteria, feiten versus aannames, risico's, beslisser, gekozen optie en herzieningsmoment. Voorbeeld: kies lokale SQLite voor de demonstratie vanwege kleine scope en eenvoudig herstel; herzie vóór gelijktijdig enterprisegebruik, HA-eisen of meerdere appinstances. 'Het werkte op mijn laptop' is geen schaalbaarheidsargument.
