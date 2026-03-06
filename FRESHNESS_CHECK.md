# FRESHNESS_CHECK

- Repo: `rio2016`
- Checked on: `2026-03-02`

## Located Files
- README: `README.md`
- Datapackage: `not present`
- Auto-update scripts: `none found`

## Dataset Description
- <a className="gh-badge" href="https://datahub.io/core/rio2016"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

## Steps Taken
- 1. Read README and datapackage (when present) to identify dataset purpose and source references.
- 2. Inspected update scripts to locate automatic refresh pipelines and hardcoded source URLs.
- 3. Scanned local data files for max date/year values.
- 4. Probed upstream source URLs and extracted latest available date from payload or Last-Modified header.
- 5. Compared local latest vs upstream latest and recorded staleness verdict.

## Source Probes
- URL: `https://datahub.io/core/rio2016` | relevant: `false` | reachable: `true` | status: `200` | latest inferred: `unknown` | reason: `ok`
- URL: `https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25` | relevant: `false` | reachable: `true` | status: `200` | latest inferred: `2000-12-31` | reason: `ok`
- URL: `https://www.rio2016.com/` | relevant: `false` | reachable: `false` | status: `0` | latest inferred: `unknown` | reason: `network error: timed out`
- URL: `https://flother.is/2017/olympic-games-data/` | relevant: `false` | reachable: `true` | status: `200` | latest inferred: `unknown` | reason: `ok`
- URL: `https://raw.githubusercontent.com/flother/rio2016/master/athletes.csv` | relevant: `true` | reachable: `true` | status: `200` | latest inferred: `2016-12-31` | reason: `ok`
- URL: `https://raw.githubusercontent.com/flother/rio2016/master/events.csv` | relevant: `true` | reachable: `true` | status: `200` | latest inferred: `unknown` | reason: `ok`
- URL: `https://en.wikipedia.org/wiki/List_of_IOC_country_codes` | relevant: `false` | reachable: `true` | status: `200` | latest inferred: `2026-03-02` | reason: `ok`
- URL: `https://en.wikipedia.org/wiki/Refugee_Olympic_Team_at_the_2016_Summer_Olympics` | relevant: `false` | reachable: `true` | status: `200` | latest inferred: `2026-03-02` | reason: `ok`
- URL: `https://www.olympic.org/news/suspension-of-the-kuwait-olympic-committee` | relevant: `false` | reachable: `false` | status: `403` | latest inferred: `unknown` | reason: `HTTP 403`
- URL: `https://www.olympic.org/the-ioc` | relevant: `false` | reachable: `false` | status: `403` | latest inferred: `unknown` | reason: `HTTP 403`

## Freshness Result
- Latest local date: `2002-09-12`
- Latest upstream date: `2016-12-31`
- Assessment: Local latest 2002-09-12 is 5224 days behind upstream 2016-12-31
