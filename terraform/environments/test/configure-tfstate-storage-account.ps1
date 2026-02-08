# PowerShell version of the Bash script

# Variables
$RESOURCE_GROUP_NAME = "rg-test"
$RANDOM_SUFFIX = Get-Random -Maximum 99999
$STORAGE_ACCOUNT_NAME = "tfstate$RANDOM_SUFFIX$RANDOM_SUFFIX"
$CONTAINER_NAME = "tfstate"

# Create storage account
az storage account create `
    --resource-group $RESOURCE_GROUP_NAME `
    --name $STORAGE_ACCOUNT_NAME `
    --sku Standard_LRS `
    --encryption-services blob

# Get storage account key
$ACCOUNT_KEY = az storage account keys list `
    --resource-group $RESOURCE_GROUP_NAME `
    --account-name $STORAGE_ACCOUNT_NAME `
    --query '[0].value' -o tsv

# Set environment variable for Terraform
$env:ARM_ACCESS_KEY = $ACCOUNT_KEY

# Create blob container
az storage container create `
    --name $CONTAINER_NAME `
    --account-name $STORAGE_ACCOUNT_NAME `
    --account-key $ACCOUNT_KEY

# Output values
Write-Output "RESOURCE_GROUP_NAME=$RESOURCE_GROUP_NAME"
Write-Output "STORAGE_ACCOUNT_NAME=$STORAGE_ACCOUNT_NAME"
Write-Output "CONTAINER_NAME=$CONTAINER_NAME"
Write-Output "ACCOUNT_KEY=$ACCOUNT_KEY"
