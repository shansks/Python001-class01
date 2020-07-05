# -*- coding: utf-8 -*-
import mysql.connector
from scrapy.utils.project import get_project_settings
from mysql.connector import errorcode
import logging

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

SETTINGS = get_project_settings()
logger = logging.getLogger(__name__)

class MaoyanspiderPipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        type = item['type']
        date = item['date']
        output = f'{title},{type},{date}|\n\n'
        with open('./doubanmovie.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item

class SavetoMySQLPipeline(object):
    def __init__(self):
        #connect to mysql server
        self.cnx = mysql.connector.connect(
            user=SETTINGS["MYSQL_USER"],
            password=SETTINGS["MYSQL_PWD"],
            host=SETTINGS["MYSQL_SERVER"],
            database=SETTINGS["MYSQL_DB"],
            buffered=True
        )
        self.cursor = self.cnx.cursor()
        self.table_name=SETTINGS["MYSQL_TABLE"]
        create_table_query= "CREATE TABLE `" + self.table_name + "` (\
                `title` CHAR(20) NOT NULL,\
                `type` VARCHAR(140) NOT NULL,\
                `datetime` VARCHAR(22)\
                )"
        try:
            self.cursor.execute(create_table_query)
        except mysql.connector.Error as err:
            logger.info(err.msg)
        else:
            self.cnx.commit()

    def insert_one(self,item):
        title = item['title']
        type = item['type']
        date = item['date']
        insert_query = 'INSERT INTO ' + self.table_name + ' (title, type, date)'
        insert_query += ' VALUES ( %s, %s, %s)'
        insert_query += ' title = %s, type = %s, date= %s'

        try:
            self.cursor.execute(insert_query,(title,type,date,title,type,date))
        except mysql.connector.Error as err:
            logger.info(err.msg)
        else:
            self.cnx.commit()

    def process_item(self,item,spider):
        self.insert_one(dict(item))
        logger.debug("Add movie:%s" %item['title'])