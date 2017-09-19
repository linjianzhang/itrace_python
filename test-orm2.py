# -*- coding:utf-8 -*-

import time
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import pandas as pd

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://esb:esb@132.122.1.161:3316/esb?charset=utf8"
db = SQLAlchemy(app)


@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"


current_stat = ""


@app.route("/<username>", methods=['GET'])
def hello_with_username(username):
    return "Hello " + username + "!"


@app.route("/itsyc/openstack", methods=['GET'])
def openstack():
    global current_stat

    action = request.args.get('action')
    step = current_stat + "|" + action

    if "|create" == step:
        current_stat = "running"
    elif "running|suspend" == step:
        current_stat = "suspended"
    elif "running|pause" == step:
        current_stat = "paused"
    elif "suspended|resume" == step:
        current_stat = "running"
    elif "paused|unpause" == step:
        current_stat = "running"
    elif "running|stop" == step:
        current_stat = "stop"
    else:
        return "error"
    return current_stat


@app.route("/cust/get")
def get_cust():
    cust = Cust.query.all()
    return cust[0].cust_name


@app.route("/cust/set")
def set_cust():
    count = Cust.query.count() + 1
    name = request.args.get('name')
    cust = Cust(cust_id=count,area_id=200,create_date=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),cust_group_id=1,cust_name=name,cust_number=1,update_date=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    db.session.add(cust)
    db.session.commit()
    return cust.cust_name


@app.route("/scores_mean")
def scores_mean():
    scores = Score.query.all()
    result = "姓名, 平均成绩"

    for item in scores:
        ave = (item.chinese + item.math + item.english + item.science + item.liberal) / 5
        result = '%s\n%s,%d' % (result,item.name,ave)
    print result

    df = pd.io.sql.read_sql('select name as 姓名,(chinese+math+english+science+liberal) / 5 平均成绩 from score',db.engine.connect(),columns=['姓名','平均成绩'])
    print df

    d = pd.io.sql.read_sql('select * from score',db.engine.connect())
    avg = d.drop(['id','name'],axis=1).mean(1)
    rs = pd.DataFrame()
    rs['姓名'] = d['name']
    rs['平均成绩'] = avg
    print rs
    return df.to_html()
    #return json.dumps(result,ensure_ascii=False)


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    chinese = db.Column(db.Integer)
    math = db.Column(db.Integer)
    english = db.Column(db.Integer)
    science = db.Column(db.Integer)
    liberal = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Score %r>' % self.name


class Cust(db.Model):
    cust_id = db.Column(db.Integer, primary_key=True, unique=True)
    area_id = db.Column(db.Integer)
    create_date = db.Column(db.Date)
    cust_group_id = db.Column(db.Integer)
    cust_name = db.Column(db.String(255))
    cust_number = db.Column(db.String(255))
    update_date = db.Column(db.Date)

    def __init__(self, cust_id, area_id, create_date, cust_group_id, cust_name, cust_number, update_date):
        self.cust_id = cust_id
        self.area_id = area_id
        self.create_date = create_date
        self.cust_group_id = cust_group_id
        self.cust_name = cust_name
        self.cust_number = cust_number
        self.update_date = update_date

    def __repr__(self):
        return '<Cust %r>' % self.cust_name

@app.route("/dep/get2")
def get_busi2():
    d = pd.io.sql.read_sql('select a.entity_name,b.* from dep_business_entity a,dep_business_service b where a.entity_id=b.entity_id',db.engine.connect())
    return  d.to_html()

@app.route("/dep/get9")
def get_busi9():
    entity_id = request.args.get('id')
    d = pd.io.sql.read_sql('select a.entity_name,b.* from dep_business_entity a,dep_business_service b where a.entity_id=b.entity_id and a.entity_id=%(entityid)s',db.engine.connect(),params={'entityid':entity_id})
    return  d.to_html()

@app.route("/dep/get3")
def get_busi3():
    results = BusiEntity.query.all()
    #print busi
    #return busi[0].ENTITY_NAME
    busis= []
    #data = {}
    for item in results:
        print item
        busis.append(item.to_json())
    #data['code'] = 0
    #data['busis'] =  busis 
    #return json.dumps(data)
    return json.dumps(busis)

@app.route("/dep/get")
def get_busi():
    busi = BusiEntity.query.all()
    return busi[0].ENTITY_NAME

class BusiEntity(db.Model):
    __tablename__ = 'dep_business_entity'
    ENTITY_ID = db.Column(db.Integer, primary_key=True)
    ENTITY_NAME = db.Column(db.String(100))
    DESCRIPTION = db.Column(db.String(256))
    CONTACTS = db.Column(db.String(128))
    CATEGORY_BAG = db.Column(db.String(10))
    DISCOVERY_URLS = db.Column(db.String(512))
    STATE = db.Column(db.String(3))
    STAFF_ID = db.Column(db.String(20))
    MOD_DATE = db.Column(db.Date)
    REMARK = db.Column(db.String(100))

    def to_json(self):
        json_busi = {
            'ENTITY_ID': self.ENTITY_ID,
            'ENTITY_NAME': self.ENTITY_NAME,
            'DESCRIPTION': self.DESCRIPTION,
            'CONTACTS': self.CONTACTS,
            'CATEGORY_BAG': self.CATEGORY_BAG,
            'DISCOVERY_URLS': self.DISCOVERY_URLS,
            'STATE': self.STATE,
            'STAFF_ID': self.STAFF_ID,
            'MOD_DATE': self.MOD_DATE.strftime('%Y-%m-%d %H:%M:%S')    
        }

        return json_busi

    def __repr__(self):
        return '<BusiEntity %r>' % self.ENTITY_NAME




if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=6001,
        debug=True
    )