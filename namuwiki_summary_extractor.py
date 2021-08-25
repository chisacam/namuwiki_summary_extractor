import ijson
from namuwiki.extractor import extract_text
import re
import json
import datetime
import argparse

def get_argparser():
    today_string = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
    outputfile_path = f'./result_{today_string}.json'
    inputfile_path = './input.json'
    parser = argparse.ArgumentParser(description='namu_summary_extracter')
    parser.add_argument('--dump_path', type=str, required=False,
                        default=inputfile_path)
    parser.add_argument('--output_file', type=str, required=False,
                        default= outputfile_path)
    return parser

if __name__ == '__main__':
    result = {}
    section_regex = re.compile(r'==[ 가-힣]+==')
    parser = get_argparser()
    args = parser.parse_args()

    with open(args.dump_path, 'r') as namu_dirty:
        parser = ijson.items(namu_dirty, 'item')
        for dirty_object in parser:
            sections = section_regex.findall(dirty_object['text'])
            try:
                index = sections.index('== 개요 ==')
                paragraphs = section_regex.split(dirty_object['text'])
                clean_text = extract_text(paragraphs[index+1])
                if clean_text != '':
                    result[dirty_object['title']] = clean_text
            except:
                if len(sections) < 1:
                    paragraphs = section_regex.split(dirty_object['text'])
                    clean_text = extract_text(paragraphs[0])
                    if clean_text != '':
                        result[dirty_object['title']] = clean_text
                continue
        print('작업끝!')

    with open(args.output_file, 'w') as clean_json:
        json.dump(result, clean_json, indent=4, ensure_ascii=False)