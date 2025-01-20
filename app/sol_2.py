def split_ignore_brackets(s):
    parts = []
    bracket_level = 0
    start = 0

    for i, char in enumerate(s):
        if (char == '('):
            bracket_level += 1
        elif (char == ')'):
            bracket_level -= 1
        elif (char == ',' and bracket_level == 0):
            parts.append(s[start:i].strip())
            start = i + 1

    if (start < len(s)):
        parts.append(s[start:].strip())

    return parts


def parse_highlight(highlight_str):
    conditions = []
    for item in split_ignore_brackets(highlight_str):
        parts = item.split('=')
        if (len(parts) == 3):
            conditions.append({
                'type': parts[0],
                'value': parts[1],
                'color': parts[2]
            })
        elif (len(parts) == 2):
            conditions.append({
                'type': parts[0],
                'value': parts[1],
                'color': ''
            })
        else:
            print(f"Ошибка формата строки: {item}")
    return conditions


def generate_request(table, websocket_response, base_ws):
    result = {
        'columns': [],
        'order_by': {},
        'conditions_data': {},
        'page_size': '',
        'row_height': '',
        'color_conditions': {},
        'module': 'SO'
    }

    for row in table:
        columns_view = row.get('Columns View', '')
        if (columns_view in websocket_response):
            column_info = websocket_response[columns_view]
            result['columns'].append({
                'index': column_info['index'],
                'sort': len(result['columns'])
            })

        for key, value in row.items():
            if (key in base_ws):
                result_key = base_ws[key]

                if (key == 'Sort By' and value):
                    result['order_by'] = {
                        'direction': value,
                        'index': websocket_response[columns_view]['index']
                    }

                if (key == 'Condition' and value):
                    filter_key = websocket_response[columns_view]['filter']
                    result[result_key][filter_key] = []
                    for condition in value.split(','):
                        if ('=' in condition):
                            type_, val = condition.split('=')
                            result[result_key][filter_key].append({
                                'type': type_,
                                'value': val
                            })

                if (key == 'Highlight By' and value):
                    filter_key = websocket_response[columns_view]['filter']
                    result[result_key][filter_key] = parse_highlight(value)

                if (key == 'Row Height' and value):
                    result[result_key] = value
                if (key == 'Lines per page' and value):
                    result[result_key] = value

            else:
                print(f"Предупреждение: ключ {key} не найден в base_ws")

    print("Generated Result:", result)
    if (not result.get('order_by')):
        result['order_by'] = {}

    if (not result.get('columns')):
        result['columns'] = []
    return result

table = [
    {'Columns View': 'SO Number', 'Sort By': '', 'Highlight By': 'equals=S110=rgba(172,86,86,1),equals=S111', 'Condition': 'equals=S110,equals=S111', 'Row Height': '60', 'Lines per page': '25'},
    {'Columns View': 'Client PO', 'Sort By': '', 'Highlight By': 'equals=P110,equals=P111', 'Condition': 'equals=P110', 'Row Height': '', 'Lines per page': ''},
    {'Columns View': 'Terms of Sale', 'Sort By': 'asc', 'Highlight By': 'equals=S110=rgba(172,86,86,1)', 'Condition': '', 'Row Height': '', 'Lines per page': ''}
]

websocket_response = {
    'Client PO': {'index': 'so_list_client_po', 'filter': 'client_po'},
    'SO Number': {'index': 'so_list_so_number', 'filter': 'so_no'},
    'Terms of Sale': {'index': 'so_list_terms_of_sale', 'filter': 'term_sale'}
}

base_ws = {
    'Columns View': 'columns',
    'Sort By': 'order_by',
    'Condition': 'conditions_data',
    'Lines per page': 'page_size',
    'Row Height': 'row_height',
    'Highlight By': 'color_conditions'
}

result = generate_request(table, websocket_response, base_ws)
print(result)
