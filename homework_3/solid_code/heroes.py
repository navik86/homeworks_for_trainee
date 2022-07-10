from antagonistfinder import AntagonistFinder


class FireGunInterface:
    def fire_a_gun(self):
        print('PIU PIU')


class LasersInterface:
    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')


class KickInterface:
    def roundhouse_kick(self):
        print('Bump')


class SuperHero:

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        return 'KICK'

    def ultimate(self):
        pass


class Superman(SuperHero, LasersInterface):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def ultimate(self):
        return self.incinerate_with_lasers()


class ChackNorris(SuperHero, FireGunInterface, KickInterface):

    def __init__(self):
        super(ChackNorris, self).__init__('Chack Norris', False)

    def attack(self):
        return self.fire_a_gun()

    def ultimate(self):
        return self.roundhouse_kick()
