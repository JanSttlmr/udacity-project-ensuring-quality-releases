resource "azurerm_network_interface" "example_nic" {
  name                = "${var.application_type}-${var.resource_type}-nic"
  location            = var.location
  resource_group_name = var.resource_group

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
    #public_ip_address_id          = ""
  }
}

resource "azurerm_linux_virtual_machine" "example_vm" {
  name                = "test-vm"
  location            = var.location
  resource_group_name = var.resource_group
  size                = var.vm_size
  admin_username      = var.vm_admin_username
  network_interface_ids = [azurerm_network_interface.example_nic.id]
  admin_ssh_key {
    username   = var.vm_admin_username
    public_key = var.vm_admin_ssh_key
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
  #source_image_id = "/subscriptions/f0f1e4fe-3d67-40e7-9a32-b6e793e4d7c4/resourcegroups/linux-test_group/providers/Microsoft.Compute/galleries/compute_gallery/images/linux-test/versions/0.0.1"
}
