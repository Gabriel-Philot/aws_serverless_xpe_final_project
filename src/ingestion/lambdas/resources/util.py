def control_sucess(control):
   
    if control == "OK":
       sucess_var = "sucess"

    else:
        sucess_var = "failure"
    
    return sucess_var


def convert_to_string(df):
    """
    Converts all columns of a DataFrame to string type.

    Args:
        df (pandas.DataFrame): DataFrame to be converted.

    Returns:
        pandas.DataFrame: DataFrame with all columns converted to string type.
    """
    for col in df.columns:
        df[col] = df[col].astype(str)
    return df


def infer_schema(json_data):

    schema = {}

    for record in json_data:
        for key, value in record.items():

            if isinstance(value, int):
                dtype = "integer"  
            elif isinstance(value, float):
                dtype = "float"
            elif isinstance(value, str):
                dtype = "string"
            elif isinstance(value, bool):
                dtype = "boolean"
            elif value is None:
                dtype = "null"

            if key not in schema:
                schema[key] = {dtype} 
            else:
                schema[key].add(dtype)

    inferred_schema = {}
    for key, types in schema.items():
        if len(types) > 1:
            inferred_type = "string" 
        else:
            inferred_type = list(types)[0]
            
        inferred_schema[key] = inferred_type

    return inferred_schema