# namuwiki_summary_extractor
본 프로그램은 나무위키 덤프에서 개요에 해당하는 부분만 추출해 위키 문법 제거 및 제목-개요 쌍의 json으로 제공하는 프로그램 입니다.

문법 제거 프로그램은 [namu-wiki-extractor](https://github.com/jonghwanhyeon/namu-wiki-extractor)를 사용 하였습니다.

- 작성 및 테스트한 파이썬 버전: 3.9.6
- 권장 파이썬 버전: 3.8+


*****
# 사용법
## 1. 프로젝트 clone
프로젝트를 clone 받습니다.

```sh
git clone https://github.com/chisacam/namuwiki_summary_extractor.git
cd namuwiki_summary_extractor
```

## 2. requirements 설치
먼저 필요한 라이브러리를 pip으로 설치합니다.


```sh
pip install -r requirements.txt
```

설치가 끝났다면, 아래 두가지 방법으로 활용이 가능합니다.    

## 3.1. 명령줄로 사용

```sh
python namuwiki_summary_extracter.py [--dump_path "namuwiki_dump_path"] [--output_file "output_file_path"] [--limit 100]
```

경로는 따로 명시하지 않는다면 동일 폴더 안의 input.json 파일 읽기를 시도하고, result_YYYYMMdd.json 으로 내보냅니다.

--limit 옵션은 지정한 정수만큼만 추출을 시행합니다. 기본값은 0이고(입력된 json 전체 추출시도), 반드시 0 또는 양수여야 합니다.

참 쉽죠?    

## 3.2. 다른 코드에서 함수로 사용

다른 파이썬 코드에 import 해서 쓸 수도 있습니다.

```python
from namuwiki_summary_extarctor import extract_summary

summary, count = extract_summary(dump_path, limit) # dump_path: string, limit: int(must be positive or zero)
print(summary, count)
```

summary에 저장되는 값은 명령줄로 실행했을때 json으로 저장되는 값과 같으며, 아래 입출력 예시와 example.json 에서 확인하실 수 있습니다.

count는 개요를 추출한 문서의 갯수입니다. 각 문서는 최소한 1글자 이상의 개요 텍스트가 들어있습니다.
*****
# 입출력 예시

입력과 출력의 예시는 다음과 같습니다.

- 입력


```json
[
    {
        "namespace":0,
        "title":"!!아앗!!",
        "text":"\n[목차]\n\n\\'\\'\\'{{{+1 ！！ああっと！！}}}\\'\\'\\'\n\n== 개요 ==\n[[파일:3444050440.jpg|width=60%]]\n▲[[신 세계수의 미궁 2 파프니르기사|신 세계수의 미궁 2]]에서 뜬 !!아앗!!\n\n[[세계수의 미궁 시리즈]]에 전통으로 등장하는 대 사. [[세계수의 미궁 2 제왕의 성배|2편]]부터 등장했으며 훌륭한 [[사망 플래그]]의 예시이다.\n\n세계수의 모험가들이 탐험하는 던전인 수해의 구석구석에는 채취/벌채/채굴 포인트가 있으며, 이를 위한 채집 스킬에 투자하면 제한된 채집 기회에서 보다 큰 이득을 챙길 수 있다. 그러나  분배할 수 있는 스킬 포인트는 한정되어 있기 때문에 채집 스킬에 투자하는 만큼 전투 스킬 레벨은 낮아지게 된다.[* 다만 채집 시스템은 신 세 계수 시리즈의 그리모어 복제, 복합 채집 스킬인 야생의 감, 5편의 종족 특유 스킬, 크로스의 1레벨이 만렙인 채집 스킬 등으로 편의성이 점차  나아져서 채집 스킬 때문에 스킬 트리가 내려가는 일은 점점 줄어들었다.] !!아앗!!이 발생하는 과정을 요약하면 다음과 같다.\n\n 1. 채집용 캐릭터들로 이루어진 약한 파티(ex: [[레인저(세계수의 미궁 2)|레인저]] 5명)가 수해에 입장한다.\n 1. 필드 전투를 피해 채집 포인트에 도착한  후 열심히 아이템을 캐는 중에...\n 1. \\'\\'\\'!!아앗!!\\'\\'\\' ~~라플레시아가 나타났다!~~\n 이때 등장하는 것은 [[FOE(세계수의 미궁 시리즈)|FOE]]는 아니지만 \\'\\'\\'훨씬 위층에 등장하는 강력한 필드 몬스터이며 선제 공격을 당하게 된다!\\'\\'\\'\n 1. \\'\\'\\'으앙 죽음\\'\\'\\'(hage)\n\n여담으로 !!아앗!!의 유래는 1인칭 던전 크롤러의 원조 [[위저드리]]에서 함정을 건드렸을 때 나오는 대사 Oops!(おおっと！)라고 한다.\n\n== 각 작품에서의 모습 ==\n=== [[세계수의 미궁 2 제왕의 성배]] ===\n!!아앗!!의 악랄함은 첫 등장한 작품이자 시리즈 중에서도 불친절하기로 정평이 난 2편이 절정이었다. 그야말로 위의 !!아앗!! 시퀀스 그대로, 묻지도 따지지도 않고 채집할 때마다 일정 확률로 \\'\\'\\'강제로\\'\\'\\' 전투에 돌입해야 했다. 게다가 이럴 때 쓰라고 있는 레인저의 스킬 \\'위험 감지(중간 확률로 적의 선제 공격을 무효화)\\'는 정작 작동하지 않는다!\n\n참 고로 2편에서 채집 도중 !!아앗!!이 뜰 확률은 [[http://www.atlusnet.jp/topic/detail/910|고작 1%다.]] [[던파확률의 법칙|낮아 보이는 확률이어도 플레이 중 한 번이라도 일어나는 것]]을 경험하는 체감 확률을 고려하여 확률을 설정한다고.\n\n=== [[세계수의 미궁 3 성해의 내방자]] ===\n다행히 채집 중 낮은 확률로 \"좋은 아이템을 얻을 수 있을 것 같지만... 주변에서 몬스터들의 기척이 느껴진다.\"는 메시지가 뜨고 이때 운이 좋으면 레어 아이템을 얻을 수 있지만 반대의 경우 적과 싸우게 되는 것으로 조정되었다.\n\n=== [[세계수의 미궁 4 전승의 거신]] ===\n기본적 인 것은 3편과 같지만, 4편에서는 움직이지 않고 채집할 때도 턴이 경과하도록 조정되었기 때문에 주변에 있는 FOE를 잊고 채집에 몰두하다가 FOE와 부딪히면 FOE 버전 !!아앗!!이 뜬다. 그리고 난이도 CASUAL로 플레이시, FOE로 인한 !!아앗!!을 제외하면 절대로 발생하지 않는다.\n\n=== [[신 세계수의 미궁 밀레니엄의 소녀|신 세계수의]] [[신 세계수의 미궁 2 파프니르기사|미궁 시리즈]] ===\n채집 방식이 한 턴으로 끝나는 구조[* 채집으로 한 번 아이템을 획득하면 \"다시, (채집 스킬)에 의해...\"가 뜨면서 한꺼번에 획득되는 구조.]로 바뀐 덕분인지 강제 조우로 다시 회 귀해버렸다(...). 그나마 위험 감지 먹통과 같은 버그성 난점들은 수정되었다. 그 이후에 나온 [[세계수의 미궁 5 오랜 신화의 끝]]과 시리즈의 집대성 작품이자 3DS 마지막 작품인 [[세계수의 미궁 X]]도 마찬가지.\n\n=== [[세계수의 미궁 X]] ===\n본작의 채집은 신 세계수 시리즈와 같은 매커니즘이라 굳이 언급할 필요는 없으나, 퀘스트중에 2편의 !!아앗!! 시퀀스를 재현하면서 \\'\\'\\'라플레시아\\'\\'\\'가 등장하는 퀘스트가 존재 한다.(...) 깨알같이 시스템 메세지 창이 아니라 대화창을 이용해서 완벽 재현한 것이 포인트.\n\n=== [[페르소나 Q 섀도우 오브 더 래버린스]] ===\n세계수 시스템을 기반으로 한 [[페르소나 시리즈]]와의 콜라보 작품인 페르소나 Q에서도 등장한다. 3, 4편과 같이 파워 스폿에서 채집 도중 메시지가 뜨며, 실패하면 파티에 참가하고 있는 멤버 중 한 명의 [[http://nico.ms/sm25683358|!!아앗!! 하는 음성]] ~~또는 [[코로마루|개소리]]~~과 함께 그 던전의 \\'강적\\'인 거대 [[섀도(페르소나 시리즈)|섀도우]]가 나타난다.\n\n그러나 내비 전용 스킬인 뱀눈 노려보기(위험 감지와 같은 효과)와 채집 보조 스킬은 파티의 전투력에 전혀 지장을 주지 않으며, \\'대안심\\'을 달면 거의 볼 일이 없어져서 초중반 이후에는 존재감 이 급격히 줄어든다.\n[[분류:세계수의 미궁 시리즈]]",
        "contributors":[
            "some",
            "good",
            "people",
            ...
        ]
    },
    ...
]
```

- 출력

```json
[
    {
        "title": "!!아앗!!",
        "summary": "▲신 세계수의 미궁 2에서 뜬 !!아앗!!\n세계수의 미궁 시리즈에 전통으로 등장하는 대사. 2편부터 등장했으며 훌륭한 사망 플래그의 예시이다.\n세계수의 모험가들이 탐험하는 던전인 수해의 구석구석에는 채취/벌채/채굴 포인트가 있으며, 이를 위한 채집 스킬에 투자하면 제한된 채집 기회에서 보다 큰 이득을 챙길 수 있다. 그러나 분배할 수 있는 스킬 포인트는 한정되어 있기 때문에 채집 스킬에 투자하는 만큼 전투 스킬 레벨은 낮아지게 된다. !!아앗!!이 발생하는 과정을 요약하면 다음과 같다.\n채집용 캐릭터들로 이루어진 약한 파티(ex: 레인저 5명)가 수해에 입장한다.\n필드 전투를 피해 채집 포인트에 도착한 후 열심히 아이템을 캐는 중에...\n!!아앗!!\n이때 등장하는 것은 FOE는 아니지만 훨씬 위층에 등장하는 강력한 필드 몬스터이며 선제 공격을 당하게 된다!\n으앙 죽음(hage)\n여담으로 !!아앗!!의 유래는 1인칭 던전 크롤러의 원조 위저드리에서 함정을 건드렸을 때 나오는 대사 Oops!(おおっと！)라고 한다.\n라플레시아가 나타났다!\n다만 채집 시스템은 신 세계수 시리즈의 그리모어 복제, 복합 채집 스킬인 야생의 감, 5편의 종족 특유 스킬, 크로스의 1레벨이 만렙인 채집 스킬 등으로 편의성이 점차 나아져서 채집 스킬 때문에 스킬 트리가 내려가는 일은 점점 줄어들었다."
    },
    ...
]
```

# issue

처리 후 VSCode에서 결과물 json 파일을 열었을때, 비 정상적인 줄바꿈 문자를 발견했다는 메세지가 뜹니다.
자동 제거를 수락하면 이후 사용에 문제가 없긴 하나(sqlite_import.py 기준), 어디에서 문제가 발생하는지는 확인이 필요합니다.