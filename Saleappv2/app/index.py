from flask import render_template,request

from app import app
import dao

@app.route('/')
def home():
    cates=dao.load_categories()
    cate_id=request.args.get('category_id')
    products = dao.load_products(cate_id=cate_id)

    return render_template('index.html',cates=cates,products=products)

if __name__=='__main__':
    app.run(debug=True, port=5001)
