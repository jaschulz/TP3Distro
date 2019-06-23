# START DIJKSTRA MODULE
import sys
import heapq
from collections import defaultdict

def dijkstra(src,
             g,
             weight = lambda u,v: 1,
             neighbors = lambda g,v: g[v]):

  prev = defaultdict(set)

  dist = defaultdict(lambda:sys.float_info.max)
  dist[src] = 0

  q = []
  heapq.heappush(q, (dist[src], src))

  while q:
    root_dist, root = heapq.heappop(q)
    for nb in neighbors(g, root):
      alt = dist[root] + weight(root, nb)
      nb_dist = dist[nb]
      if alt == nb_dist:
        prev[nb].add(root)
      elif alt < nb_dist:
        dist[nb] = alt
        prev[nb] = {root}
        heapq.heappush(q, (alt, nb))
  return dist, prev, src

def paths_to(prev_chain, dst):
  dst_prev = prev_chain[dst]
  if dst_prev:
    return [path + [dst]
            for u    in dst_prev
            for path in paths_to(prev_chain, u)]
  return [[dst]]

def all_paths((dist, prev_chain, src)):
  return {v:paths_to(prev_chain,v)
          for v in dist
          if v != src }

# example: all_paths(dijkstra(1, {1:[2,3], 2:[4], 3:[4], 4:[]}))

# END DIJKSTRA MODULE
