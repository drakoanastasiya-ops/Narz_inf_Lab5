import pytest
from src.manager import Manager
from src.models import Parameters


def test_apartment_costs_basic_and_edge_cases():
    parameters = Parameters()
    manager = Manager(parameters)
    assert manager.get_apartment_costs('apart-polanka', 2025, 1) == 910.0
    assert manager.get_apartment_costs('apart-polanka', 2025, 3) == 0.0

    with pytest.raises(ValueError):
        manager.get_apartment_costs('no-apartment', 2025, 1)

    assert manager.get_apartment_costs('apart-polanka', year=2025) == 910.0
    assert manager.get_apartment_costs('apart-polanka') == 910.0
    
    with pytest.raises(ValueError):
        manager.get_apartment_costs('apart-polanka', 2025, 100)



# "amount_pln": 760.00,
#"date_due": "2025-02-15",
#"amount_pln": 150.00,
#"date_due": "2025-02-12"