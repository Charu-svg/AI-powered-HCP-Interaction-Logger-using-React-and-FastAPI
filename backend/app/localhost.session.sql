show databases;
use ai_crm_hcp;
show tables;

INSERT INTO interactions (hcp_id, interaction_type, date, time, notes, sentiment)
VALUES (1, 'Meeting', '2026-03-08', '15:30:00', 'Discussed diabetes medicine', 'Positive');

INSERT INTO interactions (hcp_id, interaction_type, date, time, notes, sentiment)
VALUES 
(1, 'Call', '2026-03-07', '11:00:00', 'Follow up about new drug', 'Neutral'),
(1, 'Email', '2026-03-06', '09:15:00', 'Shared product brochure', 'Positive');

SELECT * FROM interactions;

USE ai_crm_hcp;
CREATE table interactions

INSERT INTO hcp (name, specialization, hospital)
VALUES 
('Dr Sharma','Cardiology','Apollo Hospital'),
('Dr Mehta','Oncology','Fortis Hospital'),
('Dr Kumar','Diabetology','AIIMS');
SELECT *FROM hcp;

