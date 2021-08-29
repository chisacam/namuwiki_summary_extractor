import ijson
from namuwiki.extractor import extract_text
import re
import json
from argparser import get_argparser

section_regex = re.compile(r'^=+[^=]+=+$',re.MULTILINE)
summary_regex = re.compile(r'=+[ 개요]+=+')

def clean_object(dirty_object):
    sections = section_regex.findall(dirty_object['text'])
    summary_index = [i for i, s in enumerate(sections) if summary_regex.search(s)]
    paragraphs = section_regex.split(dirty_object['text'])
    cleaned_summary = extract_text(paragraphs[0 if len(summary_index) == 0 else summary_index[0]+1])
    return cleaned_summary

def extract_summary(dump_path = './input.json', limit = 0):
    with open(dump_path, 'r') as namu_dirty:
        result = []
        json_parser = ijson.items(namu_dirty, 'item')
        if limit == 0:
            for dirty_object in json_parser:
                cleaned_summary = clean_object(dirty_object)
                if cleaned_summary != '':
                    result.append({
                        'title': dirty_object['title'],
                        'summary': cleaned_summary
                    })
        elif limit > 0:
            count = 0
            for dirty_object in json_parser:
                cleaned_summary = clean_object(dirty_object)
                if cleaned_summary != '':
                    result.append({
                        'title': dirty_object['title'],
                        'summary': cleaned_summary
                    })
                    count += 1
                    if count >= limit:
                        break
        else:
            print('limit는 반드시 0 또는 양수가 지정되어야 합니다!')
            raise TypeError('limit must be zero or positive.')
        return result, len(result)

if __name__ == '__main__':
    parser = get_argparser()
    args = parser.parse_args()

    result, count = extract_summary(args.dump_path, args.limit)
    print('작업끝! 파일 쓰는중!', '추출된 문서 수 : ' + str(count))

    with open(args.output_file, 'w') as clean_json:
        json.dump(result, clean_json, indent=4, ensure_ascii=False)