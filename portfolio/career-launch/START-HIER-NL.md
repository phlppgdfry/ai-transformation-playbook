# Start hier — jouw Enterprise AI-portfolio

Dit zijn zes zelfstandige repositories rond één fictief bedrijfsproces. Ze tonen hoe je een bedrijfsprobleem analyseert, software maakt, beslissingen begrenst en resultaten controleert. Het is onafhankelijk werk met veel AI-ondersteuning, geen bewijs van klantprojecten of zelfstandig technisch meesterschap.

## In vijf minuten begrijpen

1. Lees de [centrale case](../SHOWCASE.md): welk probleem lossen we op, wie beslist en wat is buiten scope?
2. Bekijk de [korte video met Nederlandse captions](video/README.md). De opname toont echte publieke browserinteracties; opgenomen uitvoeringen blijven expliciet replays.
3. Open het onderdeel dat past bij de functie waarvoor je solliciteert:

| Onderdelen | Openbare showcase | Wat je er leert |
|---|---|---|
| Businessanalyse | [Transformation Playbook](https://phlppgdfry.github.io/ai-transformation-playbook/) | Aannames, adoptie, capaciteit en risico scheiden |
| Bedrijfsproces | [Accounting Copilot](https://phlppgdfry.github.io/enterprise-ai-accounting-copilot/) | Exacte bedragen, uitzonderingen en menselijke review |
| Orchestratie | [Workflow Platform](https://phlppgdfry.github.io/agentic-workflow-platform/) | Modelvoorstellen, servercontroles en goedkeuring; Qwen-replay |
| Kennis | [RAG Assistant](https://phlppgdfry.github.io/azure-ai-rag-knowledge-assistant/) | Toegang vóór retrieval en antwoorden met bronnen |
| Kwaliteit | [Evals & Governance](https://phlppgdfry.github.io/enterprise-ai-evals-governance/) | Goede en onveilige resultaten vergelijken |
| Microsoft | [Copilot Automation](https://phlppgdfry.github.io/microsoft-copilot-studio-automation/) | Connectorgrenzen en lokale API-goedkeuring; geen bewezen cloudruntime |

## In vijftien minuten zelf demonstreren

- **Businesscase:** zet adoptie op nul. Leg uit waarom tijdwinst dan verdwijnt en waarom vrijgemaakte uren niet automatisch cashbesparing zijn.
- **Factuur:** kies eerst een geldige factuur, daarna “Off by one cent” en “Unknown supplier”. Leg het verschil uit tussen ongeldige invoer en een geldige factuur met een reviewvlag.
- **Workflow:** bekijk “approval requested” vóór “case created”. Leg uit waarom het model geen beslissingsbevoegdheid heeft.
- **Kennis:** zoek “opleidingsbudget 7312” als finance en vervolgens als HR. Leg uit waarom het systeem niet mag verklappen welke niet-toegankelijke documenten bestaan.
- **Evaluatie:** wissel tussen good en unsafe. Een verwachte afwijzing van een onveilige fixture is een werkende controle, niet iets wat je groen moet maken door de verwachtingen aan te passen.
- **Microsoft:** bekijk uitvoering zonder akkoord. Een chatbotzin “approved” is geen serverbesluit.

De browserdemo's zijn geen permanent gehoste volledige bedrijfsapplicaties. Voor echte API- en opslagflows gebruik je de [bestaande lokale integratie-instructies](../../integration/README.md). Geen nieuwe Azure-resources of betaalde modellen zijn nodig voor de deterministische route.

## De eerste drie zelfstandige oefeningen

1. Teken uit het hoofd waar de menselijke goedkeuring zit. Vergelijk pas daarna met de architectuur. Bewaar je verbeterde tekening.
2. Volg één factuuraanvraag door `api.py`, `models.py` en `store.py`. Schrijf op waar identiteit, bedrag, tenant en replay worden gecontroleerd.
3. Draai één bestaande afwijzingstest. Leg in eigen woorden uit welk bedrijfsrisico die voorkomt en wat de test niet bewijst.

Exacte bestanden, stappen, criteria en het volledige 14-daagse schema staan al in het [ownershipplan](OWNERSHIP-PLAN.md). Die oefeningen zijn niet namens jou uitgevoerd. Probeer eerst zelf; vraag daarna om een beperkte hint en leg de oplossing later zonder hulp opnieuw uit.

## Professioneel gebruiken

Gebruik de [recruiterbrief](RECRUITER-BRIEF.md) en kies één [functierichting](CAREER-POSITIONING.md). Pas de [CV-tekst](CV-PROJECT-ENTRY.md) en [LinkedIn-tekst](LINKEDIN-PROJECT.md) zelf aan. Claim geen ervaring, diploma's, talen, klantresultaten of cloudimplementaties die je niet kunt onderbouwen. Het [interviewdocument](INTERVIEW-PREP.md) helpt ook eerlijk uitleggen hoe je AI gebruikte.

Technische voorbereiding is klaar binnen de gedocumenteerde scope. Jouw resterende werk is oefenen, je eigen verhaal controleren, persoonlijk presenteren en echte sollicitaties versturen. Een eigen gesproken video is optioneel naast de beschikbare ondertitelde rondleiding. Start geen nieuwe featurecyclus om die stappen uit te stellen.
