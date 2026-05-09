def save_report(df, city):

    output_path = f"outputs/{city}_forecast.csv"

    df.to_csv(output_path, index=False)

    return output_path