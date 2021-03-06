from collections import deque

def number_is_threedigit(name):
      return len(name) == 6

graph = {}
graph["1"] = ["6", "3", "7"]
graph["3"] = ["8", "9"]
graph["6"] = ["9"]
graph["7"] = ["100", "10"]
graph["8"] = []
graph["9"] = []
graph["10"] = ["1000", "5000", "6000", "10000"]
graph["100"] = []
graph["1000"] = []
graph["5000"] = []
graph["6000"] = ["300000"]
graph["10000"] = ["99999"]
graph["99999"] = ["200000"]
graph["200000"] = []
graph["300000"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    # 探索処理済みの数値を入れるリスト
    searched = []
    while search_queue:
        number = search_queue.popleft()
        # 未処理の数値のみ探索する
        if not number in searched:
            if number_is_threedigit(number):
                print(number + " is 6-digit number that initially found!")
                return True
            else:
                search_queue += graph[number]
                # 処理済みにする
                searched.append(number)
    return False

search("1")
