from bs4 import BeautifulSoup
import requests


class PlaylistGenerator:
    def __init__(self, chosen_year) -> None:
        self.__end_point = f"https://www.billboard.com/charts/hot-100/{chosen_year}"
        self.__playlist = self.generate_playlist()

    def generate_playlist(self) -> list:

        response = requests.get(self.__end_point)
        soup = BeautifulSoup(response.text, "html.parser")

        # TODO - Seleção das divs onde estão localizados os títulos das músicas
        divs_with_contents = soup.find_all(
            "div", class_="o-chart-results-list-row-container")

        # TODO - Seleção dos títulos das músicas
        return [music.find("h3", class_="c-title").getText().strip() for music in divs_with_contents]

    def get_playlist(self):
        return self.__playlist
