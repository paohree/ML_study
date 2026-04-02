from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("Korean", "/System/Library/Fonts/Supplemental/AppleGothic.ttf"))
pdfmetrics.registerFont(TTFont("KoreanBold", "/Library/Fonts/Arial Unicode.ttf"))

W, H = A4
doc = SimpleDocTemplate(
    "/Users/paohree/Desktop/ML_Study/books/모의고사2.pdf",
    pagesize=A4,
    leftMargin=20*mm, rightMargin=20*mm,
    topMargin=20*mm, bottomMargin=20*mm
)

def style(name, font="Korean", size=10, leading=16, spaceBefore=0, spaceAfter=2, bold=False):
    return ParagraphStyle(name, fontName="KoreanBold" if bold else "Korean",
        fontSize=size, leading=leading, spaceBefore=spaceBefore, spaceAfter=spaceAfter)

title_style = style("title", size=16, leading=22, bold=True, spaceAfter=6)
subj_style  = style("subj",  size=12, leading=18, bold=True, spaceBefore=10, spaceAfter=4)
q_style     = style("q",     size=10, leading=15, spaceBefore=6, spaceAfter=1)
opt_style   = style("opt",   size=9.5, leading=14)
note_style  = style("note",  size=9, leading=13, spaceBefore=12, spaceAfter=2)

story = []
story.append(Paragraph("빅데이터분석기사 필기 모의고사 2회", title_style))
story.append(Paragraph("총 40문제 (과목당 10문제) | 2026-04-02", note_style))
story.append(Spacer(1, 4*mm))

questions = [
    # ─── 1과목 ───
    ("1과목: 빅데이터 분석 기획 (1~10번)", None, None),
    (1, "SECI 모델에서 '형식지 → 암묵지'로 전환되는 단계는?",
        ["① 공동화(Socialization)", "② 표출화(Externalization)",
         "③ 연결화(Combination)", "④ 내면화(Internalization)"]),
    (2, "관계형 데이터베이스에서 하둡으로 대용량 데이터를 배치로 수집하는 도구는?",
        ["① Kafka", "② Flume", "③ Sqoop", "④ Spark"]),
    (3, "개인정보 비식별화 기술 중 특정 값을 범위로 변환하는 기법은?\n예) 나이 27 → '20대'",
        ["① 가명처리", "② 총계처리", "③ 데이터 범주화", "④ 데이터 마스킹"]),
    (4, "빅데이터 분석 준비도 평가 항목에 해당하지 않는 것은?",
        ["① 분석 업무", "② 인력 및 조직", "③ 분석 기법", "④ 기업 규모"]),
    (5, "다음 중 비율척도(Ratio Scale)에 해당하는 것은?",
        ["① 성별 (남/여)", "② 학점 (A/B/C)", "③ 온도(°C)", "④ 매출액(만원)"]),
    (6, "빅데이터 분석방법론 5단계를 올바른 순서로 나열한 것은?",
        ["① 분석 기획 → 데이터 수집 → 데이터 분석 → 시스템 구현 → 평가 및 전개",
         "② 분석 기획 → 데이터 준비 → 데이터 분석 → 시스템 구현 → 평가 및 전개",
         "③ 데이터 준비 → 분석 기획 → 데이터 분석 → 시스템 구현 → 평가 및 전개",
         "④ 분석 기획 → 데이터 준비 → 모델링 → 시스템 구현 → 평가 및 전개"]),
    (7, "데이터 레이크(Data Lake)에 대한 설명으로 옳은 것은?",
        ["① 정형 데이터만 저장하며 분석 목적에 최적화되어 있다",
         "② 원시 데이터를 정형/비정형 구분 없이 그대로 저장한다",
         "③ ETL 과정을 거쳐 변환된 데이터만 저장한다",
         "④ 특정 부서나 주제에 특화된 소규모 저장소이다"]),
    (8, "OLAP(Online Analytical Processing)에 대한 설명으로 옳은 것은?",
        ["① 실시간 트랜잭션 처리에 최적화된 시스템이다",
         "② 다차원 데이터 분석을 지원하는 시스템이다",
         "③ 데이터를 삽입/수정/삭제하는 작업에 특화되어 있다",
         "④ 소량의 레코드를 빠르게 처리하는 시스템이다"]),
    (9, "다음 중 외부 데이터에 해당하는 것은?",
        ["① 기업의 고객 구매 이력 DB",
         "② SNS 댓글 및 리뷰 데이터",
         "③ 회사 내부 ERP 시스템 데이터",
         "④ 직원 인사 기록"]),
    (10, "분석 마스터 플랜 수립 시 과제 우선순위 선정 기준으로 옳은 것은?",
        ["① 분석 복잡도, 데이터 크기, 실행 기간",
         "② 전략적 중요도, ROI, 실행 용이성",
         "③ 담당자 역량, 예산 규모, 기술 난이도",
         "④ 데이터 품질, 모델 정확도, 배포 속도"]),

    # ─── 2과목 ───
    ("2과목: 빅데이터 탐색 (11~20번)", None, None),
    (11, "흡연자 1,000명 중 100명에게 폐암이 발생하고, 비흡연자 1,000명 중 20명에게 폐암이 발생하였다.\n흡연의 상대위험도(RR)는?",
        ["① 2", "② 3", "③ 5", "④ 10"]),
    (12, "Box-Cox 변환에 대한 설명으로 옳은 것은?",
        ["① 음수 값을 포함한 모든 데이터에 적용 가능하다",
         "② 양수 데이터에만 적용 가능하며 정규성을 높이는 변환이다",
         "③ 이상치를 제거하기 위해 사용하는 기법이다",
         "④ 데이터의 스케일을 0~1로 정규화하는 기법이다"]),
    (13, "표본분산을 계산할 때 n이 아닌 (n-1)로 나누는 이유로 옳은 것은?",
        ["① 표본 크기가 클수록 정확해지기 때문에",
         "② 모분산의 불편추정량을 얻기 위해",
         "③ 계산의 편의를 위해",
         "④ 중심극한정리를 적용하기 위해"]),
    (14, "순서가 있는 범주형 변수(예: 교육수준 초<중<고<대)를 수치로 변환할 때 가장 적합한 인코딩 방법은?",
        ["① 원핫(One-hot) 인코딩", "② 레이블(Label) 인코딩",
         "③ 순서형(Ordinal) 인코딩", "④ 타겟(Target) 인코딩"]),
    (15, "결측값 대체 방법 중 회귀분석을 이용한 대체의 특징으로 옳은 것은?",
        ["① 변수 간의 관계를 보존하면서 결측값을 대체한다",
         "② 단순하고 계산 비용이 가장 적다",
         "③ 반드시 데이터가 MCAR인 경우에만 사용 가능하다",
         "④ 결측값을 해당 변수의 평균으로 대체한다"]),
    (16, "학교 전체 학생의 학업 성취도 조사를 위해 학년별로 나누고, 각 학년에서 무작위 추출하였다. 이 방법은?",
        ["① 단순무작위추출", "② 층화추출", "③ 군집추출", "④ 계통추출"]),
    (17, "다음 중 좋은 점추정량의 조건이 아닌 것은?",
        ["① 불편성: 추정량의 기댓값이 모수와 같다",
         "② 효율성: 분산이 작다",
         "③ 일치성: 표본 크기가 커질수록 모수에 수렴한다",
         "④ 정규성: 추정량의 분포가 정규분포를 따른다"]),
    (18, "데이터의 왜도(Skewness)가 0에 가까울 때의 특징으로 옳은 것은?",
        ["① 오른쪽 꼬리가 길다",
         "② 평균이 중앙값보다 크다",
         "③ 평균과 중앙값이 비슷하다",
         "④ 최빈값이 평균보다 크다"]),
    (19, "변수들의 단위가 다르거나 척도 차이가 클 때 PCA에 적용하기 적합한 행렬은?",
        ["① 공분산행렬 — 단위가 같을 때 사용",
         "② 상관행렬 — 단위를 표준화하여 비교",
         "③ 항등행렬 — 분산이 모두 같을 때 사용",
         "④ 전치행렬 — 변수가 많을 때 사용"]),
    (20, "정준상관분석(Canonical Correlation Analysis)에 대한 설명으로 옳은 것은?",
        ["① 하나의 독립변수와 하나의 종속변수 간의 관계를 분석한다",
         "② 두 변수 집합 간의 상관관계를 분석하는 방법이다",
         "③ 제3 변수 영향을 통제하고 두 변수의 순수한 상관을 분석한다",
         "④ 여러 범주형 변수 간의 독립성을 검정한다"]),

    # ─── 3과목 ───
    ("3과목: 빅데이터 모델링 (21~30번)", None, None),
    (21, "ADF 검정 결과 p-value = 0.03일 때의 해석으로 옳은 것은?",
        ["① 귀무가설 채택 — 시계열은 비정상이다",
         "② 귀무가설 기각 — 시계열은 정상이다",
         "③ 귀무가설 채택 — 시계열은 정상이다",
         "④ 귀무가설 기각 — 시계열은 비정상이다"]),
    (22, "Lasso 회귀에 대한 설명으로 옳은 것은?",
        ["① 계수의 제곱합에 패널티를 부과한다 (L2 정규화)",
         "② 계수의 절댓값 합에 패널티를 부과하며 일부 계수를 0으로 만든다 (L1 정규화)",
         "③ 계수를 0으로 만들지 않고 작게 줄이는 효과만 있다",
         "④ 다중공선성 해결에 Ridge보다 효과적이다"]),
    (23, "SOM(Self-Organizing Map)에 대한 설명으로 옳은 것은?",
        ["① 지도 학습 기반의 분류 알고리즘이다",
         "② 입력 데이터를 고차원 공간으로 매핑한다",
         "③ 비지도 학습으로 고차원 데이터를 저차원 격자로 시각화한다",
         "④ 반드시 군집 수(k)를 사전에 지정해야 한다"]),
    (24, "나이브 베이즈(Naïve Bayes) 분류기의 핵심 가정은?",
        ["① 모든 특성(feature)이 선형 관계를 갖는다",
         "② 특성들이 주어진 클래스 내에서 서로 조건부 독립이다",
         "③ 데이터가 반드시 정규분포를 따른다",
         "④ 훈련 데이터와 테스트 데이터의 분포가 동일하다"]),
    (25, "k-fold 교차검증의 장점으로 옳은 것은?",
        ["① 홀드아웃보다 계산 속도가 빠르다",
         "② 모든 데이터가 훈련과 검증에 1번씩 사용되어 데이터를 효율적으로 활용한다",
         "③ 홀드아웃보다 데이터 활용률이 낮다",
         "④ 데이터 크기에 상관없이 항상 적합하다"]),
    (26, "부트스트랩(Bootstrap) 방법에 대한 설명으로 옳은 것은?",
        ["① 복원 추출로 표본을 반복 생성하여 통계량의 분포를 추정한다",
         "② 비복원 추출로 표본을 여러 번 추출한다",
         "③ 반드시 정규분포를 가정해야 적용 가능하다",
         "④ 0.632 Bootstrap에서 0.632는 검증에 사용되는 고유 샘플 비율이다"]),
    (27, "MANOVA에 대한 설명으로 옳은 것은?",
        ["① 독립변수 1개, 종속변수 1개인 분석이다",
         "② 독립변수 여러 개, 종속변수 1개인 분석이다",
         "③ 독립변수 1개 이상, 종속변수 여러 개인 분석이다",
         "④ 독립변수와 종속변수 모두 범주형이어야 한다"]),
    (28, "단순회귀분석(독립변수 1개)에서 관측치가 20개일 때 잔차의 자유도는?",
        ["① 19", "② 18", "③ 20", "④ 1"]),
    (29, "특잇값 분해(SVD)에 대한 설명으로 옳지 않은 것은?",
        ["① 행렬을 세 개의 행렬의 곱으로 분해한다",
         "② 정방행렬에만 적용 가능하다",
         "③ 추천 시스템 등 차원 축소에 활용된다",
         "④ PCA보다 일반적인 분해 방법이다"]),
    (30, "스태킹(Stacking) 앙상블에 대한 설명으로 옳은 것은?",
        ["① 여러 모델의 예측 결과를 단순 평균내어 최종 예측한다",
         "② 여러 기본 모델의 예측 결과를 메타 학습기에 입력하여 최종 예측한다",
         "③ 오답에 가중치를 높이는 순차적 학습 방법이다",
         "④ 동일한 모델을 서로 다른 훈련 데이터로 병렬 학습한다"]),

    # ─── 4과목 ───
    ("4과목: 빅데이터 결과 해석 (31~40번)", None, None),
    (31, "MAPE(Mean Absolute Percentage Error)에 대한 설명으로 옳은 것은?",
        ["① 오차의 제곱 평균의 제곱근이다",
         "② 실제값 대비 오차의 절댓값 비율의 평균이다",
         "③ 실제값이 0일 때도 안정적으로 계산된다",
         "④ 음수 값이 나올 수 있다"]),
    (32, "Adjusted R²(수정 결정계수)에 대한 설명으로 옳은 것은?",
        ["① 독립변수를 추가하면 항상 증가한다",
         "② 독립변수 개수에 패널티를 부과하여 무의미한 변수 추가 시 감소할 수 있다",
         "③ R²보다 항상 크다",
         "④ 반드시 0~1 범위 안에 있다"]),
    (33, "Lift chart(향상도 차트)에 대한 설명으로 옳은 것은?",
        ["① 모델을 사용했을 때와 사용하지 않았을 때의 성능 비율을 나타낸다",
         "② 모델의 FPR 대비 TPR을 나타내는 곡선이다",
         "③ 군집 분석의 성능을 평가하는 지표이다",
         "④ 정밀도와 재현율의 관계를 나타내는 곡선이다"]),
    (34, "코헨의 카파 계수(Cohen's Kappa)에 대한 설명으로 옳은 것은?",
        ["① 군집 분석의 응집도를 측정하는 지표이다",
         "② 우연에 의한 일치를 보정한 분류 모델 성능 지표이다",
         "③ 회귀 모델의 설명력을 나타내는 지표이다",
         "④ 반드시 0~1 범위 안에 있다"]),
    (35, "Q-Q plot에서 데이터 포인트가 기준선의 오른쪽 위로 굽어 있을 때 의미하는 것은?",
        ["① 데이터가 정규분포를 따른다",
         "② 데이터가 왼쪽으로 치우친 분포 (음의 왜도)이다",
         "③ 데이터가 오른쪽으로 치우친 분포 (양의 왜도)이다",
         "④ 데이터에 이상치가 없다"]),
    (36, "히스토그램에 대한 설명으로 옳은 것은?",
        ["① 범주형 변수의 빈도를 나타내는 데 사용된다",
         "② 연속형 변수의 분포를 나타내는 데 사용된다",
         "③ 막대와 막대 사이에 간격이 있다",
         "④ 두 변수의 관계를 나타내는 데 사용된다"]),
    (37, "시계열 데이터의 교차검증에 대한 설명으로 옳은 것은?",
        ["① 일반 k-fold처럼 데이터를 무작위로 분할한다",
         "② 시간 순서를 유지하여 과거 데이터로 훈련, 미래 데이터로 검증한다",
         "③ 홀드아웃 방법보다 항상 성능이 낮다",
         "④ 시계열 데이터는 교차검증이 불가능하다"]),
    (38, "앙상블 모델에 대한 설명으로 옳지 않은 것은?",
        ["① 여러 모델의 예측을 결합하여 성능을 향상시킬 수 있다",
         "② 개별 모델보다 항상 성능이 뛰어나다",
         "③ 배깅은 분산을 줄이는 효과가 있다",
         "④ 부스팅은 편향을 줄이는 효과가 있다"]),
    (39, "PR 곡선(Precision-Recall 곡선)이 ROC 곡선보다 유용한 경우는?",
        ["① 데이터가 균형 잡혀 있을 때",
         "② 양성 클래스가 매우 적은 불균형 데이터일 때",
         "③ 회귀 모델을 평가할 때",
         "④ 다중 클래스 분류 문제일 때"]),
    (40, "오분류율(Misclassification Rate)에 대한 설명으로 옳은 것은?",
        ["① 1 - Accuracy와 같으며 낮을수록 좋다",
         "② 재현율(Recall)과 동일한 개념이다",
         "③ FP / (FP + TN)으로 계산한다",
         "④ 값이 클수록 좋은 모델이다"]),
]

for item in questions:
    num, q_text, opts = item
    if isinstance(num, str):
        story.append(Spacer(1, 3*mm))
        story.append(Paragraph(num, subj_style))
        story.append(Spacer(1, 1*mm))
        continue

    q_lines = q_text.split("\n")
    story.append(Paragraph(f"<b>{num}.</b> {q_lines[0]}", q_style))
    for extra in q_lines[1:]:
        story.append(Paragraph(f"    {extra}", opt_style))

    if opts:
        mid = len(opts) // 2
        col_w = (W - 40*mm) / 2
        for r1, r2 in zip(opts[:mid], opts[mid:]):
            tbl = Table([[Paragraph(r1, opt_style), Paragraph(r2, opt_style)]],
                        colWidths=[col_w, col_w])
            tbl.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                                     ("LEFTPADDING",(0,0),(-1,-1),0),
                                     ("RIGHTPADDING",(0,0),(-1,-1),4)]))
            story.append(tbl)
    story.append(Spacer(1, 1*mm))

# 답안 작성란
story.append(Spacer(1, 6*mm))
story.append(Paragraph("[ 답안 작성란 ]", subj_style))
rows = [["번호","답"]*5]
for i in range(8):
    row = []
    for j in range(5):
        idx = i + j*8 + 1
        row.extend([str(idx) if idx <= 40 else "", ""])
    rows.append(row)

col_w2 = (W - 40*mm) / 10
ans_table = Table(rows, colWidths=[col_w2]*10)
ans_table.setStyle(TableStyle([
    ("FONTNAME",(0,0),(-1,-1),"Korean"),
    ("FONTSIZE",(0,0),(-1,-1),9),
    ("GRID",(0,0),(-1,-1),0.5,colors.grey),
    ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
    ("ALIGN",(0,0),(-1,-1),"CENTER"),
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("ROWHEIGHT",(0,1),(-1,-1),14),
]))
story.append(ans_table)

doc.build(story)
print("PDF 생성 완료: books/모의고사2.pdf")
