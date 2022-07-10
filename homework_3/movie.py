from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        for i, j in self.dates:
            difference = j - i
            for s in range(difference.days + 1):
                yield datetime(i.year, i.month, i.day) + timedelta(s)


m = Movie('sw', [
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7))
])


if __name__ == '__main__':

    for d in m.schedule():
        print(d)