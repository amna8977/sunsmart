
import requests
import streamlit as st


st.write("Enter a city to get the current UV Index and some safety tips")

city = st.text_input("Enter your city (e.g., Las Vegas, NV):")

def geocode(city_name: str):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    resp = requests.get(url, params={"name": city_name, "count": 5}, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    return data.get("results") or []

def get_uv_index(lat: float, lon: float):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "timezone": "auto",
        "current": "uv_index"
    }
    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    current = data.get("current") or {}
    uvi = current.get("uv_index")
    return uvi, data

if city:
    try:
        with st.spinner("Looking up your city..."):
            candidates = geocode(city)

        if not candidates:
            st.error("No results found. Try a more specific query (e.g., 'Portland, OR' or 'Paris, France').")
        else:
            labels = []
            for candidate in candidates:
                name = candidate.get("name", "")
                region = candidate.get("admin1", candidate.get("country", ""))
                latitude = candidate.get("latitude", 0.0)
                longitude = candidate.get("longitude", 0.0)
                labels.append(f"{name}, {region} (lat {latitude:.3f}, lon {longitude:.3f})")

            def city_label(index):
                return labels[index]

            idx = st.selectbox(
                "Select your city:",
                options=range(len(candidates)),
                format_func=city_label
            )
            choice = candidates[idx]
            lat = float(choice["latitude"])
            lon = float(choice["longitude"])
            st.write(f"You selected: {labels[idx]}")

            with st.spinner("Fetching current UV Index..."):
                uvi, raw = get_uv_index(lat, lon)

            if uvi is None:
                st.error("UV Index not found in response.")
                if st.checkbox("Show the code!"):
                    st.json(raw)
            else:
                st.success(f"Current UV Index: {uvi:.1f}")
                if uvi <= 2:
                    tip = "Good! No protection needed; if you burn easily (or just want to feel safer), use SPF 15+."
                elif uvi <= 5:
                    tip = "Stay safe! use SPF 30+, reapply every 2 hours, and seek shade during midday."
                elif uvi <= 7:
                    tip = "Uh oh! Use SPF 50, reapply about every 2 hours, and seek shade at midday."
                else:
                    tip = "Yikes! Use SPF 50+, reapply every 1.5 to 2 hours, and avoid midday sun."
                st.write(tip)

                if st.checkbox("Show the code!"):
                    st.json(raw)

    except requests.HTTPError as e:
        st.error(f"API error: {e}")
    except Exception as e:
        st.error(f"Something went wrong: {e}")
