# API Snapshot

## elysia_engine.efp

- `EFPState`: `energy`, `force`, `momentum`를 보유. `step(dt=1.0, decay=0.95)`와 `as_dict()` 제공.

## elysia_engine.entities

- `Entity`: `update_force_components(world)`를 오버라이드하여 `f_body`, `f_soul`, `f_spirit`를 채우고, `role` 가중치에 따라 최종 force를 결정.

## elysia_engine.world

- `World`: `add_entity(entity)`, `step(dt=1.0)`, `export_persona_snapshot()` 제공.

## elysia_engine.roles

- `RoleProfile`: `normalized` 속성으로 가중치 합계를 1로 정규화.
- `ROLE_PROFILES`: warrior/mage/priest 기본 사전.

## elysia_engine.memory

- `Episode`: tick과 kind, data를 기록하는 단일 에피소드 데이터.
- `RingMemory`: 고정 길이 버퍼. `add(episode)`와 `to_list()` 제공.

## elysia_engine.persona

- `PersonaFrame`: tick/time/energy/momentum 요약.
- `build_persona_frame(snapshot)`: `World.export_persona_snapshot()` 결과 → `PersonaFrame`.

## elysia_engine.fields

- `ScalarField`: 이름, 차원, 값을 보관하는 단순 스칼라 필드.
- `FieldRegistry`: `register(field)`, `get(name)`, `sample(name, coords)`.

## hooks

- `hooks.godot_stub.publish(snapshot)`: Godot/WebSocket으로 보낼 데이터를 구성하는 템플릿.
- `hooks.logging.log_snapshot(snapshot)`: 표준 출력 기반 빠른 로깅 훅.
