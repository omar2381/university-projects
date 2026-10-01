# Where UK MPs Were Born

Collects the birthplace of every UK Member of Parliament recorded in Wikidata, across 57 Parliaments, and produces a CSV ready for mapping in QGIS.

University coursework on data collection and modelling.

## How it works

1. **Query.** For each Parliament, it runs a SPARQL query against the [Wikidata Query Service](https://query.wikidata.org/) for members of that Parliament and the coordinates of their place of birth.
2. **Reverse geocode.** It looks up each set of coordinates with Nominatim (OpenStreetMap) to find the country and UK nation or region. It keeps only MPs born in the UK and counts each MP once, even if they sat in several Parliaments.
3. **Output.** It writes `MPs.csv` with the place ID, place name, region, latitude and longitude, ready to load into QGIS.

### Performance

Reverse geocoding is rate-limited and was the bottleneck. Many MPs share a birthplace, so caching results by coordinates cut the run time from about 2.3 hours to 27 minutes.

## Running it

```bash
pip install SPARQLWrapper pandas geopy
python mp_birthplaces.py
```

The `get_data()` call near the bottom of the script is commented out, so by default the script only converts an existing `MPs.txt` to CSV. Uncomment it to collect the data from scratch.

## Tech

Python, SPARQL (Wikidata), geopy (Nominatim), pandas, QGIS
