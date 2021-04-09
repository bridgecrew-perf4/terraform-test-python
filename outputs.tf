output "something" {
  value = azurerm_resource_group.myterraformgroup.name
}

output "tls_private_key" {
  value = tls_private_key.example_ssh.private_key_pem
}
