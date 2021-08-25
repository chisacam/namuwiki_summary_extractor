import argparse
import datetime

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