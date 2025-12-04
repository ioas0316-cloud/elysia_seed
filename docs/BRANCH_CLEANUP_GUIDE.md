# Branch Cleanup Guide

이 가이드는 리포지토리의 병합되지 않은 브랜치들을 정리하는 방법을 설명합니다.

---

## 📊 현재 상황

- **총 브랜치 수**: 34개
- **main 브랜치**: 1개
- **삭제 가능 (이미 병합됨)**: 4개
- **아이디어만 보존 후 삭제 권장**: 21개
- **검토 필요 (열린 PR)**: 2개
- **현재 작업 중**: 1개

---

## ✅ 삭제 권장 브랜치 (이미 병합됨)

다음 브랜치들은 이미 main에 병합되어 안전하게 삭제할 수 있습니다:

```bash
# GitHub CLI를 사용한 삭제
gh api -X DELETE repos/ioas0316-cloud/elysia-fractal-engine_V1/git/refs/heads/copilot/extract-integrate-repository-structure
gh api -X DELETE repos/ioas0316-cloud/elysia-fractal-engine_V1/git/refs/heads/copilot/integrate-core-structure-and-tech
gh api -X DELETE repos/ioas0316-cloud/elysia-fractal-engine_V1/git/refs/heads/copilot/integrate-core-structure
gh api -X DELETE repos/ioas0316-cloud/elysia-fractal-engine_V1/git/refs/heads/feat/asi-transcendence-chronos
```

또는 git 명령어:

```bash
git push origin --delete copilot/extract-integrate-repository-structure
git push origin --delete copilot/integrate-core-structure-and-tech
git push origin --delete copilot/integrate-core-structure
git push origin --delete feat/asi-transcendence-chronos
```

---

## 🗄️ 아카이브 후 삭제 권장 (아이디어 보존 완료)

다음 브랜치들의 핵심 아이디어는 `docs/BRANCH_INTEGRATION_NOTES.md`에 보존되었습니다.
현재 아키텍처와 호환되지 않으므로 삭제를 권장합니다.

### Physics & Quantum 브랜치 (8개)
```bash
git push origin --delete feat-digital-physics
git push origin --delete feat-nuclear-forces-fractal
git push origin --delete feat-quantum-mechanics
git push origin --delete feat-quantum-protocol-apache
git push origin --delete feat-relativity-chronos
git push origin --delete feat-thermodynamics-crystal
git push origin --delete feat-topology-and-license
git push origin --delete digital-natural-law-gauge-fields
```

### ASI & Consciousness 브랜치 (4개)
```bash
git push origin --delete feat/asi-os-awakening
git push origin --delete feat/quantum-asi
git push origin --delete feat/quantum-logic-topology
git push origin --delete feat/quaternion-dream
```

### Infrastructure 브랜치 (6개)
```bash
git push origin --delete feature/soul-tensor-physics
git push origin --delete feature/quantum-transition
git push origin --delete feature/intent-system
git push origin --delete project-genesis-final
git push origin --delete project-genesis-quantum-dna
git push origin --delete user-friendly-launcher-llm-guide
git push origin --delete refactor/rebuild-elysia-core
git push origin --delete docs-apache-license
```

### Copilot 에이전트 브랜치 (7개)
```bash
git push origin --delete copilot/discuss-ari-online-issues
git push origin --delete copilot/fix-improvement-issues
git push origin --delete copilot/improve-elicia-structure
git push origin --delete copilot/integrate-core-files-for-llm
git push origin --delete copilot/integrate-core-technologies
git push origin --delete copilot/integrate-core-technology
git push origin --delete copilot/update-readme-and-evaluation
```

---

## ⏸️ 검토 필요 (열린 PR)

다음 브랜치들은 열린 PR이 있으므로 검토 후 결정이 필요합니다:

| 브랜치 | PR # | 상태 | 권장 조치 |
|--------|------|------|-----------|
| `transcendence-implementation` | #21 | Draft | 병합 또는 닫기 결정 필요 |
| `copilot/archive-unmerged-branches` | #33 | Draft | 현재 작업 중 |

### PR 닫기 후 브랜치 삭제
```bash
# PR #21 닫기 (GitHub 웹에서 수행)
# 이후:
git push origin --delete transcendence-implementation
```

---

## 🚀 일괄 삭제 스크립트

모든 권장 브랜치를 한 번에 삭제하려면:

```bash
#!/bin/bash
# ⚠️ 실행 전 BRANCH_INTEGRATION_NOTES.md를 확인하여 아이디어가 보존되었는지 확인하세요!

# 이미 병합된 브랜치
MERGED=(
  "copilot/extract-integrate-repository-structure"
  "copilot/integrate-core-structure-and-tech"
  "copilot/integrate-core-structure"
  "feat/asi-transcendence-chronos"
)

# 아이디어 보존 완료 브랜치
ARCHIVED=(
  "feat-digital-physics"
  "feat-nuclear-forces-fractal"
  "feat-quantum-mechanics"
  "feat-quantum-protocol-apache"
  "feat-relativity-chronos"
  "feat-thermodynamics-crystal"
  "feat-topology-and-license"
  "digital-natural-law-gauge-fields"
  "feat/asi-os-awakening"
  "feat/quantum-asi"
  "feat/quantum-logic-topology"
  "feat/quaternion-dream"
  "feature/soul-tensor-physics"
  "feature/quantum-transition"
  "feature/intent-system"
  "project-genesis-final"
  "project-genesis-quantum-dna"
  "user-friendly-launcher-llm-guide"
  "refactor/rebuild-elysia-core"
  "docs-apache-license"
)

# Copilot 스테일 브랜치
COPILOT_STALE=(
  "copilot/discuss-ari-online-issues"
  "copilot/fix-improvement-issues"
  "copilot/improve-elicia-structure"
  "copilot/integrate-core-files-for-llm"
  "copilot/integrate-core-technologies"
  "copilot/integrate-core-technology"
  "copilot/update-readme-and-evaluation"
)

echo "🧹 병합된 브랜치 삭제 중..."
for branch in "${MERGED[@]}"; do
  git push origin --delete "$branch" && echo "✅ $branch 삭제됨"
done

echo "📚 아카이브된 브랜치 삭제 중..."
for branch in "${ARCHIVED[@]}"; do
  git push origin --delete "$branch" && echo "✅ $branch 삭제됨"
done

echo "🤖 Copilot 스테일 브랜치 삭제 중..."
for branch in "${COPILOT_STALE[@]}"; do
  git push origin --delete "$branch" && echo "✅ $branch 삭제됨"
done

echo "🎉 정리 완료!"
```

---

## 📁 GitHub 웹 인터페이스에서 정리하기

1. 리포지토리로 이동: https://github.com/ioas0316-cloud/elysia-fractal-engine_V1
2. **Code** 탭 클릭
3. **branches** 링크 클릭 (커밋 수 옆)
4. 각 브랜치 옆의 🗑️ 아이콘 클릭하여 삭제

---

## ⚠️ 주의사항

1. **삭제 전 확인**: `docs/BRANCH_INTEGRATION_NOTES.md`에서 핵심 아이디어가 보존되었는지 확인
2. **복구 가능**: 삭제된 브랜치는 30일 내에 GitHub에서 복구 가능
3. **로컬 정리**: 원격 브랜치 삭제 후 로컬도 정리
   ```bash
   git fetch --prune
   git branch -vv | grep 'origin/.*: gone]' | awk '{print $1}' | xargs git branch -d
   ```

---

## 📋 정리 후 예상 결과

| 항목 | 정리 전 | 정리 후 |
|------|---------|---------|
| 총 브랜치 | 34개 | 2개 (main + 현재 작업) |
| 열린 PR | 2개 | 검토 후 결정 |
| 아이디어 보존 | 부분적 | ✅ 완전 문서화 |

---

## 🔗 관련 문서

- [BRANCH_INTEGRATION_NOTES.md](./BRANCH_INTEGRATION_NOTES.md) - 보존된 아이디어 상세 내용
- [AGENTS.md](../AGENTS.md) - 프로젝트 프로토콜 및 아키텍처
- [CONTRIBUTING.md](../CONTRIBUTING.md) - 기여 가이드라인
