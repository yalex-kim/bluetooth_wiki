# Bluetooth Spec Wiki

> Bluetooth Core Specification knowledge base for LLMs — based on [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

Claude Code에서 Bluetooth Core Spec 관련 질문에 정확하고 출처 있는 답변을 제공하기 위한 위키입니다.
Core Spec 5.0부터 6.2까지 버전별 요약, 버전 간 차이점 인덱스, 핵심 개념 페이지를 포함합니다.
모든 버전의 공식 PDF와 변환된 마크다운 소스가 포함되어 있으며, 실제 스펙 문서에서 추출한 정확한 인용(`[Core 6.2, Vol 6, Part B, §4.6.50]`)을 제공합니다.

---

## 빠른 시작

```bash
git clone https://github.com/yalex-kim/bluetooth_wiki.git
cd bluetooth_wiki
claude
```

```
> Bluetooth 6.0에서 Channel Sounding이 뭐야?
> 5.1에서 5.2로 넘어가면서 뭐가 바뀌었어?
> LE Audio와 Classic Bluetooth 오디오의 차이점은?
> PAwR은 어떤 용도로 쓰여?
```

---

## 구조

```
bluetooth_wiki/
├── CLAUDE.md                    ← LLM 동작 방식 정의 (wiki 스키마)
├── index.md                     ← 전체 페이지 카탈로그 + 쿼리 라우팅 가이드
├── log.md                       ← append-only 활동 로그
│
├── wiki/
│   ├── overview.md              ← Bluetooth 기술 개요
│   ├── versions/                ← Core Spec 버전별 요약 (5.0–6.0)
│   ├── version-diff/            ← 버전 간 차이점 사전 인덱싱
│   └── concepts/                ← BLE 아키텍처, 보안, 프로파일 등 개념 페이지
│
├── sources/
│   ├── README.md                ← PDF 다운로드 방법
│   └── specs/                   ← bluetooth.com PDF + 변환된 .md 저장 위치
│
├── scripts/
│   ├── download_specs.sh        ← bluetooth.com에서 PDF 자동 다운로드
│   ├── convert_to_md.py         ← OpenDataLoader로 PDF → Markdown 변환
│   └── ingest.py                ← 변환된 spec을 wiki에 반영하는 워크플로우
│
└── guide/
    └── claude-code-integration.md  ← Claude Code 연결 가이드
```

---

## 커버리지

| 버전 | 출시일 | 핵심 기능 | 소스 |
|------|--------|----------|------|
| [5.0](wiki/versions/core-spec-5.0.md) | 2016-12 | 2× 속도 (LE 2M PHY), 4× 범위 (Coded PHY), 8× 브로드캐스트 | PDF + MD ✓ |
| [5.1](wiki/versions/core-spec-5.1.md) | 2019-01 | Direction Finding (AoA/AoD), GATT 캐싱 | PDF + MD ✓ |
| [5.2](wiki/versions/core-spec-5.2.md) | 2019-12 | LE Audio, LC3 코덱, Isochronous Channels (CIS/BIS), EATT | PDF + MD ✓ |
| [5.3](wiki/versions/core-spec-5.3.md) | 2021-07 | Connection Subrating, Enhanced Connection Update | PDF + MD ✓ |
| [5.4](wiki/versions/core-spec-5.4.md) | 2023-02 | PAwR, Encrypted Advertising Data (EAD) | PDF + MD ✓ |
| [6.0](wiki/versions/core-spec-6.0.md) | 2024-08 | Channel Sounding (정밀 거리측정), DBAF | PDF + MD ✓ |
| [6.1](wiki/versions/core-spec-6.1.md) | 2025-04 | Randomized RPA Updates (BLE 프라이버시 강화) | PDF + MD ✓ |
| [6.2](wiki/versions/core-spec-6.2.md) | 2025-11 | Shorter Connection Intervals (375 µs), LE UTP, CS 보안 강화 | PDF + MD ✓ |

버전 간 차이점: [5.0→5.1](wiki/version-diff/diff-5.0-to-5.1.md) · [5.1→5.2](wiki/version-diff/diff-5.1-to-5.2.md) · [5.2→5.3](wiki/version-diff/diff-5.2-to-5.3.md) · [5.3→5.4](wiki/version-diff/diff-5.3-to-5.4.md) · [5.4→6.0](wiki/version-diff/diff-5.4-to-6.0.md) · [6.0→6.1](wiki/version-diff/diff-6.0-to-6.1.md) · [6.1→6.2](wiki/version-diff/diff-6.1-to-6.2.md)

---

## 새 버전 추가하기

새 Core Spec이 출시되면:

```bash
# 1. bluetooth.com에서 PDF 다운로드 후 sources/specs/X.Y/ 폴더에 정리

# 2. OpenDataLoader로 Markdown 변환 (Java 필요)
pip install -U opendataloader-pdf
python scripts/convert_to_md.py X.Y

# 3. 상태 확인
python scripts/ingest.py --status

# 4. Claude Code에서 INGEST 실행
claude
> Core Spec X.Y를 sources/specs/core-spec-X.Y.md 기반으로 wiki에 ingest해줘
```

---

## 다른 프로젝트에서 연결하기

`~/.claude/claude.json`에 MCP Filesystem 서버로 등록하면 모든 프로젝트에서 사용 가능합니다:

```json
{
  "mcpServers": {
    "bluetooth-wiki": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/bluetooth_wiki"]
    }
  }
}
```

자세한 내용: [guide/claude-code-integration.md](guide/claude-code-integration.md)

---

## 아키텍처

[Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 패턴의 3계층 구조:

```
Layer 1  sources/specs/   원본 PDF + 변환된 .md (읽기 전용, LLM이 수정 불가)
Layer 2  wiki/            LLM이 유지하는 요약/분석 마크다운 페이지
Layer 3  CLAUDE.md        스키마: LLM이 wiki를 어떻게 관리할지 정의
```

`CLAUDE.md`는 Claude에게 3가지 오퍼레이션을 지시합니다:
- **INGEST**: 새 spec을 읽고 wiki 페이지들을 업데이트
- **QUERY**: 질문에 답하고 필요시 새 페이지 생성
- **LINT**: wiki 일관성 검사 (outdated 정보, broken links, 모순 탐지)
