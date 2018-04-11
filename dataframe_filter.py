
import pandas as pd

from chart_data import level_data


def filter_data(filter_type):

    filter_name = filter_type.lower()
    file_path = "/home/msingh/Documents/PycharmProjects/LeadDashboard/data/crmnextleaddatadf.csv"
    df = pd.read_csv(file_path)
    df = df[["leadowner", "endyear", filter_name]]
    df_year_wise = df.groupby(["endyear", filter_name]).size().groupby(level=0).head(3).reset_index(name='count')
    df_year_wise["endyear"] = pd.to_datetime(df_year_wise["endyear"])
    df_year_wise["year"] = pd.to_datetime(df_year_wise["endyear"]).dt.year
    row_count = df_year_wise.shape[0]

    if row_count != 45:
        years_list = df_year_wise["year"].values.tolist()
        year_frequency_count = {x: years_list.count(x) for x in years_list}
        doc_list = []
        for each_count in year_frequency_count:
            year = each_count
            count = year_frequency_count[year]

            if count < 3:
                for index, i in enumerate(range(count,3)):
                    doc = {}
                    end_year = str(year) + "-12-31"
                    doc["endyear"] = end_year
                    doc[filter_name] = "null" + str(index + 1)
                    doc["count"] = 0
                    doc["year"] = year
                    doc_list.append(doc)

        df_add = pd.DataFrame(doc_list)
        df_add = df_add[["endyear", filter_name, "count", "year"]]
        df_add["endyear"] = pd.to_datetime(df_add["endyear"])
        final_df = df_year_wise.append(df_add)
        final_df = final_df.sort_values(['endyear', 'count'], ascending=[True, False]).reset_index().drop("index", axis=1)
    else:
        final_df = df_year_wise

    level_list = ["Level1", "Level2", "Level3"]
    df_level = pd.DataFrame({"level": level_list*15})
    df_result = pd.concat([final_df, df_level], axis=1)
    plotly_obj = level_data(df_result, filter_name)
    return plotly_obj
