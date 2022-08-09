import acquire
import pandas as pd



def prep_iris():
    df_iris = acquire.get_iris_data()
    df_iris.drop(columns=['measurement_id', 'species_id', 'species_id.1'], inplace=True)
    df_iris.rename(columns = {'species_name':'species'}, inplace=True)
    dummy_df = pd.get_dummies(df_iris.species, drop_first=True)
    df = pd.concat([df_iris, dummy_df], axis=1)
    print(df.info())
    return df

def prep_titanic():
    df = acquire.get_titanic_data()
    df.drop(columns = ['class', 'embarked', 'deck', 'age'], inplace=True)
    
    dummy_df = pd.get_dummies(df[['sex', 'embark_town']], drop_first=True)
    df = pd.concat([df, dummy_df], axis=1)
    
    df.drop(columns= ['sex', 'embark_town'], inplace=True)
    print(df.info())

    return df


def prep_telco():
    df = acquire.get_telco_data()

    encode = ['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'internet_service_type', 
             'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies',
             'contract_type', 'paperless_billing', 'payment_type', 'churn']

    df['null_charges'] = pd.to_numeric(df['total_charges'], errors='coerce').isnull()

    df['total_charges'][df['null_charges']== True] = df['monthly_charges'][df['null_charges']== True]

    df.total_charges = df.total_charges.astype(float)

    df.drop(columns= 'null_charges', inplace=True)

    dummy_df = pd.get_dummies(df[encode], drop_first=True)

    df = pd.concat([df, dummy_df], axis=1)

    df = df.drop(columns=encode)
    print(df.info())
    return df

    
    
    # train, test = train_test_split(df, test_size=.2, 
    #                            random_state=123, stratify=df.survived)

    # train, validate = train_test_split(train, test_size=.25, 
    #              random_state=123, stratify=train.survived)

def split_data(df, strat_by):
    '''
    Takes in a dataframe and a string type field to stratify by
    return train, validate, test subset dataframes
    '''
    from sklearn.model_selection import train_test_split
    train, test = train_test_split(df, test_size=.2, 
                               random_state=123, stratify=df[strat_by])
    train, validate = train_test_split(train, test_size=.25, 
                 random_state=123, stratify=train[strat_by])
    print(f'Prepared df: {df.shape}')
    print()
    print(f'Train: {train.shape}')
    print(f'Validate: {validate.shape}')
    print(f'Test: {test.shape}')


    return train, validate, test