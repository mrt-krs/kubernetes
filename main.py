#from indeed import indeed_pages, indeed_jobs
import time
from flask import  Flask

app =  Flask(__name__)

@app.route('/')
def hello_world():
  ##  last_indeed_page =  indeed_pages()
  ## x = indeed_jobs(last_indeed_page)
  ## print(x)
    return 'Hello World'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

 
