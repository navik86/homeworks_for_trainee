from abc import abstractmethod


class Place:
    @abstractmethod
    def find_evil(self):
        pass


class Kostroma(Place):
    place_name = 'Kostroma'

    def find_evil(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    place_name = 'Tokyo'

    def find_evil(self):
        print('Godzilla stands near a skyscraper')