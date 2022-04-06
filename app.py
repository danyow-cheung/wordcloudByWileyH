from flask import Flask, render_template, request
from analysci import main
import numpy as np
from PIL import Image
from wordcloud import WordCloud

app = Flask(__name__)

'''地址映射'''


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def home():
    return index()


@app.route('/word', methods=["POST", "GET"])
def word():
    return render_template("word.html")


@app.route('/team')
def team():
    return render_template("team.html")


@app.route('/about')
def about():
    return render_template("about.html")


# 生成词云主页面
@app.route('/wordcloud', methods=["POST", "GET"])
def wordcloud():
    if request.method == "POST":

        words = request.form["words"]

        height = request.form["height"]
        width = request.form["width"]
        minfontsize = request.form["minfontsize"]
        maxfontsize = request.form["maxfontsize"]

        width = int(width)
        height = int(height)
        minfontsize = int(minfontsize)
        maxfontsize = int(maxfontsize)

        print(words)

        with open('data/content.txt', 'w') as f:
            f.write(words)

        main()

        text = open('data/word.txt', 'r', encoding='utf8').read()
        font_path = 'font/msyh.ttf'

        background = np.array(Image.open("cloud.png"))

        # 产生词云
        wc = WordCloud(
            background_color="black",
            width=width,
            min_font_size=minfontsize,
            max_font_size=maxfontsize,
            height=height,
            mask=background,
            font_path=font_path,
            stopwords="stop_words.utf8"
        )
        wc.generate(text)

        wc.to_file("output/wordcloud.png")

        filename = Image.open("output/wordcloud.png")
        filename.show()

        return render_template('wordcloud.html')
    else:
        return render_template('wordcloud.html')


if __name__ == '__main__':
    app.run()
