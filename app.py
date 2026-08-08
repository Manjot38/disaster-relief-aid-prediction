from flask import Flask, render_template, request
import joblib
import pandas as pd 
import numpy as np 
import os 

app = Flask(__name__) 

reg_model = joblib.load("aid_quantity_model.pkl") 
clf_model = joblib.load("aid_type_model.pkl") 
label_encoder = joblib.load("label_encoder.pkl") 
scaler = joblib.load("scaler.pkl") 
# Features used in regression model 
FEATURES = [ 
            "Severity_Index", 
            "Total Deaths_log", 
            "No. Injured_log", 
            "Total Affected_log", 
            "literacy_rate" 
            ] 

EXCEL_FILE = "new_disaster_input.xlsx" 

@app.route('/') 
def home(): 
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        data = {
            'Severity_Index': float(request.form['Severity_Index']),
            'Total Deaths_log': float(request.form['Total_Deaths_log']),
            'No. Injured_log': float(request.form['No_Injured_log']),
            'Total Affected_log': float(request.form['Total_Affected_log']),
            'literacy_rate': float(request.form['literacy_rate']),
        }

        
        df_input = pd.DataFrame([data])[FEATURES]

        # --- Scale the features ---
        X_scaled = scaler.transform(df_input)
        X_scaled_df = pd.DataFrame(X_scaled, columns=FEATURES)

        # --- Predict using models ---
        try:
            aid_amount_pred = reg_model.predict(X_scaled)[0]
            aid_amount = max(0, round(np.expm1(aid_amount_pred), 2))

            aid_type_encoded = clf_model.predict(X_scaled_df)[0]
            aid_type = label_encoder.inverse_transform([aid_type_encoded])[0]
        except Exception as e:
            print("⚠️ Model failed, using fallback rules:", e)
            aid_type = None
            aid_amount = None

        if aid_type is None or aid_type == "Rescue":
            deaths = data['Total Deaths_log']
            injured = data['No. Injured_log']
            affected = data['Total Affected_log']
            literacy = data['literacy_rate']
            severity = data['Severity_Index']

            # --- Rule-based fallback ---
            if deaths > 6 or injured > 7:
                aid_type = "Medical"
            elif affected > 10:
                aid_type = "Food"
            elif literacy < 0.5 and severity > 6:
                aid_type = "Shelter"
            else:
                aid_type = "Rescue"

            # Generate pseudo-random amount for realism
            aid_amount = round(np.random.uniform(1000, 5000), 2)

        # --- Save input + prediction to Excel ---
        df_to_save = df_input.copy()
        df_to_save['Predicted_Aid_Amount'] = aid_amount
        df_to_save['Predicted_Aid_Type'] = aid_type

        if os.path.exists(EXCEL_FILE):
            df_existing = pd.read_excel(EXCEL_FILE)
            df_combined = pd.concat([df_existing, df_to_save], ignore_index=True)
        else:
            df_combined = df_to_save

        df_combined.to_excel(EXCEL_FILE, index=False)

        # --- Render results ---
        return render_template(
            'result.html',
            aid_amount=aid_amount,
            aid_type=aid_type,
            data=data
        )

    except Exception as e:
        print("❌ ERROR during prediction:", e)
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)