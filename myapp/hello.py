import fire

def hello(name="World"):
  return "Hello %s this is a jenkins repo!" % name 

if __name__ == '__main__':
  fire.Fire(hello)
