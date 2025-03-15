from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model_path = 'saved_model/linear_svc_model.joblib'
model = joblib.load(model_path)

# Feature schema with names and expected types
FEATURE_SCHEMA = {
    "event_type_x": {"type": int, "required": True},
    "scheduling_class_x": {"type": int, "required": True},
    "priority": {"type": int, "required": True},
    "requested_cpu": {"type": float, "required": True},
    "requested_ram": {"type": float, "required": True},
    "requested_disk_space": {"type": float, "required": True},
    "diff_machine_constraint": {"type": int, "required": True},
    "event_type_y": {"type": int, "required": True},
    "scheduling_class_y": {"type": int, "required": True},
    "mean_cpu_usage": {"type": float, "required": True},
    "canonical_memory_usage": {"type": float, "required": True},
    "assigned_memory_usage": {"type": float, "required": True},
    "unmapped_page_cache": {"type": float, "required": True},
    "total_page_cache": {"type": float, "required": True},
    "max_memory_usage": {"type": float, "required": True},
    "mean_disk_io_time": {"type": float, "required": True},
    "mean_local_disk_space": {"type": float, "required": True},
    "max_cpu_usage": {"type": float, "required": True},
    "max_disk_io_time": {"type": float, "required": True},
    "cpi": {"type": float, "required": True},
    "mai": {"type": float, "required": True},
    "sample_portion": {"type": float, "required": True},
    "aggregation_type": {"type": int, "required": True},
    "sampled_cpu_usage": {"type": float, "required": True},
    "job_duration": {"type": float, "required": True},
    "cpu_utilization_ratio": {"type": float, "required": True},
    "memory_utilization_ratio": {"type": float, "required": True},
    "job_occurrences": {"type": int, "required": True},
    "access_frequency": {"type": float, "required": True},
    "data_size": {"type": float, "required": True},
    "latency_sensitivity": {"type": float, "required": True},
    "read_write_ratio": {"type": float, "required": True}
}

# Helper function to validate incoming JSON data
def validate_input(json_data):
    errors = []
    validated_data = []

    for feature_name, rules in FEATURE_SCHEMA.items():
        # Presence check
        if feature_name not in json_data:
            errors.append(f"Missing required feature: '{feature_name}'")
            continue

        value = json_data[feature_name]
        expected_type = rules["type"]

        # Type check
        if not isinstance(value, expected_type):
            # Special case: allow float inputs for int features if safe to convert
            if expected_type is int and isinstance(value, float) and value.is_integer():
                value = int(value)
            else:
                errors.append(
                    f"Feature '{feature_name}' should be {expected_type.__name__}, but got {type(value).__name__}"
                )
                continue

        validated_data.append(value)

    return errors, validated_data

# Root endpoint to confirm the API is running
@app.route('/')
def index():
    return jsonify({'message': 'HybridRecovery ML API is running!'})

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Receive JSON data
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No JSON payload received!'}), 400

        # Validate the input
        errors, validated_features = validate_input(data)

        if errors:
            return jsonify({'error': errors}), 400

        # Convert to numpy array for the model
        features_array = np.array(validated_features).reshape(1, -1)

        # Prediction
        prediction = model.predict(features_array)

        # Placeholder confidence score (replace with your logic if needed)
        confidence_score = float(np.sum(features_array))

        # Return the prediction and confidence score
        return jsonify({
            'prediction': int(prediction[0]),
            'confidence_score': confidence_score
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

