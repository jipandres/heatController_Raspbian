from flask import Flask, render_template, redirect
from chauldron import *
import datetime



app = Flask(__name__)

#basic_auth = BasicAuth(app)

@app.route('/')
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
#    ch = connect()
#    ch = Chauldron()

    templateData = {
        'name' : 'Villa de Palos',
        'time' : timeString,
        'chauldron_status' : 'on'
        #ch.getStatus() 
        }
    return render_template('index.html', **templateData) 


@app.route('/caldera/on')
#@basic_auth.required
def chauldron_start():
    #Función que enciende la caldera
    print ("turning on the cauldron")
    return redirect('/')

@app.route('/caldera/off')
def chauldron_stop():
    #Función que apaga la caldera
    print ("turning off the cauldron")
    return redirect('/')

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
