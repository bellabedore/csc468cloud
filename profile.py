import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request - portal,context, makeRequestRSpec()

#Create a XenVM
noe = request.XenVM("node")
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU-64-STD"
node.routable_control_ip ="true"

node.addService(rspec.Execute(shell="/bon/sh",
                              command= "sudo apt update"))
node.addService(rspec.Execute(shell="/bon/sh",
                              command= "sudo apt install -y apache 2"))
node.addService(rspec.Execute(shell="/bon/sh",
                              command= 'sudo ufw allow in "Apache Full"'))
node.addService(rspec.Execute(shell="/bon/sh",
                              command= 'sudo systemt1 stsus apache2'))

#Print the RSpec to the enclosing page.
portal.context.printRequestRspec()
