from flask import Blueprint
# main是蓝图的名字,同时设置了static的位置(URI和文件夹位置)
main = Blueprint('main',__name__,static_url_path='/static',static_folder='../static')
