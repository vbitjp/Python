# スタート地点から各ノードへの重み
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# Aからゴール、BからA、Bからゴールへの重み

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# 各ノードのコスト
infinity = float("inf") # 無限大
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 親ハッシュ
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 処理済み
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # 各ノードをループする
    for node in costs:
        cost = costs[node]
        # 今まで最もコストが最低で、かつ、未処理のノードである場合
        if cost < lowest_cost and node not in processed:
            # 新たに最低コストなノードとして代入する
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# 未処理のノードのうち、コストが最も低いものをfind_lowest_cost_nodeで探す
node = find_lowest_cost_node(costs)
# ノードを処理し切る(nodeがNoneになる)まで探し続ける
while node is not None:
    cost = costs[node]
    # このノードに相隣り合うノード全てを代入する
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # このノード経由で隣接ノードに移動する方がコストが安い場合
        if costs[n] > new_cost:
            # ノードのコストを更新
            costs[n] = new_cost
            # ノードの新しい親となる
            parents[n] = node
    # ノードを処理済み扱いにする
    processed.append(node)
    # 次に処理する、最低コストのノードを探す
    node = find_lowest_cost_node(costs)

print("各々のノード(a, b, fin)へ最低限かかるコストの一覧:")
print(costs)

