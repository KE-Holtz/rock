TOP_OF_FILE = """
<!DOCTYPE html>
<html>

<head>
  <title>Pet Rock!</title>
</head>
"""


BOTTOM_OF_FILE = """
</html>
"""

ATTRIBUTE_MIN = 1
ATTRIBUTE_MAX = 10


def link(path: str, message: str) -> str:
    return '<a href="' + path + '">' + message + "</a>"


def generate_rock(action: str) -> str:
    return '<img src="../rock' + action + '.png" alt="rock">'


def filename(
    happiness: int,
    hungryness: int,
    tiredness: int,
    dirtyness: int,
    last_action: str,
    generating: bool = False,
) -> str:
    if generating:
        start = "site/state/"
    else:
        start = ""

    return (
        start
        + "happiness"
        + str(happiness)
        + "hungryness"
        + str(hungryness)
        + "tiredness"
        + str(tiredness)
        + "dirtyness"
        + str(dirtyness)
        + "lastaction"
        + last_action
        + ".html"
    )


def generate_links(
    happiness: int,
    hungryness: int,
    tiredness: int,
    dirtyness: int,
) -> str:
    link1 = link(
        filename(
            min(happiness + 2, ATTRIBUTE_MAX),
            min(ATTRIBUTE_MAX, hungryness + 1),
            min(ATTRIBUTE_MAX, tiredness + 1),
            dirtyness,
            "Play",
        ),
        "Play",
    )
    link2 = link(
        filename(
            happiness,
            max(ATTRIBUTE_MIN, hungryness - 2),
            min(ATTRIBUTE_MAX, tiredness + 1),
            min(ATTRIBUTE_MAX, dirtyness + 1),
            "Feed",
        ),
        "Feed",
    )

    link3 = link(
        filename(
            happiness,
            min(ATTRIBUTE_MAX, hungryness + 1),
            max(ATTRIBUTE_MIN, tiredness - 2),
            min(ATTRIBUTE_MAX, dirtyness + 1),
            "Sleep",
        ),
        "Sleep",
    )

    link4 = link(
        filename(
            max(ATTRIBUTE_MIN, happiness - 2),
            hungryness,
            tiredness,
            max(ATTRIBUTE_MIN, dirtyness - 4),
            "Wash",
        ),
        "Wash",
    )
    return link1 + "\n" + link2 + "\n" + link3 + "\n" + link4 + "\n"


def h1(string: str) -> str:
    return "<h1>" + string + "</h1>"


def h2(string: str) -> str:
    return "<h2>" + string + "</h2>"


def main():
    attrubute_range = range(ATTRIBUTE_MIN, ATTRIBUTE_MAX + 1)
    possible_actions = ["Play", "Feed", "Sleep", "Wash"]
    last_action_message = {
        "Play": "I had fun playing!",
        "Feed": "That food was delicious!",
        "Sleep": "I just woke up from my nap!",
        "Wash": "I sure do feel squeaky-clean!",
    }
    for happiness in attrubute_range:
        for hungryness in attrubute_range:
            for tiredness in attrubute_range:
                for dirtyness in attrubute_range:
                    for last_action in possible_actions:
                        with open(
                            filename(
                                happiness,
                                hungryness,
                                tiredness,
                                dirtyness,
                                last_action,
                                generating=True,
                            ),
                            "w",
                        ) as file:
                            file_contents = TOP_OF_FILE
                            file_contents += h1(last_action_message[last_action]) + "\n"
                            file_contents += generate_rock(last_action) + "\n"
                            file_contents += (
                                h2(
                                    "Happiness: "
                                    + str(happiness)
                                    + "/"
                                    + str(ATTRIBUTE_MAX)
                                )
                                + "\n"
                            )
                            file_contents += (
                                h2(
                                    "Hungryness: "
                                    + str(hungryness)
                                    + "/"
                                    + str(ATTRIBUTE_MAX)
                                )
                                + "\n"
                            )
                            file_contents += (
                                h2(
                                    "Tiredness: "
                                    + str(tiredness)
                                    + "/"
                                    + str(ATTRIBUTE_MAX)
                                )
                                + "\n"
                            )
                            file_contents += (
                                h2(
                                    "Dirtyness: "
                                    + str(dirtyness)
                                    + "/"
                                    + str(ATTRIBUTE_MAX)
                                )
                                + "\n"
                            )

                            file_contents += generate_links(
                                happiness, hungryness, tiredness, dirtyness
                            )

                            file_contents += BOTTOM_OF_FILE
                            file.write(file_contents)


if __name__ == "__main__":
    main()
