# Recording guide

## Prepare the existing demonstration

Clone/install the six repositories as sibling directories, with a separate locked `.venv` for each API; follow their READMEs or clean-install guide. The playbook needs only Python. Use synthetic data and fixture mode. No cloud credential, new model or video-generation pipeline is required.

From the playbook in two terminals:

```bash
python3 -m consulting.server --port 18086
```

```bash
python3 -m integration.scenario --root .. --serve --session-file /tmp/portfolio-recording-session.json --output reports/recording-scenario.json
```

The runner executes the scenario, prints random loopback API origins and leaves its own temporary services available. Append `/console` for accounting, workflow, RAG and governance; automation uses `/docs`. The calculator is `http://127.0.0.1:18086`. Existing instructions: [integration guide](../../integration/README.md).

The session JSON contains ephemeral role keys. Read it locally off-record, enter only the key needed by the current role into the masked console field, and never display the file or terminal containing keys. No credentials should be embedded in URLs or recorded captions. Runner-created state already includes a completed invoice; use [the additional invoice](assets/invoice-demo.json) for the visible new review. Fresh runner state avoids duplicate-number conflicts between takes.

## Capture procedure

1. Use an ordinary screen recorder already available to you, a 1440×1000 or similarly readable desktop area, and notifications disabled. No finished recording tool/codec is assumed.
2. Open only the required tabs; verify synthetic labels, fixture mode, source fields and local mock export captions. Load the new JSON in accounting's source-file control and submit it. Use the guide's independent reviewer/exporter roles for separate actions.
3. Rehearse all actions once. Prepare role changes off-record; edit cuts are acceptable when they do not imply an unperformed action. Show the denial and resulting state, not just a click.
4. Narrate the script in your own words. Explain the distinction between JSON import and OCR, fixture planning and genuine local inference, and mock export and ERP deployment.
5. Review the exported file end-to-end for readable fields, audio, keys, unrelated personal windows and unsupported claims. Add captions or a transcript. Record filename, duration, date, scenario report and source revision in a private recording log.
6. Export a normal shareable MP4 if your existing recorder supports it. Only add a public link after the actual file plays and its contents are reviewed. No video artifact has been created by this task.
7. Interrupt the runner normally; it removes its own session file/databases/services. Stop your calculator process. Do not kill unrelated processes or delete historical evidence.

## Fallback

If the environment is unavailable, use the authentic gallery with an explicit “recorded application screenshot” caption and postpone live-action claims. If local-Qwen inference fails, keep the failure visible; the model-free demo may be shown as a separate labelled mode. Do not activate Azure for filming.
