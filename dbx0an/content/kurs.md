---
title: Aktueller Zinssatz und Kurs
seo_title: Aktueller Zinssatz und Kurs
description: "Tagesaktueller Kurs des DBX0AN ETFs. Sieh dir die Kursentwicklung an und verfolge die aktuellen Zinserträge auf einen Blick."
---

## Aktueller Zinssatz

**Stand 15.06.2025:**\
**➔ 1,923 % p.a.**

*(Zins ändert sich täglich mit dem EZB-Leitzins.)*

## Tagesaktueller Kurs

Lasse dir hier den aktuellen Kurs anzeigen:

<div id="button-container" style="display: flex; justify-content: center; padding: 20px;">
<button id="load-chart" style="padding: 10px 20px; font-size: 1rem; cursor: pointer;">
  📈 Kurs anzeigen
</button>
</div>

<p id="info-paragraph" style="text-align: center; font-size: 0.9rem;">Beim Klick auf "Kurs anzeigen" können personenbezogene Daten an TradingView.com übermittelt werden.<br>Sie erklären sich mit der <a target="_blank" href="https://de.tradingview.com/privacy-policy/">Datenschutzrichtlinie von TradingView.com</a> einverstanden.</p>

<div id="chart-container" style="margin-top:20px;"></div>

<script>
document.getElementById("load-chart").addEventListener("click", function() {
    const button = this;
    button.style.display = "none";
    document.getElementById("info-paragraph").style.display = "none";

    const script = document.createElement("script");
    script.src = "https://s3.tradingview.com/tv.js";
    script.onload = function() {
        new TradingView.widget({
            width: "100%",
            height: 600,
            symbol: "TRADEGATE:XEON",
            interval: "D",
            timezone: "Etc/UTC",
            theme: "light",
            style: "2",
            locale: "de_DE",
            toolbar_bg: "#f1f3f6",
            enable_publishing: false,
            save_image: false,
            container_id: "chart-container"
        });
    };
    document.body.appendChild(script);
});
</script>
