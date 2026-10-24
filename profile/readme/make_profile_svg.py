"""조직 프로필 README용 애니메이션 SVG (다크, 라이트 두 벌)

실행 (저장소 루트에서):
    python profile/readme/make_profile_svg.py

- 외부 도구 없이 문자열로 SVG를 씀. 애니메이션은 SVG 표준(SMIL)이라 GitHub에서 그대로 움직임
- 양각(올라온 판), 음각(파인 홈), 겹친 도형으로 입체감을 냄. 스타일 부품은 pdm-project figures/readme/make_readme_svg.py와 같음
- 만드는 파일: hero, repos (각각 -dark.svg, -light.svg)
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = "Pretendard, 'Apple SD Gothic Neo', 'Malgun Gothic', 'Noto Sans KR', sans-serif"

THEMES = {
    "dark": {"bg": "#0d110e", "bg2": "#161d17", "plate": "#1a231c", "plate2": "#212c23", "deep": "#080b09",
             "ink": "#eef4ec", "sub": "#9fb39d", "accent": "#a8ff3e", "warm": "#ffb347", "hot": "#ff5a5f", "cool": "#5ec8ff",
             "hi": "#ffffff", "lo": "#000000", "hi_a": "0.10", "lo_a": "0.55", "shadow_a": "0.45", "grain_a": "0.05"},
    "light": {"bg": "#eef1ea", "bg2": "#e4e9df", "plate": "#f7f9f4", "plate2": "#eef2ea", "deep": "#d9dfd4",
              "ink": "#17221b", "sub": "#5b6b5d", "accent": "#3f8f1a", "warm": "#d9741a", "hot": "#d8323a", "cool": "#1f7fb8",
              "hi": "#ffffff", "lo": "#1a2a1e", "hi_a": "0.9", "lo_a": "0.18", "shadow_a": "0.18", "grain_a": "0.06"},
}


# ---------------------------------------------------------------- 공통 부품
def defs(t):
    return (
        '<defs>\n'
        '<filter id="shadow" x="-10%%" y="-10%%" width="120%%" height="140%%"><feDropShadow dx="0" dy="8" stdDeviation="8" flood-color="#000" flood-opacity="%s"/></filter>\n'
        '<filter id="shadow-sm" x="-10%%" y="-10%%" width="120%%" height="140%%"><feDropShadow dx="0" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="%s"/></filter>\n'
        '<filter id="inset" x="-10%%" y="-10%%" width="120%%" height="130%%">'
        '<feOffset dx="0" dy="3"/><feGaussianBlur stdDeviation="3" result="ob"/>'
        '<feComposite operator="out" in="SourceGraphic" in2="ob" result="inv"/>'
        '<feFlood flood-color="#000" flood-opacity="0.55" result="col"/>'
        '<feComposite operator="in" in="col" in2="inv" result="sh"/>'
        '<feComposite operator="over" in="sh" in2="SourceGraphic"/></filter>\n'
        '<filter id="glow" x="-50%%" y="-50%%" width="200%%" height="200%%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>\n'
        '<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 0.5  0 0 0 0 0.5  0 0 0 0 0.5  0 0 0 0.6 0"/></filter>\n'
        '<linearGradient id="plate" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>\n'
        '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>\n'
        '<radialGradient id="coin" cx="0.35" cy="0.3" r="0.8"><stop offset="0" stop-color="%s" stop-opacity="0.9"/><stop offset="0.55" stop-color="%s" stop-opacity="0"/><stop offset="1" stop-color="%s" stop-opacity="0.35"/></radialGradient>\n'
        '</defs>\n' % (t["shadow_a"], t["shadow_a"], t["plate"], t["plate2"], t["bg"], t["bg2"], t["hi"], t["hi"], t["lo"]))


def head(width, height, t):
    s = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="%s">\n'
         % (width, height, width, height, FONT))
    s += defs(t)
    s += '<rect width="%d" height="%d" rx="22" fill="url(#bg)"/>\n' % (width, height)
    s += '<rect width="%d" height="%d" rx="22" filter="url(#grain)" opacity="%s"/>\n' % (width, height, t["grain_a"])
    return s


def text(x, y, s, size, fill, weight="normal", anchor="start", extra=""):
    return '<text x="%s" y="%s" font-size="%s" fill="%s" font-weight="%s" text-anchor="%s" %s>%s</text>\n' % (
        x, y, size, fill, weight, anchor, extra, s)


def emboss_text(t, x, y, s, size, fill, weight="bold", anchor="start"):
    """글자를 양각처럼: 아래 그림자, 위 하이라이트, 본글자 세 겹"""
    out = text(x + 1, y + 2, s, size, t["lo"], weight, anchor, 'opacity="%s"' % t["lo_a"])
    out += text(x - 1, y - 1, s, size, t["hi"], weight, anchor, 'opacity="%s"' % t["hi_a"])
    out += text(x, y, s, size, fill, weight, anchor)
    return out


def raised(t, x, y, w, h, r=16, fill="url(#plate)", back=True, edge=None):
    """올라온 판: 뒤에 어긋난 판 한 겹, 그림자, 윗변 하이라이트, 아랫변 그늘"""
    s = ""
    if back:
        s += '<rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="%s" opacity="0.55"/>\n' % (x + 10, y + 12, w, h, r, t["deep"])
    s += '<rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="%s" filter="url(#shadow)"/>\n' % (x, y, w, h, r, fill)
    if edge:
        s += '<rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="none" stroke="%s" stroke-opacity="0.55" stroke-width="1.5"/>\n' % (x, y, w, h, r, edge)
    s += '<path d="M %d %d L %d %d Q %d %d %d %d L %d %d" fill="none" stroke="%s" stroke-opacity="%s" stroke-width="1.5"/>\n' % (
        x + 1, y + h - r, x + 1, y + r, x + 1, y + 1, x + r, y + 1, x + w - r, y + 1, t["hi"], t["hi_a"])
    s += '<path d="M %d %d L %d %d Q %d %d %d %d L %d %d" fill="none" stroke="%s" stroke-opacity="%s" stroke-width="1.5"/>\n' % (
        x + r, y + h - 1, x + w - r, y + h - 1, x + w - 1, y + h - 1, x + w - 1, y + h - r, x + w - 1, y + r, t["lo"], t["lo_a"])
    return s


def inset(t, x, y, w, h, r=12, fill=None):
    """파인 홈(음각): 안쪽 그림자 필터, 아랫변 하이라이트"""
    fill = fill or t["deep"]
    s = '<rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="%s" filter="url(#inset)"/>\n' % (x, y, w, h, r, fill)
    s += '<path d="M %d %d L %d %d" stroke="%s" stroke-opacity="%s" stroke-width="1.5"/>\n' % (x + r, y + h + 1, x + w - r, y + h + 1, t["hi"], t["hi_a"])
    return s


def coin(t, cx, cy, r, fill, extra=""):
    """볼록한 단추: 색 원 + 하이라이트 원 + 그림자"""
    s = '<circle cx="%d" cy="%d" r="%d" fill="%s" filter="url(#shadow-sm)"%s/>\n' % (cx, cy, r, fill, extra)
    s += '<circle cx="%d" cy="%d" r="%d" fill="url(#coin)"/>\n' % (cx, cy, r)
    return s


def pipe(t, x1, x2, y, col, label="", dur=1.6):
    """연결 관: 파인 홈 속을 빛 덩이가 지나가고 끝에 화살촉. label은 무엇이 흐르는지"""
    s = inset(t, x1, y - 8, x2 - x1 - 10, 16, 8)
    s += '<polygon points="%d,%d %d,%d %d,%d" fill="%s" filter="url(#shadow-sm)"/>\n' % (x2 - 14, y - 11, x2, y, x2 - 14, y + 11, col)
    for begin in [0, dur / 2]:
        s += ('<rect x="%d" y="%d" width="26" height="8" rx="4" fill="%s" filter="url(#glow)" opacity="0">'
              '<animate attributeName="x" from="%d" to="%d" dur="%ss" begin="%ss" repeatCount="indefinite"/>'
              '<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.15;0.85;1" dur="%ss" begin="%ss" repeatCount="indefinite"/></rect>\n'
              % (x1 + 2, y - 4, col, x1 + 2, x2 - 40, dur, begin, dur, begin))
    if label:
        s += text((x1 + x2) / 2 - 5, y - 16, label, 11, t["sub"], anchor="middle")
    return s


def curve_pipe(t, d, col, label="", lx=0, ly=0, dur=2.4, begin=0):
    """굽은 관: 홈 선 위로 캡슐이 경로(d)를 따라 감. 화살촉은 호출 쪽에서 붙임"""
    s = '<path d="%s" fill="none" stroke="%s" stroke-opacity="%s" stroke-width="10" stroke-linecap="round"/>\n' % (d, t["lo"], t["lo_a"])
    s += '<path d="%s" fill="none" stroke="%s" stroke-opacity="%s" stroke-width="3" stroke-linecap="round"/>\n' % (d, t["hi"], t["hi_a"])
    s += '<path d="%s" fill="none" stroke="%s" stroke-opacity="0.35" stroke-width="2"/>\n' % (d, col)
    s += ('<rect x="-14" y="-4" width="28" height="8" rx="4" fill="%s" filter="url(#glow)">'
          '<animateMotion dur="%ss" begin="%ss" repeatCount="indefinite" rotate="auto" path="%s"/></rect>\n' % (col, dur, begin, d))
    if label:
        s += text(lx, ly, label, 11.5, col, "bold", "middle")
    return s


def up_arrow(t, x, y, col):
    return '<polygon points="%d,%d %d,%d %d,%d" fill="%s" filter="url(#shadow-sm)"/>\n' % (x - 9, y + 10, x + 9, y + 10, x, y - 4, col)


def pill(t, x, y, label, col, size=14):
    w = 26 + len(label) * size * 0.68
    s = raised(t, x, y, w, 36, 18, back=False, edge=col)
    s += coin(t, x + 18, y + 18, 7, col)
    s += text(x + 34, y + 23, label, size, t["ink"])
    return s, w


def layered_decor(t, x, y, r, col):
    """뒤에 겹쳐 둔 원 세 개 (종이를 포갠 느낌)"""
    s = ""
    for i, op in enumerate(["0.05", "0.08", "0.12"]):
        s += '<circle cx="%d" cy="%d" r="%d" fill="%s" opacity="%s"/>\n' % (x - i * 26, y + i * 18, r - i * 28, col, op)
    return s


def write(name, theme, body):
    path = os.path.join(HERE, "%s-%s.svg" % (name, theme))
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)
    print("wrote", os.path.relpath(path))


# ---------------------------------------------------------------- 1. 머리 배너: 세 정거장을 도는 한 바퀴
def hero(theme):
    t = THEMES[theme]
    W, H = 1200, 444
    s = head(W, H, t)
    s += layered_decor(t, 1060, 90, 190, t["accent"])
    s += layered_decor(t, 210, 430, 150, t["cool"])
    s += text(56, 78, "POSCO K-NEWDEAL ACADEMY · TEAM 3 오운완", 15, t["sub"], extra='letter-spacing="3"')
    s += emboss_text(t, 56, 134, "연속 소둔로 CAL01의 이상을 찾고,", 40, t["ink"])
    s += emboss_text(t, 56, 186, "팀이 같은 근거로 판단함", 40, t["accent"])
    s += text(56, 226, "분석 → 공동 검토 → 관제. 저장소 세 개가 한 바퀴를 돌며 정답과 모델을 다듬음", 16, t["sub"])

    x = 56
    for label, col in [("LOT 14개 · 센서 21개 · 2024년 한 해", t["cool"]), ("정답 v1 → v7 · 검토 표 395행", t["warm"]),
                       ("Z4 F1 0.60 Z-score · 0.59 RandomForest", t["accent"])]:
        piece, w = pill(t, x, 250, label, col)
        s += piece
        x += w + 14

    # 바퀴: 길쭉한 고리 홈을 캡슐 두 개가 돌고, 정거장 판 세 개 뒤로 지나감
    left, right, top, bottom = 110, 1090, 330, 386
    r = (bottom - top) / 2
    d = "M %d %d H %d A %d %d 0 0 1 %d %d H %d A %d %d 0 0 1 %d %d Z" % (left, top, right, r, r, right, bottom, left, r, r, left, top)
    s += inset(t, left - 40, top - 22, right - left + 80, bottom - top + 44, 26)
    s += curve_pipe(t, d, t["accent"], dur=9)
    s += curve_pipe(t, d, t["warm"], dur=9, begin=4.5)
    stations = [("분석", "pdm-project", t["accent"], 300), ("공동 검토", "cal01-review", t["warm"], 600), ("관제", "cal01-monitor", t["cool"], 900)]
    for role, repo, col, cx in stations:
        pw, ph = 236, 52
        px, py = cx - pw / 2, top - ph / 2 + 2
        s += raised(t, px, py, pw, ph, 14, back=False, edge=col)
        s += coin(t, px + 24, py + ph / 2, 8, col)
        s += emboss_text(t, px + 42, py + 23, role, 15, t["ink"])
        s += text(px + 42, py + 41, repo, 12, col)
    s += text(600, bottom + 42, "후보 → 팀 판단 → 검토 표 → 다음 정답 → 모델 → 관제, 그리고 다시 후보", 12, t["sub"], anchor="middle")
    s += "</svg>\n"
    write("hero", theme, s)


# ---------------------------------------------------------------- 2. 세 저장소
def repos(theme):
    t = THEMES[theme]
    W, H = 1200, 404
    s = head(W, H, t)
    s += layered_decor(t, 1120, 40, 150, t["cool"])
    s += emboss_text(t, 56, 48, "저장소 세 개가 한 바퀴로 이어짐", 20, t["ink"])
    cards = [("pdm-project", "분석 저장소", ["노트북으로 정답 v1 → v7을 만듦", "Z-score, IF, RF를 같은 조건에서 비교", "관제용 모델을 registry에 저장"], t["accent"]),
             ("cal01-review", "공동 검토 사이트", ["후보를 LOT 그래프 위에 띄움", "팀이 1, 0, 보류와 메모를 남김", "판단을 검토 표 CSV로 내보냄"], t["warm"]),
             ("cal01-monitor", "소둔로 관제", ["3D 소둔로와 채널 그래프", "Z-score 경보와 현장 확인 요청", "구역별 모델을 레지스트리에서 읽음"], t["cool"])]
    cw, ch, y0 = 320, 196, 78
    xs = [56, 440, 824]
    for (title, sub, lines, col), x in zip(cards, xs):
        s += raised(t, x, y0, cw, ch, 18)
        s += '<rect x="%d" y="%d" width="10" height="%d" rx="5" fill="%s" filter="url(#shadow-sm)"/>\n' % (x + 16, y0 + 18, ch - 36, col)
        s += '<rect x="%d" y="%d" width="3" height="%d" rx="1.5" fill="%s" opacity="0.5"/>\n' % (x + 18, y0 + 22, ch - 44, t["hi"])
        s += emboss_text(t, x + 42, y0 + 46, title, 22, t["ink"])
        s += text(x + 42, y0 + 70, sub, 14, col)
        s += inset(t, x + 38, y0 + 86, cw - 56, 92, 10)
        for i, line in enumerate(lines):
            s += coin(t, x + 54, y0 + 106 + i * 28, 4, col)
            s += text(x + 66, y0 + 111 + i * 28, line, 13, t["ink"])
    s += pipe(t, 376, 440, y0 + 100, t["warm"], "후보 (3σ, 모델)")
    s += pipe(t, 760, 824, y0 + 100, t["cool"], "팀 판단")
    d1 = "M 600 %d C 600 %d, 216 %d, 216 %d" % (y0 + ch + 2, y0 + ch + 50, y0 + ch + 50, y0 + ch + 4)
    s += curve_pipe(t, d1, t["warm"], "검토 표 → 다음 정답", 408, y0 + ch + 72)
    s += up_arrow(t, 216, y0 + ch - 2, t["warm"])
    d2 = "M 300 %d C 300 %d, 984 %d, 984 %d" % (y0 + ch + 2, y0 + ch + 96, y0 + ch + 96, y0 + ch + 4)
    s += curve_pipe(t, d2, t["accent"], "모델 registry", 642, y0 + ch + 116, dur=3.2)
    s += up_arrow(t, 984, y0 + ch - 2, t["accent"])
    s += "</svg>\n"
    write("repos", theme, s)


if __name__ == "__main__":
    for theme in THEMES:
        hero(theme)
        repos(theme)
