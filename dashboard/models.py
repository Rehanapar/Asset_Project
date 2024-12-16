from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    
    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return f'{self.name}'

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class  Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'

   





















# pip install requests
# import os
# import subprocess
# import requests

# # Step 1: Define the URL for the MySQL Installer and where to save it
# installer_url = "https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-web-community-8.0.32.0.msi"
# installer_file = "mysql-installer.msi"

# # Step 2: Download the MySQL Installer
# print("Downloading MySQL Installer...")

# response = requests.get(installer_url)
# if response.status_code == 200:
#     with open(installer_file, 'wb') as f:
#         f.write(response.content)
#     print(f"MySQL Installer downloaded successfully: {installer_file}")
# else:
#     print("Failed to download the MySQL Installer.")
#     exit(1)

# # Step 3: Run the installer (silent installation)
# print("Running MySQL Installer...")

# # Command to run the installer silently
# command = f"msiexec /i {installer_file} /quiet /norestart"

# # Run the installer using subprocess
# try:
#     subprocess.run(command, shell=True, check=True)
#     print("MySQL Server installed successfully.")
# except subprocess.CalledProcessError as e:
#     print(f"Error during installation: {e}")
#     exit(1)

# # Step 4: Verify if MySQL is installed and running
# print("Verifying MySQL installation...")

# # Check if the MySQL service is running
# try:
#     result = subprocess.run("sc query MySQL", shell=True, capture_output=True, text=True)
#     if "RUNNING" in result.stdout:
#         print("MySQL Server is running successfully.")
#     else:
#         print("MySQL Server installation may have failed.")
# except subprocess.CalledProcessError:
#     print("Error checking MySQL service status.")
# Example of setting the root password
# root_password = "your_password_here"
# command = f"msiexec /i {installer_file} /quiet /norestart MYSQL_ROOT_PASSWORD={root_password}"

# # Run the installer with the root password set
# subprocess.run(command, shell=True, check=True)
