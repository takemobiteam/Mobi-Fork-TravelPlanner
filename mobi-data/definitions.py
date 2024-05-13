import uuid


class Serializable:
    def to_json(self):
        raise NotImplementedError


class Problem(Serializable):
    def __init__(self, start_event, end_event):
        self.id = str(uuid.uuid4())
        self.start_event = start_event
        self.end_event = end_event
        self.id2event = {}
        self.episodes = []
        self.goal_groups = []
        self.locations = []
        self.agents = []
        self.decision_variables = []
        self.global_constraints = []

    def add_event(self, event):
        if event.id not in self.id2event:
            self.id2event[event.id] = event
        return event

    def add_episode(self, from_event, to_event, lb, ub, is_activity=False):
        episode = Episode(from_event, to_event, is_activity=is_activity)
        episode.lb = lb
        episode.ub = ub
        self.episodes.append(episode)
        self.add_event(from_event)
        self.add_event(to_event)
        from_event.outgoing_episodes.append(episode)
        to_event.incoming_episodes.append(episode)
        return episode

    def add_location(self, name, lat, lon):
        location = Location(name, lat, lon)
        self.locations.append(location)
        return location

    def add_decision_variable(self, name, domain2value):
        decision_variable = DecisionVariable(name)
        for domain, value in domain2value.items():
            assignment = Assignment()
            assignment.decision_variable = decision_variable
            assignment.decision_value = domain
            assignment.g = value
            decision_variable.domain_assignment_map[domain] = assignment
        self.decision_variables.append(decision_variable)
        return decision_variable

    def add_goal_group(self, name, start_event, end_event,
                       arrival_event, departure_event, priority):
        goal_group = GoalGroup()
        goal_group.name = name
        goal_group.start_event = start_event
        goal_group.end_event = end_event
        goal_group.arrival_event = arrival_event
        goal_group.departure_event = departure_event
        goal_group.priority = priority
        self.goal_groups.append(goal_group)
        return goal_group

    def to_json(self):
        return {
            "@type": "Problem",
            "id": self.id,
            "startEvent": self.start_event,
            "endEvent": self.end_event,
            "all_events": [event for event in self.id2event.values()],
            "all_episodes": self.episodes,
            "all_locations": self.locations,
            "all_agents": self.agents,
            "all_decision_variables": self.decision_variables,
            "all_global_constraints": self.global_constraints
        }


class Event(Serializable):
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.outgoing_episodes = []
        self.incoming_episodes = []
        self.earliest_time = None
        self.latest_time = None
        self.scheduled_time = None
        self.name = None

    def to_json(self):
        return {
            "@type": "Event",
            "id": self.id,
            "outgoingEpisodes": self.outgoing_episodes,
            "incomingEpisodes": self.incoming_episodes,
            "earliestTime": self.earliest_time,
            "latestTime": self.latest_time,
            "scheduledTime": self.scheduled_time,
            "name": self.name
        }


class Episode(Serializable):
    def __init__(self, from_event, to_event, is_activity=False):
        self.id = str(uuid.uuid4())
        self.name = None
        self.from_event = from_event
        self.to_event = to_event
        self.type = "ACTIVITY" if is_activity else "CONSTRAINT"
        self.lb = None
        self.ub = None
        self.lb_relaxable = False
        self.ub_relaxable = False
        self.guards = []
        self.start_location = None
        self.end_location = None
        self.cost = 0.0
        self.time_windows = []
        self.description = None

    def add_guard(self, guard):
        self.guards.append(guard)
        guard.activating_episodes.append(self)

    def to_json(self):
        return {
            "@type": "Episode",
            "id": self.id,
            "name": self.name,
            "fromEvent": self.from_event,
            "toEvent": self.to_event,
            "type": self.type,
            "lb": self.lb,
            "ub": self.ub,
            "lbRelaxable": self.lb_relaxable,
            "ubRelaxable": self.ub_relaxable,
            "guards": self.guards,
            "startLocation": self.start_location,
            "endLocation": self.end_location,
            "cost": self.cost,
            "timeWindows": self.time_windows,
            "description": self.description
        }


class DecisionVariable(Serializable):
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.guards = []
        self.domain_assignment_map = {}
        self.f = 0.0

    def get_assignment(self, domain):
        return self.domain_assignment_map[domain]

    def add_guard(self, guard):
        self.guards.append(guard)
        guard.activating_variables.append(self)

    def to_json(self):
        return {
            "@type": "DecisionVariable",
            "id": self.id,
            "name": self.name,
            "guards": self.guards,
            "domainAssignmentMap": self.domain_assignment_map,
            "f": self.f
        }


class Assignment(Serializable):
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.decision_variable = None
        self.decision_value = None
        self.activating_episodes = []
        self.activating_variables = []
        self.activating_goalgroups = []
        self.g = None
        self.h = None

    def to_json(self):
        return {
            "@type": "Assignment",
            "id": self.id,
            "decisionVariableId": self.decision_variable.id,
            "decisionValue": self.decision_value,
            "activatingEpisodes": [ep.id for ep in self.activating_episodes],
            "activatingVariables": [var.id for var in self.activating_variables],
            "activatingGoalGroups": [goal.id for goal in self.activating_goalgroups],
            "g": self.g,
            "h": self.h
        }


class GoalGroup(Serializable):
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.name = None
        self.goal_episodes = []
        self.selection_variable = None
        self.start_event = None
        self.end_event = None
        self.arrival_event = None
        self.departure_event = None
        self.priority = None
        self.guards = []

    def add_guard(self, guard):
        self.guards.append(guard)
        guard.activating_goalgroups.append(self)

    def add_goal_episode(self, episode):
        self.goal_episodes.append(episode)

    def to_json(self):
        return {
            "@type": "GoalGroup",
            "id": self.id,
            "name": self.name,
            "goalEpisodes": self.goal_episodes,
            "selectionVariable": self.selection_variable,
            "startEvent": self.start_event,
            "endEvent": self.end_event,
            "arrivalEvent": self.arrival_event,
            "departureEvent": self.departure_event,
            "priority": self.priority,
            "guards": self.guards
        }


class Location(Serializable):
    def __init__(self, name, lat, lon):
        self.id = str(uuid.uuid4())
        self.name = name
        self.lat = lat
        self.lon = lon

    def to_json(self):
        return {
                "@type": "Location",
                "id": self.id,
                "name": self.name,
                "lat": self.lat,
                "lon": self.lon
        }

