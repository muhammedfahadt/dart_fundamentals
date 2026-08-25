"""
Pac-Man Game Rules Implementation

In Python, we use type hints (similar to Java's type declarations or Dart's static types)
to specify parameter and return types. Unlike Java/Dart, Python type hints are optional
and not enforced at runtime without additional tools.
"""


def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """
    Determine if Pac-Man can eat a ghost.
    
    Java equivalent: public boolean eatGhost(boolean powerPelletActive, boolean touchingGhost)
    Dart equivalent: bool eatGhost(bool powerPelletActive, bool touchingGhost)
    
    Args:
        power_pellet_active: Whether Pac-Man has an active power pellet
        touching_ghost: Whether Pac-Man is currently touching a ghost
    
    Returns:
        True only if BOTH conditions are met (logical AND)
    """
    # The 'and' operator works like Java's && and Dart's &&
    # Returns True only if both operands are True
    return power_pellet_active and touching_ghost


def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    """
    Determine if Pac-Man scores points.
    
    Java equivalent: public boolean score(boolean touchingPowerPellet, boolean touchingDot)
    Dart equivalent: bool score(bool touchingPowerPellet, bool touchingDot)
    
    Args:
        touching_power_pellet: Whether Pac-Man is touching a power pellet
        touching_dot: Whether Pac-Man is touching a dot
    
    Returns:
        True if EITHER condition is met (logical OR)
    """
    # The 'or' operator works like Java's || and Dart's ||
    # Returns True if at least one operand is True
    return touching_power_pellet or touching_dot


def lose(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """
    Determine if Pac-Man loses the game.
    
    Java equivalent: public boolean lose(boolean powerPelletActive, boolean touchingGhost)
    Dart equivalent: bool lose(bool powerPelletActive, bool touchingGhost)
    
    Args:
        power_pellet_active: Whether Pac-Man has an active power pellet
        touching_ghost: Whether Pac-Man is currently touching a ghost
    
    Returns:
        True if touching ghost WITHOUT power pellet (ghost touches AND NOT power pellet)
    """
    # Combine 'and' and 'not' operators
    # 'not' works like Java's ! and Dart's !
    # Parentheses clarify precedence, though 'not' has higher precedence than 'and'
    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots: bool, power_pellet_active: bool, touching_ghost: bool) -> bool:
    """
    Determine if Pac-Man wins the game.
    
    Java equivalent: 
        public boolean win(boolean hasEatenAllDots, boolean powerPelletActive, boolean touchingGhost)
    Dart equivalent: 
        bool win(bool hasEatenAllDots, bool powerPelletActive, bool touchingGhost)
    
    Args:
        has_eaten_all_dots: Whether all dots have been eaten
        power_pellet_active: Whether Pac-Man has an active power pellet
        touching_ghost: Whether Pac-Man is currently touching a ghost
    
    Returns:
        True if all dots eaten AND not losing (based on lose() logic)
    """
    # Reuse the lose() function - this is like calling a helper method in Java/Dart
    # Win condition: all dots eaten AND NOT losing
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)