class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class All:
    def __init__(self):
        pass
    def matches(self, player):
        return True

class Not:
    def __init__(self, matcher):
        self._matcher = matcher
    
    def matches(self, player):
        if self._matcher.matches(player):
            return False

        return True

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)
        return player_value < self._value
    
class Or:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True
        return False

class QueryBuilder:
    def __init__(self, list_matchers = [], or_list_matchers = []):
        self.list_matchers = list_matchers
        self.or_list_matchers = or_list_matchers

    def plays_in(self, team):
        new_list_for_matchers = self.list_matchers[:]
        new_list_for_matchers.append(PlaysIn(team))
        return QueryBuilder(new_list_for_matchers)

    def has_at_least(self, value, attr):
        new_list_for_matchers = self.list_matchers[:]
        new_list_for_matchers.append(HasAtLeast(value, attr))
        return QueryBuilder(new_list_for_matchers)

    def has_fewer_than(self, value, attr):
        new_list_for_matchers = self.list_matchers[:]
        new_list_for_matchers.append(HasFewerThan(value, attr))
        return QueryBuilder(new_list_for_matchers)

    def oneOf(self, *matchers):
        return QueryBuilder(or_list_matchers=matchers)

    def build(self):
        if len(self.or_list_matchers) > 0:
            return Or(*self.or_list_matchers)
        return And(*self.list_matchers)
