from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# 한글 폰트 등록
pdfmetrics.registerFont(TTFont("Korean", "/System/Library/Fonts/Supplemental/AppleGothic.ttf"))
pdfmetrics.registerFont(TTFont("KoreanBold", "/Library/Fonts/Arial Unicode.ttf"))

W, H = A4
doc = SimpleDocTemplate(
    "/Users/paohree/Desktop/ML_Study/모의고사.pdf",
    pagesize=A4,
    leftMargin=20*mm, rightMargin=20*mm,
    topMargin=20*mm, bottomMargin=20*mm
)

# 스타일
def style(name, font="Korean", size=10, leading=16, spaceBefore=0, spaceAfter=2, bold=False):
    return ParagraphStyle(
        name,
        fontName="KoreanBold" if bold else "Korean",
        fontSize=size,
        leading=leading,
        spaceBefore=spaceBefore,
        spaceAfter=spaceAfter,
    )

title_style   = style("title", size=16, leading=22, bold=True, spaceBefore=0, spaceAfter=6)
subj_style    = style("subj",  size=12, leading=18, bold=True, spaceBefore=10, spaceAfter=4)
q_style       = style("q",     size=10, leading=15, spaceBefore=6, spaceAfter=1)
opt_style     = style("opt",   size=9.5, leading=14, spaceBefore=0, spaceAfter=0)
note_style    = style("note",  size=9, leading=13, spaceBefore=12, spaceAfter=2)
table_style   = style("tbl",   size=9.5, leading=14)

story = []

story.append(Paragraph("빅데이터분석기사 필기 모의고사", title_style))
story.append(Paragraph("총 40문제 (과목당 10문제) | 제한시간 없음 | 정답은 제출 후 확인", note_style))
story.append(Spacer(1, 4*mm))

questions = [
    # (번호, 문제, [선지])
    # ─── 1과목 ───
    ("1과목: 빅데이터 분석 기획 (1~10번)", None, None),
    (1, "빅데이터의 5V에서 '데이터의 신뢰성과 정확성'을 뜻하는 것은?",
        ["① Volume", "② Velocity", "③ Veracity", "④ Value"]),
    (2, "DIKW 모델에서 '35도 이상이면 아이스크림 판매가 증가한다는 패턴을 발견한 것'에 해당하는 단계는?",
        ["① Data", "② Information", "③ Knowledge", "④ Wisdom"]),
    (3, "다음 중 데이터 웨어하우스(DW)의 4가지 특성에 해당하지 않는 것은?",
        ["① 주제지향성", "② 비휘발성", "③ 실시간성", "④ 통합성"]),
    (4, "HBase에 대한 설명으로 옳은 것은?",
        ["① 키-값 저장 방식의 캐시 데이터베이스이다",
         "② 분산 파일 시스템이다",
         "③ 분산 환경에서 동작하는 컬럼 기반 NoSQL이다",
         "④ JSON 기반의 문서형 데이터베이스이다"]),
    (5, "ETL에서 Transform(T) 단계에 해당하는 작업은?",
        ["① 원본 데이터를 소스에서 가져오는 작업",
         "② 데이터를 최종 목적지에 저장하는 작업",
         "③ 데이터를 정제하고 형식을 변환하는 작업",
         "④ 데이터를 실시간으로 전송하는 작업"]),
    (6, "CRISP-DM의 6단계를 올바른 순서로 나열한 것은?",
        ["① 데이터 이해 → 비즈니스 이해 → 데이터 준비 → 모델링 → 평가 → 배포",
         "② 비즈니스 이해 → 데이터 이해 → 데이터 준비 → 모델링 → 평가 → 배포",
         "③ 비즈니스 이해 → 데이터 준비 → 데이터 이해 → 모델링 → 평가 → 배포",
         "④ 데이터 이해 → 데이터 준비 → 비즈니스 이해 → 모델링 → 평가 → 배포"]),
    (7, "다음 중 데이터 거버넌스의 3요소에 해당하지 않는 것은?",
        ["① 원칙(Principle)", "② 조직(Organization)", "③ 프로세스(Process)", "④ IT 인프라(Infrastructure)"]),
    (8, "'말로 표현하기 어려운 경험이나 노하우로 축적된 지식'에 해당하는 것은?",
        ["① 형식지", "② 암묵지", "③ 메타데이터", "④ 마스터데이터"]),
    (9, "ERP(Enterprise Resource Planning)에 대한 설명으로 옳은 것은?",
        ["① 고객 관계를 관리하고 마케팅을 지원하는 시스템",
         "② 공급망의 원자재부터 유통까지 관리하는 시스템",
         "③ 회계, 인사, 생산 등 전사적 자원을 통합 관리하는 시스템",
         "④ 데이터 분석으로 예측 및 처방 분석을 제공하는 시스템"]),
    (10, "분석 활용 계획의 수립 시점으로 옳은 것은?",
        ["① 모델링이 완료된 이후",
         "② 평가 단계에서",
         "③ 프로젝트 시작 단계부터",
         "④ 데이터 수집이 완료된 이후"]),

    # ─── 2과목 ───
    ("2과목: 빅데이터 탐색 (11~20번)", None, None),
    (11, "어떤 시험의 평균은 50점, 표준편차는 10점이다. 철수의 점수가 70점일 때 z-score는?",
        ["① 1", "② 1.5", "③ 2", "④ 2.5"]),
    (12, "어떤 질병의 유병률은 2%이다. 질병이 있으면 양성 판정 확률 90%, 질병이 없어도 양성 판정 확률 5%이다.\n양성 판정을 받은 사람이 실제로 질병을 가질 확률은? (소수점 둘째 자리 반올림)",
        ["① 약 12.0%", "② 약 18.0%", "③ 약 26.9%", "④ 약 36.0%"]),
    (13, "결측값 종류 중 MCAR(완전 무작위 결측)에 해당하는 예시는?",
        ["① 소득이 낮을수록 소득을 기입하지 않는 경향이 있다",
         "② 우울증이 심할수록 설문에 응답하지 않는 경향이 있다",
         "③ 실험 중 장비 오류로 무작위로 측정값이 누락되었다",
         "④ 나이가 많을수록 IT 설문 항목을 건너뛰는 경향이 있다"]),
    (14, "중심극한정리에 대한 설명으로 옳은 것은?",
        ["① 모집단이 정규분포일 때만 적용 가능하다",
         "② 표본 크기가 충분히 크면 표본평균의 분포는 정규분포에 근사한다",
         "③ 연속형 변수에만 적용 가능하다",
         "④ 표본 크기에 관계없이 항상 성립한다"]),
    (15, "SMOTE에 대한 설명으로 옳은 것은?",
        ["① 다수 클래스 샘플을 일부 제거하는 언더샘플링 기법이다",
         "② 소수 클래스의 합성 샘플을 생성하는 오버샘플링 기법이다",
         "③ 다수 클래스와 소수 클래스를 동일 비율로 맞추는 리샘플링 기법이다",
         "④ 소수 클래스 샘플을 단순 복제하는 오버샘플링 기법이다"]),
    (16, "층화추출법과 군집추출법에 대한 설명으로 옳은 것은?",
        ["① 층화추출: 집락 내 이질적, 집락 간 동질적",
         "② 군집추출: 층 내 동질적, 층 간 이질적",
         "③ 층화추출은 층 내 동질·층 간 이질 / 군집추출은 집락 내 이질·집락 간 동질",
         "④ 층화추출은 층 내 이질·층 간 동질 / 군집추출은 집락 내 동질·집락 간 이질"]),
    (17, "오른쪽 꼬리가 긴 분포(양의 왜도)에서 대푯값의 크기 관계로 옳은 것은?",
        ["① 최빈값 < 중앙값 < 평균",
         "② 평균 < 중앙값 < 최빈값",
         "③ 중앙값 < 최빈값 < 평균",
         "④ 최빈값 = 중앙값 = 평균"]),
    (18, "1종 오류(Type I Error)에 대한 설명으로 옳은 것은?",
        ["① 귀무가설이 거짓인데 채택하는 오류 (β)",
         "② 귀무가설이 참인데 기각하는 오류 (α)",
         "③ 대립가설이 참인데 기각하는 오류",
         "④ 검정력(Power)과 같은 개념이다"]),
    (19, "제3의 변수의 영향을 통제한 후 두 변수 간의 순수한 상관관계를 분석하는 방법은?",
        ["① 정준상관분석", "② 단순상관분석", "③ 편상관분석", "④ 스피어만 상관분석"]),
    (20, "단위가 다른 두 자료의 상대적 산포를 비교할 때 사용하는 통계량은?",
        ["① 표준편차", "② 분산", "③ 변동계수(CV)", "④ 범위(Range)"]),

    # ─── 3과목 ───
    ("3과목: 빅데이터 모델링 (21~30번)", None, None),
    (21, "다음 신경망에서 출력값을 계산하시오.\n입력: x₁=1, x₂=2 / 가중치: w₁=0.5, w₂=0.3 / 편향: b=0.1 / 활성화함수: 없음(선형)",
        ["① 1.0", "② 1.2", "③ 1.4", "④ 1.6"]),
    (22, "Vanishing Gradient 문제에 대한 설명으로 옳은 것은?",
        ["① 학습률이 너무 클 때 손실이 발산하는 현상이다",
         "② 시그모이드 함수 사용 시 역전파 과정에서 기울기가 소실되는 현상이다",
         "③ ReLU 함수가 이 문제를 유발한다",
         "④ 클리핑(Clipping)으로 해결할 수 있다"]),
    (23, "앙상블 기법에 대한 설명으로 옳은 것은?",
        ["① 배깅(Bagging)은 순차적으로 약학습기를 학습시킨다",
         "② 부스팅(Boosting)은 병렬로 약학습기를 학습시킨다",
         "③ 배깅은 병렬, 부스팅은 순차 방식이다",
         "④ 배깅과 부스팅 모두 순차 방식이다"]),
    (24, "ARIMA(p, d, q)에서 각 파라미터의 의미를 바르게 연결한 것은?",
        ["① p=차분 횟수, d=AR 차수, q=MA 차수",
         "② p=AR 차수, d=차분 횟수, q=MA 차수",
         "③ p=MA 차수, d=차분 횟수, q=AR 차수",
         "④ p=AR 차수, d=MA 차수, q=차분 횟수"]),
    (25, "의사결정나무의 특성으로 옳은 것은?",
        ["① 모수적 방법으로 정규분포 가정이 필요하다",
         "② 과적합이 발생하지 않는 장점이 있다",
         "③ 비모수적 방법으로 학습 데이터에 과적합되기 쉽다",
         "④ SVM과 달리 초매개변수 최적화가 필요 없다"]),
    (26, "카이제곱 검정의 종류와 목적의 연결이 옳은 것은?",
        ["① 적합도 검정 — 두 집단의 분포가 같은지",
         "② 독립성 검정 — 이론적 분포와 실제 분포가 같은지",
         "③ 동질성 검정 — 두 범주형 변수 간 독립 여부",
         "④ 독립성 검정 — 두 범주형 변수 간 독립 여부"]),
    (27, "다음 고유값을 가진 데이터에서 1~2번째 주성분의 누적 기여율은?\nλ₁=4, λ₂=2, λ₃=1, λ₄=1",
        ["① 50%", "② 62.5%", "③ 75%", "④ 87.5%"]),
    (28, "Transformer 모델에 대한 설명으로 옳지 않은 것은?",
        ["① Self-Attention 메커니즘을 사용한다",
         "② Forget Gate가 핵심 구성요소이다",
         "③ 인코더-디코더 구조를 기본으로 한다",
         "④ 병렬 처리가 가능하여 RNN보다 학습이 빠르다"]),
    (29, "K-means와 K-medoids의 차이에 대한 설명으로 옳은 것은?",
        ["① K-means는 이상치에 강하고 K-medoids는 이상치에 취약하다",
         "② K-medoids는 실제 데이터 포인트를 중심으로 사용하여 이상치에 강하다",
         "③ K-medoids는 연속형 데이터에만 사용 가능하다",
         "④ K-means가 항상 K-medoids보다 정확하다"]),
    (30, "비모수 검정에 대한 설명으로 옳은 것은?",
        ["① Mann-Whitney U 검정은 대응표본 두 집단 비교에 사용한다",
         "② Wilcoxon signed-rank 검정은 독립표본 두 집단 비교에 사용한다",
         "③ Kruskal-Wallis 검정은 세 집단 이상의 비교에 사용하는 비모수 검정이다",
         "④ 비모수 검정은 정규분포 가정이 필요하다"]),

    # ─── 4과목 ───
    ("4과목: 빅데이터 결과 해석 (31~40번)", None, None),
    (31, "다음 혼동행렬에서 Recall(재현율)을 계산하시오.\n실제 양성: 예측 양성 80 / 예측 음성 20\n실제 음성: 예측 양성 10 / 예측 음성 90",
        ["① 0.80", "② 0.85", "③ 0.89", "④ 0.90"]),
    (32, "ROC 곡선의 X축과 Y축으로 옳은 것은?",
        ["① X축: 민감도(TPR), Y축: 1-특이도(FPR)",
         "② X축: 1-특이도(FPR), Y축: 민감도(TPR)",
         "③ X축: 특이도, Y축: 민감도(TPR)",
         "④ X축: 정밀도(Precision), Y축: 재현율(Recall)"]),
    (33, "박스플롯(Box plot)으로 알 수 없는 정보는?",
        ["① 중앙값", "② 사분위수 범위(IQR)", "③ 이상치 존재 여부", "④ 평균"]),
    (34, "카토그램(Cartogram)에 대한 설명으로 옳은 것은?",
        ["① 지리적 면적을 정확히 반영한 지도 시각화",
         "② 통계값의 크기에 따라 지역의 크기를 왜곡하여 표현한 지도",
         "③ 색상의 진하기로 통계값을 표현하는 단계구분도",
         "④ 지역 간 이동 흐름을 화살표로 표현하는 지도"]),
    (35, "편향-분산 트레이드오프에 대한 설명으로 옳은 것은?",
        ["① 복잡한 모델은 편향이 높고 분산이 낮다",
         "② 단순한 모델은 편향이 낮고 분산이 높다",
         "③ 단순한 모델은 편향이 높고 분산이 낮다",
         "④ 복잡한 모델과 단순한 모델의 편향과 분산은 동일하다"]),
    (36, "실루엣(Silhouette) 점수에 대한 설명으로 옳은 것은?",
        ["① 범위는 0~1이며 1에 가까울수록 좋은 군집화이다",
         "② 범위는 -1~1이며 1에 가까울수록 좋은 군집화이다",
         "③ 범위는 -1~1이며 0에 가까울수록 좋은 군집화이다",
         "④ 범위는 0~∞이며 값이 작을수록 좋은 군집화이다"]),
    (37, "다음 중 분류 모델에는 사용할 수 없고 회귀 모델에만 사용 가능한 평가지표는?",
        ["① Accuracy", "② F1 Score", "③ MAPE", "④ AUC"]),
    (38, "과적합(Overfitting)을 방지하는 방법으로 옳지 않은 것은?",
        ["① 훈련 데이터를 늘린다",
         "② 정규화(Regularization)를 적용한다",
         "③ 모델의 복잡도를 낮춘다",
         "④ 훈련 데이터를 줄인다"]),
    (39, "다중공선성(Multicollinearity) 진단에 사용하는 통계량과 판단 기준으로 옳은 것은?",
        ["① AIC > 10이면 다중공선성 있음",
         "② VIF > 10이면 다중공선성 의심",
         "③ VIF < 0.1이면 다중공선성 의심",
         "④ Cook's distance > 4/n이면 다중공선성 있음"]),
    (40, "결정계수(R²)에 대한 설명으로 옳지 않은 것은?",
        ["① 독립변수가 종속변수를 설명하는 비율이다",
         "② 범위는 0~1이다",
         "③ 독립변수를 추가하면 R²은 항상 증가하거나 유지된다",
         "④ 독립변수를 추가할수록 R²은 자동으로 감소한다"]),
]

# 답안 작성란
answer_boxes = []
for i in range(1, 41):
    answer_boxes.append([str(i), "     "])

for item in questions:
    num, q_text, opts = item

    # 과목 헤더
    if isinstance(num, str):
        story.append(Spacer(1, 3*mm))
        story.append(Paragraph(num, subj_style))
        story.append(Spacer(1, 1*mm))
        continue

    # 문제
    q_lines = q_text.split("\n")
    story.append(Paragraph(f"<b>{num}.</b> {q_lines[0]}", q_style))
    for extra in q_lines[1:]:
        story.append(Paragraph(f"    {extra}", opt_style))

    # 선지 2열 배치
    if opts:
        mid = len(opts) // 2
        row1 = opts[:mid]
        row2 = opts[mid:]
        col_w = (W - 40*mm) / 2
        for r1, r2 in zip(row1, row2):
            tbl = Table([[Paragraph(r1, opt_style), Paragraph(r2, opt_style)]],
                        colWidths=[col_w, col_w])
            tbl.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "TOP"),
                                     ("LEFTPADDING", (0,0), (-1,-1), 0),
                                     ("RIGHTPADDING", (0,0), (-1,-1), 4)]))
            story.append(tbl)

    story.append(Spacer(1, 1*mm))

# 답안 작성란
story.append(Spacer(1, 6*mm))
story.append(Paragraph("[ 답안 작성란 ]", subj_style))

rows = []
header = ["번호", "답"] * 5
rows.append(header)
for i in range(8):
    row = []
    for j in range(5):
        idx = i + j*8 + 1
        if idx <= 40:
            row.extend([str(idx), ""])
        else:
            row.extend(["", ""])
    rows.append(row)

col_w2 = (W - 40*mm) / 10
ans_table = Table(rows, colWidths=[col_w2]*10)
ans_table.setStyle(TableStyle([
    ("FONTNAME", (0,0), (-1,-1), "Korean"),
    ("FONTSIZE", (0,0), (-1,-1), 9),
    ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
    ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("ROWBACKGROUND", (0,1), (-1,-1), [colors.white, colors.HexColor("#f9f9f9")]),
    ("ROWHEIGHT", (0,1), (-1,-1), 14),
]))
story.append(ans_table)

doc.build(story)
print("PDF 생성 완료: 모의고사.pdf")
