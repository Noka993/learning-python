from dataclasses import dataclass, InitVar

@dataclass
class C:
    i: int
    j: int
    database: InitVar[str | None] = None
    
    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup('j')

c = C(10, database={'j': 'value'})