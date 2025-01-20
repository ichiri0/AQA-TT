import pdfplumber
import re
from typing import Dict, List


class PDFParser:
    @staticmethod
    def parse_pdf_to_dict(pdf_path: str) -> Dict[str, str]:
        """
        Извлекает информацию из PDF-файла и возвращает ее в виде структурированного словаря
        """
        data = {}
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages):
                    text = page.extract_text()
                    if text:
                        lines = text.split("\n")
                        for line in lines:
                            if ":" in line:
                                key, value = map(str.strip, line.split(":", 1))
                                data[key] = value
                    else:
                        print(f"Предупреждение: Текст на странице {page_num + 1} не был извлечен.")
        except Exception as e:
            print(f"Ошибка при обработке PDF: {e}")
        return PDFParser.clean_and_structure_data(data)

    @staticmethod
    def clean_and_structure_data(raw_data: Dict[str, str]) -> Dict[str, str]:
        """
        Очищает и структурирует необработанные данные, разделяя строки с ключами на отдельные ключи и значения.
        """
        structured_data = {}
        for key, value in raw_data.items():
            pairs = re.split(r"\s+(?=[A-Z]+:)", f"{key}: {value}")
            for pair in pairs:
                if ":" in pair:
                    sub_key, sub_value = map(str.strip, pair.split(":", 1))
                    structured_data[sub_key] = sub_value
        return structured_data


class PDFValidator:
    def __init__(self, reference_template: Dict[str, type]):
        self.reference_template = reference_template

    def validate(self, pdf_data: Dict[str, str]) -> Dict[str, List[str]]:
        """
        Валидирует данные PDF-файла по сравнению с заданным эталоном.
        """
        errors = []
        for key, expected_type in self.reference_template.items():
            if key not in pdf_data:
                errors.append(f"Отсутствует ключ: {key}")
            elif not isinstance(pdf_data[key], expected_type):
                errors.append(f"Неверный тип для ключа '{key}': Ожидался {expected_type}, получено {type(pdf_data[key])}.")

        # Дополнительные ключи, которые не встречаются в эталоне
        extra_keys = set(pdf_data.keys()) - set(self.reference_template.keys())
        return {"errors": errors, "extra_keys": list(extra_keys)}

    def validate_layout(self, pdf_path: str) -> bool:
        """
        Проверяет расположение данных на странице (для проверки структуры и порядка элементов).
        """
        with pdfplumber.open(pdf_path) as pdf:
            # Проводим базовую проверку на расположение текста
            for page_num, page in enumerate(pdf.pages):
                for table in page.extract_tables():
                    for row in table:
                        print(f"Страница {page_num + 1}: {row}")
            # Для примера возвращаем True, проверку можно улучшить
        return True


reference_template = {
    'PN': str,
    'SN': str,
    'DESCRIPTION': str,
    'LOCATION': str,
    'CONDITION': str,
    'RECEIVER#': str,
    'UOM': str,
    'DATE': str,
    'PO': str,
    'SOURCE': str,
    'REC.DATE': str,
    'MFG': str,
    'BATCH#': str,
    'DOM': str,
    'REMARK': str,
    'BY': str,
    'NOTES': str,
    'Qty': str,
}

pdf_file_path = "test_task.pdf"

# Парсим PDF
parser = PDFParser()
parsed_data = parser.parse_pdf_to_dict(pdf_file_path)

# Валидируем данные
validator = PDFValidator(reference_template)
validation_results = validator.validate(parsed_data)

# Проверка на расположение данных
layout_valid = validator.validate_layout(pdf_file_path)

print("Извлеченные данные:", parsed_data)
print("Результаты валидации:", validation_results)
print("Результаты проверки расположения:", layout_valid)