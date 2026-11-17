# Cross-domain wiki: rules

Pages that connect the memories of all applications. One page per concept (person, project, topic, decision, preference).

- File name: lowercase, hyphens, `.md`. Link pages with `[[wikilinks]]`.
- Front matter: `type` (person | project | topic | decision | preference), `updated` (date), `sources` (list of links).
- Every fact links its source: a chat in `bigmike/chats/`, a document in `library/`, a summary in `finance/` or `health/`.
- A concept page says where the numbers live (e.g. protein: intake in `health/`, cost in `finance/`) and never copies raw figures.
- Write in English. Never add secrets or credentials.
- Update only when asked; do not rewrite pages without new sources.
- Standing rules for all agents: read `wiki/standing-rule-ship-automatically.md` before shipping.
