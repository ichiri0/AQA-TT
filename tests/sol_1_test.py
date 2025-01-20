import pytest
from unittest.mock import patch, MagicMock
from app.sol_1 import PDFParser, PDFValidator

class TestPDFParser:
    
    @pytest.fixture
    def mock_pdfplumber(self):
        with patch('pdfplumber.open') as mock:
            yield mock

    def test_parse_pdf_to_dict(self, mock_pdfplumber):
        mock_page = MagicMock()
        mock_page.extract_text.return_value = "PN: 1234\nSN: 5678\nDESCRIPTION: Test product\n"
        mock_pdfplumber.return_value.__enter__.return_value.pages = [mock_page]

        pdf_path = "mock_pdf.pdf"
        expected_result = {
            'PN': '1234',
            'SN': '5678',
            'DESCRIPTION': 'Test product'
        }
        
        parser = PDFParser()
        result = parser.parse_pdf_to_dict(pdf_path)
        
        assert result == expected_result

    def test_clean_and_structure_data(self):
        raw_data = {
            'PN': '1234',
            'SN': '5678',
            'DESCRIPTION': 'Test product',
            'LOCATION': 'Warehouse'
        }

        expected_structured_data = {
            'PN': '1234',
            'SN': '5678',
            'DESCRIPTION': 'Test product',
            'LOCATION': 'Warehouse'
        }

        result = PDFParser.clean_and_structure_data(raw_data)
        
        assert result == expected_structured_data

class TestPDFValidator:
    
    def test_validate(self):
        reference_template = {
            'PN': str,
            'SN': str,
            'DESCRIPTION': str,
            'LOCATION': str
        }

        valid_data = {
            'PN': '1234',
            'SN': '5678',
            'DESCRIPTION': 'Test product',
            'LOCATION': 'Warehouse'
        }

        invalid_data = {
            'PN': '1234',
            'SN': '5678',
            'DESCRIPTION': 'Test product'
        }

        validator = PDFValidator(reference_template)

        validation_result_valid = validator.validate(valid_data)
        assert validation_result_valid['errors'] == []
        assert validation_result_valid['extra_keys'] == []

        validation_result_invalid = validator.validate(invalid_data)
        assert "Отсутствует ключ: LOCATION" in validation_result_invalid['errors']
        assert validation_result_invalid['extra_keys'] == []
