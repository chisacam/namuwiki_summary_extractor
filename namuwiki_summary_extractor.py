import ijson
from namuwiki.extractor import extract_text
import re
import json
from argparser import get_argparser

def extract_summary(dump_path, max_extract = 0):
    result = []
    section_regex = re.compile(r'^=+[^=]+=+$',re.MULTILINE)
    summary_regex = re.compile(r'=+[ 개요]+=+')
    with open(dump_path, 'r') as namu_dirty:
        count = 0
        json_parser = ijson.items(namu_dirty, 'item')
        for dirty_object in json_parser:
            sections = section_regex.findall(dirty_object['text'])
            #print(sections)
            index = [i for i, s in enumerate(sections) if summary_regex.search(s)]
            #print(index)
            summary_length = len(index)
            paragraphs = section_regex.split(dirty_object['text'])
            clean_text = extract_text(paragraphs[0 if summary_length == 0 else index[0]+1])
            #print(clean_text)
            if clean_text != '':
                result.append({
                    'title': dirty_object['title'],
                    'summary': clean_text
                })
                count += 1
                if max_extract != 0 and count >= max_extract:
                    break
        return result, len(result)

if __name__ == '__main__':
    parser = get_argparser()
    args = parser.parse_args()

    result, count = extract_summary(args.dump_path, args.max_extract)
    print('작업끝! 파일 쓰는중!', '추출된 문서 수 : ' + str(count))

    with open(args.output_file, 'w') as clean_json:
        json.dump(result, clean_json, indent=4, ensure_ascii=False)