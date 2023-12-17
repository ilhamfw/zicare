-- Tabel Cinics
CREATE TABLE Clinics (
    clinic_id SERIAL PRIMARY KEY,
    clinic_name VARCHAR(255) NOT NULL
);

-- Tabel Patients
CREATE TABLE Patients (
    patient_id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    date_of_birth DATE,
    gender VARCHAR(10)
);
-- Tabel Schedules
CREATE TABLE Schedules (
    schedule_id SERIAL PRIMARY KEY,
    clinic_id INTEGER REFERENCES Clinics(clinic_id),
    day_of_week VARCHAR(15) NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL
);

-- Tabel Reservations
CREATE TABLE Reservations (
    reservation_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES Patients(patient_id),
    schedule_id INTEGER REFERENCES Schedules(schedule_id),
    reservation_date DATE,
    queue_number INTEGER
);

