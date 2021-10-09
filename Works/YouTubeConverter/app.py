from flask import Flask,redirect,url_for,render_template,request,send_file,session
from pytube import YouTube
from tempfile import TemporaryDirectory
from io import BytesIO
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY'] = "MySecret"
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///example.db'


ENV = 'product'

if ENV == 'dev':
    app.debug = True
    # app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:yusif@localhost:5432/url'
else:
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://hqsmehndaqglmb:2319825064d8b3162275e8530588558884037bc872f8530a74e7b65b7620ccd3@ec2-23-23-162-138.compute-1.amazonaws.com:5432/d8fsij8tfddd3a'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Urls(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    link = db.Column(db.String(250))

@app.route('/',methods=['GET','POST'])
def index():
    links = Urls.query.all()
    if request.method=='POST':
        session['link'] = request.form.get('url')
        url = YouTube(session['link'])
        urls = Urls(
            link = request.form['url']
        )
        db.session.add(urls)
        db.session.commit()
        return render_template('video.html', url=url)
    return render_template('index.html', links=links)

@app.route("/download", methods=["GET","POST"])
def download_video():
    if request.method == "POST":
        url = YouTube(session['link'])
        itag = request.form.get('itag')
        video = url.streams.get_by_itag(itag)
        filename = video.download()
        return send_file(filename,as_attachment=True)
    return redirect (url_for('index'))

@app.route("/download_mp3", methods=["GET","POST"])
def download_mp3():
    if request.method == "POST":
        with TemporaryDirectory() as tmp_dir:
            url = YouTube(session['link']).streams.filter(only_audio=True).all()
            # mp3name = url[0].download().replace("mp4","mp3").replace(" ","-")
            download_path=url[0].download(tmp_dir)
            audio_name = download_path.split("\\")[-1].replace("mp4","mp3")
            file_bytes = b""
            with open(download_path, "rb") as f:
                file_bytes = f.read()
            return send_file(BytesIO(file_bytes),download_name=audio_name, as_attachment=True)
    return redirect(url_for('index'))


        
if __name__ == '__main__':
    
    app.run(debug=True)