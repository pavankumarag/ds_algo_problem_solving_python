from collections import defaultdict, namedtuple
from itertools import chain, product, tee


def pairwise(iterable):
	"s -> (s0,s1), (s1,s2), (s2, s3), ..."
	a, b = tee(iterable)
	next(b, None)
	return zip(a, b)


_DEFAULT = object()


class FlightGraph:
	Flight = namedtuple('Flight', 'dep arr dep_dt arr_dt price')
	class Airport:
		__slots__ = ['name', '_graph', '_flights']

		def __init__(self, graph, name):
			self._graph = graph
			self.name = name
			self._flights = defaultdict(set)

		def __getitem__(self, airport):
			if airport not in self._flights:
				raise KeyError('Airport has no flights to {!r}'.format(airport))
			return self._graph[airport]

		def __iter__(self):
			return iter(self._flights.items())

		def add_flight(self, airport, flight):
			# ensure airport exists
			self._graph[airport]
			self._flights[airport].add(flight)

		def remove_flight(self, airport, flight):
			self._flights[airport].remove(flight)

		def flights(self, airport, default=_DEFAULT):
			if airport in self._flights:
				return frozenset(self._flights[airport])
			if default is _DEFAULT:
				raise KeyError('Airport has no flights to {!r}'.format(airport))
			else:
				return default

		def flights_to(self):
			return tuple(self._flights.keys())

		def _routes(self, destination, depth=1):
			depth += 1
			l = [[self.name]]
			while l:
				route = l.pop()
				name = route[-1]
				if name == destination:
					yield route
				if len(route) == depth:
					continue
				l.extend([
					(route + [a])
					for a in self._graph[name]._flights.keys()
				])

		def routes(self, destination, depth=1):
			root = self._graph
			return chain.from_iterable(
				product(*(
					root[dep].flights(arr)
					for dep, arr in pairwise(route)
				))
				for route in self._routes(destination, depth)
			)

	def __init__(self, flights=[]):
		self._airports = {}
		for flight in flights:
			flight = self.Flight(**flight)
			self[flight.dep].add_flight(flight.arr, flight)

	def __getitem__(self, key):
		try:
			return self._airports[key]
		except KeyError:
			ret = self._airports[key] = self.Airport(self, key)
			return ret


flights = FlightGraph([
	{'dep': 'FRA', 'arr': 'AMS', 'dep_dt': '2017-05-01 12:00:00', 'arr_dt': '2017-05-01 13:15:00', 'price': 100},
	{'dep': 'FRA', 'arr': 'AMS', 'dep_dt': '2017-05-01 12:00:00', 'arr_dt': '2017-05-01 13:15:00', 'price': 150},
	{'dep': 'FRA', 'arr': 'CPH', 'dep_dt': '2017-05-01 10:00:00', 'arr_dt': '2017-05-01 12:00:00', 'price': 80},
	{'dep': 'FRA', 'arr': 'MAD', 'dep_dt': '2017-05-01 09:00:00', 'arr_dt': '2017-05-01 10:50:00', 'price': 30},
	{'dep': 'CPH', 'arr': 'AMS', 'dep_dt': '2017-05-01 15:00:00', 'arr_dt': '2017-05-01 16:30:00', 'price': 60},
	{'dep': 'CPH', 'arr': 'MAD', 'dep_dt': '2017-05-01 14:15:00', 'arr_dt': '2017-05-01 17:10:00', 'price': 70},
	{'dep': 'MAD', 'arr': 'AMS', 'dep_dt': '2017-05-01 19:00:00', 'arr_dt': '2017-05-01 21:40:00', 'price': 20},
])

for route in flights['FRA'].routes('AMS', 3):
	# TODO: filter if the arr_dt and dep_dt don't allow the route to be possible
	print(', '.join('{0.dep} -> {0.arr} ({0.price})'.format(f) for f in route))
