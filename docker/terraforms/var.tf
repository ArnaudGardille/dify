variable "subscription-id" {
  type = string
  default = "5d1e2f23-087b-4c4c-ac5d-6df64ba47c69"
}

#virtual network variables
variable "region" {
  type = string
  default = "francecentral"
}

variable "ip-prefix" {
  type = string
  default = "10.99"
}
#end virtual network variables

variable "storage-account" {
  type = string
  default = "vigiestorage"
}

variable "storage-account-container" {
  type = string
  default = "dfy"
}

variable "redis" {
  type = string
  default = "vigie-redis"
}

variable "psql-flexible" {
  type = string
  default = "vigie-psql"
}

variable "pgsql-user" {
  type = string
  default = "postgres"
}

variable "pgsql-password" {
  type = string
  default = "#QWEASDasdqwe"
}

variable "aca-env" {
  type = string
  default = "dify-aca-env"
}

variable "aca-loga" {
  type = string
  default = "dify-loga"
}

variable "aca-cert-path" {
  type = string
  default = "/Users/gardille/Development/dify-azure-terraform/certs/*.vigie.ai_private_key.pfx"
}

variable "aca-cert-password" {
  type = string
  default = "Dechiktorren92!"
}

variable "aca-dify-customer-domain" {
  type = string
  default = "dashboard.vigie.ai"
}

#default = "langgenius/dify-api:latest"
variable "dify-api-image" {
  type = string
  default = "arnaudvigieai/vigie-api:latest"
}

#default = "langgenius/dify-web:latest"
variable "dify-web-image" {
  type = string
  default = "arnaudvigieai/vigie-web:latest"
}

variable "dify-sandbox-image" {
  type = string
  default = "langgenius/dify-sandbox:latest"
}