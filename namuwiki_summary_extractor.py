import ijson
from namuwiki.extractor import extract_text
import re
import json
from argparser import get_argparser

if __name__ == '__main__':
    result = []
    section_regex = re.compile(r'=+[ 가-힣]+=+')
    summary_regex = re.compile(r'=+[ 개요]+=+')
    parser = get_argparser()
    args = parser.parse_args()
    count = 0
    with open(args.dump_path, 'r') as namu_dirty:
        json_parser = ijson.items(namu_dirty, 'item')
        for dirty_object in json_parser:
            sections = section_regex.findall(dirty_object['text'])
            #print(sections)
            index = [i for i, s in enumerate(sections) if summary_regex.search(s)]
            #print(index)
            summary_length = len(index)
            if summary_length > 0:
                paragraphs = section_regex.split(dirty_object['text'])
                clean_text = extract_text(paragraphs[index[0]+1])
                #print(clean_text)
                if clean_text != '':
                    result.append({
                        'title': dirty_object['title'],
                        'summary': clean_text
                    })
                    count += 1
            else:
                paragraphs = section_regex.split(dirty_object['text'])
                clean_text = extract_text(paragraphs[0])
                #print(clean_text)
                if clean_text != '':
                    result.append({
                        'title': dirty_object['title'],
                        'summary': clean_text
                    })
                    count += 1
                continue
        print('작업끝! 파일 쓰는중!', '추출된 문서 수 : ' + str(count))

    with open(args.output_file, 'w') as clean_json:
        json.dump(result, clean_json, indent=4, ensure_ascii=False)