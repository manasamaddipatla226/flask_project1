from flask import Flask

FAI=Flask(__name__)


@FAI.route('/mango')

def mango():
    return ('<h1>mango is very sweet</h1>')

if __name__=='__main__':
    FAI.run(debug=True)