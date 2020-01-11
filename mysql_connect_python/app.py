from flask import Flask,render_template,request,escape
import mysql.connector
app = Flask(__name__)


@app.route('/')
def entry_page()->'html':
    return render_template('entry.html',
                           the_title="后台添加商品系统 ")

@app.route('/search4',methods=['POST'])
def do_search()->'html':
    name =request.form['name']
    price =int(request.form['price'])
    discount = request.form['discount']
    img = request.form['img']
    log_request(name,price,discount,img) #request是一个对象，在这里没有指定方法，所以指代网络请求的所有数据
    log_requests(name,price,discount,img)
    title  = '这是你提交的商品信息:'
    return render_template('results.html',
                           the_title=title,
                           the_name=name,
                           the_price=price,
                           the_discount=discount,
                           the_img=img)

def log_request(name,price,discount,img)->None:
    dbconfig={ 'host':'127.0.0.1',
               'user':'root',
               'password':'hzy.lucas18.com',
               'database':'demo',}

    conn =mysql.connector.connect(**dbconfig)
    cursor =conn.cursor()
    _SQL ="""insert into shop 
             (name,price,discount,img)
             values 
             (%s,%s,%s,%s)"""
    cursor.execute(_SQL,(name,price,discount,img))#rep实际指代网络请求数据，在这里实指request的所有内容
    conn.commit()
    cursor.close()
    conn.close()
def log_requests (name,price,discount,img)->None:
    with open ("vsearch.log","a") as log:
        print(name,price,discount,img)
@app.route("/viewlog")
def  view_the_log() ->str:
    contents = []
    with open("vsearch.log") as log:
        for line in log:
            contents.append([])
            for item in line.split("|"):
                contents[-1].append(escape(item))
    titles=("name","price","discount","img")
    return render_template("viewlog.html",
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)
if __name__ == "__main__":
   app.run(debug=True)
