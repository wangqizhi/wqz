from flask import Flask

import markdown2

app = Flask(__name__)


@app.route('/')
def index():
    f = open('/Users/YiBan/PycharmProjects/wqz/doc/hello.md','r')
    content = f.read()
    f.close()
    return markdown2.markdown(content)
    # return 'hello world'


if __name__ == '__main__':
    app.debug = True
    app.run()
