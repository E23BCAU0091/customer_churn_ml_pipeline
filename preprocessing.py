
from sklearn.preprocessing import LabelEncoder

class Preprocessing:

    def transform(self, df):

        # Drop ID if exists
        if "customerID" in df.columns:
            df = df.drop("customerID", axis=1)

        # Ensure target column is numeric
        if df["Churn"].dtype == "object":
            df["Churn"] = df["Churn"].astype(str).str.strip()
            df["Churn"] = df["Churn"].map({"Yes":1, "No":0})

        # Remove rows with missing target
        df = df.dropna(subset=["Churn"])

        encoder = LabelEncoder()

        # Encode categorical columns
        for col in df.select_dtypes(include="object").columns:
            df[col] = encoder.fit_transform(df[col])

        return df
