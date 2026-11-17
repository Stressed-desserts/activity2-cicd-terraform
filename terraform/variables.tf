variable "aws_region" {
  description = "AWS deployment region"
  type        = string
  default     = "ap-south-1"
}

variable "instance_type" {
  description = "EC2 compute instance size"
  type        = string
  default     = "t2.micro"
}

variable "tag_prefix" {
  description = "Resource tagging prefix"
  type        = string
  default     = "activity2-cicd"
}
