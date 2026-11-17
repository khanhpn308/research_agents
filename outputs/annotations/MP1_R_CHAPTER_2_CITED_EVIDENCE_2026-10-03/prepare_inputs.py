from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).parent
pairs=[
('S01','data/papers/verification/MP1-V001/2022-Detachable Soft Actuators with Tunable Stiffness Based on Wire Jamming.pdf'),
('S02','data/papers/verification/MP1-V001/2021-A Positive Pressure Jamming Based Variable Stiffness Structure and its Application on Wearable Robots.pdf'),
('S03','data/papers/verification/MP1-V001/2026-A variable stiffness omnidirectional chain based on positive-pressure fiber jamming.pdf'),
('S15','data/papers/verification/D1-V003/A Review of Mechanisms to Vary the Stiffness of Laminar Jamming Structures and Their Applications in Robotics.pdf'),
('S18','data/papers/verification/D1-V002/2025-A continuum-based model for a layer jamming beam.pdf'),
('S06','data/papers/verification/MP1-V002/2025-A new mechanical model of short wire ropes Theory and experimental.pdf'),
('V-W02','data/papers/verification/MP1-V002/A3-2022-Mechanical response of single and double-helix.pdf'),
('S13','data/papers/verification/MP1-V002/A7-2026-High damping capacity with a wide temperature window in braided NiTi microfilaments.pdf'),
('S17','outputs/reports/MP1_R_PHASE_3_2026-10-02/S17_fulltext.pdf'),
('S04','/mnt/c/Users/khanh/Downloads/Towards_a_Snake-Like_Flexible_Robot_With_Variable_Stiffness_Using_an_SMA_Spring-Based_Friction_Change_Mechanism.pdf'),
('S22','data/papers/verification/MP1-V002/A5-Cable vibration considering internal friction.pdf'),
('S05a','data/papers/verification/MP1-V002/2013-Superelastic shape memory alloy cables Part I – Isothermal tension experiments.pdf'),
('S05b','data/papers/verification/MP1-V002/2013-Superelastic shape memory alloy cables Part II – Subcomponent isothermal responses.pdf'),
('S09','data/papers/verification/MP1-V001/2013-A Biologically Inspired Wet Shape Memory Alloy Actuated Robotic Pump.pdf'),
('S07','data/papers/verification/MP1-V002/2025-Finite Element Method for Mechanical Behavior of Shape Memory Alloy .pdf'),
('S11','data/papers/verification/MP1-V002/2016-Nonlinear Vibration Absorber with Pinched Hysteresis Theory and Experiments.pdf'),
('S12','data/papers/verification/MP1-V002/2024-Experimental-Numerical Assessment of Mechanical Behavior of Laboratory-Made Steel and NiTi Shape Memory Alloy Wire Ropes.pdf'),
('S10','data/papers/verification/MP1-V001/2022-Soft actuator with switchable stiffness using a micropump-activated jamming system.pdf')]
inputs=[]
for n,(sid,rel) in enumerate(pairs,1):
 p=ROOT/rel
 inputs.append({'reference_number':n,'source_work_id':sid,'path':rel,'exists':p.exists(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None})
(OUT/'inputs.json').write_text(json.dumps(inputs,ensure_ascii=False,indent=2))
for x in inputs:print(x['reference_number'],x['source_work_id'],'OK' if x['exists'] else 'MISSING',x['path'])
