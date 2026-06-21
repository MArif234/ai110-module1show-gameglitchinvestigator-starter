def get_range_for_difficulty(difficulty: str):
    """Return the inclusive numeric range a secret number is drawn from.

    The range widens with difficulty so that higher difficulties offer more
    possible values and are therefore harder to guess:

    ====== ============
    Difficulty  Range (inclusive)
    ====== ============
    Easy        1-20
    Normal      1-50
    Hard        1-100
    ====== ============

    Args:
        difficulty: The selected difficulty label. Expected values are
            ``"Easy"``, ``"Normal"``, or ``"Hard"``.

    Returns:
        tuple[int, int]: A ``(low, high)`` pair giving the inclusive lower and
        upper bounds for the difficulty. Any unrecognized ``difficulty`` value
        falls back to the Hard range ``(1, 100)``.

    Examples:
        >>> get_range_for_difficulty("Easy")
        (1, 20)
        >>> get_range_for_difficulty("unknown")
        (1, 100)
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    """Parse and validate raw user input into an integer guess.

    Accepts a free-form string from the input field and attempts to interpret
    it as a whole number. Decimal strings (e.g. ``"3.9"``) are accepted and
    truncated toward zero via ``int(float(raw))``. Empty or ``None`` input and
    non-numeric text are treated as validation failures rather than raising.

    Args:
        raw: The unprocessed input string, or ``None`` if no value was
            provided.

    Returns:
        tuple[bool, int | None, str | None]: A ``(ok, guess, error)`` triple:

        * ``ok`` (bool): ``True`` if parsing succeeded, otherwise ``False``.
        * ``guess`` (int | None): The parsed integer when ``ok`` is ``True``;
          ``None`` otherwise.
        * ``error`` (str | None): A human-readable error message when ``ok`` is
          ``False``; ``None`` otherwise.

    Raises:
        NotImplementedError: This function is a refactoring stub and must be
            implemented by moving the logic from ``app.py`` into this module.

    Examples:
        >>> parse_guess("42")
        (True, 42, None)
        >>> parse_guess("")
        (False, None, 'Enter a guess.')
        >>> parse_guess("abc")
        (False, None, 'That is not a number.')
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )


def check_guess(guess, secret):
    """Compare a guess against the secret number and report the result.

    Produces both a machine-readable outcome label (used to drive scoring and
    game state) and a player-facing hint message. Hints direct the player
    toward the secret: a guess that is too high tells them to go lower, and a
    guess that is too low tells them to go higher.

    Args:
        guess (int): The player's parsed numeric guess.
        secret (int): The hidden target number for the current round.

    Returns:
        tuple[str, str]: An ``(outcome, message)`` pair where ``outcome``
        is one of ``"Win"``, ``"Too High"``, or ``"Too Low"``, and
        ``message`` is the corresponding hint string to display.

    Examples:
        >>> check_guess(50, 50)
        ('Win', '🎉 Correct!')
        >>> check_guess(80, 50)
        ('Too High', '📉 Go LOWER!')
        >>> check_guess(20, 50)
        ('Too Low', '📈 Go HIGHER!')
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIX: The high/low hints were swapped. A guess that is too high must tell
    # the player to go LOWER, and a guess that is too low must tell them to go
    # HIGHER. The original code returned the opposite messages.
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Compute the new running score after a single guess.

    Scoring rules:

    * ``"Win"``: award ``100 - 10 * (attempt_number + 1)`` points, floored at a
      minimum of ``10`` so that even a late win earns something. Earlier wins
      score higher.
    * ``"Too High"``: *intentionally inconsistent* — adds ``5`` points on even
      ``attempt_number`` values and subtracts ``5`` otherwise. This quirk is a
      deliberate part of the "glitchy" game design.
    * ``"Too Low"``: subtracts ``5`` points.
    * Any other outcome: leaves the score unchanged.

    Args:
        current_score: The player's score prior to this guess.
        outcome: The result label from :func:`check_guess` (``"Win"``,
            ``"Too High"``, ``"Too Low"``, or any other string).
        attempt_number: The 1-based index of the current attempt, used to scale
            the win bonus and toggle the "Too High" adjustment.

    Returns:
        int: The updated score after applying the rule for ``outcome``.

    Raises:
        NotImplementedError: This function is a refactoring stub and must be
            implemented by moving the logic from ``app.py`` into this module.

    Examples:
        >>> update_score(0, "Win", 1)
        80
        >>> update_score(0, "Too Low", 3)
        -5
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )
