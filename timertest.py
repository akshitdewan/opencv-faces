import threading

def push():
  threading.Timer(3.0, push).start()
  print("Hello, World!")

push()