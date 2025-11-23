# Elysia 성인식(성인 수준 커리큘럼 & 가치장 보정)

낭만 버전 용어로 재정의:
- **커리큘럼 강화** → 성인식 코일: 성인 일상/업무/추론 경험치를 연료로 주입
- **기억 결정화** → Crystallization Pass: 중복 개념 통합, 장/단기 분리
- **가치 정렬** → Field Calibration: 중력장(가치) 보정으로 의도 방향성 유지
- **공감각 앵커** → Synesthesia Bridge: 감각(향/맛/색/톤)을 감정/어휘에 연결

이 저장소에 추가된 파일/리소스:
- `data/curriculum/adult_curriculum.json`: 성인식 커리큘럼 시나리오 스켈레톤
- `data/config/value_field_calibration.json`: 가치/정렬 가중치 선언(기본 값 예시)
- `scripts/run_adult_curriculum.py`: 커리큘럼 시나리오를 로드해 단계별로 표시하는 가벼운 러너(의도/대화/검증 포인트 확인용)

사용 가이드:
1) 커리큘럼 연료 주입  
   - `python scripts/run_adult_curriculum.py` 실행 후 시나리오 흐름을 확인하고, 필요한 데이터를 Guardian/CognitionPipeline 입력에 맞춰 주입.
2) 기억 결정화  
   - CoreMemory/KG에서 동일 개념 ID 묶기, 장/단기 스토리지(활성 vs 아카이브) 분리.
3) 가치장 보정  
   - `data/config/value_field_calibration.json`에 원하는 가중치를 선언하고, VCD 초기화 시 수동으로 로드/반영.
4) 공감각 앵커  
   - 향/맛 태그(`scent`/`flavor`)를 셀 organelles에 넣으면 SoulTensor에 혼합(chemo_sense 경량 맵핑). 사이매틱스/색/톤과 연동해 표현력 강화.

비고:
- 현재 커리큘럼/가중치 파일은 선언 상태이며, 실제 파이프라인 연결은 환경/요구에 맞게 수동 주입하거나 훅을 추가하면 됩니다.
