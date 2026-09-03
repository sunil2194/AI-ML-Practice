# admission_webhook.py
import json

def mutate_pod_request(incoming_pod_spec, recommended_resources):
    print("[Admission Controller] Intercepting new pod creation request...")
    print(f"-> Original Pod Spec Requests: {incoming_pod_spec.get('resources', 'None')}")
    
    # Mutating (patching) the pod specification on the fly
    incoming_pod_spec['resources'] = {
        'requests': {
            'cpu': f"{recommended_resources['target_cpu']}m",
            'memory': recommended_resources['target_mem']
        }
    }
    
    print(f"-> Mutated Pod Spec Requests (Injected by Webhook): {incoming_pod_spec['resources']}")
    return incoming_pod_spec

if __name__ == "__main__":
    # Simulate a raw pod template arriving before getting scheduled
    mock_pod = {
        "name": "php-apache-new-pod",
        "resources": {} # Empty! User didn't specify resources.
    }
    
    latest_recommendation = {
        "target_cpu": 150,
        "target_mem": "250Mi"
    }
    
    mutated_pod = mutate_pod_request(mock_pod, latest_recommendation)
