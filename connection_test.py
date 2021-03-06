from google.cloud import automl_v1beta1 as automl
from google.oauth2 import service_account

project_id = 'gcp-chili-project'
compute_region = 'us-central1'
model_display_name = 'backup_plan_20210227040744'

t=service_account.Credentials.from_service_account_file('ACC CRED HERE')
model_id = 'backup_plan_20210227040744'

client = automl.TablesClient(credentials=t,project=project_id, region=compute_region)

model = client.get_model(model_display_name=model_display_name)

if model.deployment_state == automl.Model.DeploymentState.DEPLOYED:
    deployment_state = "deployed"
else:
    deployment_state = "undeployed"
print(deployment_state)

response = client.deploy_model(model_display_name=model_display_name)

# returns status
print("Model deployed. {}".format(response.result()))

def con_test():
    assert deployment_state == "deployed"
