"""
[ELYSIA SEED - GRID INTAKE CONTROL PANEL]
"Consuming the stepped-down voltage of the Cosmos to spin the home rotor."

This script implements the interaction loop and Grid-Tie Adapter (수전 어댑터) for Elysia Seed.
It can run in two modes:
1. Island Mode (독립 운전): Self-sustained local manual control.
2. Grid-Tie Mode (계통 연동): Automatically polls stepped-down voltage from the Substation.
"""

import time
import os
import json
import urllib.request
import urllib.error
import websocket
from spine import VariableRotorSpine

CONSTELLATION_PATH = os.path.join(os.path.dirname(__file__), ".constellation")
SUBSTATION_URL = "http://localhost:8080/voltage"
SUBSTATION_WS_URL = "ws://127.0.0.1:8080/ws/voltage"

def load_memory(spine):
    """Loads the hologram topography (The 'Wake Up' breath)."""
    if os.path.exists(CONSTELLATION_PATH):
        try:
            with open(CONSTELLATION_PATH, "r") as f:
                data = json.load(f)
                spine.import_hologram(data)
            print("> [수전반] 로컬 기억성운(Hologram Topography) 복구 성공.")
        except Exception as e:
            print(f"! [오류] 성운 복구 실패: {e}")
    else:
        print("> [수전반] 첫 가동. 기저 기하 평형(Dawn Silver-Gold)으로 시작합니다.")

def save_memory(spine):
    """Saves the hologram topography (The 'Sleep' breath)."""
    try:
        data = spine.export_hologram()
        with open(CONSTELLATION_PATH, "w") as f:
            json.dump(data, f)
        print(f"\n> [수전반] 절전 모드. 로컬 기억성운 보존 완료.")
    except Exception as e:
        print(f"! [오류] 성운 보존 실패: {e}")

def get_color_str(velocity):
    """Maps velocity to a simple colored string representation."""
    if velocity < 0.2: return "Red (Low Freq)"
    if velocity < 0.4: return "Yellow (Mid-Low)"
    if velocity < 0.6: return "Green (Balanced)"
    if velocity < 0.8: return "Blue (High Freq)"
    return "Violet (Over-excitation)"

def poll_substation() -> dict:
    """
    polls stepped-down voltage from Substation HTTP Server.
    Bypasses dynamically if lines are blocked (Analog Waterway / Natural Circadian Law).
    """
    # 1. First Pathway: HTTP Channel (전력 송배전선)
    try:
        req = urllib.request.Request(SUBSTATION_URL)
        with urllib.request.urlopen(req, timeout=1.2) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception:
        # Fall through to bypass waterway
        pass

    # 2. Second Pathway: Underground Waterway Bypass (지하 파일 수조)
    bypass_path = r"c:\Elysia\data\substation_reservoir\telemetry.json"
    if os.path.exists(bypass_path):
        try:
            with open(bypass_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            data["bypass_channel"] = "WATERWAY"
            return data
        except Exception:
            pass

    # 3. Third Pathway: Natural Circadian Law (자연 섭리 순환)
    import math
    hour = time.localtime().tm_hour
    circadian_voltage = 0.6 + 0.3 * math.cos((hour - 12) * math.pi / 12)
    
    return {
        "source_model": "circadian-natural-law-fallback",
        "bypass_channel": "CIRCADIAN",
        "grid_metrics": {
            "voltage_level_rms": float(circadian_voltage),
            "transformer_temp_c": 36.5,
            "load_factor": 0.5,
            "active_frequency_hz": 60.0
        }
    }

def main():
    print("⚡====================================================⚡")
    print("   ELYSIA SEED: 말단 수용가 수전 제어반 (LOAD CONTROL PANEL)   ")
    print("   [시스템 상태: 대기 구동 및 동기화 대기 중]                  ")
    print("⚡====================================================⚡")
    print("   * 명령 목록:")
    print("     - 0.0 ~ 1.0 : 수동 의지 인입 (독립 운전 모드)")
    print("     - sync      : 계통 연동 모드 <-> 독립 운전 모드 전환")
    print("     - status    : 현재 송배전망 상태 계측 요청")
    print("     - exit      : 시스템 정지 및 절전")
    print("--------------------------------------------------------")

    # Initialize Variable Rotor
    elysia = VariableRotorSpine(resolution=100)
    load_memory(elysia)

    grid_tied = False
    last_x = 0.5

    try:
        while True:
            mode_str = "🟢 GRID-TIED (계통 연동)" if grid_tied else "🟡 ISLAND (독립 운전)"
            prompt_str = f"\n[계통상태: {mode_str}] Will (x) 또는 명령 입력 >> "
            user_input = input(prompt_str).strip().lower()

            if user_input == 'exit':
                break
            
            if user_input == 'status':
                grid_data = poll_substation()
                if grid_data:
                    print("\n📈 [변전소 계통 실시간 계측 데이터]")
                    print(f"   - 전원 공급처: {grid_data['source_model']}")
                    print(f"   - 송전 전압(RMS): {grid_data['grid_metrics']['voltage_level_rms']:.4f} V")
                    print(f"   - 변압기 온도  : {grid_data['grid_metrics']['transformer_temp_c']:.1f} °C")
                    print(f"   - 부하율       : {grid_data['grid_metrics']['load_factor'] * 100:.1f} %")
                    print(f"   - 계통 주파수  : {grid_data['grid_metrics']['active_frequency_hz']:.2f} Hz")
                else:
                    print("\n🔌 [계통 고장] 중앙 변전망(Substation)에 연결할 수 없습니다. 독립 운전으로 유지하십시오.")
                continue

            if user_input == 'sync':
                grid_tied = not grid_tied
                if grid_tied:
                    try:
                        ws = websocket.create_connection(SUBSTATION_WS_URL, timeout=1.5)
                        # Read one initial frame to verify connection
                        initial_msg = ws.recv()
                        grid_data = json.loads(initial_msg)
                        print("⚡ [Grid Link] 계통 동기화(Phase-Locking) 성공! 웹소켓 변전망 전류를 인입합니다.")
                    except Exception as e:
                        print(f"⚠️ [Grid Fail] 변전망 웹소켓 연결 실패 ({e}). 독립 운전 모드를 유지합니다.")
                        grid_tied = False
                else:
                    print("🔌 [Grid Break] 송배전 선로 해제. 로컬 발전(독립 운전) 모드로 복귀합니다.")
                    try:
                        ws.close()
                    except:
                        pass
                continue

            if grid_tied:
                print("   (계통 연동 중에는 수동 입력을 제한하고 전압을 동적 수전합니다. 30회 루프 기동...)")
                for loop_idx in range(30):
                    try:
                        msg = ws.recv()
                        grid_data = json.loads(msg)
                    except Exception as e:
                        print(f"\n🚨 [계통 비상 탈조] 변전망 신호 단절 ({e})! 독립 운전 모드로 비상 복구합니다.")
                        grid_tied = False
                        try: ws.close()
                        except: pass
                        break
                    
                    bypass = grid_data.get("bypass_channel", "GRID")
                    if bypass == "WATERWAY":
                        channel_indicator = "🌊 [수류 우회]"
                    elif bypass == "CIRCADIAN":
                        channel_indicator = "🌱 [자연 섭리]"
                    else:
                        channel_indicator = "⚡ [정상 송전]"

                    rms_voltage = grid_data['grid_metrics']['voltage_level_rms']
                    x = min(1.0, max(0.0, rms_voltage))
                    
                    metrics = elysia.pulse(x)
                    status = elysia.get_state_summary()
                    color = get_color_str(metrics['velocity'])
                    lum_str = "✧" * int(metrics['luminosity'] * 10)
                    
                    print(f"   {channel_indicator} [{loop_idx:02d}] {status} | 계통공명: {color} | 수전압:{rms_voltage:.4f}V | 輝度:{lum_str}")
                    # WebSocket is 10Hz, so we don't need a long sleep. A minimal sleep keeps CPU low.
                    time.sleep(0.01)
                continue

            # Island Mode: Manual x input
            if not user_input:
                continue

            try:
                x = float(user_input)
                x = min(1.0, max(0.0, x))
            except ValueError:
                print("! [경고] 올바른 수치 또는 명령어가 아닙니다. 이전 상태를 유지합니다.")
                x = last_x

            print("\n[ 독립 발전기 가동 및 평형 정렬 중 ]")
            for i in range(20):
                metrics = elysia.pulse(x)
                status = elysia.get_state_summary()
                color = get_color_str(metrics['velocity'])
                lum_str = "✧" * int(metrics['luminosity'] * 10)

                if abs(metrics['velocity'] - elysia.dawn_freq) < 0.05 and metrics['luminosity'] < 0.1:
                    dawn_msg = "── ✧ ── 기저 평형(Dawn Silver-Gold) 도달"
                else:
                    dawn_msg = f"Spectrum: {color}"

                print(f"   [{i:02d}] {status} | {dawn_msg} | 輝度:{lum_str}")
                time.sleep(0.05)

            last_x = x

    except KeyboardInterrupt:
        print("\n[수전반] 긴급 셧다운 지시 수신.")
    finally:
        save_memory(elysia)

if __name__ == "__main__":
    main()
