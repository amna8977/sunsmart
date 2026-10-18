let selectedCityTimeZone = null;

function updateCityClock() {
  if (!selectedCityTimeZone) return;
  const clock = document.getElementById("cityTime");
  const now = new Date();
  clock.textContent = new Intl.DateTimeFormat("en-US", {
    timeZone: selectedCityTimeZone,
    hour: "numeric",
    minute: "2-digit",
    hour12: true
  }).format(now);
  clock.dateTime = now.toISOString();
}

function setCityTimeZone(timeZone) {
  const clock = document.getElementById("cityTime");
  selectedCityTimeZone = timeZone || null;
  clock.textContent = "--";
  clock.removeAttribute("datetime");
  updateCityClock();
}

setInterval(updateCityClock, 1000);
