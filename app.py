from flask import Flask

FAI=Flask(__name__)

@FAI.route('/wish')

def wish():
    return ('<center><h1>hii hlo</h1></center>')

if __name__=='__main__':

    FAI.run(debug=True)
