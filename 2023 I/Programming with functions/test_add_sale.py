import pytest
from add_sale import validate_sale_data

def test_validate_sale_data():
    # Test a valid sale
    sale_data = [['Product', 'Client Name', 10.0, 5, '2023-04-06', 0.0, 1.0, 'Seller']]
    assert validate_sale_data(sale_data) == True
    
    # Test an invalid sale with empty product name
    sale_data = [['', 'Client Name', 10.0, 5, '2023-04-06', 0.0, 1.0, 'Seller']]
    assert validate_sale_data(sale_data) == False
    
    # Test an invalid sale with invalid unit price
    sale_data = [['Product', 'Client Name', 'abc', 5, '2023-04-06', 0.0, 1.0, 'Seller']]
    assert validate_sale_data(sale_data) == False
    
    # Test an invalid sale with empty seller name
    sale_data = [['Product', 'Client Name', 10.0, 5, '2023-04-06', 0.0, 1.0, '']]
    assert validate_sale_data(sale_data) == False
    
    # Test an invalid sale with multiple errors
    sale_data = [['', '', 'abc', -5, '', -1.0, -2.0, '']]
    assert validate_sale_data(sale_data) == False

    
pytest.main(["-v", "--tb=line", "-rN", __file__])
