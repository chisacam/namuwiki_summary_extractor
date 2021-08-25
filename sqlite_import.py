import sqlite3
import ijson
from argparser import get_argparser

parser = get_argparser()
args = parser.parse_args()

with open(args.dump_path, 'r') as namu_json:
    conn = sqlite3.connect('./namu.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS namu(title text PRIMARY KEY, summary text)")

    myData =[]
    json_parser = ijson.items(namu_json, 'item')

    for jsonobj in json_parser:
        t = (jsonobj['title'], jsonobj['summary'])
        myData.append(t)

    c.executemany("INSERT INTO namu(title, summary) VALUES (?,?)",myData)

    conn.commit()
