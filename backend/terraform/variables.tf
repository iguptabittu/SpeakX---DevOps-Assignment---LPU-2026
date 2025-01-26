variable "aws_region" {
  description = "AWS region where resources will be deployed"
  default     = "ap-south-1"
}

variable "vpc_name" {
  description = "Name of the VPC"
  default     = "my-vpc"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  default     = "10.0.0.0/16"
}

variable "public_subnets" {
  description = "List of public subnet CIDRs"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "private_subnets" {
  description = "List of private subnet CIDRs"
  type        = list(string)
  default     = ["10.0.101.0/24", "10.0.102.0/24"]
}

variable "ecs_cluster_name" {
  description = "Name of the ECS cluster"
  default     = "backend-cluster"
}

variable "lb_name" {
  description = "Name of the Application Load Balancer"
  default     = "application-lb"
}
