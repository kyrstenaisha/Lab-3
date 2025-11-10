import bmi 

def test_bmi_under_weight():
    result = bmi.calculate_bmi(50, 1.80)
    assert result == "Under Weight"


def test_bmi_normal_weight():
    result = bmi.calculate_bmi(60, 1.70)
    assert result == "Normal Weight"


def test_bmi_over_weight():
    result = bmi.calculate_bmi(90, 1.70)
    assert result == "Over Weight"