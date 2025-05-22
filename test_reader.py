import os
import pytest
from reader import parse_csv_manual, generate_report_text

TEST_CSV_CONTENT = """name,department,hours_worked,hourly_rate
Alice,Marketing,160,50
Bob,Marketing,140,45
Charlie,IT,170,60
"""

@pytest.fixture
def tmp_csv_file(tmp_path):
    file_path = tmp_path / "data1.csv"
    file_path.write_text(TEST_CSV_CONTENT, encoding='utf-8')
    return str(file_path)

def test_parse_csv_manual(tmp_csv_file):
    departments = parse_csv_manual([tmp_csv_file])

    assert "Marketing" in departments
    assert "IT" in departments

    assert len(departments["Marketing"]) == 2
    assert len(departments["IT"]) == 1

    assert departments["Marketing"][0]["name"] == "Alice"
    assert departments["Marketing"][0]["payout"] == 8000
    assert departments["IT"][0]["payout"] == 10200

def test_generate_report_output(tmp_csv_file):
    departments = parse_csv_manual([tmp_csv_file])
    report = generate_report_text(departments)

    assert "Marketing" in report
    assert "Alice" in report
    assert "$8000" in report
    assert "Charlie" in report
    assert "$10200" in report
