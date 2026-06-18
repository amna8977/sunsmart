# SunSmart UV Tracker

A small personal project for exploring UV index information and showing simplified SunSmart interface pages.

## Project Contents

- `SunSmartUVtracker.py` - A Python Streamlit app that:
  - accepts a city name from the user
  - looks up matching locations via the Open-Meteo geocoding API
  - fetches the current UV index for the selected location
  - displays UV guidance and optional raw API output
- `index.html` - Main SunSmart landing page.
- `tracker.html` - A more advanced UV tracker page.
- `tracker-basic.html` - A simpler UV tracker page.

## Getting Started

### Run the Streamlit app

1. Install dependencies:

```powershell
python -m pip install requests streamlit
```

2. Run the app:

```powershell
streamlit run SunSmartUVtracker.py
```

3. Open the local URL shown in the terminal (usually `http://localhost:8501`).

### Use the app

- Enter a city name like `Las Vegas, NV` or `Paris, France`.
- Select the correct location from the list of matches.
- View the current UV index and safety guidance.
- Optionally click `Show raw API response` to inspect the JSON data.

### View the HTML pages

Open any of these files directly in a browser:

- `index.html`
- `tracker.html`
- `tracker-basic.html`

## Notes

- The app uses the Open-Meteo geocoding API and forecast API.
- The HTML files are static examples and do not require a server.

## License

No license specified.
