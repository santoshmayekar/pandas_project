from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def get_match_specific_df(m_code):
    reqd_df = ipl_df[ipl_df.match_code==m_code]
    return reqd_df
