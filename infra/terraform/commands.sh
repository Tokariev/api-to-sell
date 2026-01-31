# First, login with the account (if not already done)
gcloud auth login mykola.tokariev@gmail.com


# Set mykola.tokariev@gmail.com as the active account
gcloud config set account mykola.tokariev@gmail.com

# Now set the project
gcloud config set project parsa1

# Verify the configuration
gcloud config list

# login with the correct account:
gcloud auth application-default login --account=mykola.tokariev@gmail.com

# set the quota project:
gcloud auth application-default set-quota-project parsa1

# The CLI is targeting project skimpel-infra instead of parsa1. Set the correct project:
gcloud config set project parsa1