# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
db = sqlite3.connect("tmall.sqlite")
cursor = db.cursor()

class TmallPipeline(object):
    def process_item(self, item, spider):
        cursor.execute("insert into loreal(command, times, explain, grade, append_command) values (?,?,?,?,?)",[item["command"],item["times"],item["explain"],item["grade"],item["append_command"]])
        db.commit()