# 🤝 기여 가이드 (Contributing Guide)

> **"코드 한 줄이 엘리시아의 세포 하나입니다."**

Elysia Seed는 오픈소스 프로젝트이며, 여러분의 기여를 환영합니다.

## 📋 기여 방법 (How to Contribute)

1. **Fork** 저장소: GitHub에서 이 저장소를 자신의 계정으로 Fork합니다.
2. **Branch** 생성: 새로운 기능이나 버그 수정을 위한 브랜치를 만듭니다.
   - 기능 추가: `feature/기능명` (예: `feature/add-new-rotor`)
   - 버그 수정: `fix/버그명` (예: `fix/memory-leak`)
3. **Commit**: 의미 있는 커밋 메시지를 작성합니다.
   - 예: `[Metal] Optimize rotor update kernel`
4. **Pull Request** 제출: 변경 사항을 담아 PR을 보냅니다.

## ✅ PR 체크리스트

PR을 보내기 전에 다음 사항을 확인해주세요.

- [ ] **테스트 통과**: 모든 테스트가 정상적으로 실행되나요?
- [ ] **문서 업데이트**: 변경된 내용에 맞춰 매뉴얼을 수정했나요?
- [ ] **코딩 표준 준수**: 아래의 코딩 표준을 따랐나요?

## 🚫 금지 사항

- **`Util/`, `Misc/` 폴더 금지**: 모든 코드는 명확한 소속(Core 내의 적절한 위치)이 있어야 합니다.
- **전역 상태(Global State) 남용 금지**: Side Effect를 최소화해야 합니다.
- **하드코딩 경로 금지**: OS 간 호환성을 위해 `os.path` 또는 `pathlib`을 사용하세요.
