"""Local browser checks for the WWW solutions. Requires Python Playwright and Chrome."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from tempfile import gettempdir
from threading import Thread
import json

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


def value(page, selector):
    return float(page.locator(selector).inner_text().split()[0].replace(",", "."))


def run(base):
    with sync_playwright() as playwright:
        launch = {"headless": True}
        if CHROME.exists():
            launch["executable_path"] = str(CHROME)
        browser = playwright.chromium.launch(**launch)
        page = browser.new_page(viewport={"width": 1280, "height": 850})
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))

        page.goto(base + "01_sol/index.html")
        assert page.locator("h1").count() == 1
        assert page.locator("table").count() == 1
        page.goto(base + "02_sol/index.html")
        assert page.locator("img").evaluate("e => e.complete && e.naturalWidth > 0")

        page.goto(base + "03_sol/index.html")
        assert abs(value(page, "#range") - 40.8) < 0.2
        page.locator("#speed").evaluate(
            "e => { e.value = '30'; e.dispatchEvent(new Event('input', {bubbles: true})); }"
        )
        assert abs(value(page, "#range") - 91.8) < 0.2
        page.locator("#start").click()
        page.wait_for_timeout(350)
        page.locator("#pause").click()
        assert value(page, "#current-time") > 0
        page.locator("#reset").click()
        assert value(page, "#current-time") == 0
        print("01–03: HTML, obraz, suwaki i animacja OK")

        page.goto(base + "do_publikacji/edukacja/index.html")
        assert page.locator("#flight-path").get_attribute("d")
        page.locator("#angle").evaluate(
            "e => { e.value = '30'; e.dispatchEvent(new Event('input', {bubbles: true})); }"
        )
        first_range = value(page, "#range")
        page.locator("#compare").click()
        page.locator("#angle").evaluate(
            "e => { e.value = '60'; e.dispatchEvent(new Event('input', {bubbles: true})); }"
        )
        assert page.locator("#saved-path").get_attribute("d")
        assert abs(first_range - value(page, "#range")) < 0.11
        page.locator("#play").click()
        page.wait_for_timeout(250)
        page.locator("#pause").click()
        assert value(page, "#elapsed") > 0
        desktop = Path(gettempdir()) / "www_edukacja_desktop.png"
        page.screenshot(path=str(desktop), full_page=True)
        print("05: wykres, porównanie torów i animacja OK")

        page.goto(base + "do_publikacji/quiz/index.html")
        assert page.locator("fieldset").count() == 10
        page.locator('input[name="q0"][value="1"]').check()
        page.locator("#check").click()
        assert "1 / 10" in page.locator("#result").inner_text()
        assert "Poprawnie." in page.locator("fieldset").first.inner_text()
        page.locator("#restart").click()
        assert page.locator("#result").is_hidden()
        assert "0 / 10" in page.locator("#progress-label").inner_text()
        print("06: 10 pytań, ocena i reset OK")

        geocode = {"results": [{"name": "Warszawa", "country": "Polska", "latitude": 52.23, "longitude": 21.01}]}
        forecast = {"hourly": {
            "time": ["2026-11-10T00:00", "2026-11-10T01:00", "2026-11-11T00:00", "2026-11-11T01:00"],
            "temperature_2m": [1, 2, 3, 4], "precipitation": [0, 0.5, 1, 0],
        }}
        page.route("**/v1/search?**", lambda route: route.fulfill(status=200, content_type="application/json", body=json.dumps(geocode)))
        page.route("**/v1/forecast?**", lambda route: route.fulfill(status=200, content_type="application/json", body=json.dumps(forecast)))
        page.goto(base + "do_publikacji/pogoda/index.html")
        page.wait_for_function("document.querySelector('#day').disabled === false")
        assert page.locator("#rows tr").count() == 2
        page.locator("#day").select_option("2026-11-11")
        assert page.locator("#rows tr").count() == 2
        page.locator("#metric").select_option("precipitation")
        assert "opady" in page.locator("#chart").get_attribute("aria-label")
        page.route("**/v1/search?**", lambda route: route.fulfill(status=200, content_type="application/json", body='{"results":[]}'))
        page.locator("#city").fill("NieistniejaceMiasto")
        page.locator("#search-button").click()
        page.wait_for_function("document.querySelector('#status').classList.contains('error')")
        assert page.locator("#rows tr").count() == 0
        print("07: API z podstawionymi danymi, filtry i obsługa błędu OK")

        page.set_viewport_size({"width": 390, "height": 844})
        for route in (
            "03_sol/index.html", "do_publikacji/edukacja/index.html",
            "do_publikacji/quiz/index.html", "do_publikacji/pogoda/index.html",
        ):
            page.goto(base + route)
            assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth + 2"), route
        page.goto(base + "do_publikacji/edukacja/index.html")
        mobile = Path(gettempdir()) / "www_edukacja_mobile.png"
        page.screenshot(path=str(mobile), full_page=True)
        assert not errors, errors
        print("Widok mobilny i błędy JavaScript: OK")
        print(f"Zrzuty ekranu: {desktop}, {mobile}")
        browser.close()


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        run(f"http://127.0.0.1:{server.server_port}/")
    finally:
        server.shutdown()
        server.server_close()
