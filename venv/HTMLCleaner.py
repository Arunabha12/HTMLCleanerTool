from flask import Flask, flash, redirect, render_template, request, url_for
from bs4 import BeautifulSoup
app = Flask(__name__)
app.secret_key = 'random string'

def htmlconverter(html):
   soup = BeautifulSoup(html, 'html.parser')
   for tag in soup():
      for attri in set(tag.attrs):
         del tag[attri]
   return str(soup)


def textconverter(html):
   soup = BeautifulSoup(html, 'html.parser')
   return str(soup.get_text())


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    otpt = None

    if request.method == 'POST':
       if request.form['Submit_button']=='Text_Converter':
          if request.form['html']:
               htmlstr= request.form['html']
               otpt= textconverter(htmlstr)
               flash(otpt)
               return redirect(url_for('result'))
       elif request.form['Submit_button']=='Clean_HTML':
          if request.form['html']:
             htmlstr = request.form['html']
             otpt = htmlconverter(htmlstr)
             flash(otpt)
             return redirect(url_for('result'))

    return render_template('index.html', otpt=otpt)


if __name__ == "__main__":
    app.run(debug=True)