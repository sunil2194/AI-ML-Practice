# Kubernetes Vertical Pod Autoscaler (VPA) — Study Notes

## 1. What is VPA?
Unlike HPA (Horizontal Pod Autoscaler) which scales the number of replica pods horizontally, VPA (Vertical Pod Autoscaler) dynamically adjusts the CPU and memory resource requests and limits of a running deployment to fit actual workload patterns.

## 2. Core Architecture: The 3 Main Components
When VPA is installed via `./hack/vpa-up.sh`, it deploys three core microservices into the `kube-system` namespace:
- **The Recommender (The Brain):** Continuously queries the Kubernetes Metrics Server to collect historical CPU and memory usage metrics, computing a Target, Lower Bound, and Upper Bound.
- **The Admission Controller (The Gatekeeper / Webhook):** Acts as a secure HTTPS Mutating Admission Webhook that intercepts new pod creation requests on the fly and injects the recommended resources before writing to etcd.
- **The Updater (The Enforcer):** Monitors active, running pods and gracefully evicts them if significant resource drift is detected so they can be recreated with correct sizing.

## 3. VPA Update Modes
- `Off`: VPA analyzes usage and provides recommendations in status, but takes no automatic action (ideal for safe auditing).
- `Initial`: Assigns recommended resources only when pods are first created.
- `Auto`: Automatically evicts and updates running pods when resource drift occurs.

## 4. Quick VPA Manifest Example
```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: php-apache-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind: Deployment
    name: php-apache
  updatePolicy:
    updateMode: "Off"
