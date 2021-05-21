def tup_to_str(tup):
    concat_str = ' '.join([str(elem) for elem in tup])
    return concat_str

def build_data_str(records):
    records_data_str = []

    for record in records:
        records_data_str.append(tup_to_str(record))
    
    return records_data_str