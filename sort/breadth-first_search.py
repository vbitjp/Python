from collections import deque

def number_is_threedigit(name):
      return len(name) == 3

graph = {}
graph["1"] = ["6", "3", "7"]
graph["3"] = ["8", "9"]
graph["6"] = ["9"]
graph["7"] = ["100", "10"]
graph["8"] = []
graph["9"] = []
graph["100"] = []
graph["10"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    # This array is how you keep track of which number you've searched before.
    searched = []
    while search_queue:
        number = search_queue.popleft()
        # Only search this number if you haven't already searched them.
        if not number in searched:
            if number_is_threedigit(number):
                print(number + " is 3-digit number!")
                return True
            else:
                search_queue += graph[number]
                # Marks this number as searched
                searched.append(number)
    return False

search("1")
