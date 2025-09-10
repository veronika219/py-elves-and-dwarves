from app.players.player import Player


def calculate_team_total_rating(members: list[Player]) -> int | float:
    return sum(member.get_rating() for member in members)


def elves_concert(members: list["Elf"]) -> str:
    [member.play_elf_song() for member in members]


def feast_of_the_dwarves(members: list["Dwarf"]) -> str:
    [member.eat_favourite_dish() for member in members]
