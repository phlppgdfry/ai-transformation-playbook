# Businesscase en technologische keuzes

## Formule

Vrijgekomen minuten per maand = volume × adoptie × procesdekking × (tijd vóór − tijd na − herwerkfractie × herwerkminuten).

Capaciteitswaarde = vrijgekomen uren × uurwaarde. Netto capaciteitswaarde = capaciteitswaarde − maandelijkse gebruikskosten. Indicatieve terugverdientijd = implementatiekosten / positieve netto maandwaarde. Bij nul of negatieve waarde is de terugverdientijd `null`.

Dit model veronderstelt constante volumes en adoptie binnen een scenario. Het houdt geen rekening met een geleidelijke ramp-up, financiering, belastingen, prijsinflatie, ziekte of capaciteit die niet herinzetbaar is. Voeg die factoren toe als je een echte investeringsbeslissing voorbereidt. Benoem expliciet welk deel daadwerkelijk in cash, capaciteit of kwaliteitswinst kan worden omgezet.

## Uitgewerkte aannames

De inputbestanden bevatten een conservatief, basis- en optimistisch scenario. Het basisgeval gebruikt 70% adoptie, 75% dekking, acht naar drie minuten, 8% herwerk van vier minuten, €45 uurwaarde, €350 maandkosten en €9.000 implementatiekosten. De waarden zijn oefeninputs, geen marktprijzen of klantmetingen. De CLI berekent de uitkomst; [het rapport](../evidence/business-case.json) is de bron voor de getallen.

## Prioriteren

De transparante score is 35% impact, 25% haalbaarheid, 20% datareadiness en 20% adoptiereadiness, elk beoordeeld op 1–5. Risico staat los van de score: vanaf 4 is specialistische beoordeling verplicht. Een hoge impact kan een risico niet wegmiddelen. De score ordent discoverywerk en verleent geen toestemming om een toepassing te bouwen.

## Toolkeuze: beoordeel per proces

| Optie | Past wanneer | Aandachtspunt |
|---|---|---|
| Bestaande ERP-regel | Vast controleerbaar criterium | Vaak minder beheer dan AI |
| Power Automate | Bekende connectors en voorspelbare flow | Licenties, connections, DLP, ALM |
| Copilot Studio | Gesprek en Microsoft-integraties nuttig | Autorisatie blijft servertaak |
| Python/FastAPI | Eigen validatie/API's en tests nodig | Hosting, identity, observability zelf beheren |
| Azure Search + model | Brongebaseerd semantisch zoeken nodig | ACL, bronactualiteit, evaluatie en kosten |
| Begrensde agent | Stappen variëren en tools bieden meerwaarde | Max stappen, toegestane tools, effectcontrole |

De portfolio-workflow gebruikt bewust een kleine expliciete state machine. Dat toont state, fencing en retries zonder extra frameworklaag. Microsoft Agent Framework, LangGraph of MCP zouden een aparte gemotiveerde keuze en implementatie vereisen; de repo claimt die frameworks/protocollen niet gebruikt te hebben.
