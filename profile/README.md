<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="readme/hero-dark.svg">
  <img alt="포스코 K-뉴딜 아카데미 3조 오운완: 연속 소둔로 CAL01의 이상을 찾고 팀이 같은 근거로 판단함. 분석, 공동 검토, 관제 세 정거장을 도는 한 바퀴" src="readme/hero-light.svg" width="100%">
</picture>

[![CI](https://github.com/posco-3bungi-pdm/pdm-project/actions/workflows/ci.yml/badge.svg)](https://github.com/posco-3bungi-pdm/pdm-project/actions/workflows/ci.yml)
[![정답](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fposco-3bungi-pdm%2Fpdm-project%2Fmain%2Ffigures%2Freadme%2Fmetrics.json&query=%24.label_version&label=%EC%A0%95%EB%8B%B5&color=5ec8ff&style=flat-square&labelColor=0b0f0c)](https://github.com/posco-3bungi-pdm/pdm-project#정답을-일곱-번-다듬음-v1--v7)
[![Z4 F1 (Z-score)](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fposco-3bungi-pdm%2Fpdm-project%2Fmain%2Ffigures%2Freadme%2Fmetrics.json&query=%24.z4.zscore_f1&label=Z4%20F1%20%28Z-score%29&color=ffb347&style=flat-square&labelColor=0b0f0c)](https://github.com/posco-3bungi-pdm/pdm-project#결과)
[![Z4 F1 (RandomForest)](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fposco-3bungi-pdm%2Fpdm-project%2Fmain%2Ffigures%2Freadme%2Fmetrics.json&query=%24.z4.rf_f1&label=Z4%20F1%20%28RandomForest%29&color=a8ff3e&style=flat-square&labelColor=0b0f0c)](https://github.com/posco-3bungi-pdm/pdm-project#결과)

[![관제 CAL01 Monitor](https://img.shields.io/website?url=https%3A%2F%2Fcal01-monitor.onrender.com%2Findex.html&label=%EA%B4%80%EC%A0%9C%20CAL01%20Monitor&up_message=%EC%BC%9C%EC%A7%90&down_message=%EC%9E%A0%EB%93%A6&up_color=a8ff3e&down_color=6b7280&logo=render&logoColor=white&style=flat-square&labelColor=0b0f0c)](https://cal01-monitor.onrender.com/)
[![공동 검토 cal01-review](https://img.shields.io/website?url=https%3A%2F%2Fcal01-review.onrender.com%2Fhealth&label=%EA%B3%B5%EB%8F%99%20%EA%B2%80%ED%86%A0%20cal01-review&up_message=%EC%BC%9C%EC%A7%90&down_message=%EC%9E%A0%EB%93%A6&up_color=ffb347&down_color=6b7280&logo=render&logoColor=white&style=flat-square&labelColor=0b0f0c)](https://cal01-review.onrender.com/)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=python,sklearn,jupyter,django,react,ts,vite,threejs,electron,flask,postgres,docker,git,github&theme=dark">
  <img alt="쓴 기술: Python, scikit-learn, Jupyter, Django, React, TypeScript, Vite, three.js, Electron, Flask, PostgreSQL, Docker, Git, GitHub" src="https://skillicons.dev/icons?i=python,sklearn,jupyter,django,react,ts,vite,threejs,electron,flask,postgres,docker,git,github&theme=light" height="40">
</picture>

</div>

포스코 K-뉴딜 아카데미 3조 **오운완**의 설비 고장 예측 프로젝트임. 연속 소둔로(CAL01) 한 대의 2024년 센서 기록에서 이상 후보를 찾음. 팀이 같은 그래프를 보며 판단한 정답으로 모델을 시험한 뒤, 그 결과를 관제 화면까지 이어 붙임. 데이터는 교육용 재현 데이터이며 실제 조업 데이터가 아님.

## 저장소 세 개, 한 바퀴

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="readme/repos-dark.svg">
  <img alt="분석 저장소에서 정답과 모델을 만들고, 검토 사이트에서 팀이 판단하고, 관제가 모델을 읽는 흐름" src="readme/repos-light.svg" width="100%">
</picture>

| 저장소 | 하는 일 | 바로 가기 |
| --- | --- | --- |
| [pdm-project](https://github.com/posco-3bungi-pdm/pdm-project) | 정답 만들기(v1 → v7), 모델 비교, 관제용 모델 저장. 데이터·정답·결과 설명은 여기에 다 있음 | [README](https://github.com/posco-3bungi-pdm/pdm-project#readme) · [작업 목록](https://github.com/posco-3bungi-pdm/pdm-project/issues) · [프로젝트 보드](https://github.com/orgs/posco-3bungi-pdm/projects/1) |
| [cal01-review](https://github.com/posco-3bungi-pdm/cal01-review) | 3σ 후보와 모델 후보를 LOT 그래프 위에 띄우고 팀이 1, 0, 보류를 남김 | [사이트](https://cal01-review.onrender.com/) · [README](https://github.com/posco-3bungi-pdm/cal01-review#readme) |
| [cal01-monitor](https://github.com/posco-3bungi-pdm/cal01-monitor) | 3D 소둔로, Z-score 경보, 현장 확인 요청, 구역별 모델 레지스트리 | [사이트](https://cal01-monitor.onrender.com/) · [README](https://github.com/posco-3bungi-pdm/cal01-monitor#readme) |

## 바로 보기

<table>
<tr>
<th width="50%">관제 · CAL01 Monitor</th>
<th width="50%">공동 검토 · cal01-review</th>
</tr>
<tr>
<td><img alt="관제 화면: 3D 소둔로, 홀로그램, 기록 재생, 구역 확대, 채널 그래프, 과거 LOT 이상 후보, 팀 확인 요청" src="https://raw.githubusercontent.com/posco-3bungi-pdm/pdm-project/main/figures/readme/monitor.gif" width="100%"></td>
<td><img alt="검토 화면: LOT 고르기, 후보 목록과 그래프, 판단 메모, 채널 선택, 팀원 기록, LOT 나란히 비교" src="https://raw.githubusercontent.com/posco-3bungi-pdm/pdm-project/main/figures/readme/review.gif" width="100%"></td>
</tr>
</table>

두 사이트 모두 팀 계정으로 들어감. 무료 서버라 15분 동안 쓰지 않으면 잠들고 다시 열 때 1분쯤 걸림.

## 지금까지

| 무엇 | 얼마나 |
| --- | --- |
| 데이터 | LOT 14개, 센서 21개, 원기록 345,390행 → 1분 5,938행 |
| 정답 | v1 → v7. 3σ 통계 후보를 팀 판단 33건, 전 구역 검토 81건, 모델 후보 60건, 규칙 2개로 다듬음 |
| 모델 | Dummy, Z-score, IsolationForest, RandomForest × 구역 9개, 시험 LOT 10개 |
| 결과 | 팀 판단이 있는 Z4에서 Z-score 0.60, RandomForest 0.59. 자세한 표는 [pdm-project 결과](https://github.com/posco-3bungi-pdm/pdm-project#결과) |

## 일하는 방식

**Issue → 작업 브랜치 → PR → CI → 동료 3명 승인 → Squash merge**

- 목적과 완료 기준을 Issue에 남김
- 원본 데이터, CSV, 모델 파일, 비밀값은 올리지 않음
- 시간 순서로 나누고 통계와 전처리는 지나간 값에만 적용함
- 단순 기준선(Z-score)과 모델을 같은 조건에서 비교함
- 팀이 확정한 정답이 없는 구역에서는 F1을 주장하지 않음

자세한 규칙은 [참여 안내](https://github.com/posco-3bungi-pdm/.github/blob/main/CONTRIBUTING.md)와 [pdm-project CONTRIBUTING](https://github.com/posco-3bungi-pdm/pdm-project/blob/main/CONTRIBUTING.md)에 있음.

## 팀

3조 오운완: 김태구(팀장), 김정렬, 박민호, 정수진, 황유진

교육 프로젝트를 위한 팀 조직임. 특정 기업의 공식 서비스나 운영 시스템이 아님.
