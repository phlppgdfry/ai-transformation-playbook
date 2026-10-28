# Start hier

## Eerst zelf demonstreren

1. Open de README van `enterprise-ai-accounting-copilot`. Draai de demo, test de factuurwerkbank en leg goedkeuring plus outbox uit.
2. Draai `agentic-workflow-platform`. Verklaar een retry, lease en hervatting na herstart. Wijs aan welke stappen deterministisch zijn en wanneer Azure een plan maakt.
3. Draai de goede én onveilige fixture in `enterprise-ai-evals-governance`. De laatste hoort te falen. Leg uit waarom die score geen modelbenchmark is.
4. Gebruik de RAG-ACL-tests en de Copilot-connector om te tonen waar de autorisatiegrens ligt.
5. Wijzig adoptie in `data/scenarios.json`, genereer de businesscase opnieuw en verklaar de uitkomst.

## Wat nu is geleverd

Zes zelfstandige repositories, samen 101 lokale tests. De vijf applicatie-images zijn gebouwd, hun verpakte API's zijn gecontroleerd en hun standaard Uvicorn-commando's zijn gestart met een geslaagde healthrequest. De accounting-console is handmatig in Chrome doorlopen. Uitvoer en beperkingen staan per repo in `evidence/`.

## Wat je zelf nog moet bewijzen

Een echte Azure-test met model- en OCR-kwaliteit, Microsoft-tenantimport/publicatie, Entra-identiteit en echte externe sinks vereisen jouw bevoegde accounts en een afzonderlijke pilot. Een aantal onderwerpen uit het leerplan — MCP, specifieke agentframeworks, Functions, managed identity en enterprise-observability — is expliciet als verdere oefening gemarkeerd. Ze worden niet als geïmplementeerd voorgesteld.

Deze repo's vormen werkende portfolio-referenties; ze zijn geen productiecertificering of bewijs dat je persoonlijk alle onderdelen beheerst. Gebruik [de 30 vaardigheden](06-learning-roadmap.md) en [de eigenaarschapstoets](07-interview-evidence.md) om dat verschil zelf te overbruggen.

Voor Titeca is een sollicitatie verdedigbaar wanneer je dit eerlijk demonstreert. De vacature vraagt ook professionele AI-implementatie- en Azure-ervaring. Alleen de aanwezigheid van deze repo's bevestigt die ervaring niet.
