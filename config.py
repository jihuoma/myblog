#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
from os import path
import datetime


class Config:
    # 数据库
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_SLOW_DB_QUERY_TIME = 0.5

    REDIS_URL = "redis://localhost:6379/3" #存储输入密码错误用户的IP

    # 邮件
    MAIL_SERVER = 'smtp.126.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT')

    # 文件上传
    # UPLOAD_FOLDER = r'app/static/avatar/avatar'
    # ZFB_FOLDER = r'app/static/zfbimg/zfbimg'
    # WX_FOLDER = r'app/static/wximg/wximg'
    ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif', 'bmp']
    BASE_PATH = path.abspath(path.dirname(__file__))


    # 搜索
    WHOOSH_BASE = os.path.join(BASE_PATH, 'search')
    MAX_SEARCH_RESULTS = 50
    PROPAGATE_EXCEPTIONS = True


    # 记住我
    REMEMBER_COOKIE_DURATION = datetime.timedelta(weeks=1)
    # JSON_AS_ASCII = False

    # 第三方登录
    QQ = {
        'consumer_key': os.environ.get('QQ_KEY'),
        'consumer_secret': os.environ.get('QQ_SECRET'),
        'base_url': 'https://graph.qq.com',
        'request_token_url': None,
        'request_token_params': {'scope': 'get_user_info'},
        'access_token_url': '/oauth2.0/token',
        'authorize_url': '/oauth2.0/authorize',
    }

    GITHUB = {
        'consumer_key': os.environ.get('GITHUB_KEY'),
        'consumer_secret': os.environ.get('GITHUB_SECRET'),
        'request_token_params': {'scope': 'user:email'},
        'base_url': 'https://api.github.com/',
        'request_token_url': None,
        'access_token_method': 'POST',
        'access_token_url': 'https://github.com/login/oauth/access_token',
        'authorize_url': 'https://github.com/login/oauth/authorize'
    }


class DevelopmentConfig(Config):  # mysqlconnector
    # 开发 模式
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:qyzxg@localhost:3306/blog??charset=utf8mb4'


class TestingConfig(Config):
    # 测试 模式
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:qyzxg@localhost:3306/test_blog??charset=utf8mb4'


class ProductionConfig(Config):
    # 发布 模式
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:qyzxg@localhost:3306/blog??charset=utf8mb4'


config = {
    'development': DevelopmentConfig,
    'test': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
