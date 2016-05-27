#启动脚本

#!/usr/bin/env python
from app import create_app,db


app =create_app('default')

if __name__=='__main__':
        app.run()