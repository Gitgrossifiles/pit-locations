# Pit Locations

GPS coordinates for water meter pits, used to find pits in the field.

## Files

- `Pit_GPS.xlsx` — the source spreadsheet, edited by hand
- `make_pit_locations_json.py` — regenerates the JSON from the spreadsheet
- `pit_locations.json` — generated; 244 records

## Record shape

```json
{
  "address": "10 E Algonquin Rd",
  "business": "Vacant",
  "description": "On Corner Of Arlington Heights And Algonquin Road 15 Feet South From Hydrant",
  "lat": 42.04447,
  "lng": -87.98273,
  "serial": "7194403"
}
```

Columns A–F of the spreadsheet map to address, business, description, lat, lng, serial.
Rows without usable coordinates are dropped.

## Regenerating

```bash
python make_pit_locations_json.py
```

Requires `pandas` and `openpyxl`.
