# Progress: corporate and trade-press evidence (done)

`data/history/corporate.yaml` holds 29 records: Cypress's annual reports and SEC filings from fiscal
1993 to 2013 (annualreports.com copies, and EDGAR documents through the Wayback Machine), the trade
press (EE Times, EDN, Electronics Weekly, Semiconductor Digest, Connect CRE) and two company histories
(the Gale *International Directory of Company Histories* text, republished by FundingUniverse and
Encyclopedia.com, counted as one source; and Wikipedia). EE Times and EDN refuse scripted fetches and
have no Wayback captures, so those records cite text captures taken with the Chrome browser.

Coordinator additions are in `data/history/extra.yaml`. Gaps: no annual report before fiscal 1993 was
found online; the fiscal 2000 report is a scanned PDF whose text could not be extracted; there is no
fiscal 2007 annual-report copy in the cache (the fiscal 2007 10-K is cited from `data/filings.yaml`).

The timeline, the fab history and the conflicts between sources are on `docs/history/index.md` and
`docs/history/fabs.md`.
