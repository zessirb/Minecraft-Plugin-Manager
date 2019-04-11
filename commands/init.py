from bs4 import BeautifulSoup
import requests
import time

from utils.web_client import WebClient


class Init:

    def __init__(self, type, version=None):
        self.type = type
        self.version = version

    def get_version_url(self):
        if self.type == 'vanilla':
            versions = self.fetch_vanilla_versions()
        elif self.type == 'spongevanilla':
            versions = self.fetch_spongevanilla_versions()
        else:
            # TODO : Raise exception here
            return
        if self.version:
            # TODO : Raise exception here
            url = versions[self.version]
        else:
            # TODO : Raise exception here
            url = versions['latest'] if self.type == 'vanilla' else versions['recommended']
        return url


    @staticmethod
    def fetch_vanilla_versions():
        mcversions_page = requests.get('https://mcversions.net')
        mcversions_soup = BeautifulSoup(mcversions_page.text, 'html.parser')
        versions = {}
        versions['latest'] = mcversions_soup.find('li', attrs={'class': 'latest'}).find('a').get('href')
        releases = mcversions_soup.find_all('li', attrs={'class': 'release'})
        for release in releases:
            version_id = release.get('id')
            version_url = release.find('a').get('href')
            versions[version_id] = version_url
        return versions

    @staticmethod
    def fetch_spongevanilla_versions():
        build_found = False
        try_count = 0
        while not build_found:
            spongepowered_page = WebClient('https://www.spongepowered.org/downloads/spongevanilla')
            spongepowered_soup = BeautifulSoup(spongepowered_page.html, 'html.parser')
            build_found = len(spongepowered_soup.find_all('li', attrs={'class': 'build'})) > 0
            time.sleep(3)
            try_count += 1
            if try_count > 5:
                # TODO : Raise exception here
                return
        versions = {}
        versions['recommended'] = spongepowered_soup.find('div', attrs={'id': 'recommended-build'})\
            .find('li', attrs={'class': 'build'}).find('a', attrs={'title': 'Download'}).get('href')
        releases = spongepowered_soup.find('div', attrs={'id': 'all-builds'}).find('li', attrs={'class': 'build'})
        for release in releases:
            version_id = release.get('id')
            release_download_button = release.find('a', attrs={'title': 'Download'})
            if release_download_button:
                version_url = release_download_button.get('href')
                versions[version_id] = version_url
        return versions
