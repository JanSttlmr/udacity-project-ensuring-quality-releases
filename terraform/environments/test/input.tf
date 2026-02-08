# Azure GUIDS
variable "subscription_id" {}
variable "client_id" {}
variable "client_secret" {}
variable "tenant_id" {}

# Resource Group/Location
variable "location" {}
variable "resource_group" {}
variable "application_type" {}

# Network
variable virtual_network_name {}
variable address_prefix_test {}
variable address_space {}

# VM-related variables
variable "vm_size" {}
variable "vm_admin_username" {}
variable "vm_admin_ssh_key" {}
#variable "resource_type" {}
#variable "subnet_id_test" {}
#variable "public_ip_address_id" {}
