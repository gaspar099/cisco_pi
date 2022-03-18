from netmiko import ConnectHandler 

cisco_device = input('Please enter IP address: ')
cisco_username = input('Please enter username: ')
cisco_password = input('Please enter password: ')

connection = {'ip': cisco_device,
                'device_type': 'cisco_ios',
                'username': cisco_username,
                'password': cisco_password
                }

connect = ConnectHandler(**connection)

connect.enable()

print(connect.send_command('sh ip int brief'))