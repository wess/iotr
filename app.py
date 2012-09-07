from random import randrange

from flask import Flask
from flask import render_template
from flask import request

app = Flask("lotripsum")

@app.route("/", methods=['GET', 'POST'])
def index():
   
   generated = '....'
   
   if request.method == 'POST':
      if not request.form.get('paragraph_count'):
         generated = "<h4 style='color:red;text-align:center;>Number of paragraphs are required</h4>"
      else:
         
         paragraph_count = int(request.form['paragraph_count'])

         with open('lotr.txt', 'r') as f:
            text        = f.read()
            textList    = text.split("####-")
            textlen     = len(textList)
            textlenCap  = textlen - paragraph_count
            starting    = randrange(1, textlenCap)
            ending      = starting + paragraph_count
            paragraphs  = "</p><p>".join(textList[starting:ending])
            generated   = u"<p>%s</p>" % paragraphs.decode('utf-8')
            
   
   return render_template("index.html", generated=generated)
   
   
if __name__ == '__main__':
   port = int(os.environ.get('PORT', 5000))
   app.run(host="0.0.0.0", port=port)