from places import Place
from abc import abstractmethod


class Media:
    @abstractmethod
    def create_news(self):
        pass


class TV(Media):
    name = 'TV'

    def create_news(self, name_hero: str, place: Place):
        print(f'{self.name}: {name_hero} saved the {place.place_name}!')


class NewsPaper(TV):
    name = 'Newspaper'



