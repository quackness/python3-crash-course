#append the end

todos = [
  "Feed the cats",
  "Wash the car",
  "Make supper",
  "Code",
  "Sleep"
]

newTask = todos.append("Check the mail")
print(todos)

#insert at a certain index

todos.insert(1, "Buy groceries")
print(todos)

#change the value of an element
todos[0] = "Feed the cats and a dog"
print(todos)

#delete an element
del todos[0]
print(todos)

#concatenate lists
eveningTasks = ["shower", "brush teeth", "sleep"]
todos = todos + eveningTasks
print(todos)


