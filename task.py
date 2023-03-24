import codecs
from flask import Flask, render_template, request, Markup
app = Flask(__name__)


@app.route('/', defaults={'filename': "file1.txt"})
@app.route('/<filename>')
def read_file(filename):
    start = int(request.args.get('start', 0))
    end = int(request.args.get('end', -1))
    try:
        encoding = "UTF-16"
        if filename in ["file1.txt", "file3.txt"]:
            encoding = "UTF-8"
        with codecs.open(filename, 'r', encoding=encoding, errors='replace') as file:
            # lines = file.readlines()
            # if end == -1:
            #     content = ''.join(lines[start:])
            # else:
            #     content = ''.join(lines[start:end])
            content = Markup(file.read())
            return render_template('file.html', content=content, filename=filename)
    except Exception as e:
        return render_template('error.html', error=str(e))


if __name__ == '__main__':
    app.run()
