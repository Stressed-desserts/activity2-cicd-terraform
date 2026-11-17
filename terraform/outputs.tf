output "ec2_instance_id" {
  description = "Provisioned AWS EC2 Instance ID"
  value       = aws_instance.app_ec2.id
}

output "ec2_public_ip" {
  description = "Public IPv4 address of the EC2 instance"
  value       = aws_instance.app_ec2.public_ip
}
