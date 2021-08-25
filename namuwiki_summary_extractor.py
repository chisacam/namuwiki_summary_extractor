import ijson
from namuwiki.extractor import extract_text
import re
import json
import datetime
from argparser import get_argparser

if __name__ == '__main__':
    result = []
    section_regex = re.compile(r'==[ 가-힣]+==')
    parser = get_argparser()
    args = parser.parse_args()
    with open(args.dump_path, 'r') as namu_dirty:
        json_parser = ijson.items(namu_dirty, 'item')
        for dirty_object in json_parser:
            sections = section_regex.findall(dirty_object['text'])
            try:
                index = sections.index('== 개요 ==')
                paragraphs = section_regex.split(dirty_object['text'])
                clean_text = extract_text(paragraphs[index+1])
                if clean_text != '':
                    result.append({
                        'title': dirty_object['title'],
                        'summary': clean_text
                    })
            except:
                if len(sections) < 1:
                    paragraphs = section_regex.split(dirty_object['text'])
                    clean_text = extract_text(paragraphs[0])
                    if clean_text != '':
                        result.append({
                            'title': dirty_object['title'],
                            'summary': clean_text
                        })
                continue
        print('작업끝! 파일 쓰는중!')

    with open(args.output_file, 'w') as clean_json:
        json.dump(result, clean_json, indent=4, ensure_ascii=False)